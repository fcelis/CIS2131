# *****************************************************
# Developer: Fernando Celis
# Date: 04/06/2025
# Class: CIS2131 / Python Programming
# Project: Black Jack Simulator
# Description: The purpose of this program is to simulate black jack game, it simulate 10000 hands against the dealer.
# *****************************************************
import random
from collections import defaultdict


class BlackjackSimulator:
    # ******************************************************************************************************************
    def __init__(self, num_simulations=100000):
        self.num_simulations = num_simulations
        self.deck = self.create_deck()
        self.results = defaultdict(
            lambda: {'hit': {'win': 0, 'loss': 0, 'draw': 0}, 'stand': {'win': 0, 'loss': 0, 'draw': 0}})

    # ******************************************************************************************************************
    def create_deck(self):
        # Creates a standard deck of 52 cards with assigned values.
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10,
                  'A': 11}
        deck = list(values.keys()) * 4  # Four suits per value
        return deck, values

    # ******************************************************************************************************************
    def deal_card(self):
        # Draws a random card from the deck.
        return random.choice(self.deck[0])

    # ******************************************************************************************************************
    def hand_value(self, hand):
        # Calculates the value of a hand, adjusting for Aces if necessary.
        values = self.deck[1]
        total = sum(values[card] for card in hand)
        aces = hand.count('A')
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    # ******************************************************************************************************************
    def dealer_turn(self, dealer_hand):
        # Dealer follows standard rules: hit on 16 or less, stand on 17+.
        while self.hand_value(dealer_hand) < 17:
            dealer_hand.append(self.deal_card())
        return self.hand_value(dealer_hand)

    # ******************************************************************************************************************
    def play_hand(self, starting_hand, action):
        # Simulates a single hand of Blackjack with a given action (hit or stand).
        player_hand = starting_hand[:]
        dealer_hand = [self.deal_card(), self.deal_card()]

        if action == 'hit':
            player_hand.append(self.deal_card())

        player_total = self.hand_value(player_hand)
        if player_total > 21:
            return 'loss'

        dealer_total = self.dealer_turn(dealer_hand)
        if dealer_total > 21 or player_total > dealer_total:
            return 'win'
        elif player_total < dealer_total:
            return 'loss'
        else:
            return 'draw'

    # ******************************************************************************************************************
    def run_simulation(self):
        # Runs the Blackjack simulation for 100,000 hands.
        for _ in range(self.num_simulations):
            starting_hand = [self.deal_card(), self.deal_card()]
            start_value = self.hand_value(starting_hand)

            if start_value < 4 or start_value > 22:
                continue

            for action in ['hit', 'stand']:
                result = self.play_hand(starting_hand, action)
                self.results[start_value][action][result] += 1

    # ******************************************************************************************************************
    def print_results(self):
        # Outputs the results in a readable format.
        print(
            f"{'Hand Value':<12} {'Hit Wins':<10} {'Hit Losses':<12} {'Hit Draws':<10} {'Stand Wins':<12} {'Stand Losses':<14} {'Stand Draws':<10}")
        print("-" * 80)
        for value in sorted(self.results.keys()):
            hit = self.results[value]['hit']
            stand = self.results[value]['stand']
            print(
                f"{value:<12} {hit['win']:<10} {hit['loss']:<12} {hit['draw']:<10} {stand['win']:<12} {stand['loss']:<14} {stand['draw']:<10}")

# ******************************************************************************************************************
if __name__ == "__main__":
    simulator = BlackjackSimulator()
    simulator.run_simulation()
    simulator.print_results()
