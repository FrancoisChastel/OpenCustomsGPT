# Copyright (C) 2025 Francois Chastel
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.


import pandas as pd
import streamlit as st
from plotly.graph_objs import Figure


class Message:
    def __init__(self, author: str):
        self.author = author

class AgentMessage(Message):
    def __init__(self, author: str, content: str):
        super().__init__(author)
        self.content = content
    
    def render(self):
        with st.expander(f"{self.author} has spoken"):
            st.markdown(self.content.strip())

class MainMesage(Message):
    def __init__(self, author: str, content: str):
        super().__init__(author)
        self.content = content
    
    def render(self):
        with st.chat_message(self.author):
            st.markdown(self.content.replace("APPROVE.", "").replace("APPROVE", "").strip())

class DataFrameMessage(Message):
    def __init__(self, author: str, dataframe: pd.DataFrame):
        super().__init__(author)
        self.dataframe = dataframe
    
    def render(self):
        with st.expander(f"See the dataset"):
            if self.dataframe is None or self.dataframe.empty:
                st.markdown("The dataset is empty.")
            else:
                st.dataframe(self.dataframe,     
                            selection_mode=["multi-row", "multi-column"])

class FunctionMessage(Message):
    def __init__(self, author: str, results: str):
        super().__init__(author)
        self.results = results
    
    def render(self):
        with st.expander(f"See results the excuted function ```{self.author}```"):
            st.json(self.results)

class PlotlyMessage(Message):
    def __init__(self, author: str, figure: Figure):
        super().__init__(author)
        self.figure = figure
    
    def render(self):
        st.plotly_chart(self.figure)
