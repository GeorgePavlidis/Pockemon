import random

class Pokemon:
    def __init__(self, name, level, type):
        self.name = name
        self.level = level
        self.type = type
        self.health = level * 10  # Assume health is 10 times the level
        self.is_fainted = False

    def display_info(self):
        """Display information about the Pokemon."""
        print(f"{self.name} (Level {self.level}) - Type: {self.type}")
        print(f"Health: {self.health}")
        if self.is_fainted:
            print("Status: Fainted")
        else:
            print("Status: Active")

    def take_damage(self, damage):
        """Reduce the Pokemon's health by the given damage."""
        if not self.is_fainted:
            self.health -= damage
            if self.health <= 0:
                self.health = 0
                self.is_fainted = True
                print(f"{self.name} has fainted!")

    def heal(self, healing_points):
        """Heal the Pokemon by the given amount."""
        if not self.is_fainted:
            self.health += healing_points
            print(f"{self.name} has been healed by {healing_points} points.")

    def hit_opponent(self, max_power):
        """Generate random damage and hit the opponent."""
        if not self.is_fainted:
            damage = random.randint(0, max_power)
            print(f"{self.name} hits the opponent for {damage} damage.")
            return damage
        return 0

# Example usage: Fight between two Pokemon

# Create two Pokemon 
pikachu = Pokemon("Pikachu", 5, "Electric")
charmander = Pokemon("Charmander", 7, "Fire")

# Show the information about the Pokemon
pikachu.display_info()
charmander.display_info()

# Start a battle 
while not pikachu.is_fainted and not charmander.is_fainted:
    pikachu_damage = pikachu.hit_opponent(15)
    charmander.take_damage(pikachu_damage)

    charmander_damage = charmander.hit_opponent(12)
    pikachu.take_damage(charmander_damage)
    
    # Show the Status of the battle 
    print("\n--- Battle Status ---")
    pikachu.display_info()
    charmander.display_info()

print("\n--- Battle Result ---")
if pikachu.is_fainted:
    print(f"{pikachu.name} has fainted. {charmander.name} wins!")
elif charmander.is_fainted:
    print(f"{charmander.name} has fainted. {pikachu.name} wins!")
else:
    print("It's a draw!")
