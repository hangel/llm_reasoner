import streamlit as st
#from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from dotenv import load_dotenv
import os
import requests
import json
import uuid
import time
#from werkzeug.utils import secure_filename

# Load environment variables from .env file (if it exists)
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("COCO_SECRET_KEY", "dev_key_for_coco_llm")

# Directory for COBOL file uploads and other app data
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'cbl', 'cob', 'cobol', 'txt'}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Ensure other necessary directories exist
for directory in ['static/logs', 'static/temp']:
    os.makedirs(directory, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# API Proxy Configuration
MCP_PORT = os.getenv("MCP_PORT", 5001)
SENSO_PORT = os.getenv("SENSO_PORT", 6001)
LLM_PORT = os.getenv("LLM_PORT", 7001)

# Use localhost for internal service communication
MCP_HOST = os.getenv("MCP_HOST", "localhost") 
SENSO_HOST = os.getenv("SENSO_HOST", "localhost")
LLM_HOST = os.getenv("LLM_HOST", "localhost")

@app.route('/')
def home():
    return render_template('index.html')

HOLD_001 = """
# Redirect old routes to the main interface
@app.route('/agent-manager')
def agent_manager():
    return redirect(url_for('home'))

@app.route('/monitoring')
def monitoring():
    return redirect(url_for('home'))

@app.route('/cobol-analyzer')
def cobol_analyzer():
    return redirect(url_for('home'))

# MCP API Proxy Routes
@app.route('/api/mcp/status/all')
def mcp_status_all():
    try:
        response = requests.get(f"http://{MCP_HOST}:{MCP_PORT}/status/all")
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/mcp/start/<server>')
def mcp_start_server(server):
    try:
        response = requests.get(f"http://{MCP_HOST}:{MCP_PORT}/start/{server}")
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/mcp/stop/<server>')
def mcp_stop_server(server):
    try:
        response = requests.get(f"http://{MCP_HOST}:{MCP_PORT}/stop/{server}")
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/mcp/status/<server>')
def mcp_server_status(server):
    try:
        response = requests.get(f"http://{MCP_HOST}:{MCP_PORT}/status/{server}")
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# SENSO Parser API Proxy Routes
@app.route('/api/senso/health')
def senso_health():
    try:
        response = requests.get(f"http://{SENSO_HOST}:{SENSO_PORT}/health")
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/senso/translate', methods=['POST'])
def senso_translate():
    try:
        response = requests.post(
            f"http://{SENSO_HOST}:{SENSO_PORT}/translate",
            json=request.json
        )
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# LLM Agent API Proxy Routes
@app.route('/api/llm/health')
def llm_health():
    try:
        response = requests.get(f"http://{LLM_HOST}:{LLM_PORT}/health")
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/llm/analyze', methods=['POST'])
def llm_analyze():
    try:
        response = requests.post(
            f"http://{LLM_HOST}:{LLM_PORT}/analyze",
            json=request.json
        )
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/cobol/upload', methods=['POST'])
def upload_cobol():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    if file and allowed_file(file.filename):
        job_id = str(uuid.uuid4())
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{job_id}_{filename}")
        file.save(file_path)
        
        # Create a job record
        job_data = {
            "job_id": job_id,
            "filename": filename,
            "file_path": file_path,
            "status": "queued",
            "created_at": time.time()
        }
        
        # Store job info (in a real app, this would go to a database)
        with open(f"{app.config['UPLOAD_FOLDER']}/{job_id}.json", 'w') as f:
            json.dump(job_data, f)
        
        # Trigger LLM analysis in the background
        try:
            # Send to LLM service for processing
            with open(file_path, 'r') as f:
                cobol_code = f.read()
            
            # Make API call to LLM agent
            response = requests.post(
                f"http://{LLM_HOST}:{LLM_PORT}/analyze",
                json={"text": cobol_code, "job_id": job_id, "type": "cobol"}
            )
            
            if response.status_code == 200:
                return jsonify({"job_id": job_id, "status": "processing"})
            else:
                return jsonify({"error": "LLM processing error", "details": response.text}), 500
                
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    return jsonify({"error": "Invalid file type"}), 400

@app.route('/api/cobol/job/<job_id>')
def get_job_status(job_id):
    try:
        with open(f"{app.config['UPLOAD_FOLDER']}/{job_id}.json", 'r') as f:
            job_data = json.load(f)
        return jsonify(job_data)
    except FileNotFoundError:
        return jsonify({"error": "Job not found"}), 404

@app.route('/api/cobol/jobs')
def list_jobs():
    jobs = []
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        if filename.endswith('.json'):
            with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'r') as f:
                jobs.append(json.load(f))
    return jsonify(jobs)

@app.route('/info')
def info():
    return jsonify({
        "name": "COCO LLM",
        "description": "A Large Language Model for Mainframe Modernization",
        "version": "1.0.0",
        "components": [
            {"name": "Main API", "port": os.environ.get("PORT", 5000)},
            {"name": "MCP Control", "port": MCP_PORT},
            {"name": "SENSO Parser", "port": SENSO_PORT},
            {"name": "LLM Agent", "port": LLM_PORT}
        ]
    })

@app.route('/cobol-analyzer')
def cobol_analyzer():
    return render_template('cobol_analyzer.html')

@app.route('/documentation/<job_id>')
def view_documentation(job_id):
    try:
        with open(f"{app.config['UPLOAD_FOLDER']}/{job_id}.json", 'r') as f:
            job_data = json.load(f)
        
        # If documentation exists, render it
        doc_path = f"{app.config['UPLOAD_FOLDER']}/{job_id}_documentation.json"
        if os.path.exists(doc_path):
            with open(doc_path, 'r') as f:
                documentation = json.load(f)
            return render_template('documentation.html', job=job_data, documentation=documentation)
        else:
            return render_template('documentation.html', job=job_data, documentation=None)
    except FileNotFoundError:
        return redirect(url_for('home'))
        
@app.route('/api/cobol/documentation/<job_id>')
def get_documentation(job_id):
    try:
        doc_path = f"{app.config['UPLOAD_FOLDER']}/{job_id}_documentation.json"
        if os.path.exists(doc_path):
            with open(doc_path, 'r') as f:
                documentation = json.load(f)
            return jsonify(documentation)
        else:
            return jsonify({"error": "Documentation not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
"""

import time  # Add this import at the top

if __name__ == '__main__':
    # Use port 5000 for development
    port = int(os.environ.get("PORT", 4000))
    max_port_attempt = 5
    
    # Try to find an available port
    for attempt in range(max_port_attempt):
        try:
            app.run(host="0.0.0.0", port=port, debug=True)
            break
        except OSError as e:
            if "Address already in use" in str(e) and attempt < max_port_attempt - 1:
                st.write(f"Port {port} is in use, trying port {port+1}")
                port += 1
            else:
                raise

