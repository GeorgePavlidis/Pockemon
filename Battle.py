""""Create a Battle Class:

Develop a Python class named Battle that simulates a battle scenario between two players, each with a team of Pokémon.
Initialization:

Implement an __init__ method to initialize the Battle object with two players, available Pokémon, and an empty dictionary to store chosen Pokémon teams.
Choose Pokémon:

Create a method choose_pokemons to allow each player to choose two Pokémon from the available list.
Choose Pokémon Pair:

Implement a choose_pokemon_pair method to facilitate the selection of two Pokémon by each player.
Display Available Pokémon:

Develop a method display_available_pokemons to show the available Pokémon to choose from.
Start Battle:

Create a start_battle method to initiate the battle between the two players.
Players take turns choosing Pokémon and performing rounds until one player loses all Pokémon.
Round Mechanics:

Implement a perform_round method to simulate a round in the battle.
Players choose their Pokémon, attack type, and perform attacks on the opponent.
Determine Starting Player:

Create a determine_starting_player method to decide which player and Pokémon start the battle based on speed.
Choose Pokémon During Battle:

Allow players to change their chosen Pokémon during the battle if desired.
Player Has Lost Check:

Implement methods player1_has_lost and player2_has_lost to check if a player has lost all Pokémon.
Choose Pokémon Method:

Develop a choose_pokemon method to facilitate choosing a Pokémon from the player's team during battle rounds.
Attack Type Selection:

Create a choose_attack_type method to allow players to select the type of attack (simple or special) during battle rounds.
Battle Status Display:

Implement a display_battle_status method to show the current status of Pokémon for both players after each round.
Import Pokémon Class:

Import the previously created Pokemon class to use it in the battle simulation.
Randomization:

Use user input and randomization to introduce variability in Pokémon selection and attack outcomes."""


import Pokemon
class Battle:
    def __init__(self, player1, player2, available_pokemons):
        self.player1 = player1
        self.player2 = player2
        self.available_pokemons = available_pokemons
        self.pokemons = {}

    def choose_pokemons(self):
        print("Player 1, choose two Pokémon:")
        # TODO
        print("\nPlayer 2, choose two Pokémon:")
        # TODO
    def choose_pokemon_pair(self):
        chosen_pokemons = []
        self.display_available_pokemons()
        for i in range(2):
            print(f"Choose Pokémon {i + 1} from the available list:")
            #TODO
        return chosen_pokemons

    def display_available_pokemons(self):
        print("Available Pokémon:")
        # TODO

    def start_battle(self):
        print("\nBattle begins!")
        print(f"\n{self.player1}'s turn to choose Pokémon:")
        # TODO
        print(f"\n{self.player2}'s turn to choose Pokémon:")
        #TODO
        # Determine who starts the round based on speed
        # TODO

    def determine_starting_player(self):
        pass
        #TODO

    def choose_pokemon(self, pokemon_team):
        while True:
            print(f"Choose Pokémon from your team:")
            for i, pokemon in enumerate(pokemon_team):
                print(f"{i+1}. {pokemon.name} (HP: {pokemon.health})")

            choice = int(input("Enter the number of the Pokémon you want to use: "))
            if 1 <= choice <= len(pokemon_team):
                return pokemon_team[choice - 1]
            else:
                print("Invalid choice. Try again.")

    def perform_round(self, player, chosen_pokemon, opponent_pokemon):
        pass
        #TODO



    def choose_attack_type(self):
        while True:
            attack_type = input("Choose attack type simple or special (1 or 2): ").lower()
            if attack_type in ['1', '2']:
                if attack_type == 1:
                    return "simple"
                else:
                    return "special"

            else:
                print("Invalid attack type. Try again.")

    def display_battle_status(self):
        print("\n--- Battle Status ---")
        print(f"{self.player1}'s Pokémon:")
        for pokemon in self.pokemons[self.player1]:
            pokemon.display_info()
        print(f"\n{self.player2}'s Pokémon:")
        for pokemon in self.pokemons[self.player2]:
            pokemon.display_info()

    def player1_has_lost(self):
        pass
        #TODO
    def player2_has_lost(self):
        pass
        #TODO