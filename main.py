from enum import Enum

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#  Normal, Fire, Water, Grass, Flying, Fighting, Poison, Electric, Ground, Rock, Psychic, Ice, Bug, Ghost, Steel, Dragon, Dark, and Fairy

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


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def printPokemonTypesAndHP(pokemon):
    print("Pokemon " + pokemon + " is: ")
    print(names[pokemonStats[pokemon][PokemonType].value])
    print(pokemonStats[pokemon][PokemonHP])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pokemonStats = {
        Pikachu: {
            PokemonType: PokemonTypes.ELECTRIC,
            PokemonHP: 80
        },
        Noivern: {
            PokemonType: PokemonTypes.FLYING,
            PokemonHP: 100
        }
    }
    printPokemonTypesAndHP(Pikachu)
    printPokemonTypesAndHP(Noivern)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
