import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import os

def visualize_top_scorers(players, top_n=10):
    # Extracting information for the top scorers
    top_scorers = sorted(players, key=lambda x: x.goals, reverse=True)[:top_n]
    player_names = [player.player_name for player in top_scorers]
    goals = [player.goals for player in top_scorers]

    # Creating a bar plot for top scorers
    plt.figure(figsize=(10, 6))
    sns.barplot(x=goals, y=player_names, palette="viridis")
    plt.title(f'Top 8 Goal Scorers')
    plt.xlabel('Goals')
    plt.ylabel('Player Names')
    
    # Saving the plot in the 'figures' folder
    plt.savefig(os.path.join('figures', 'top_scorers.png'))
    
    plt.show()

def visualize_shots_vs_goals(players):
    # Extracting information for shots vs goals
    shots = [getattr(player, 'shots', 0) for player in players]
    goals = [getattr(player, 'goals', 0) for player in players]
    league = [getattr(player, 'league', 'Unknown') for player in players]

    # Creating a scatter plot for shots vs goals using Plotly
    df = pd.DataFrame({"Shots": shots, "Goals": goals, "League": league})
    fig = px.scatter(df, x="Shots", y="Goals", color="League", title='Shots vs Goals')

    # Saving the plot in the 'figures' folder
    fig.write_html(os.path.join('figures', 'shots_vs_goals_interactive.html'))

    # Showing the plot in a separate window
    fig.show()
