import random

class Pokemon:
    types = None  # Assuming this is a pandas DataFrame containing type effectiveness

    def __init__(self, name, type1, type2, hp, attack, defense, sp_atk, sp_def, speed,
                 generation, legendary):
        """
        Initialize a Pokemon instance with its attributes.

        Args:
        - name (str): The name of the Pokemon.
        - type1 (str): The primary type of the Pokemon.
        - type2 (str): The secondary type of the Pokemon.
        - hp (int): Base health points of the Pokemon.
        - attack (int): Base attack stat of the Pokemon.
        - defense (int): Base defense stat of the Pokemon.
        - sp_atk (int): Base special attack stat of the Pokemon.
        - sp_def (int): Base special defense stat of the Pokemon.
        - speed (int): Base speed stat of the Pokemon.
        - generation (int): The generation in which the Pokemon was introduced.
        - legendary (bool): True if the Pokemon is legendary, False otherwise.
        """
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
        if self.is_fainted:
            print("Status: Fainted")
        else:
            print("Status: Active")

    def take_damage(self, damage):
        """
        Reduce the Pokemon's health by the given damage, considering defense.

        Args:
        - damage (int): The damage to be inflicted on the Pokemon.
        """
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
        """Heal the Pokemon by 10% of its current health."""
        if not self.is_fainted:
            self.health += self.health * 0.1
            print(f"{self.name} has been healed.")

    def hit_opponent(self, attack_type, opponent_type1=None):
        """
        Generate random damage and hit the opponent based on the attack type.

        Args:
        - attack_type (str): The type of attack ("simple" or "special").
        - opponent_type1 (str): The primary type of the opponent Pokemon.

        Returns:
        Damage inflicted on the opponent.
        """
        if not self.is_fainted:
            if attack_type == "simple":
                attack_power = random.uniform(self.attack * 0.4, self.attack)
                damage = int(attack_power / 5)
                print(f"{self.name} uses simple attack and hits the opponent for {damage} damage.")
            elif attack_type == "special":
                if not opponent_type1:
                    print("You need to provide the opponent's type for special attack.")
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
