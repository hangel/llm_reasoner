# [Streamlit MCP Server](https://gemini.google.com/app/91f0d97b4251c9b9)
# --- streamlit_app.py (UI Layer) ---
import streamlit as st
import pandas as pd
from core_logic import load_and_filter_data # Import the logic

UVICORN_PORT = 9001

st.title("Data Filter App")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
min_value_filter = st.number_input("Minimum value to keep", value=0.0)

if uploaded_file is not None:
    st.write("Processing...")
    try:
        # Streamlit uses the core logic
        # Note: For larger files, saving the uploaded file temporarily might be needed
        # For simplicity here, we assume it can be read directly
        # If load_and_filter_data expects a filepath, save the uploaded_file first
        # temp_filepath = f"/tmp/{uploaded_file.name}"
        # with open(temp_filepath, "wb") as f:
        #     f.write(uploaded_file.getbuffer())
        # filtered_data = load_and_filter_data(temp_filepath, min_value_filter)

        # Simpler if logic can handle file-like objects (modify core_logic if needed)
        filtered_data = load_and_filter_data(uploaded_file, min_value_filter)

        st.write("Filtered Data:")
        st.dataframe(filtered_data)
    except (FileNotFoundError, ValueError, RuntimeError) as e:
        st.error(f"An error occurred: {e}")
    # except Exception as e: # Catch unexpected errors
    #     st.error(f"An unexpected error occurred: {e}")

# --- mcp_server.py (Exposing Core Logic via API) ---
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from pydantic import BaseModel
import pandas as pd
import uvicorn
import io # To handle UploadFile object

from core_logic import load_and_filter_data # Import the same logic

app = FastAPI(title="Data Processor MCP Server")

class FilterResponse(BaseModel):
    filtered_data_json: str # Return data as JSON string
    row_count: int

@app.post("/filter-data", response_model=FilterResponse, summary="Filters uploaded CSV data")
async def execute_filter_data(min_value: float = Form(...), file: UploadFile = File(...)):
    """
    MCP endpoint to load a CSV file, filter by 'value' column,
    and return the filtered data as JSON.
    """
    if not file.filename.endswith('.csv'):
         raise HTTPException(status_code=400, detail="Invalid file type. Please upload a CSV.")

    try:
        # Read the uploaded file content directly into a buffer
        # core_logic needs to be able to handle a file-like object or filepath
        # Option 1: Modify core_logic to accept BytesIO
        content = await file.read()
        buffer = io.BytesIO(content)
        buffer.name = file.filename # Some pandas functions might need a name attribute

        # Option 2: Save to a temporary file (less ideal for serverless/scaling)
        # temp_filepath = f"/tmp/{file.filename}"
        # with open(temp_filepath, "wb") as f:
        #     f.write(content)

        # Assuming core_logic can handle the buffer/file-like object:
        filtered_df = load_and_filter_data(buffer, min_value) # Pass buffer
        # Or if using temp file: filtered_df = load_and_filter_data(temp_filepath, min_value)

        return FilterResponse(
            filtered_data_json=filtered_df.to_json(orient='records'),
            row_count=len(filtered_df)
        )
    except (FileNotFoundError, ValueError, RuntimeError) as e:
         raise HTTPException(status_code=400, detail=f"Processing Error: {str(e)}")
    except Exception as e:
         # Log the exception here for debugging
         print(f"Unexpected error: {e}")
         raise HTTPException(status_code=500, detail=f"Internal Server Error")
    finally:
        # Clean up temp file if created
        # if 'temp_filepath' in locals() and os.path.exists(temp_filepath):
        #     os.remove(temp_filepath)
        pass # Ensure buffer is closed if necessary (usually handled by GC or context manager)


if __name__ == "__main__":
    #app.run(debug=False)
    uvicorn.run("mcp_server:app", host="0.0.0.0", port=UVICORN_PORT, log_config=None, reload=True) # Use a different port
