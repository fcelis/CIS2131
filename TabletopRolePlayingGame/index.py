# *****************************************************
# Developer: Fernando Celis
# Date: 02/10/2025
# Class: CIS2131 / Python Programming
# Project # : Tableto-RoleGame Character
# Lab4 Description: allows users to create an RPG character by assigning randomized
# ability scores and performing actions like attacking, negotiating, searching, and
# eating, using dice rolls and ability modifiers based on D&D 5e mechanics. The program guides the user through character creation, implements a menu-driven action system, and determines outcomes based on random rolls and ability scores.
# *****************************************************

import random
import heapq
# Function to get character name
def get_name():
    return input("Enter your character's name: ")

# Function to roll 4 six-sided dice and drop the lowest
def sum_of_four_six_sided_dice_with_lowest_dropped():
    rolls = []

    # interation based on chapter 5
    for _ in range(4):
        rolls.append(random.randint(1, 6))
    # sum and return the 3 largest numbers
    return sum(heapq.nlargest(3, rolls))
# Function to calculate ability modifier based on the provided table
def get_ability_modifier(score):
    return (score - 10) // 2

# Function to display the action menu and get user's choice
def menu():
    actions = ["Attack", "Negotiate", "Search", "Eat"]
    print("\nChoose an action:")
    for i, action in enumerate(actions, start=1):
        print(f"{i}. {action}")

    choice = int(input("Enter the number of your choice: "))
    return actions[choice - 1] if 1 <= choice <= len(actions) else None

# Action functions

def attack_action(str_mod, dex_mod):
    roll = random.randint(1, 20) + max(str_mod, dex_mod)
    if roll >= 12:
        damage = max(0, random.randint(1, 6) + max(str_mod, dex_mod))
        print(f"You hit! Damage dealt: {damage}")
    else:
        print("You missed!")


def negotiate_action(cha_mod):
    roll = random.randint(1, 20) + cha_mod
    if roll >= 15:
        print("You successfully negotiated a truce.")
    else:
        print("Negotiation failed.")

def search_action(int_mod, wis_mod):
    roll = random.randint(1, 20) + max(int_mod, wis_mod)
    treasures = ["gems", "gold", "jade figurine", "ancient scroll"]
    if roll >= 12:
        print(f"You found treasure: {random.choice(treasures)}")
    else:
        print("You found nothing.")

def eat_action(con_mod):
    roll = random.randint(1, 20) + con_mod
    if roll >= 10:
        print("You handled the rancid food without getting sick.")
    else:
        print("You got sick and need to stay in bed.")

# Perform a single action based on user input
def perform_action(str_mod, dex_mod, cha_mod, int_mod, wis_mod, con_mod):
    while True:
        try:
            action = menu()

            if action == "Attack":
                attack_action(str_mod, dex_mod)
                break  # Exit loop after a valid action
            elif action == "Negotiate":
                negotiate_action(cha_mod)
                break
            elif action == "Search":
                search_action(int_mod, wis_mod)
                break
            elif action == "Eat":
                eat_action(con_mod)
                break
            else:
                raise ValueError("Invalid choice, please enter a valid action.")
        except ValueError as e:
            print("Invalid choice, please enter a valid action. Select from 1 thru 4")

# Main game logic
def main():
    print("Welcome to the Tabletop RPG Character Creator!")

    # Get character name
    name = get_name()

    # Roll ability scores simplify
    # abilities = {attr: sum_of_four_six_sided_dice_with_lowest_dropped() for attr in ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]}

    # Roll ability score traditional
    abilities = {}
    for attr in ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]:
        abilities[attr] = sum_of_four_six_sided_dice_with_lowest_dropped()

    # Display character stats
    print(f"\nCharacter Name: {name}")
    for attr, score in abilities.items():
        mod = get_ability_modifier(score)
        print(f"{attr}: {score} (Modifier: {mod})")

    # Perform 4 actions
    for _ in range(4):
        perform_action(
            get_ability_modifier(abilities["Strength"]), get_ability_modifier(abilities["Dexterity"]),
            get_ability_modifier(abilities["Charisma"]), get_ability_modifier(abilities["Intelligence"]),
            get_ability_modifier(abilities["Wisdom"]), get_ability_modifier(abilities["Constitution"])
        )

# only use if we intend to be used for import by another script.
# if __name__ == "__main__":
main()
