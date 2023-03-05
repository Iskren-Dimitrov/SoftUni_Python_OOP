'''You are tasked to create two classes: a Player class and a Guild class.

The Player class should receive a name (string), a hp (int), and a mp (int) upon initialization.\
The Player also has 2 instance attributes: skills (empty dictionary that will contain the skills\
of each player and its mana cost) and a guild set to "Unaffiliated" by default.
The Player class should also have two additional methods:
-	add_skill(skill_name, mana_cost)
o	Adds the skill and the corresponding mana cost to the dictionary of skills.\
Returns "Skill {skill_name} added to the collection of the player {player_name}"
o	If the skill is already in the collection, returns "Skill already added"
-	player_info()
o	Returns the player's information, including their skills, in this format:
"Name: {player_name}
 Guild: {guild_name}
 HP: {hp}
 MP: {mp}
 ==={skill_name_1} - {skill_mana_cost}
 ==={skill_name_2} - {skill_mana_cost}
 …
 ==={skill_name_N} - {skill_mana_cost}"

The Guild class receives a name (string).\
The Guild should also have one instance attribute players (an empty list which will contain the players of the guild).\
The class also has 3 additional methods:
-	assign_player(player: Player)
o	Adds the player to the guild and returns "Welcome player {player_name} to the guild {guild_name}".\
Remember to change the player's guild in the player class.
o	If he is already in the guild, returns "Player {player_name} is already in the guild."
o	If the player is in another guild, returns "Player {player_name} is in another guild."
-	kick_player(player_name: str)
o	Removes the player from the guild and returns "Player {player_name} has been removed from the guild.".\
Remember to change the player's guild in the player class to "Unaffiliated".
o	If there is no such player in the guild, returns "Player {player_name} is not in the guild."
-	guild_info()
o	Returns the guild's information, including the players in the guild, in the format:
"Guild: {guild_name}
{first_player's info}
…
{Nplayer's info}"
'''

from typing import List
from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player) -> str:
        if player in self.players:
            return f"Player {player.name} is already in the guild."

        if player.guild != Player.NOT_IN_OTHER_GUILD_WORD:
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name

        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str) -> str:
        try:
            player = [p for p in self.players if p.name == player_name][0]
        except IndexError:
            return f"Player {player_name} is not in the guild."

        self.players.remove(player)
        player.guild = Player.NOT_IN_OTHER_GUILD_WORD

        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        players_info = '\n'.join([p.player_info() for p in self.players])

        return f"Guild: {self.name}\n" \
               f"{players_info}"


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
