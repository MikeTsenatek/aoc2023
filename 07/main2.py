import re
from time import perf_counter_ns
from ordered_enum import OrderedEnum
from functools import cmp_to_key

units = ['ns', 'µs', 'ms', 's']

class TypeOfHands(OrderedEnum):
    FiveOfAKind = 7
    FourOfAKind = 6
    FullHouse = 5
    ThreeOfAKind = 4
    TwoPair = 3
    OnePair = 2
    HighCard = 1

def einheiten(zeit):
    i = 0
    while zeit > 1000:
        zeit /= 1000
        i += 1
    return str(round(zeit,2)) + " " + units[i]


timestart = perf_counter_ns()

input = open("input", "r").read().split("\n")

default_cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
default_weight = [14, 13, 12, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2]

weight_per_card = {x: y for x, y in zip(default_cards, default_weight)}

def count_cards(hand, weight):
    cards = {x: 0 for x in default_cards}
    for card in hand:
        cards[card] += 1
    return (hand, cards, weight)

def parse_cards_with_joker(hand):
    maxamountofcard = [value for key, value in hand[1].items() if key != 'J']
    maxamountofcard = max(maxamountofcard)
    if maxamountofcard == 5 or maxamountofcard + hand[1]['J'] >= 5:
        return TypeOfHands.FiveOfAKind
    elif maxamountofcard + hand[1]['J'] == 4:
        return TypeOfHands.FourOfAKind
    elif maxamountofcard + hand[1]['J'] == 3:
        if hand[1]['J'] == 2 and maxamountofcard == 1:
            return TypeOfHands.ThreeOfAKind
        if (maxamountofcard == 3 and list(hand[1].values()).count(2) == 2) or \
                (maxamountofcard == 2 and list(hand[1].values()).count(2) == 2 and hand[1]['J'] == 1) or \
                (list(hand[1].values()).count(2) == 2 and hand[1]['J'] == 1) or \
                (list(hand[1].values()).count(3) == 1 and list(hand[1].values()).count(2) == 1) or \
                (maxamountofcard == 1 and list(hand[1].values()).count(2) == 1 and hand[1]['J'] == 2):
            return TypeOfHands.FullHouse
        else:
            return TypeOfHands.ThreeOfAKind
    elif maxamountofcard + hand[1]['J'] == 2:
        if (list(hand[1].values()).count(2) == 1 and hand[1]['J'] == 1) or list(hand[1].values()).count(2) == 2:
            return TypeOfHands.TwoPair
        else:
            return TypeOfHands.OnePair
    else:
        return TypeOfHands.HighCard


def sorthand(hand1, hand2):
    if parse_cards_with_joker(hand1) == parse_cards_with_joker(hand2):
        for i, j in zip(hand1[0], hand2[0]):
            if i == j:
                continue
            else:
                weightcard1 = weight_per_card[i]
                weightcard2 = weight_per_card[j]
                returnvalue = 1 if weightcard1 < weightcard2 else -1
                return returnvalue
        return 0
    else:
        return 1 if parse_cards_with_joker(hand1) > parse_cards_with_joker(hand2) else -1

hands = []
for line in input:
    hand = line.split(" ")
    hand = count_cards(hand[0], hand[1])
    hands.append(hand)

sortedhand = sorted(hands, key=cmp_to_key(sorthand))

sum = 0
for rank, hand in enumerate(reversed(sortedhand)):
    print(f"Rang: {rank + 1} Hand: {hand[0]} Wert: {parse_cards_with_joker(hand)} Weight: {hand[2]}")
    sum += int(hand[2])*(rank+1)


print("Summe: " + str(sum))
print("Laufzeit: " + einheiten(perf_counter_ns() - timestart))
