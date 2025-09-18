# Project Title

Chatbot-Driven UiPath Automation via Flask API Bridge
## 📝 Project Description

This project integrates a chatbot interface with a Flask-based backend that acts as a communication bridge to UiPath Orchestrator. When users interact with the chatbot, their input is sent to the Flask API, which then triggers a UiPath robot to process the request. Once the UiPath robot completes its task, the result is returned back through the Flask API to the chatbot in near real time.

This solution enables dynamic and intelligent automation triggered by natural language conversation.

## 🎯 Project Objective

To build a seamless interaction flow where a user can engage with a chatbot to trigger complex automation tasks powered by UiPath, and receive timely responses—creating a unified interface for human-to-robot collaboration.

Key Goals:

✅ Integrate chatbot input with backend automation logic

✅ Use Flask to communicate securely with UiPath Orchestrator API

✅ Run UiPath jobs based on user input and session context

✅ Receive and return results from UiPath to the chatbot

✅ Maintain scalability and modularity for future workflow expansion

## Tools Used in This Project
### 1. ChatAgent.dev

Purpose: Web-based chat interface to test and simulate chatbot webhook endpoints.

Role: Debug and test Flask webhooks (/webhook and /receive-reply) without building a frontend.

Website: chatagent.dev

### 2. Flask (Python Web Framework)

Purpose: Backend REST API server handling chatbot requests and UiPath callbacks.

Role: Receives chat input, triggers UiPath jobs, manages session state, returns responses.

IDE: Visual Studio Code

Dependencies: Flask, requests, flask-cors

### 3. UiPath Studio

Purpose: Robotic Process Automation (RPA) development environment.

Role: Automates business workflows triggered by Flask API calls.

Outputs: XAML workflows, project.json, robot packages.

### 4. UiPath Orchestrator (Cloud Service)

Purpose: Cloud-based job scheduling and robot management platform.

Role: Runs UiPath robot jobs on demand, triggered by Flask API, returns output to Flask via webhook.

### 5. GitHub

Purpose: Version control and source code repository hosting.

Role: Stores and manages both Flask backend and UiPath project files in one repo.

Features: Online code editing, file uploads, branching, collaboration.

### 6. Ngrok (Optional)

Purpose: Create secure tunnels exposing local Flask server to the internet.

Role: Makes your local Flask API accessible by UiPath Orchestrator and ChatAgent.dev during development.

### 7. Development Tools

VS Code: Primary code editor for Python and UiPath scripts.

## Process Map
<img width="1485" height="730" alt="image" src="https://github.com/user-attachments/assets/1749ad48-d821-41d2-95cc-57eaad140f1c" />
