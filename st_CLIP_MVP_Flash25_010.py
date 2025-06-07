# [CLIP MVP Using Gemini Flash 2.5](https://gemini.google.com/app/2458c7da9ababb3d)
import streamlit as st
import os
# Import necessary components from Langchain and Google GenAI
# Note: Specific imports might vary slightly based on Langchain version
# and whether you use google-generativeai directly or via langchain_google_genai
from langchain.text_splitter import RecursiveCharacterTextSplitter # Using common splitter, NLTKTextSplitter could be used for shorter texts
#from langchain_community.embeddings import GoogleGenerativeAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate

# Set up the Google API Key
# Ensure GOOGLE_API_KEY environment variable is set
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("Google API Key not found. Please set the GOOGLE_API_KEY environment variable.")
    st.stop()

# --- Constants and Configuration ---
# Model name for Gemini 2.5 Flash
MODEL_NAME = "gemini-1.5-flash"
# Embedding model name
EMBEDDING_MODEL = "models/embedding-001" # A common embedding model for Gemini

# --- Session State Initialization ---

def initialize_session_state(documentation_text: str):
    """
    Initializes the Streamlit session state, processing the input text
    into a searchable vector store and setting up the conversation chain.
    """
    # Check if state is already initialized
    if "retriever" not in st.session_state or "conversation_chain" not in st.session_state:
        st.info("Processing documentation and setting up AI assistant...")
        try:
            # 1. Text Splitting
            # Using RecursiveCharacterTextSplitter; NLTKTextSplitter is an alternative
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len,
                is_separator_regex=False,
            )
            texts = text_splitter.split_text(documentation_text)
            if not texts:
                st.error("No text chunks were created from the documentation. Please check the input.")
                return False

            # 2. Creating Embeddings
            # Using Google's embedding model
            embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL, google_api_key=api_key)

            # 3. Creating Vector Store (FAISS in memory)
            # Creating the FAISS index from the text chunks and embeddings
            vectorstore = FAISS.from_texts(texts, embeddings)
            st.session_state.retriever = vectorstore.as_retriever()

            # 4. Setting up the LLM (Gemini 2.5 Flash)
            llm = ChatGoogleGenerativeAI(model=MODEL_NAME, google_api_key=api_key, temperature=0.3)

            # 5. Setting up Memory for Conversation History
            # Using ConversationBufferMemory to store chat history
            st.session_state.chat_history_memory = ConversationBufferMemory(
                memory_key="chat_history",
                return_messages=True
            )

            # 6. Creating the Conversational Retrieval Chain (RAG)
            # This chain combines the retriever and the LLM for RAG functionality
            # A custom prompt can be added here to guide the LLM's behavior
            # based on the context of understanding COBOL systems.
            # Example prompt structure:
            custom_prompt_template = """Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question.
Or, if the user is providing new context, just output the context.

Chat History:
{chat_history}
Follow Up Input: {question}
Standalone question:"""

            standalone_question_prompt = PromptTemplate.from_template(custom_prompt_template)

            st.session_state.conversation_chain = ConversationalRetrievalChain.from_llm(
                llm=llm,
                retriever=st.session_state.retriever,
                memory=st.session_state.chat_history_memory,
                # Use the rephrased question for retrieval
                # Pass the rephrased question to the combine_docs_chain
                # This setup might need adjustment based on specific Langchain version and desired prompt structure
                # For simplicity in MVP, let's rely on the default behavior or add context via prompt template to the LLM directly
                # Reverting to a simpler chain setup for MVP:
                # You might need to adjust the chain type or add custom steps for sophisticated prompting/rephrasing
                # Let's use the memory directly with a standard retrieval chain that considers history implicitly
                # Or stick to ConversationalRetrievalChain which handles rephrasing internally
                # Re-using the standard ConversationalRetrievalChain which is designed for this:
                 combine_docs_chain_kwargs={"prompt": PromptTemplate(template="""You are an AI assistant helping to understand a COBOL legacy system based on provided documentation.
Answer the user's question based *only* on the provided context.
If the answer cannot be found in the context, truthfully say that you don't know or that the information is not available in the provided documentation.
Do not make up information.
Context: {context}
Question: {question}
Answer:""", input_variables=["context", "question"])}
            )


            # Initialize chat history in session state if it doesn't exist
            if "messages" not in st.session_state:
                st.session_state.messages = []

            st.success("AI assistant initialized successfully!")
            return True

        except Exception as e:
            st.error(f"An error occurred during initialization: {e}")
            # Clean up partial state if error occurs
            if "retriever" in st.session_state: del st.session_state.retriever
            if "conversation_chain" in st.session_state: del st.session_state.conversation_chain
            if "chat_history_memory" in st.session_state: del st.session_state.chat_history_memory
            return False

    return True # State was already initialized


