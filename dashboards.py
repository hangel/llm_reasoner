import os
root = os.path.join(os.path.dirname(__file__))

DASHBOARDS = {
    "**ST_GROQ_DOCUMENTER**[st_groq_documenter.py]":     os.path.join(root, "st_groq_documenter.py"),
    #"**SCAN FILESYSTEM PANDAS**[st_scanfs_pl.py]"  :     os.path.join(root, "st_scan_fs_Gemini25Flash_000.py"),
    "**SCAN FILESYSTEM**[st_scanfs_pl.py]"         :     os.path.join(root, "st_scanfs_pl.py"),
    "**CLIP_MVP**"                                 :     os.path.join(root, "st_CLIP_MVP_Flash25_000.py"),
    #"ST_MERMAID_MANUAL [st_mermaid_020.py]*****"   :     os.path.join(root, "st_mermaid_020.py"),
    "**ST_MERMAID**[st_mermaid_refactored.py]"     :     os.path.join(root, "st_mermaid_refactored.py"),
    "**FREEMIND via Sax[prueba_sax.py]*****"        :     os.path.join(root, "prueba_sax.py"),
    "**update_mm.py**"                             :     os.path.join(root, "update_mm.py"),
    "**ST MCP** [streamlit_app.py]"                :     os.path.join(root, "streamlit_app.py"),
    "**COCO LLM** [st_coco_llm.py]"                :     os.path.join(root, "st_coco_llm.py"),
}

