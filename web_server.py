from flask import Flask, request, jsonify
import requests
import time
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # ✅ Allow all origins by default

# Temp memory to store AI replies (simulate cache)
last_ai_response = {}

# ---------- CONFIG (SETUP) ----------
URL = 'https://cloud.uipath.com/cloudnfxpxxr/DefaultTenant/orchestrator_/'
TOKEN = 'rt_5F1B89F956A03A391AFD44B62576F87E3175C99270C65982759342F8712D0D0C-1'
FOLDER_NAME = "AI.Integration"
HEARDERS = {
    "Authorization": "Bearer " + TOKEN,
    "X-UIPATH-OrganizationUnitId": "6669357",
    "Content-Type": "application/json"
}


# ---------- WEBHOOK 1: Chat → Flask ----------
@app.route('/webhook', methods=['POST'])
def handle_webhook():
    try:
        data = request.get_json()
        print("Received from ChatAgent:", data)

        # Extract user input
        user_text = data.get('chatInput', {})

        session_id = data.get('sessionId', 'anonymous-session')

        print(f"User text: {user_text} | Session: {session_id}")

        # Clear any previous response
        last_ai_response[session_id] = None
    
        # Trigger UiPath with session ID and user input
        start_orchestrator(user_text, session_id)
        
        # Wait max 10s for UiPath to respond
        waited = 0
        while waited < 10:
            res_ai = last_ai_response.get(session_id)
            if res_ai:
                print("Response received from UiPath!")
                return jsonify({
                    "output": res_ai
                }), 200
                break

            time.sleep(1)
            waited += 1

        print("Timeout waiting for UiPath response")
        return jsonify({
            "output": "Sorry, I'm still processing your request. Please try again."
        }), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"message": "Error processing webhook"}), 500


# ---------- WEBHOOK 2: UiPath → Flask (AI Reply) ----------
@app.route('/receive-reply', methods=['POST'])
def receive_reply():
    data = request.get_json()
    print("Received AI Reply from UiPath:", data)

    ai_response = data.get("response")
    session_id = data.get("session_id", "anonymous-session")

    last_ai_response[session_id] = ai_response

    print("Session id inside flask: " + session_id)
    print(last_ai_response[session_id])

    return jsonify({
        "status": "received",
        "session_id": session_id
    }), 200

# ---------- Trigger UiPath ----------
def start_orchestrator(user_text, session_id):
    # Get Release Key dynamically
    release_key = "c58f0f39-010e-4630-9e4d-b0fde7d6eed4"

    endpoint = "/odata/Jobs/UiPath.Server.Configuration.OData.StartJobs"
    full_url = URL + endpoint

    input_args = {
        "input_user": user_text,
        "session_id": session_id
    }

    payload = {
        "startInfo": {
            "ReleaseKey": release_key,
            "Strategy": "ModernJobsCount",
            "InputArguments": json.dumps(input_args)
        }
    }

    res = requests.post(full_url, json=payload, headers=HEARDERS)
    print(f"Triggered UiPath: {res.status_code}")
    return res

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
