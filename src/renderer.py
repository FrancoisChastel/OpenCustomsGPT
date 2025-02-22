import streamlit as st


class Message:
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content
    
    def render(self):
        if self.role == "user":
            with st.chat_message("user"):
                st.markdown(self.content)
        elif self.role == "assistant":
            with st.chat_message("assistant"):
                st.markdown(self.content)                
                st.markdown(self.content)