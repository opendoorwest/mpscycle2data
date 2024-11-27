import streamlit as st
import pandas as pd
import plotly.express as px

# Load and prepare data (mock data; replace with actual data)
df = pd.DataFrame({
    "Branch": ["Shradhapuri Phase 2", "MPS Main Wing", "Samsara", "MPGS Meerut Public Girls School", "MPS The First Step Shradhapuri"],
    "Re-Learning Avg": [92.24, 84.65, 72.27, 73.84, 72.29],
    "Overall Avg": [85.535, 78.6, 70.3, 73.84, 72.3],
    "Impact Data": [82.36, 47.07, 53.59, 69.73, 64.06],
    "Students >75%": [64.57, 53.39, 35.59, 27.51, 36.46],
    "Students <40%": [0.00, 0.00, 33.99, 1.21, 2.53]
})

# Grade-wise data (mock data; replace with actual data)
grade_df = pd.DataFrame({
    "Branch": ["Shradhapuri Phase 2", "MPS Main Wing", "Samsara", "MPGS Meerut Public Girls School", "MPS The First Step Shradhapuri"],
    "Grade": ["Grade 3", "Grade 4", "Grade 3", "Grade 4", "Grade 5"],
    "Subject": ["Math", "Science", "Science", "Math", "Math"],
    "Re-Learning Avg": [99.38, 86.22, 72.27, 74.925, 67.275]
})

# Dashboard Layout
st.title("Branch Performance Dashboard")

# KPI Section
st.header("Key Performance Metrics")
st.metric("Top Re-Learning Improvement Branch", "Shradhapuri Phase 2", "92.24")
st.metric("Branch with Best Average", "Shradhapuri Phase 2", "85.535")
st.metric("Branch with Highest Impact Data", "Shradhapuri Phase 2", "82.36%")
st.metric("Grade with Highest Re-learning Avg", "Grade 3", "76.263")

# Rankings Section
st.header("Performance Rankings")
# Re-Learning Average Rankings
ranking_chart = px.bar(df, y="Branch", x="Re-Learning Avg", orientation="h", title="Re-Learning Average Rankings", color="Re-Learning Avg")
st.plotly_chart(ranking_chart)

# Overall Average Rankings
overall_chart = px.bar(df, y="Branch", x="Overall Avg", orientation="h", title="Overall Average Rankings", color="Overall Avg")
st.plotly_chart(overall_chart)

# Impact Data Rankings
impact_chart = px.bar(df, y="Branch", x="Impact Data", orientation="h", title="Impact Data Rankings", color="Impact Data")
st.plotly_chart(impact_chart)

# Grade-Specific Insights
st.header("Grade-Specific Insights")
selected_grade = st.selectbox("Select Grade", grade_df["Grade"].unique())
grade_filtered = grade_df[grade_df["Grade"] == selected_grade]
grade_chart = px.bar(grade_filtered, x="Branch", y="Re-Learning Avg", color="Subject", barmode="group", title=f"Re-Learning Averages for {selected_grade}")
st.plotly_chart(grade_chart)

# Branch-Specific Insights
st.header("Branch-Specific Insights")
selected_branch = st.selectbox("Select Branch", df["Branch"])
branch_data = df[df["Branch"] == selected_branch]
branch_pie = px.pie(
    values=[
        branch_data["Students >75%"].values[0],
        100 - branch_data["Students >75%"].values[0] - branch_data["Students <40%"].values[0],
        branch_data["Students <40%"].values[0],
    ],
    names=[">75%", "40-75%", "<40%"],
    title=f"Performance Breakdown for {selected_branch}"
)
st.plotly_chart(branch_pie)
