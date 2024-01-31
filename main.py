import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
# we need to add requirements
from Pokemon import Pokemon
from Battle import Battle
# Read the CSV file into a DataFrame
pokemon_df = ?


#Showing the legendary pokemons


df = pokemon_df


## The index of Mega Pokemons contained extra and unneeded text. Removed all the text before "Mega"


#drop the columns with named # ( axis=1;axis=0 is for rows)


print('The columns of the dataset are: ',df.columns) #show the dataframe columns
print('The shape of the dataframe is: ',df.shape)    #shape of the dataf


# The attack distribution for the pokemons across all the genarations and the mean of the attack


# Strongest Pokemons By Types



plt.figure(figsize=(12,6))
top_types=df['Type 1'].value_counts()[:10] #take the top 10 Types
df1=df[df['Type 1'].isin(top_types.index)] #take the pokemons of the type with highest numbers, top 10
sns.swarmplot(x='Type 1',y='Total',data=df1,hue='Legendary') # this plot shows the points belonging to individual pokemons
# It is distributed by Type
plt.axhline(df1['Total'].mean(),color='red',linestyle='dashed')
plt.show()







# Display the original DataFrame
print("Original DataFrame:")
print(pokemon_df)

# Remove the 'Total' column

# Keep only rows where Generation is 1

# Display the modified DataFrame
print("\nModified DataFrame:")
print(pokemon_df)

# Create a list of Pokemon objects based on the DataFrame
# pokemon_objects = {}
# for index, row in pokemon_df.iterrows():
#     pokemon_objects[row['Name']] = Pokemon(
#         name=row['Name'],
#         type1=row['Type 1'],
#         type2=row['Type 2'],
#         hp=row['HP'],
#         attack=row['Attack'],
#         defense=row['Defense'],
#         sp_atk=row['Sp. Atk'],
#         sp_def=row['Sp. Def'],
#         speed=row['Speed'],
#         generation=row['Generation'],
#         legendary=row['Legendary']
#     )


# Display the list of Pokemon objects
print("\nList of Pokemon Objects:")
for name, pokemon in pokemon_objects.items():
    pokemon.display_info()
    print()
Pokemon.types = types

# Example usage:
# Create instances of the Player class and the Pokémon class with the added functionalities
# Assume you have a dictionary named 'available_pokemons' where keys are Pokémon names and values are their attributes
player1 = "Player 1"
player2 = "Player 2"
battle = Battle(player1, player2, pokemon_objects)
battle.choose_pokemons()
battle.start_battle()
