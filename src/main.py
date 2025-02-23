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
    st.set_page_config(page_title="OpenCustomsGPT - Discuss with Sydonia's data", page_icon="🤖")
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
    
    prompt = st.chat_input("Type a message...", disabled=not(st.session_state.can_write))

    options = ["Give me the biggest importer", "Write me an SQL query to get all the countries of origins", "Plot a bar chart for the biggest importer of hscode starting with 1511"]
    selection = st.pills("Example", options, selection_mode="single")

    prompt = selection if selection else prompt

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
        selection = None
        prompt = None



if __name__ == "__main__":
  main()
                                