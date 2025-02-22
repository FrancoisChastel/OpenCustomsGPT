import asyncio

import streamlit as st
from streamlit_pills import pills

from agents.setup import setup_group_chat
from cache import init


def main() -> None:
    init()    
    st.set_page_config(page_title="OpenCustomsGPT - Discuss with your dataset", page_icon="🤖")
    st.title("OpenCustomsGPT")

    if "team" not in st.session_state:
        st.session_state["team"] = setup_group_chat()
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # for message in st.session_state["messages"]:
    #     render_message(message)

    
    prompt = st.chat_input("Type a message...")
    pills(
        label="Select an agent",
        options=["Admin", "Data Analyst", "SQL Coder", "SQL Executor"],
        key="agent",
    )
    # if prompt:
    #     st.session_state["messages"].append({"role": "user", "content": prompt})
    #     with st.chat_message("user"):
    #         st.markdown(prompt)

    #     response = asyncio.run(st.session_state["agent"].chat(prompt))
    #     st.session_state["messages"].append({"role": "assistant", "content": response})
    #     with st.chat_message("assistant"):
    #         st.markdown(response)


if __name__ == "__main__":
    main()