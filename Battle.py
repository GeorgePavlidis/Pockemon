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
        """
        Initialize the Battle class with players and available Pokémon.

        Args:
        - player1 (str): Name of the first player.
        - player2 (str): Name of the second player.
        - available_pokemons (dict): Dictionary of available Pokémon.
        """
        self.player1 = player1
        self.player2 = player2
        self.available_pokemons = available_pokemons
        self.pokemons = {}

    def choose_pokemons(self):
        """
        Allow players to choose their Pokémon teams.
        """
        print("Player 1, choose two Pokémon:")
        self.pokemons[self.player1] = self.choose_pokemon_pair()

        print("\nPlayer 2, choose two Pokémon:")
        self.pokemons[self.player2] = self.choose_pokemon_pair()

    def choose_pokemon_pair(self):
        """
        Helper method to choose a pair of Pokémon for a player.
        """
        chosen_pokemons = []
        self.display_available_pokemons()
        for i in range(2):
            print(f"Choose Pokémon {i + 1} from the available list:")
            while True:
                pokemon_name = input(f"Enter the name of {i+1} the Pokémon: ")
                if pokemon_name in self.available_pokemons:
                    chosen_pokemons.append(self.available_pokemons[pokemon_name])
                    break
                else:
                    print("Invalid Pokémon name. Try again.")
        return chosen_pokemons

    def display_available_pokemons(self):
        """
        Display the list of available Pokémon.
        """
        print("Available Pokémon:")
        for pokemon_name in self.available_pokemons:
            print(pokemon_name)

    def start_battle(self):
        """
        Start the battle between two players and their Pokémon teams.
        """
        print("\nBattle begins!")
        print(f"\n{self.player1}'s turn to choose Pokémon:")
        pokemon1 = self.choose_pokemon(self.pokemons[self.player1])
        print(f"\n{self.player2}'s turn to choose Pokémon:")
        pokemon2 = self.choose_pokemon(self.pokemons[self.player2])
        # Determine who starts the round based on speed
        (player_first, pokemon_first,
         player_second, pokemon_second) = self.determine_starting_player(pokemon1, pokemon2)
        self.perform_round(player_first, pokemon_first, pokemon_second)
        self.perform_round(player_second, pokemon_second, pokemon_first)

        while True:
            # Determine who starts the round based on speed
            (player_first, pokemon_first,
             player_second, pokemon_second) = self.determine_starting_player(pokemon_first, pokemon_second)

            print(f"\n{self.player1}'s turn to play:")
            # Player chooses which Pokémon to use
            print(f"\n{player_first}'s turn to perform a round.")
            if input("Would you like to change pokemon?")=='yes':
                pokemon_first = self.choose_pokemon(self.pokemons[player_first])
            # Perform the round
            self.perform_round(player_first, pokemon_first, pokemon_second)

            print(f"\n{self.player2}'s turn to play:")
            # Player chooses which Pokémon to use
            print(f"\n{player_first}'s turn to perform a round.")
            if input("Would you like to change pokemon?")=='yes':
                pokemon_first = self.choose_pokemon(self.pokemons[player_first])
            # Perform the round
            self.perform_round(player_second, pokemon_second, pokemon_first)

            # Check if any player has lost both Pokémon
            if self.player1_has_lost() or self.player2_has_lost():
                break

    def determine_starting_player(self, pokemon1, pokemon2):
        """
        Determine which player goes first based on Pokémon speed.

        Returns:
        Tuple of (player_first, pokemon_first, player_second, pokemon_second)
        """
        if pokemon1.speed > pokemon2.speed:
            print(f"{self.player1} plays first")
            return self.player1, pokemon1, self.player2, pokemon2
        else:
            print(f"{self.player2} plays first")
            return self.player2, pokemon2, self.player1, pokemon1

    def choose_pokemon(self, pokemon_team):
        """
        Allow a player to choose a Pokémon from their team.

        Args:
        - pokemon_team (list): List of Pokémon for the player.

        Returns:
        Chosen Pokémon.
        """
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
        """
        Perform a round of the battle.

        Args:
        - player (str): Name of the player.
        - chosen_pokemon (Pokemon): Pokémon chosen for the round.
        - opponent_pokemon (Pokemon): Opponent's Pokémon.
        """
        print(f"\n{player}'s turn to perform a round.")
        print(f"Chosen Pokémon: {chosen_pokemon.name} (HP: {chosen_pokemon.health})")

        # Player chooses the type of attack
        attack_type = self.choose_attack_type()

        # Perform the attack
        damage = chosen_pokemon.hit_opponent(attack_type, opponent_pokemon.type1)
        opponent_pokemon.take_damage(damage)

        # Display battle status after the round
        self.display_battle_status()

    def choose_attack_type(self):
        """
        Allow a player to choose the type of attack.

        Returns:
        Chosen attack type ('simple' or 'special').
        """
        while True:
            attack_type = input("Choose attack type simple or special (1 or 2): ").lower()
            if attack_type in ['1', '2']:
                if attack_type == '1':
                    return "simple"
                else:
                    return "special"
            else:
                print("Invalid attack type. Try again.")

    def display_battle_status(self):
        """
        Display the current battle status.
        """
        print("\n--- Battle Status ---")
        print(f"{self.player1}'s Pokémon:")
        for pokemon in self.pokemons[self.player1]:
            pokemon.display_info()
        print(f"\n{self.player2}'s Pokémon:")
        for pokemon in self.pokemons[self.player2]:
            pokemon.display_info()

    def player1_has_lost(self):
        """
        Check if player 1 has lost both Pokémon.

        Returns:
        True if player 1 has lost, False otherwise.
        """
        return all(pokemon.is_fainted for pokemon in self.pokemons[self.player1])

    def player2_has_lost(self):
        """
        Check if player 2 has lost both Pokémon.

        Returns:
        True if player 2 has lost, False otherwise.
        """
        return all(pokemon.is_fainted for pokemon in self.pokemons[self.player2])
