import streamlit as st
import os
# Import necessary components from Langchain and Google GenAI
# ... (rest of your imports, including the corrected GoogleGenerativeAIEmbeddings import)
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings # Ensure this is correct
#from langchain_community.embeddings import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate

# Local Application Imports
import mvp_config as config # Renamed import for clarity
import mvp_utils as utils   # Renamed import for clarity

def setup_sidebar(modules):
    """Configures and displays the Streamlit sidebar elements."""
    st.sidebar.image(
        str(config.LOGOS[config.SIDEBAR_LOGO_KEY]), # Ensure path is string
        caption=f"OKRocket® Platform\nCOBOLpro MVP Preview v{config.MVP_VERSION} [{utils.get_current_timestamp('%Y/%m/%d')}]",
        width=250
    )

    with st.sidebar.expander("**Execution Info**", expanded=False):
        exec_data = utils.get_system_info_markdown()
        st.markdown(exec_data, unsafe_allow_html=True) # Allow HTML for details tag

    with st.sidebar.expander("**Session State**", expanded=False):
        st.write(st.session_state)

    st.sidebar.markdown("---")

    # --- Module Selection ---
    module_names = list(modules.keys())
    default_module = module_names[0] # Default to the first module

    # Try to get selection from URL query parameters
    query_params = st.query_params.get("module", [default_module])
    # Ensure query_param value is a valid key before finding index
    selected_module_name = query_params[0] if query_params[0] in module_names else default_module

    try:
        # Get index based on potentially updated selected_module_name
        index = module_names.index(selected_module_name)
    except ValueError:
        index = 0 # Fallback if name somehow still invalid

    choice = st.sidebar.radio(
        "**MODULE SELECTOR**",
        module_names,
        index=index,
        help="Select the module to execute",
        label_visibility="visible"
    )

    # Update query params when selection changes for bookmarking/sharing
    if selected_module_name != choice:
        st.query_params["module"] = choice

    return modules[choice] # Return the Path object for the selected module


# --- Streamlit Page Configuration ---
# Set the page title and default layout to wide
PAGE_CONFIG_NO = """
    st.set_page_config(
    page_title="CLIP Outline COBOLpro Legacy Intelligent Platform MVP",
    layout="wide" # This makes the page default to wide layout
)
"""

st.title("CLIP Outline COBOLpro Legacy Intelligent Platform MVP")
st.subheader("Intelligent Assistant for COBOL Legacy Systems")

# Set up the Google API Key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("Google API Key not found. Please set the GOOGLE_API_KEY environment variable.")
    st.stop()

# --- Constants and Configuration ---
MODEL_NAME = "gemini-1.5-flash"
EMBEDDING_MODEL = "models/embedding-001"

# --- Session State Initialization ---
# ... (your initialize_session_state function remains the same)
def initialize_session_state(documentation_text: str):
    """
    Initializes the Streamlit session state...
    """
    # ... (function content as before)
    if "retriever" not in st.session_state or "conversation_chain" not in st.session_state:
        st.info("Processing documentation and setting up AI assistant...")
        try:
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000, chunk_overlap=200, length_function=len, is_separator_regex=False
            )
            texts = text_splitter.split_text(documentation_text)
            if not texts:
                st.error("No text chunks were created...")
                return False

            embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL, google_api_key=api_key)
            vectorstore = FAISS.from_texts(texts, embeddings)
            st.session_state.retriever = vectorstore.as_retriever()

            llm = ChatGoogleGenerativeAI(model=MODEL_NAME, google_api_key=api_key, temperature=0.3)
            st.session_state.chat_history_memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

            custom_prompt_template = """You are an AI assistant helping to understand a COBOL legacy system based on provided documentation.
Answer the user's question based *only* on the provided context.
If the answer cannot be found in the context, truthfully say that you don't know or that the information is not available in the provided documentation.
Do not make up information.
Context: {context}
Question: {question}
Answer:"""

            st.session_state.conversation_chain = ConversationalRetrievalChain.from_llm(
                llm=llm,
                retriever=st.session_state.retriever,
                memory=st.session_state.chat_history_memory,
                 combine_docs_chain_kwargs={"prompt": PromptTemplate(template=custom_prompt_template, input_variables=["context", "question"])}
            )

            if "messages" not in st.session_state:
                st.session_state.messages = []

            st.success("AI assistant initialized successfully!")
            return True

        except Exception as e:
            st.error(f"An error occurred during initialization: {e}")
            if "retriever" in st.session_state: del st.session_state.retriever
            if "conversation_chain" in st.session_state: del st.session_state.conversation_chain
            if "chat_history_memory" in st.session_state: del st.session_state.chat_history_memory
            if "messages" in st.session_state: del st.session_state.messages # Clear messages too on error
            return False
    return True

# --- Main Content ---
# Input area for legacy system documentation
# ... (your text_area code)
documentation_input = st.text_area(
    "Paste your COBOL system documentation/context here:",
    height=300,
    key="documentation_text",
    help="Include relevant program descriptions, JCL, database layouts, incident reports, etc."
)


# Handle initialization based on documentation_input presence
if documentation_input:
    initialization_successful = initialize_session_state(documentation_input)
    if not initialization_successful:
        st.warning("Please resolve the initialization error before proceeding.")
        # Don't stop, just disable chat input
        # st.stop() # Removed st.stop() so sidebar can still render
elif "retriever" in st.session_state:
    # If documentation is cleared after initialization, clear state
    st.warning("Documentation removed. Clearing assistant state.")
    if "retriever" in st.session_state: del st.session_state.retriever
    if "conversation_chain" in st.session_state: del st.session_state.conversation_chain
    if "chat_history_memory" in st.session_state: del st.session_state.chat_history_memory
    if "messages" in st.session_state: del st.session_state.messages
    st.experimental_rerun() # Rerun to clear the chat interface


# --- Chat Interface ---
# ... (your chat interface code remains the same)
# Display chat messages from history on app rerun
for message in st.session_state.get("messages", []):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input for user questions
if documentation_input and "conversation_chain" in st.session_state:
    prompt = st.chat_input("Ask a question about the COBOL system documentation...")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = st.session_state.conversation_chain.invoke({"question": prompt})
                    ai_response = response.get("answer", "Could not retrieve an answer.")
                    st.markdown(ai_response)
                    st.session_state.messages.append({"role": "assistant", "content": ai_response})

                except Exception as e:
                    st.error(f"An error occurred while generating response: {e}")
                    st.markdown("I'm sorry, I couldn't process that request.")

elif not documentation_input and "conversation_chain" not in st.session_state:
     st.info("Please paste your COBOL system documentation above to begin.")


# --- Sidebar Content (New) ---

# Add an expander for Session State inspection
with st.sidebar.expander("SESSION_STATE"):
    st.write("Current contents of `st.session_state`:")
    # Display the entire session state dictionary.
    # st.write(st.session_state) # Simple dictionary print
    st.json({key: str(type(value)) for key, value in st.session_state.items()})
    st.write("Note: Values are shown by type to keep output brief. Use st.write(st.session_state) for full values if needed.")
    # Optionally, display specific keys more clearly
    # if "retriever" in st.session_state:
    #     st.write(f"Retriever: {type(st.session_state.retriever)}")
    # if "conversation_chain" in st.session_state:
    #      st.write(f"Conversation Chain: {type(st.session_state.conversation_chain)}")
    # if "messages" in st.session_state:
    #      st.write(f"Messages ({len(st.session_state.messages)}): {st.session_state.messages[-min(5, len(st.session_state.messages)):]} (last 5)")
