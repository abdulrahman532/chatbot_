import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000/api/chat"

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Abdulrahman Hamada")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Thinking..."):
        payload = {
            "messages": st.session_state.messages,
            "user_id": "current_user"
        }
        
        response = requests.post(BACKEND_URL, json=payload)
        ai_response = response.json().get("answer", "No response")
        
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        with st.chat_message("assistant"):
            st.markdown(ai_response)