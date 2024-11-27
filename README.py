import streamlit as st
import pandas as pd
import plotly.express as px  # Ensure this is installed and listed in requirements.txt

# Load and prepare data (mock data; replace with actual data)
df = pd.DataFrame({
    "Branch": ["Shradhapuri Phase 2", "MPS Main Wing", "Samsara", "MPGS Meerut Public Girls School", "MPS The First Step Shradhapuri"],
    "Re-Learning Avg": [92.24, 84.65, 72.27, 73.84, 72.29],
    "Overall Avg": [85.535, 78.6, 70.3, 73.84, 72.3],
    "Impact Data": [82.36, 47.07, 53.59, 69.73, 64.06],
    "Students >75%": [64.57, 53.39, 35.59, 27.51, 36.46],
    "Students <
