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
            st.markdown(self.content)

class MainMesage(Message):
    def __init__(self, author: str, content: str):
        super().__init__(author)
        self.content = content
    
    def render(self):
        with st.chat_message(self.author):
            st.markdown(self.content.replace("APPROVE", ""))

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
