# FPLHead2HeadAnalysisDashboard
Analysis of a Fantasy Premier League head to head league, which minimises the luck element by simulating 10,000 different player fixture lists.

To view the results, follow the link: https://fplhead2headanalysisdashboard-oqtxefe9p2lxlzxhhuwm78.streamlit.app/

To get this outcome, I ran the .ipynb file to get the results (using league ID 41583 as an input), and then the .py file to dashboard and visualise.

For pre-requisites, refer to the Requirements.txt file. These can be installed by running pip install -r requirements.txt in the terminal.

## Explanation:

In H2H leagues in Fantasy Premier League, you play against one other member of your league, based on a random fixture list generated when you set up the league. If you score more FPL points than this opponent, you will gain 3 league points. There is 1 for a draw, and 0 for a loss. Therefore, you league points are heavily influenced by the performance of your opponents - so the luck of the fixture list has a large impact.

To mitigate this, we pull the scored from the FPL API, and create a random fixture list, and simulate league results. This is done 10,000 times. The end result hopes to eliminate this aforementioned fixture list variance.


Contact nathanleversedge@gmail.com for more info.
