import streamlit as st
import os
# Import necessary components from Langchain and Google GenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, AIMessage # Import message types

# Local Application Imports (Assuming these files exist and are structured correctly)
# import mvp_config as config # Uncomment if you have a config file
# import mvp_utils as utils   # Uncomment if you have a utils file

# --- Configuration (If not using mvp_config) ---
# Define constants if not importing from a config file
# PEP 8: Uppercase with Underscores for Constants
MODEL_NAME = "gemini-1.5-flash" # Example model name
EMBEDDING_MODEL = "models/embedding-001" # Example embedding model name
CHUNK_SIZE = 1000 # Example text splitter chunk size
CHUNK_OVERLAP = 200 # Example text splitter chunk overlap
SIDEBAR_LOGO_PATH = "assets/images/COBOLpro/COBOLpro_QR.png" # Example logo path
MVP_VERSION = "0.0.0.1" # Example version
# Add other configurations here as needed

# --- Session State Keys (PEP 8: Uppercase with Underscores) ---
SESSION_STATE_MESSAGES = "messages"
SESSION_STATE_CONVERSATION_CHAIN = "conversation_chain"
SESSION_STATE_VECTOR_STORE = "vector_store" # Added key for vector store

# --- Helper Functions ---

def initialize_session_state():
    """
    Initializes the session state with default values.
    """
    if SESSION_STATE_MESSAGES not in st.session_state:
        st.session_state[SESSION_STATE_MESSAGES] = []
    if SESSION_STATE_CONVERSATION_CHAIN not in st.session_state:
        st.session_state[SESSION_STATE_CONVERSATION_CHAIN] = None
    if SESSION_STATE_VECTOR_STORE not in st.session_state:
         st.session_state[SESSION_STATE_VECTOR_STORE] = None


def get_api_key(key_name="GOOGLE_API_KEY"):
    """
    Retrieves the API key from environment variables or Streamlit secrets.
    """
    # Prioritize Streamlit secrets if available
    if key_name in st.secrets:
        return st.secrets[key_name]
    # Fallback to environment variables
    return os.getenv(key_name)

