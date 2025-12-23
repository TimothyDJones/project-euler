"""
Problem 54
https://projecteuler.net/problem=54

Poker Hands


In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:
Hand        Player 1        Player 2          Winner
1       5H 5C 6S 7S KD    2C 3S 8S 8D TD
        Pair of Fives     Pair of Eights      Player 2

2       5D 8C 9S JS AC    2C 5C 7D 8S QH
        Highest card Ace  Highest card Queen  Player 1

3       2D 9C AS AH AC    3D 6D 7D TD QD
        Three Aces        Flush with Diamonds Player 2

4       4D 6S 9H QH QC    3D 6D 7H QD QS
        Pair of Queens    Pair of Queens
        Highest card Nine Highest card Seven  Player 1

5       2H 2D 4C 4D 4S    3C 3D 3S 9S 9D
        Full House        Full House
        With Three Fours  with Three Threes   Player 1

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""
from itertools import groupby
from math import sqrt
from pprint import pprint

CARD_VALUES = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
    "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
SUITS = ["C", "D", "H", "S"]

def main():
    hands = list()
    count_wins_player_1 = 0

    with open("0054_poker.txt", "r") as f:
        raw_data = [line.strip() for line in f.readlines()]

    for line in raw_data:
        cards = [list(c) for c in line.split(" ")]
        cards = [[CARD_VALUES[p[0]], p[1]] for p in cards]
        # cards = [tuple(p) for p in cards]
        cards = [cards[:5], cards[5:]]
        cards = [[tuple(p) for p in c] for c in cards]
        hands.append(cards)
    # pprint(hands[0])
    # print(len(hands))


    # print(is_high_card(hands[0][0]))
    # print(group_card_values(hands[1][0]))

    for hand in hands:
        if resolve_hand(hand[0]) > resolve_hand(hand[1]):
            count_wins_player_1 += 1

    print("Number of wins by Player 1:", count_wins_player_1)


def flatten_lists(list_of_lists: list):
    return [value for _list in list_of_lists for value in _list]

def group_card_values(hand: list):
    values = sorted([value for value, suit in hand], reverse=True)
    groups = [list(group) for key, group in groupby(values)]
    groups.sort(key=lambda group: (len(group), group[0]), reverse=True)
    return groups

def is_high_card(hand: list):
    return sorted([value for value, suit in hand], reverse=True)

def is_one_pair(hand: list):
    groups = group_card_values(hand)
    if len(groups[0]) == 2:
        return flatten_lists(groups)

def is_two_pair(hand: list):
    groups = group_card_values(hand)
    if len(groups[0]) == 2 and len(groups[1]) == 2:
        return flatten_lists(groups)

def is_three_of_kind(hand: list):
    groups = group_card_values(hand)
    if len(groups[0]) == 3:
        return flatten_lists(groups)

def is_full_house(hand: list):
    groups = group_card_values(hand)
    if len(groups[0]) == 3 and len(groups[1]) == 2:
        return flatten_lists(groups)

def is_four_of_kind(hand: list):
    groups = group_card_values(hand)
    if len(groups[0]) == 4:
        return flatten_lists(groups)

def is_straight(hand: list):
    values = sorted([value for value, suit in hand], reverse=True)
    desired = list(reversed(range(min(values), max(values) + 1)))
    if values == desired:
        return values

def is_flush(hand: list):
    if len({suit for value, suit in hand}) == 1:
        return sorted([value for value, suit in hand], reverse=True)

def is_straight_flush(hand: list):
    if is_straight(hand):
        return is_flush(hand)

def is_royal_flush(hand: list):
    if max([value for value, suit in hand]) == 14:
        return is_straight_flush(hand)

def resolve_hand(hand: list):
    check_methods = [
        is_high_card,
        is_one_pair,
        is_two_pair,
        is_three_of_kind,
        is_straight,
        is_flush,
        is_full_house,
        is_four_of_kind,
        is_straight_flush,
        is_royal_flush
    ]

    for index, check_method in reversed(list(enumerate(check_methods))):
        result = check_method(hand)
        if result:
            # print(index, check_method.__name__, result)
            return [index, check_method.__name__] + result


if __name__ == "__main__":
    main()
