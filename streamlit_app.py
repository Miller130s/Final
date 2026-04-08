from importlib.metadata import metadata
import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts
import numpy as np
from scipy import stats
import pydeck as pdk
from PIL import Image




st.title("Manning Prediction Model")

st.markdown(
""" Overview
- What is the current trend of Space launch
- How will it impact both coasts
- What is mission assurance
- Why mission assurance standards needs to be kept the same
- Our recommendations to each squadron to prepare for more Space flight
"""
)

# page_1 = st.Page("pages/page_1.py", title="Page 1")

# page_nav = st.navigation(["pages/page_1.py"])

# page_nav.run()