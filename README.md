# AI-CHATBOT
A Streamlit-based chatbot powered by the DeepSeek-R1:1.5b model via Ollama, running entirely locally with memory support.


🤖 Nexa AI – Local Chatbot with DeepSeek-R1:1.5b & Ollama
Nexa AI is a lightweight chatbot application built using Streamlit for the frontend and Ollama to run the DeepSeek-R1:1.5b language model locally. No cloud APIs or external servers required!

🔧 Features
🧠 Local chatbot powered by DeepSeek-R1:1.5b via Ollama

💬 Streamlit-based web interface with conversation history

🔁 Session memory maintained across chat turns

🖱️ One-click chat clearing

✅ Private and fully offline

🚀 Getting Started
Requirements
Python 3.9+

Streamlit

Ollama

DeepSeek-R1:1.5b model (installed via Ollama)

Installation:
bash

git clone https://github.com/yourusername/nexa-ai.git
cd nexa-ai
pip install -r requirements.txt
Run the App
Start Ollama and make sure the DeepSeek model is available:

bash

ollama run deepseek-r1:1.5b
Launch the chatbot:

bash

streamlit run app.py
📺 Demo
Watch a quick video demo here (link to your demo video on LinkedIn or YouTube)

📌 Notes
Ensure Ollama is running locally

Tested with DeepSeek-R1:1.5b; other models may be used by modifying the model name

📚 Tech Stack
Streamlit (UI)

Ollama (LLM backend)

DeepSeek-R1:1.5b

