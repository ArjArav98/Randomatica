import random
from typing import Type, List

#------
# TYPES
#------

class Constraints:
        concurrent_games: int
        teams_per_game: int
        players_per_team: int
        available_mins: int
        mins_per_game: int 

        def __init__(   self,
                        concurrent_games: int,
                        teams_per_game: int,
                        players_per_team: int,
                        available_mins: int,
                        mins_per_game: int) -> None:
                self.concurrent_games = concurrent_games
                self.teams_per_game = teams_per_game
                self.players_per_team = players_per_team
                self.available_mins = available_mins
                self.mins_per_game = mins_per_game

class Player:
        id: int
        name: str
        games_played: int

        def __init__(self, id: int, name: str) -> None:
                self.id = id
                self.name = name
                self.games_played = 0

        def increment_games_played() -> None:
                self.games_played += 1
                return None

Team = List[Player]
Game = List[Team]
Round = List[Game]

#----------
# FUNCTIONS
#----------

def schedule_rounds(     players: List[Player],
                        constraints: Constraint) -> List[Round]:
 
        maximum_rounds = available_mins // mins_per_game
        
        games = [schedule_round(players, constraints, game)
                        for round in range(0, maximum_rounds)] 

def schedule_round(     players: List[Player],
                        constraints: Constraint,
                        current_round: int) -> Round:

        # we calc num of players to select
        # we get the players who are yet to play a game
        # how do we determine who is yet to play?
        #
        players_to_pick = concurrent_games * teams_per_game * players_per_team
        rounds_played_yet = max_rounds_played_yet(players)

        unplayed_player_ids = [player.id for player in players
                                if player.games_played < rounds_played_yet]

        


def max_rounds_played_yet(players: List[Player]) -> int:
        max_comparison_key = lambda player: player.games_played
        return max(players,key=max_comparison_key)













        

        unplayed_player_ids = [player.id for player in players 
                                if player.games_played < current_game]
        played_player_ids

        # if unplayed players insufficient, pick remaining from played players pool
        # if not, pick from unplayed players pool

        

        insufficient_players = len(unplayed_player_ids) < players_to_pick
        remaining_players_to_pick
        
        

        selected_player_ids = [*unplayed_players_ids] 
                                if insufficient_players else








        selected_players_ids = (unplayed_players_ids + 

        for player in players:
                if player.id in random_players_ids:
                        player.increment_games_played()
