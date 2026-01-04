# AI-Chat-assistant
An interactive AI-powered chatbot built with Streamlit and powered by Groq’s Llama models.

🚀 Live Demo
🔗 https://ai-chat-assistant-hetal.streamlit.app/

🧠 Features
Real-time conversational AI 
Powered by LLaMA 3.3–70B via Groq  
Fast inference with Groq’s LPU infrastructure  
Clean and user-friendly Streamlit UI  
Secure API key handling using st.secrets  
Easy to deploy and lightweight  

🛠️ Tech Stack  
Python  
Streamlit  
Groq API  
LLaMA 3.3 (70B)  

📂 Project Structure
├── app.py
├── requirements.txt
└── .streamlit
    └── secrets.toml



You said:
import streamlit as st
from groq import Groq

st.title("AI Chat Assistant 💬")

api_key = st.secrets["GROQ_API_KEY"]
prompt = st.text_area("Ask me anything:")

if st.button("Generate"):
    if not api_key:
        st.error("API key missing in secrets.")
    elif not prompt:
        st.warning("Enter a prompt first.")
    else:
        try:
            client = Groq(api_key=api_key)
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}]
            )
            st.success(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Error: {str(e)}")-----please i need git hub description
ChatGPT said:
Here’s a clean, professional GitHub repository description you can use for this project. I’ve also added a slightly longer README-style version in case you want it.

📌 Short GitHub Description (1–2 lines)
AI Chat Assistant built with Streamlit and Groq API, powered by LLaMA 3.3 (70B), enabling fast and interactive conversational AI via a simple web interface.

🧠 GitHub README Description (Recommended)
AI Chat Assistant 💬
An interactive AI chat assistant developed using Streamlit and the Groq API, leveraging the powerful LLaMA 3.3 70B language model. This application allows users to ask questions and receive intelligent, real-time responses through a clean and user-friendly web interface.

🚀 Features
Real-time AI-powered chat

Powered by LLaMA 3.3–70B via Groq

Simple and intuitive Streamlit UI

Secure API key management using st.secrets

Lightweight and easy to deploy

🛠️ Tech Stack
Python

Streamlit

Groq API

LLaMA 3.3 (70B)

📂 How It Works
User enters a prompt in the Streamlit interface

The prompt is sent to the Groq-hosted LLM

The AI-generated response is displayed instantly

🔐 Setup
Clone the repository

Install dependencies

pip install streamlit groq
Add your Groq API key to .streamlit/secrets.toml

GROQ_API_KEY="your_api_key_here"
Run the app

streamlit run app.py
💼 Resume-Friendly One-Liner (Bonus)
Developed an AI chat assistant using Streamlit and Groq API with LLaMA 3.3–70B, delivering fast and interactive conversational AI through a web-based interface.

If you want, I can also:

Write GitHub topics/tags

Optimize this for recruiter appeal

Add screenshots section

Convert this into a portfolio-ready README

Just tell me 👍

You said:
readme ready
ChatGPT said:
Perfect 👍
Here is a fully ready, copy-paste GitHub README.md for your project.

AI Chat Assistant 💬
An interactive AI Chat Assistant built using Streamlit and the Groq API, powered by the LLaMA 3.3 (70B) large language model. This application enables users to ask questions and receive intelligent, real-time responses through a simple and clean web interface.

🚀 Live Demo
🔗 

🧠 Features
Real-time conversational AI

Powered by LLaMA 3.3–70B via Groq

Fast inference with Groq’s LPU infrastructure

Clean and user-friendly Streamlit UI

Secure API key handling using st.secrets

Easy to deploy and lightweight

🛠️ Tech Stack
Python

Streamlit

Groq API

LLaMA 3.3 (70B)

📂 Project Structure
├── app.py
├── requirements.txt
└── .streamlit
    └── secrets.toml
⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/ai-chat-assistant.git
cd ai-chat-assistant

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Configure API Key
Create a file at:
.streamlit/secrets.toml
Add your Groq API key:
GROQ_API_KEY = "your_groq_api_key_here"

4️⃣ Run the Application
streamlit run app.py

🧪 How It Works
User enters a prompt in the chat input
The prompt is sent to Groq’s LLaMA 3.3–70B model
The model generates a response
The response is displayed instantly on the UI

💡 Use Cases
General Q&A assistant
Learning and research support
AI chatbot demo for portfolios
LLM experimentation with Groq

📌 Future Enhancements
Chat history support
Streaming responses
Role-based prompts (system/user)
UI enhancements
Multi-model selection

👤 Author
Hetal
Aspiring Data Scientist | ML & AI Enthusiast

⭐ If you like this project
Give it a ⭐ on GitHub — it helps a lot!
