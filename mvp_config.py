# mvp_config.py
import os
from pathlib import Path

# --- General App Configuration ---
MVP_VERSION = "0.0.0.1"
PAGE_TITLE = f"COBOLpro MVP Preview by OKRocket® Platform v{MVP_VERSION}"
PAGE_ICON = "assets/images/COBOLpro/COBOLpro_icon.png"
HELP_URL = 'https://www.extremelycoolapp.com/help'
BUG_URL = "https://www.extremelycoolapp.com/bug"
ABOUT_TEXT = f"[**COBOLpro** MVP Preview](https://www.cobolpro.com) SERVICES MVP v{MVP_VERSION} Preview!"

# --- Asset Paths ---
# Assuming 'assets' directory is relative to the main script location
ASSETS_DIR = Path("assets/images")
LOGOS = {
    "COBOLagency_vertical": ASSETS_DIR / "COBOLagency/COBOL_FullLockup-White_VERTICAL.png",
    "COBOLpro_vertical": ASSETS_DIR / "COBOLagency/COBOLpro_Vertical_FullLockup.png",
    "COBOLAGENCY_QR": ASSETS_DIR / "COBOLagency/COBOLagency_QR.png",
    "COBOLpro_QR": ASSETS_DIR / "COBOLpro/COBOLpro_QR.png",
    "OLLAMA_LOGO": ASSETS_DIR / "OllamaLogo_S.png",
    "OKROCKET_LOGO": ASSETS_DIR / "OKRocket_Rocket_Logo.png",
    "OKR_LOGO_3x3": ASSETS_DIR / "OKR_VerdeMosaico_3x3.png",
}
CARD_DEMO='/home1/hugo/PycharmProjects/okrocket/cobol/code/aws-mainframe-modernization-carddemo'
# Define which logo to use in the sidebar
SIDEBAR_LOGO_KEY = "COBOLpro_QR" # Or "OKR_LOGO_3x3", etc.

# --- Base Directory ---
# Assumes config.py is in the same directory as the main app script
APP_ROOT_DIR = Path(__file__).parent.resolve()

