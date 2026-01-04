# AI-Chat-assistant
An interactive AI chat assistant developed using Streamlit and the Groq API, leveraging the powerful LLaMA 3.3 70B language model. This application allows users to ask questions and receive intelligent, real-time responses through a clean and user-friendly web interface.

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
