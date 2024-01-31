# Pokemon Battle System

This repository contains a simple Pokemon battle system implemented in Python. The project consists of three files: `main.py`, `battle.py`, and `pokemon.py`.

## Files and Classes:

### 1. `main.py`

This file serves as the main entry point for the Pokemon battle system. However, certain parts of the code are unimplemented, and only a partial version is provided in the `main` branch. The completed version can be found in the `completed_code` branch. To run the fully functional code, switch to the `completed_code` branch.

### 2. `battle.py`

The `Battle` class is defined in this file, representing the core logic for Pokemon battles. The class allows two players to choose their Pokemon teams and engages them in a turn-based battle. The battle continues until one of the players loses all of their Pokemon.

Methods in `Battle`:
- `__init__(self, player1, player2, available_pokemons)`: Initialize the battle with players and available Pokemon.
- `choose_pokemons(self)`: Allow players to choose their Pokemon teams.
- `start_battle(self)`: Start the battle between the two players.
- ... (and other methods for handling battle logic)

### 3. `pokemon.py`

The `Pokemon` class is defined here, representing individual Pokemon entities. Each Pokemon has attributes such as name, type, health, and various stats. The class includes methods for displaying information, taking damage, healing, and hitting opponents.

Methods in `Pokemon`:
- `__init__(self, name, type1, type2, hp, attack, defense, sp_atk, sp_def, speed, generation, legendary)`: Initialize a Pokemon instance.
- `display_info(self)`: Display information about the Pokemon.
- `take_damage(self, damage)`: Reduce the Pokemon's health by the given damage.
- `heal(self)`: Heal the Pokemon by a given amount.
- `hit_opponent(self, attack_type, opponent_type1=None)`: Generate random damage and hit the opponent based on the attack type.

## Implementation Status:

The `main.py` file in the `main` branch contains unimplemented code. The fully implemented and functional code can be found in the `completed_code` branch. To see the completed version, switch to the `completed_code` branch using the following command:

```bash
git checkout completed_code
```

Feel free to explore the completed version and run the battle system with the implemented features.

