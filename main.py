import pandas as pd
from football_data import Player, Club, League, Country, calculate_average_goals, export_analyzed_data
from visualization import visualize_top_scorers, visualize_shots_vs_goals

# Reading data from CSV file, and some error handling
file_path = "Data.csv"
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found. Please check the file path.")
except pd.errors.EmptyDataError:
    print("Error: The CSV file is empty.")
except pd.errors.ParserError:
    print("Error: Unable to parse the CSV file. Check if it's formatted correctly.")

# Converting data to a list of player dictionaries
player_data_list = df.to_dict(orient="records")

# Creating Player objects from the player data
players = [Player(player_data) for player_data in player_data_list]

# Calculating and printing average goals per player
average_goals = calculate_average_goals(players)
print(f"Average goals per player: {average_goals}")

# Exporting analyzed data to a CSV file
export_analyzed_data(players, "analyzed_data.csv")
print("Analyzed data exported to analyzed_data.csv")

# Organizing players into countries, leagues, and clubs
countries = {}
for player in players:
    if player.country not in countries:
        countries[player.country] = Country(player.country)
    country = countries[player.country]

    if player.league not in country.leagues:
        country.add_league(League(player.league))
    league = next((l for l in country.leagues if l.name == player.league), None)

    if player.club not in [c.name for c in league.clubs]:
        new_club = Club(player.club)
        league.add_club(new_club)
    else:
        new_club = next((c for c in league.clubs if c.name == player.club), None)

    if new_club is not None:
        new_club.add_player(player)

# Printing the organized structure
for country_name, country in countries.items():
    print(country)
    for league in country.leagues:
        print(f"  {league}")
        for club in league.clubs:
            print(f"    {club}")
            for player in club.players:
                print(f"      {player}")

# Visualizing top scorers and shots vs goals
visualize_top_scorers(players)
visualize_shots_vs_goals(players)
