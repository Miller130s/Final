from importlib.metadata import metadata
import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts
import numpy as np
from scipy import stats
import pydeck as pdk
from PIL import Image




st.title("Manning Prediction Model")


page_1 = st.page("pages/page_1.py", title="Page 1")

