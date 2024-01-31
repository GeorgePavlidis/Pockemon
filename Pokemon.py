"""
Create a Pokemon class

This class will have the following attributes:
-   name
-   level
-   type
-   health (will depend on level)
-   is_fainted

This class will have the following methods:
-   display_info: Display information about the Pokemon
-   take_damage:  Reduce the Pokemon's health by the given damage
-   heal: Heal the Pokemon by the given amount.
-   hit_opponent: Generate random damage and hit the opponent from 0 to max_power

- Add code that will create two different Pokemon
- Start a fight between them until one of them faints

Show who won !
"""

import random


class Pokemon:
    types = None
    def __init__(self, name, type1, type2, hp, attack, defense, sp_atk, sp_def, speed,
                 generation, legendary):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.speed = speed
        self.generation = generation
        self.legendary = legendary
        self.health = self.hp  # Assume health is 10 times the level
        self.is_fainted = False
        self.has_used_special_attack = False


    def display_info(self):
        """Display information about the Pokemon."""
        print(f"{self.name} - Type: {self.type1}/{self.type2}")
        print(f"Health: {self.health}")
        # print(f"Attack: {self.attack}")
        # print(f"Special Attack: {self.sp_atk}")
        # print(f"defense: {self.defense}")
        # print(f"Special Defense: {self.sp_def}")
        if self.is_fainted:
            print("Status: Fainted")
        else:
            print("Status: Active")

    def take_damage(self, damage):
        """Reduce the Pokemon's health by the given damage."""
        defence = random.uniform(0, self.defense * 0.5) / 5
        weaker = (damage - defence) / damage
        print(f"The attack hit {self.name} with {(weaker * 100):.2f}% power (", end="")
        damage = weaker * damage
        print(f"{damage})")
        if not self.is_fainted:
            self.health -= damage
            if self.health <= 0:
                self.health = 0
                self.is_fainted = True
                print(f"{self.name} has fainted!")

    def heal(self):
        """Heal the Pokemon by the given amount."""
        if not self.is_fainted:
            self.health += self.health * 0.1
            print(f"{self.name} has been healed.")

    def hit_opponent(self, attack_type, opponent_type1=None):
        """Generate random damage and hit the opponent."""
        if not self.is_fainted:
            if attack_type == "simple":
                if self.has_used_special_attack:
                    self.has_used_special_attack = False
                attack_power = random.uniform(self.attack * 0.4, self.attack)
                damage = int(attack_power / 5)
                print(f"{self.name} uses simple attack and hits the opponent for {damage} damage.")
            elif attack_type == "special":
                if not type or not opponent_type1:
                    print("You need to provide type chart and/or opponent's type")
                    return None
                if not self.has_used_special_attack:
                    attack_power = random.uniform(self.sp_atk * 0.4, self.sp_atk)
                    type_affected_attack_power = \
                        attack_power * Pokemon.types[Pokemon.types.Attack == self.type1][opponent_type1].values[0]
                    damage = int(type_affected_attack_power / 5)
                    print(
                        f"{self.name} uses special attack and hits the opponent for {damage} damage.")
                    self.has_used_special_attack = True
                else:
                    print(f"{self.name} cannot use special attack again in this round.")
                    return None

            return damage
        return None

