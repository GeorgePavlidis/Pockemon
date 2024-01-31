"""
Create a Pokemon Class:

Develop a Python class named Pokemon to simulate the characteristics and actions of a Pokemon in a battle scenario.
Attributes:

Define attributes for the Pokemon class, including name, types (type1 and type2), health points (hp), attack, defense, special attack (sp_atk), special defense (sp_def), speed, generation, and legendary status.
Initialization:

Implement an __init__ method to initialize the Pokemon object with the provided attributes.
Set the initial health of the Pokemon to 10 times its level.
Display Information:

Create a method display_info to display information about the Pokemon, including its name, types, and health status.
Damage Handling:

Implement a method take_damage to reduce the Pokemon's health based on the provided damage.
Consider defense in the damage calculation and print information about the attack.
Healing:

Develop a heal method to heal the Pokemon by a certain percentage of its current health.
Attack Mechanism:

Design a hit_opponent method to simulate the Pokemon attacking its opponent.
Implement a basic attack (simple) that generates random damage within a range.
Include a special attack (special) that considers type effectiveness based on a provided type chart and opponent's type.
Special Attack Limitation:

Introduce a mechanism to limit the use of special attacks in a single round.
Battle Status:

Maintain the Pokemon's battle status, including whether it is fainted or active.
Randomization:

Use randomization to introduce variability in damage calculations and attacks.

Show who won !
"""

import random


class Pokemon:
    types = None
    def __init__(self, name, level, type):
        self.name = name
        self.level = level
        self.type = type
        self.health = level * 10  # Assume health is 10 times the level
        self.is_fainted = False


    def display_info(self):
        """Display information about the Pokemon."""
        pass

    def take_damage(self, damage):
        """Reduce the Pokemon's health by the given damage."""
        pass

    def heal(self):
        """Heal the Pokemon by the given amount."""
        pass

    def hit_opponent(self, attack_type, opponent_type1=None):
        """Generate random damage and hit the opponent."""
        if not self.is_fainted:
            if attack_type == "simple":
               pass
            elif attack_type == "special":
                pass

        return None

