import pandas as pd

# Defining a class for representing football players
class Player:
    def __init__(self, player_data):
        try: # Attempting to extract player information from the provided data dictionary and some error handling
            self.country = player_data.get('Country', '')
            self.league = player_data.get('League', '')
            self.club = player_data.get('Club', '')
            self.player_name = player_data.get('Player Names', '')
            self.matches_played = player_data.get('Matches_Played', 0)
            self.substitution = player_data.get('Substitution', 0)
            self.minutes = player_data.get('Mins', 0)
            self.goals = player_data.get('Goals', 0)
            self.xG = player_data.get('xG', 0.0)
            self.xG_per_avg_match = player_data.get('xG Per Avg Match', 0.0)
            self.shots = player_data.get('Shots', 0)
            self.on_target = player_data.get('OnTarget', 0)
            self.shots_per_avg_match = player_data.get('Shots Per Avg Match', 0.0)
            self.on_target_per_avg_match = player_data.get('On Target Per Avg Match', 0.0)
            self.year = player_data.get('Year', 0)

        except KeyError as e:
            print(f"Error: Missing key '{e}' in player data. Please check the data format.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def __str__(self):
        # Defining a string representation for the player object
        return f"{self.player_name} - {self.club}, {self.league}, {self.country} ({self.year})"

# Defining a function to calculate the average goals for a list of players
def calculate_average_goals(players):
    total_goals = sum(player.goals for player in players)
    total_players = len(players)
    return total_goals / total_players if total_players > 0 else 0

# Defining a function to export analyzed player data to a CSV file
def export_analyzed_data(players, export_path="analyzed_data.csv"):
    try:
        analyzed_data = {
            'Player Names': [player.player_name for player in players],
            'Goals': [player.goals for player in players],
            'Average Goals': [player.goals / player.matches_played if player.matches_played > 0 else 0 for player in players],
        }

        # Attempting to create a DataFrame and save it to a CSV file
        analyzed_df = pd.DataFrame(analyzed_data)
        analyzed_df.to_csv(export_path, index=False)

        print(f"Analyzed data exported to {export_path}")

    except pd.errors.EmptyDataError:
        print("Error: No data to export.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Defining a class to represent a football club
class Club:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        # Adding a player to the club's list of players
        self.players.append(player)

    def __str__(self):
        # Defining a string representation for the club object
        return f"Club: {self.name}"

# Defining a class to represent a football league
class League:
    def __init__(self, name):
        self.name = name
        self.clubs = []

    def add_club(self, club):
        # Adding a club to the league's list of clubs
        self.clubs.append(club)

    def __str__(self):
        # Defining a string representation for the league object
        return f"League: {self.name}"

# Defining a class to represent a country
class Country:
    def __init__(self, name):
        self.name = name
        self.leagues = []

    def add_league(self, league):
        # Adding a league to the country's list of leagues
        self.leagues.append(league)

    def __str__(self):
        # Defining a string representation for the country object
        return f"Country: {self.name}"
