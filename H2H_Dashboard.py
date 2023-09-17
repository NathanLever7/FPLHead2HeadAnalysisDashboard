import streamlit as st
import pandas as pd
import json
import requests
from datetime import datetime
import matplotlib.pyplot as plt

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

# Get the current date and time
last_updated_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Create a title
st.title('FPL Head2Head Analysis')

# Display dataframes as tables
st.header('Average Position')
st.write(total_position)

st.header('Times in Position')
st.write(times_in_position)

# Display Percentage in Position as data tables
st.header('Percentage in Position')
st.write(percentage_in_position)


for index, row in percentage_in_position.iterrows():
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(percentage_in_position.columns[1:], row[1:])
    ax.set_title(row[0])
    ax.set_xlabel('Finishing Position')
    ax.set_ylabel('Percentage Change')
    st.pyplot(fig)

st.header('xPoints')
st.write(xPoints)

st.header('Points Per Run Distribution')

# Select a player to display histogram
player = st.selectbox('Select a player', list(points_per_run.keys()))

# Create and display histogram for the selected player
sns.histplot(points_per_run[player], bins=10, kde=True)
st.pyplot(plt)




# Method Explanation
st.markdown("""
## Method Explanation:

In H2H leagues in Fantasy Premier League, you play against one other member of your league, based on a random fixture list generated when you set up the league. If you score more FPL points than this opponent, you will gain 3 league points. There is 1 for a draw, and 0 for a loss. Therefore, your league points are heavily influenced by the performance of your opponents - so the luck of the fixture list has a large impact.

To mitigate this, we pull the scores from the FPL API, create a random fixture list, and simulate league results. This is done 10,000 times. The end result hopes to eliminate the aforementioned fixture list variance.

Contact nathanleversedge@gmail.com for more info.

**Last Updated:** {}
""".format(last_updated_time))