@st.cache_resource # Cache the resource to avoid re-creating on each rerun
def get_text_chunks(text, chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP):
    """
    Splits the input text into chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    text_chunks = text_splitter.split_text(text)
    return text_chunks

@st.cache_resource # Cache the resource to avoid re-creating on each rerun
def get_vector_store(text_chunks, embedding_model=EMBEDDING_MODEL):
    """
    Creates and returns a FAISS vector store from text chunks.
    """
    api_key = get_api_key("GOOGLE_API_KEY")
    if not api_key:
        st.error("Google API Key not found. Please set GOOGLE_API_KEY in environment variables or Streamlit secrets.")
        return None
    embeddings = GoogleGenerativeAIEmbeddings(model=embedding_model, google_api_key=api_key)
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    return vector_store

@st.cache_resource # Cache the resource to avoid re-creating on each rerun
def get_conversation_chain(vector_store, llm_model=MODEL_NAME):
    """
    Creates and returns a ConversationalRetrievalChain.
    """
    api_key = get_api_key("GOOGLE_API_KEY")
    if not api_key:
        st.error("Google API Key not found. Please set GOOGLE_API_KEY in environment variables or Streamlit secrets.")
        return None

    llm = ChatGoogleGenerativeAI(model=llm_model, google_api_key=api_key, temperature=0.5) # Added temperature
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

    # Define the prompt template
    # Using a more structured prompt template
    template = """
    You are a helpful AI assistant specializing in COBOL systems documentation.
    Answer the questions based only on the provided documentation context.
    If you don't know the answer from the documentation, say you don't know, don't try to make up an answer.
    Be concise and relevant to the COBOL context.

    Chat History:
    {chat_history}

    Context:
    {context}

    Question:
    {question}

    Answer:
    """
    qa_prompt = PromptTemplate(
        template=template,
        input_variables=["chat_history", "context", "question"]
    )


    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory,
        combine_docs_chain_kwargs={"prompt": qa_prompt} # Use the defined prompt template
    )
    return conversation_chain

def display_message(role, content):
    """
    Displays a chat message with the given role and content.
    """
    with st.chat_message(role):
        st.markdown(content)

# --- Main Application Logic ---

def main():
    """
    Main function to run the Streamlit application.
    """
    # Set page configuration (assuming this script is run directly)
    # If run via exec from app.py, app.py should handle this.
    # st.set_page_config(
    #     page_title=f"COBOLpro CLIP MVP v{MVP_VERSION}",
    #     page_icon="assets/images/COBOLpro/COBOLpro_icon.png", # Ensure path is correct
    #     layout="wide"
    # )

    initialize_session_state()

    # --- Sidebar Setup ---
    # Assuming setup_sidebar function is defined elsewhere (e.g., mvp_utils)
    # If not, implement sidebar elements directly here.
    # Example sidebar elements:
    with st.sidebar:
        # Example: Display logo
        try:
            # Assuming SIDEBAR_LOGO_KEY and LOGOS are in mvp_config
            # st.image(str(config.LOGOS[config.SIDEBAR_LOGO_KEY]), caption=f"OKRocket® Platform\\nCOBOLpro MVP Preview v{config.MVP_VERSION}", width=250)
            # If not using config:
            st.image(SIDEBAR_LOGO_PATH, caption=f"OKRocket® Platform\\nCOBOLpro MVP Preview v{MVP_VERSION}", width=250)
        except FileNotFoundError:
            st.warning(f"Sidebar logo not found at {SIDEBAR_LOGO_PATH}")

        # Example: Display execution info (if using mvp_utils)
        # with st.expander("**Execution Info**", expanded=False):
        #     exec_data = utils.get_system_info_markdown()
        #     st.markdown(exec_data, unsafe_allow_html=True)

        # Display Session State (for debugging)
        with st.expander("SESSION STATE", expanded=False): # Kept original expander title
            # Displaying types to keep output brief
            session_data_summary = {key: str(type(value)) for key, value in st.session_state.items()}
            st.write(session_data_summary)
            # st.write(st.session_state) # Uncomment for full state


    # --- Main Content ---
    st.title("COBOLpro Documentation Chatbot")
    st.subheader(f"Powered by Gemini 1.5 Flash and Langchain (MVP v{MVP_VERSION})")

    documentation_input = st.text_area(
        "Paste your COBOL system documentation here:",
        height=300,
        key="documentation_input_area" # Unique key
    )

    # Process documentation and set up the conversation chain
    if documentation_input and st.session_state[SESSION_STATE_CONVERSATION_CHAIN] is None:
        with st.spinner("Processing documentation and setting up chatbot..."):
            text_chunks = get_text_chunks(documentation_input)
            if text_chunks:
                vector_store = get_vector_store(text_chunks)
                if vector_store:
                    st.session_state[SESSION_STATE_VECTOR_STORE] = vector_store # Store vector store in session state
                    st.session_state[SESSION_STATE_CONVERSATION_CHAIN] = get_conversation_chain(vector_store)
                    st.success("Chatbot is ready! Ask a question about the documentation.")
                else:
                    st.error("Failed to create vector store.")
            else:
                st.warning("No text chunks were generated from the documentation.")

    # Display chat history
    for message in st.session_state[SESSION_STATE_MESSAGES]:
        display_message(message["role"], message["content"])

    # Handle user input
    user_query = st.chat_input("Ask a question about the documentation:")
    if user_query:
        # Display user message
        display_message("user", user_query)
        st.session_state[SESSION_STATE_MESSAGES].append({"role": "user", "content": user_query})

        # Get AI response if conversation chain is ready
        if st.session_state[SESSION_STATE_CONVERSATION_CHAIN]:
            with st.spinner("Getting response..."):
                try:
                    # Langchain's ConversationalRetrievalChain invoke uses the chat history from memory
                    # Pass the user query as the 'question'
                    response = st.session_state[SESSION_STATE_CONVERSATION_CHAIN].invoke(
                        {"question": user_query}
                    )
                    ai_response = response.get("answer", "No answer found.") # Extract the answer

                    # Display AI response
                    display_message("assistant", ai_response)
                    st.session_state[SESSION_STATE_MESSAGES].append({"role": "assistant", "content": ai_response})

                except Exception as e:
                    st.error(f"An error occurred while generating response: {e}")
                    st.markdown("I'm sorry, I couldn't process that request.")
        else:
             st.info("Please paste your COBOL system documentation above to begin.")


    # Initial prompt if no documentation is provided and chain is not set up
    if not documentation_input and st.session_state[SESSION_STATE_CONVERSATION_CHAIN] is None:
         st.info("Please paste your COBOL system documentation above to begin.")


# --- Run the main function ---
if __name__ == "__main__":
    main()

