import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import scipy.stats as stats
import duckdb
from datetime import datetime
# Cargar datos desde DuckDB 
@st.cache_data
def load_data():
    query = """
    SELECT * FROM 'cobertura_movil_definitivo.csv'
    """
    df = duckdb.query(query).to_df()
    return df

df = load_data()

st.header("Hacia una Antioquia conectada: Diagnóstico de la cobertura digital en zonas rurales y urbanas en el departamento de Antioquia durante el tercer  trimestre del año 2023.")
