from typing import List

from project.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players: List[Player] = []

    def add_player(self, player: Player):
        if player not in self.__players:
            self.__players.append(player)

            return f"Player {player.name} joined team {self.__name}"

        return f"Player {player.name} has already joined"

    def remove_player(self, player_name: str):
        try:
            player = next(filter(lambda x: x.name == player_name, self.__players))
        except StopIteration:
            return f"Player {player_name} not found"

        self.__players.remove(player)

        return player