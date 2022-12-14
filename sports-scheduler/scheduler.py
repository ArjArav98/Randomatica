import random
from typing import Type, List

#------
# TYPES
#------

class Constraints:
        concurrent_matches: int
        teams_per_match: int
        players_per_team: int
        available_mins: int
        mins_per_match: int 

        def __init__(   self,
                        concurrent_matches: int,
                        teams_per_match: int,
                        players_per_team: int,
                        available_mins: int,
                        mins_per_match: int) -> None:
                self.concurrent_matches = concurrent_matches
                self.teams_per_match = teams_per_match
                self.players_per_team = players_per_team
                self.available_mins = available_mins
                self.mins_per_match = mins_per_match

class Player:
        name: str
        matches_played: int

        def __init__(self, name: str) -> None:
                self.name = name
                self.matches_played = 0

        def __repr__(self):
                return repr(self.name)

        def __str__(self):
                return str(self.name)

        def increment_matches_played(self) -> None:
                self.matches_played += 1
                return None

Team = List[Player]
Match = List[Team]
Round = List[Match]

#testConstraints = Constraints(concurrent_matches=2, teams_per_match=2, players_per_team=2, available_mins=30, mins_per_match=10)
#testPlayers = [Player(1,"1"), Player(2,"2"), Player(3,"3"), Player(4,"4"), Player(5,"5"), Player(6,"6"), Player(7,"7"), Player(8,"8"), Player(9,"9"), Player(10,"10")]
#testConstraints1 = Constraints(concurrent_matches=1, teams_per_match=2, players_per_team=1, available_mins=30, mins_per_match=10)

_constraints = Constraints(concurrent_matches=2, teams_per_match=2, players_per_team=2, available_mins=180, mins_per_match=18)
_players = [
    Player("Shah_Rukh_Khan"),
    Player("Salman_Khan"),
	Player("Deepika_Padukone"),
	Player("Aishwarya_Rai"),
	Player("Rajinikanth"),
	Player("Kamal_Hasan")
]

#----------------
# UTILITY CLASSES
#----------------

class Counter:
        count: int

        def __init__(self) -> None:
                self.count = 0
        
        def __call__(self) -> int:
                self.count += 1
                return self.count

#----------
# FUNCTIONS
#----------

def schedule_rounds(
        players: List[Player],
        constraints: Constraints) -> List[Round]:
 
        maximum_rounds = constraints.available_mins // constraints.mins_per_match
        
        return  [schedule_matches_for_round(players, constraints)
                        for i in range(0, maximum_rounds)] 

def schedule_matches_for_round(
        players: List[Player],
        constraints: Constraints) -> Round:

        selected_players = select_players_for_round(players, constraints)
        generated_teams = generate_teams(selected_players, constraints)
        matches = organise_matches(generated_teams, constraints)

        return matches

def select_players_for_round(
        players: List[Player],
        constraints: Constraints) -> List[Player]:

        players_to_pick = (
                constraints.concurrent_matches *
                constraints.teams_per_match *
                constraints.players_per_team)

        max_matches_played_yet = get_max_matches_played_yet(players)
 
        played_players = [player for player in players
                                if player.matches_played >= max_matches_played_yet]
        waiting_players = [player for player in players
                                if player.matches_played < max_matches_played_yet]

        waiting_players_are_sufficient = len(waiting_players) >= players_to_pick
        player_vacancies_count = players_to_pick - len(waiting_players)

        selected_players = (
                random.sample(
                        waiting_players,
                        k=players_to_pick) if waiting_players_are_sufficient
                else random.sample(
                        played_players,
                        k=player_vacancies_count) + waiting_players)

        if len(selected_players) != players_to_pick:
                raise ValueError(
                        "The number of players \
                        picked is {0}".format(len(selected_players)))

        for player in selected_players:
                player.increment_matches_played()

        return selected_players

def generate_teams(
        selected_players: List[Player],
        constraints: Constraints) -> List[Team]:

        selected_players_count = len(selected_players)
        players_per_team = constraints.players_per_team
        teams_to_generate = selected_players_count // players_per_team

        if selected_players_count % players_per_team != 0:
                raise ValueError(
                        "The selected player count, {0}, must be \
                        evenly divisible by the players-per-team, \
                        {1}".format(selected_players_count, players_per_team))

        return [selected_players[i*players_per_team :
                                (i*players_per_team)+players_per_team]
                                for i in range(0, teams_to_generate)]

def organise_matches(
        generated_teams: List[Team],
        constraints: Constraints) -> List[Match]:

        generated_teams_count = len(generated_teams)
        teams_per_match = constraints.teams_per_match
        matches_to_organise = generated_teams_count // teams_per_match

        if generated_teams_count % teams_per_match != 0:
                raise ValueError(
                        "The generated teams count, {0}, must be \
                        evenly divisible by the teams-per-match, \
                        {1}".format(generated_teams_count, teams_per_match))

        return [generated_teams[i*teams_per_match :
                                (i*teams_per_match)+teams_per_match]
                                for i in range(0, matches_to_organise)]

def get_max_matches_played_yet(players: List[Player]) -> int:
        max_comparison_key = lambda player: player.matches_played
        return max(players,key=max_comparison_key).matches_played

def format_team(team: Team) -> str:
        return "({0})".format(", ".join([str(player) for player in team]))

def display(rounds: List[Round]):
        roundCounter = Counter()
        matchCounter = Counter()

        for round in rounds:
                print("===============")
                print("#===ROUND {0}===#".format(roundCounter()))
                print("===============\n")

                for match in round:
                        print("Match {0}: ".format(matchCounter()), end='')
                        print("  vs  ".join([format_team(team) for team in match]))

                print("")
