import streamlit as st
import pandas as pd
import json
import requests
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

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

st.write("Skip to the bottom for a more comprehensive explanation")

# Display dataframes as tables
st.header('Average Position')
st.write(total_position)

st.markdown("""
On average, this is the position that each team finished in.
""")


st.header('Times in Position')
st.write(times_in_position)

st.markdown("""
From 10,000 simulations, this is the frequency that each team finished in each position.
""")


# Display Percentage in Position as data tables
st.header('Percentage in Position')
st.write(percentage_in_position)

st.markdown("""
This is the percentage that each team finishes in each position.
""")


selected_player_percentage = st.selectbox('Select a player for Percentage in Position', list(points_per_run.keys()))

for index, row in percentage_in_position.iterrows():
    if row[0] == selected_player_percentage:
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(percentage_in_position.columns[1:], row[1:], color='blue')  # Change color for Percentage in Position
        ax.set_title(row[0])
        ax.set_xlabel('Finishing Position')
        ax.set_ylabel('Percentage Chance')
        st.pyplot(fig)

    # Clear the current figure to avoid interfering with sns.histplot
    plt.clf()


st.header('xPoints')
st.write(xPoints)

st.markdown("""
This is the average amount of points that each team accumulates.
""")


st.header('Points Per Run Distribution')

# First, determine the overall range for the x-axis
all_points = []
for player_points in points_per_run.values():
    all_points.extend(player_points)
min_points, max_points = min(all_points), max(all_points)

# Setting up a 3x2 grid of subplots
fig, axes = plt.subplots(3, 2, figsize=(15, 10))  # Adjust figsize as needed
fig.suptitle('Points Per Run Distribution for All Players')

# Flatten the axes array for easy iteration
axes = axes.flatten()

for idx, (player, runs) in enumerate(points_per_run.items()):
    # Calculate frequencies
    point_frequencies = Counter(runs)
    points = list(point_frequencies.keys())
    frequencies = list(point_frequencies.values())

    # Plotting
    axes[idx].bar(points, frequencies, color='green')
    axes[idx].set_xlabel('Points')
    axes[idx].set_ylabel('Frequency')
    axes[idx].set_title(player)
    axes[idx].set_xlim(min_points, max_points)  # Set the same x-axis scale for all plots

# Adjust layout to prevent overlap
plt.tight_layout()
plt.subplots_adjust(top=0.9)  # Adjust the top spacing to accommodate the main title
st.pyplot(fig)


# Method Explanation
st.markdown("""
## Explanation:

In H2H leagues in Fantasy Premier League, you play against one other member of your league, based on a random fixture list generated when you set up the league. If you score more FPL points than this opponent, you will gain 3 league points. 1 is gained for a draw, and 0 for a loss. Therefore, your league points are heavily influenced by the performance of your opponents - so the luck of the fixture list has a large impact.

To mitigate this, we pull the scores from the FPL API, create a random fixture list, and simulate league results. This is done 10,000 times. The end result hopes to eliminate the aforementioned fixture list variance.

Contact nathanleversedge@gmail.com for more info.

Last updated: 02/11/2023 11:41
""")