# --- Dashboard / Module Definitions ---
# Centralized dictionary for module selection
# Using APP_ROOT_DIR ensures paths are correct regardless of where the script is run from
DASHBOARDS = {
    # Key: Display name in the sidebar selector
    # Value: Absolute path to the script file
    "**FREEMIND** via Sax[prueba_sax.py]*****": APP_ROOT_DIR / "prueba_sax.py",
    "Update form MM[update_mm.py]*": APP_ROOT_DIR / "update_mm.py",
    "**ST GROQ COBOL DOCUMENTER** ***** [st_groq_documenter.py]": APP_ROOT_DIR / "st_groq_documenter.py",
    "**ST_MERMAID_MANUAL** [st_mermaid_020.py]*****": APP_ROOT_DIR / "st_mermaid_020.py",
    "**ST_SCAN FILESYSTEM** [st_scan_fs.py]*****": APP_ROOT_DIR / "st_scan_fs.py",
    "**ST PHIDATA_GROQ**[st_phidata_groq_000.py]*": APP_ROOT_DIR / "st_phidata_groq_000.py",
    "**ST AUTHENTICATOR**[st_authenticator_000.py]*": APP_ROOT_DIR / "st_authenticator_000.py",
    "**OLLAMA STREAM** [st_stream_001.py]": APP_ROOT_DIR / "st_stream_001.py",
    "**ST DocChatbot**[st_DocChat_000.py]*": APP_ROOT_DIR / "st_DocChat_000.py",
    "**COBOLagency Deep Dive** ***** [st_deepdive.py]": APP_ROOT_DIR / "st_deepdive.py",
    "**FILE_TREE** ***** [st_file_tree.py]": APP_ROOT_DIR / "st_file_tree.py",
    "**ST-WebGL CODE VIEWER** [st_webgl.py]*****": APP_ROOT_DIR / "st_webgl.py",
    "**ST FLOW MODIFY** ***** [st_flow_modify.py]": APP_ROOT_DIR / "st_flow_modify.py",
    "**ST FLOW** ***** [st_flow_000.py]": APP_ROOT_DIR / "st_flow_000.py",
    "**ST FLOW MARKDOWN** ***** [st_flow_md_000.py]": APP_ROOT_DIR / "st_flow_md_000.py",
    "**ST GROQ COBOL Analyzer & Reasoner Preview** ***** [st_groq_agent_preview.py]": APP_ROOT_DIR / "st_groq_agent_preview.py",
    "**ST PYLASU PARSER** ***** [st_pylasu_000.py]": APP_ROOT_DIR / "st_pylasu_000.py",
    "**ST GROQ Agentic AGI** ***** [st_Agentic_AGI.py]": APP_ROOT_DIR / "st_Agentic_AGI.py",
    "**ST DEEPSEEK_V25** ***** [st_deepseek_v25_000.py]": APP_ROOT_DIR / "st_deepseek_v25_000.py",
    "**ST-CODE EDITOR** [st_codeeditor_000.py]*****": APP_ROOT_DIR / "st_codeeditor_000.py",
    "**FastAPI VectorDB** [st_vectordb.py]*****": APP_ROOT_DIR / "st_vectordb.py",
    "**SPLITCODE TEST** [st_splitcode_000.py]*****": APP_ROOT_DIR / "st_splitcode_000.py",
    "**BERT keyword extractor** [bert_app.py]*****" : APP_ROOT_DIR / "bert_app.py",
    "**EMBEDDINGS TEST** [st_embedding_test.py]*****" : APP_ROOT_DIR / "st_embedding_test.py",
    "**AGRAPH Code Visualization**[st_agraph.py] ***": APP_ROOT_DIR / "st_agraph.py",
    "**ST_MERMAID** [st_mermaid.py]*****": APP_ROOT_DIR / "st_mermaid.py",
    "**ST CEREBRAS** ***** [st_cerebras_000.py]": APP_ROOT_DIR / "st_cerebras_000.py",
    "**ST CEREBRAS ASYNC** ***** [st_cerebras_async_000.py]": APP_ROOT_DIR / "st_cerebras_async_000.py",
    "**ST CEREBRAS STREAM** ***** [st_cerebras_stream_000.py]": APP_ROOT_DIR / "st_cerebras_stream_000.py",
    "**ST_PYGMENS** [st_pygmens.py]*****": APP_ROOT_DIR / "st_pygmens.py",
    "**ST_INSTRUCTOR** [st_instructor_iterable_000.py] *****" : APP_ROOT_DIR / "st_instructor_iterable_000.py",
    "Demo **NLP spaCy** [spacy-demo.py] *****" : APP_ROOT_DIR / "spacy-demo.py",
    "**ST GROQ MODELS** ***** [st_groq_models.py]": APP_ROOT_DIR / "st_groq_models.py",
    "**ST GROQ AGENT DEMO** ***** [st_groq_agent_demo.py]": APP_ROOT_DIR / "st_groq_agent_demo.py",
    "**ST GROQ MoA DEMO** ***** [st_groq-MoA.py]": APP_ROOT_DIR / "st_groq-MoA.py",
    "**ST GROQ BASE** ***** [st_groq_base_000.py]": APP_ROOT_DIR / "st_groq_base_000.py",
    "**ST GROQ G1 APP Reasoner** ***** [g1/app.py]": APP_ROOT_DIR / "g1/app.py",
    "**ST GROQ CLOUD BASE** ***** [st_groq_cloud_000.py]": APP_ROOT_DIR / "st_groq_cloud_000.py",
    "**ST LLM CHAT** ***** [st_llm_chat_000.py]": APP_ROOT_DIR / "st_llm_chat_000.py",
    "**DEVIN BABYCODER** [st_devin_babycoder.py]": APP_ROOT_DIR / "st_devin_babycoder.py",
    "**ANALYZE COBOL CODE** [st_analyzeCobol_000.py]": APP_ROOT_DIR / "st_analyzeCobol_000.py",
    # Re-added duplicated entry as per original file
    "**ST GROQ MODELS** [st_groq_models.py]": APP_ROOT_DIR / "st_groq_models.py",
    "**ST GROQ** [st_groq_000.py]": APP_ROOT_DIR / "st_groq_000.py",
    "**ST GROQ WHISPER** [st_groq_whisper_000.py]": APP_ROOT_DIR / "st_groq_whisper_000.py",
    "**GROQ** [groq_000.py]": APP_ROOT_DIR / "groq_000.py",
    "**ST-GROQ-LChain** [st_groq_langchain_aichat.py]": APP_ROOT_DIR / "st_groq_langchain_aichat.py",
    "**ST-EXPERIMENTAL-DIALOG** [st_experimental_dialog_000.py]": APP_ROOT_DIR / "st_experimental_dialog_000.py",
    "**DeepSeekCodev2LiteInstruct** [st_deepseekcoderV2LiteInstruct.py]": APP_ROOT_DIR / "st_deepseekcoderV2LiteInstruct.py",
    "**NVIDIA NIM's MIXTRAL** [st_mixtral_nim_000.py]": APP_ROOT_DIR / "st_mixtral_nim_000.py",
    "**NVIDIA NIM's UDIO** [st_UDIO_nim_000.py]": APP_ROOT_DIR / "st_UDIO_nim_000.py",
    "**NVIDIA NIM's EMBED QA** [st_nvidia_embed_qa_nim_000.py]": APP_ROOT_DIR / "st_nvidia_embed_qa_nim_000.py",
    "**ANTHROPIC CLAUDE CACHING** [st_AnthropicPromptCaching_000.py]": APP_ROOT_DIR / "st_AnthropicPromptCaching_000.py",
    "**ANTHROPIC CLAUDE CHAT** [st_claude_chatbot.py]": APP_ROOT_DIR / "st_claude_chatbot.py",
    "**ANTHROPIC TOOLS** [st_anthropic_tools_000.py]": APP_ROOT_DIR / "st_anthropic_tools_000.py",
    "**ANTHROPIC CLAUDE** [st_anthropic_000.py]": APP_ROOT_DIR / "st_anthropic_000.py",
    "**ANTHROPIC PROMPT** [st_anthropic_prompt_000.py]": APP_ROOT_DIR / "st_anthropic_prompt_000.py",
    "**ANTHROPIC CLAUDE STUDIO** [st_claudestudio_000.py]": APP_ROOT_DIR / "st_claudestudio_000.py",
    "**LLAMA_CPP** [st_llama_cpp.py]": APP_ROOT_DIR / "st_llama_cpp.py",
    "**GEMINI PRO CHAT** [st_gemini_pro_chat_000.py]": APP_ROOT_DIR / "st_gemini_pro_chat_000.py",
    "**GEMINI PRO VISION** [st_geminipro_vision.py]": APP_ROOT_DIR / "st_geminipro_vision.py",
    "**GEMINI PRO** [st_geminipro_start.py]": APP_ROOT_DIR / "st_geminipro_start.py",
    "**GEMINI WIKIPEDIA** [st_gemini_wikipedia.py]": APP_ROOT_DIR / "st_gemini_wikipedia.py",
    # Re-added duplicated entry as per original file
    "**OLLAMA STREAM** [st_stream_001.py]": APP_ROOT_DIR / "st_stream_001.py",
    "**OLLAMA ALL** [st_ollama_all.py]": APP_ROOT_DIR / "st_ollama_all.py",
    "**OLLAMA ASYNC** [st_async_001.py]": APP_ROOT_DIR / "st_async_001.py",
    "**__ST2ST_Menu__**[st2st/st2st.py]*": APP_ROOT_DIR / "st2st/inventory/navigation-pages/add_book.py", # Path seems potentially incorrect based on key
    "**__ST2ST_Inventory__**[st_inventory.py]*": APP_ROOT_DIR / "st_inventory.py",
    "**ST FEEDBACK EXAMPLE** [st_examples.py]": APP_ROOT_DIR / "st_examples.py",
    "**ST FEEDBACK BUTTON EXAMPLE** [st_feedback_button.py]": APP_ROOT_DIR / "st_feedback_button.py",
    "Simple Login[st_login_000.py]*": APP_ROOT_DIR / "st_login_000.py",
    "NO SSO Login[st_no_sso_000.py]*": APP_ROOT_DIR / "st_no_sso_000.py",
    "NO SSO Individual Login[st_no_sso_000.py]*": APP_ROOT_DIR / "st_no_sso_individual_000.py", # Key indicates different file than value
    "**GOOGLE OAuth**[st_oauth_000.py]*": APP_ROOT_DIR / "st_oauth_000.py",
    "**ST LLM Chat Stream** [st_LLMchat_stream_000.py]": APP_ROOT_DIR / "st_LLMchat_stream_000.py",
    "**HF IBM_Granite-3B [st_HF_IBM_granite-3b-code-it_000.py]**": APP_ROOT_DIR / "st_HF_IBM_granite-3b-code-it_000.py",
    "**HUGGINGFACE StarCoder2-3B [st_starcoder2-3b.py]**": APP_ROOT_DIR / "st_starcoder2-3b.py",
    "**HUGGINGFACE StarCoder2-15b [st_starcoder2-15b.py]**": APP_ROOT_DIR / "st_starcoder2-15b.py",
    "**HUGGINGFACE QWENCOBOL 4 AI** [st_HF_QWEN_COBOL4AI_Generate.py]": APP_ROOT_DIR / "st_HF_QWEN_COBOL4AI_Generate.py",
    "__HUGGINGFACE Evaluate LLM's__ [st_evaluate_LLM_000.py]": APP_ROOT_DIR / "st_evaluate_LLM_000.py",
    "__HUGGINGFACE Pickle [st_hf_pickle.py]__": APP_ROOT_DIR / "st_hf_pickle.py",
    "**ST_RAWBERRY** [st_rawberry.py]*****": APP_ROOT_DIR / "st_rawberry.py",
    "**ST_RAWBERRY CLAUDE** [st_rawberry_claude.py]*****": APP_ROOT_DIR / "st_rawberry_claude.py",
    "**ST_RAWBERRY GROQ** [st_rawberryst_rawberry_groq.py]*****": APP_ROOT_DIR / "st_rawberry_groq.py", # Typo in key?
    "**ST_RAWBERRY GROQ WEB** [st_rawberryst_rawberry_groq2.py]*****": APP_ROOT_DIR / "st_rawberry_groq2.py", # Typo in key?
    "**ST_RAWBERRY GROQ 3** [st_rawberryst_rawberry_groq3.py]*****": APP_ROOT_DIR / "st_rawberry_groq3.py", # Typo in key?
    "**ST_RAWBERRY GEMINI** [st_rawberryst_rawberry_gemini.py]*****": APP_ROOT_DIR / "st_rawberry_gemini.py", # Typo in key?
    "**ST_RAWBERRY GRANITE** [st_rawberryst_rawberry_granite2.py]*****": APP_ROOT_DIR / "st_rawberry_granite2.py", # Typo in key?
    "**ST_RAWBERRY PHI3.1** [st_rawberryst_rawberry_phi31.py]*****": APP_ROOT_DIR / "st_rawberry_phi31.py", # Typo in key?
    "**__QR SEGNO__**[st_qr_segno_000.py]*": APP_ROOT_DIR / "st_qr_segno_000.py",
    "**__QR VCARD__**[st_segno_vcard.py]*": APP_ROOT_DIR / "st_segno_vcard.py",
    "**ST.WRITE_STREAM** [st_write_stream.py]": APP_ROOT_DIR / "st_write_stream.py",
    "**PHOTOSYNTHESIS** [st_photosynthesis.py]": APP_ROOT_DIR / "st_photosynthesis.py",
    "MixedBread [mixedbread_000.py]": APP_ROOT_DIR / "mixedbread_000.py",
    "Empty placeholder[st_empty.py]": APP_ROOT_DIR / "st_empty.py",
    "Update form from DRAW.IO[*****]": APP_ROOT_DIR / "update_drawio.py",
    "Paginada Ses-State CACHED [***]": APP_ROOT_DIR / "paginated_session_state.py",
    "NLP Text Analysis [AI_TextAnalysis.py]*" : APP_ROOT_DIR / "AI_TextAnalysis.py",
    "Bertopic 000 - GPU" : APP_ROOT_DIR / "bertopic_000.py",
    "Bertopic 010" : APP_ROOT_DIR / "bertopic_010.py",
    "Bertopic 020" : APP_ROOT_DIR / "bertopic_020.py",
    "Demo AI2 Biotech / Sci spaCy [*****]" : APP_ROOT_DIR / "scispacy-demo.py",
    "Summarizer [o, ¿API de Resoomer?]" : APP_ROOT_DIR / "summarizer.py",
    "Sumy Summarizer [*****]" : APP_ROOT_DIR / "sumy_summarizer.py",
    "Wikipedia Summarizer": APP_ROOT_DIR / "summarizer_00.py",
    "Scrapping de Resoomer  [*****]" : APP_ROOT_DIR / "resoomer_scrap.py",
    "Google Sheet Example [*****]" : APP_ROOT_DIR / "google-sheet.py",
    "Google Sheet Ubidots [*****]" : APP_ROOT_DIR / "google-sheet-ubidots.py",
    "Google Trends [*****]" : APP_ROOT_DIR / "pygoogletrends.py",
    "Using Custom Cell Renderer [cell_renderer_class_example.py ***]": APP_ROOT_DIR / "cell_renderer_class_example.py",
    "CSV Wrangler) [example_app_csv_wrangler/app.py***] " : APP_ROOT_DIR / "example_app_csv_wrangler/app.py",
    "Uso de Anidación de Tablas [nested_grids.py**]" : APP_ROOT_DIR / "nested_grids.py",
    "Demo Charts ST [**]": APP_ROOT_DIR / "demo_charts.py",
    "ST-Card [**]": APP_ROOT_DIR / "st_card.py",
    "Multiple Input CACHED [*****]": APP_ROOT_DIR / "pages/multiple_input.py", # Path seems potentially incorrect ('pages/')
    "Generate Article from Prompt": APP_ROOT_DIR / "generateArticle.py",
    "ST-Code-Generator [**]": APP_ROOT_DIR / "streamlit_app_local.py",
    "ST-Pydantic": APP_ROOT_DIR / "pydantic_000.py",
    "ST-Pydantic Model": APP_ROOT_DIR / "st_model.py",
    "PDF Certificate Generator [**]": APP_ROOT_DIR / "pdf_report/pdf_report.py",
    "Data labeling": APP_ROOT_DIR / "labelling.py",
    "Theming & Pre-Selection": APP_ROOT_DIR / "themes_and_pre_selection.py",
    "Multiple Form _ Advanced DF Analysis [***]" : APP_ROOT_DIR / "multiple_form.py",
    # Add any other modules from the original list here...
    # Commented out sections from original are omitted unless needed
}

# --- System Info Tables (Example, if needed elsewhere) ---
SYS_TABLES_INFO = [
    {'table': 'sqlite_master', 'description': 'Master listing of all database objects...'},
    {'table': 'sqlite_sequence', 'description': 'Lists the last sequence number...'},
    {'table': 'sqlite_stat1', 'description': 'This table is created by the ANALYZE command...'}
]


