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
            st.error(f"Error: {str(e)}")