# --- Streamlit App ---

# --- Streamlit Page Configuration ---
# Set the page title and default layout to wide
st.set_page_config(
    page_title="CLIP Outline COBOLpro Legacy Intelligent Platform MVP",
    layout="wide" # This makes the page default to wide layout
)

st.title("CLIP Outline COBOLpro Legacy Intelligent Platform MVP")
st.subheader("Intelligent Assistant for COBOL Legacy Systems")


st.markdown("""
This MVP helps you understand and troubleshoot a COBOL legacy system based on documentation you provide.
Input your system documentation below, and then ask questions in the chat interface.
""")

# Input area for legacy system documentation
documentation_input = st.text_area(
    "Paste your COBOL system documentation/context here:",
    height=300,
    key="documentation_text",
    help="Include relevant program descriptions, JCL, database layouts, incident reports, etc."
)

# Button to process documentation (optional, can also trigger on text_area change/submit implicitly)
# For simplicity, we'll trigger initialization when text_area has content and chat starts.
# Or, we can initialize when the text area content changes and is non-empty.
# Let's add a simple check and initialization trigger here.

if documentation_input:
    initialization_successful = initialize_session_state(documentation_input)
    if not initialization_successful:
        st.warning("Please resolve the initialization error before proceeding.")
        st.stop()
elif "retriever" in st.session_state:
    # If documentation is cleared after initialization, clear state
    st.warning("Documentation removed. Clearing assistant state.")
    del st.session_state.retriever
    del st.session_state.conversation_chain
    del st.session_state.chat_history_memory
    if "messages" in st.session_state: del st.session_state.messages
    st.experimental_rerun() # Rerun to clear the chat interface

# --- Chat Interface ---

# Display chat messages from history on app rerun
for message in st.session_state.get("messages", []):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input for user questions
if documentation_input and "conversation_chain" in st.session_state:
    prompt = st.chat_input("Ask a question about the COBOL system documentation...")
    if prompt:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get AI response using the RAG chain
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    # The ConversationalRetrievalChain requires the user's question
                    # and the current chat history from the memory object.
                    # It handles retrieving relevant documents and generating a response.
                    # We pass the new question and the existing chat history managed by the memory.
                    # The .invoke() method is preferred in newer Langchain versions.
                    # Ensure the input keys match what the chain expects ('question').
                    response = st.session_state.conversation_chain.invoke({"question": prompt})
                    # The output key of ConversationalRetrievalChain is typically 'answer'
                    ai_response = response.get("answer", "Could not retrieve an answer.")

                    st.markdown(ai_response)
                    # Add assistant response to chat history
                    st.session_state.messages.append({"role": "assistant", "content": ai_response})

                except Exception as e:
                    st.error(f"An error occurred while generating response: {e}")
                    st.markdown("I'm sorry, I couldn't process that request.")

elif not documentation_input:
    st.info("Please paste your COBOL system documentation above to begin.")

# Note on Libraries:
# This code assumes compatibility with recent versions of `langchain`,
# `langchain-community`, and `langchain-google-genai`.
# Ensure these are installed:
# pip install streamlit langchain langchain-community langchain-google-genai faiss-cpu sentence-transformers google-generativeai
# (sentence-transformers might be needed by some embedding models, though google-generativeai handles its own)
# (faiss-cpu is for the in-memory vector store)

# To run this script:
# 1. Save it as a Python file (e.g., clip_outline_mvp.py).
# 2. Set your Google API Key environment variable: export GOOGLE_API_KEY='YOUR_API_KEY'
# 3. Run from your terminal: streamlit run clip_outline_mvp.py
