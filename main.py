from enum import Enum

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Normal, Fire, Water, Grass, Flying, Fighting, Poison, Electric, Ground, Rock, Psychic, Ice, Bug, Ghost, Steel, Dragon, Dark, and Fairy

# Pokemon names
Pikachu = "Pikachu"
Noivern = "Noivern"


class PokemonTypes(Enum):
    ELECTRIC = 0
    FLYING = 1


names = ["Electric", "Flying"]

PokemonTypes(PokemonTypes.ELECTRIC).value
Electric = "Electric"
Flying = "Flying"

PokemonType = "PokemonType"
PokemonHP = "PokemonHP"
IsShiny = "IsShiny"


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_pokemon_types_and_HP(pokemon):
    global pokemonStats
    print("Pokemon " + pokemon + " is: ")
    print(names[pokemonStats[pokemon][PokemonType].value])
    print(pokemonStats[pokemon][PokemonHP])
    if pokemonStats[pokemon][IsShiny]:
        print("Shiny")
    else:
        print("Not shiny")

pokemonStats = {
    Pikachu: {
        PokemonType: PokemonTypes.ELECTRIC,
        PokemonHP: 80,
        IsShiny: False
    },
    Noivern: {
        PokemonType: PokemonTypes.FLYING,
        PokemonHP: 100,
        IsShiny: True
    }
}

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print_pokemon_types_and_HP(Pikachu)
    print_pokemon_types_and_HP(Noivern)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
