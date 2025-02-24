import asyncio
from typing import cast

import pandas as pd
import streamlit as st
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken
from requests import session
from streamlit.elements.plotly_chart import FigureOrData

from agents import cache
from agents.setup import setup_group_chat
from render.agents import TrackableGroupChatManager
from render.agents import render_message


if "cache" not in st.session_state:
    cache.init_cache()
    st.session_state["cache"] = cache.cached_variables

def main() -> None:
    st.set_page_config(page_title="OpenCustomsGPT - Discuss with Sydonia's data", page_icon="🚀")
    st.title("OpenCustomsGPT")

    if "dataframes" not in st.session_state:
        st.session_state["dataframes"] = []
    if "cached_variables" not in st.session_state:
        st.session_state["cached_variables"] = {}
    if "messages" not in st.session_state:
        st.session_state["messages"] = []
    if "team" not in st.session_state:
        st.session_state["team"] = setup_group_chat()
    if "loop" not in st.session_state:
        st.session_state["loop"] = asyncio.new_event_loop()
    if "can_write" not in st.session_state:
        st.session_state["can_write"] = True
    if "suggestion" not in st.session_state:
        st.session_state["suggestion"] = None
    if "suggestion_pill" not in st.session_state:
        st.session_state["suggestion_pill"] = None
    
    prompt = st.chat_input("Type a message...", disabled=not(st.session_state.can_write))

    def on_selected_suggestion():
      st.session_state.suggestion = st.session_state.suggestion_pill
      st.session_state.suggestion_pill = None

    options = ["Give me the biggest importer", "Write me an SQL query to get all the countries of origins", "Plot a bar chart for the 20 biggest importer of hscode starting with 1511"]
    st.pills("Example", options, selection_mode="single", on_change=on_selected_suggestion, key="suggestion_pill")

    prompt = st.session_state["suggestion"] if st.session_state["suggestion"] is not None else prompt

    for message_shape in st.session_state.messages:
      render_message(message_shape)
    if prompt is not None:
        st.session_state.can_write = False
        team = cast(TrackableGroupChatManager, st.session_state["team"])
        loop = cast(asyncio.AbstractEventLoop, st.session_state["loop"])
        loop.run_until_complete(team.run(
            session_state=st.session_state,
            task=[TextMessage(content=prompt, source="user")],
            cancellation_token=CancellationToken(),
        ))
        st.session_state.can_write = True
        st.session_state["suggestion"] = None
        prompt = None



if __name__ == "__main__":
  main()
                                