import streamlit as st
import pandas as pd
import json
import requests

# Specify the raw URLs of your data files
url_total_position = 'https://raw.githubusercontent.com/NathanLever7/FPLHead2HeadAnalysisDashboard/main/total_position.csv'
url_times_in_position = 'https://raw.githubusercontent.com/NathanLever7/FPLHead2HeadAnalysisDashboard/main/times_in_position.csv'
url_percentage_in_position = 'https://raw.githubusercontent.com/NathanLever7/FPLHead2HeadAnalysisDashboard/main/percentage_in_position.csv'
url_xPoints = 'https://raw.githubusercontent.com/NathanLever7/FPLHead2HeadAnalysisDashboard/main/xPoints.csv'
url_points_per_run = 'https://raw.githubusercontent.com/NathanLever7/FPLHead2HeadAnalysisDashboard/main/points_per_run.json'

# Load data
total_position = pd.read_csv(url_total_position)
times_in_position = pd.read_csv(url_times_in_position)
percentage_in_position = pd.read_csv(url_percentage_in_position)
xPoints = pd.read_csv(url_xPoints)

response = requests.get(url_points_per_run)
points_per_run = response.json()

# Create a title
st.title('FPL Head2Head Analysis')

# Display dataframes as tables
st.header('CHANGE PLEASE')
st.write(total_position)

st.header('Times in Position')
st.write(times_in_position)

st.header('Percentage in Position')
st.write(percentage_in_position)

st.header('xPoints')
st.write(xPoints)

import matplotlib.pyplot as plt
import seaborn as sns

st.header('Points Per Run Distribution')

# Select a player to display histogram
player = st.selectbox('Select a player', list(points_per_run.keys()))

# Create and display histogram for the selected player
sns.histplot(points_per_run[player], bins=10, kde=True)
st.pyplot(plt)
