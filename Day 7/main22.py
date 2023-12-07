#NOT FINISH
def parse_input(input: str) -> list:
    hand = input.split(" ")
    return hand


def five_of_a_kind(cards: str) -> (bool, str):
    # where all five cards have the same label
    if cards.count(cards[0]) == 5:
        return (True, cards)
    for card in cards:
        if cards.count(card) == 4 and cards.count("J") == 1:
            cards = cards.replace("J", card)
            return (True, cards)
    return (False, cards)

def four_of_a_kind(cards: str) -> (bool, str):
    # where four cards have the same label and one card has a different label
    for card in cards:
        if cards.count(card) == 4:
            return (True, cards)
    for card2 in cards:
        if cards.count(card2) == 3 and cards.count("J") == 1:
            cards = cards.replace("J", card2, 1)
            return (True, cards)
    return (False, cards)

def full_house(cards: str) -> (bool, str):
    # where three cards have the same label, and the remaining two cards share a different label
    for card in cards:
        if cards.count(card) == 3:
            for card2 in cards:
                if cards.count(card2) == 2:
                    return (True, cards)
    for card2 in cards:
        if cards.count(card2) == 2 and cards.count("J") == 1:
            cards = cards.replace("J", card2, 1)
            for card3 in cards:
                if cards.count(card3) == 2 and card3 != card2:
                    return (True, cards)
                else:
                    for card4 in cards:
                        if cards.count(card4) == 1 and cards.count("J") == 1:
                            cards = cards.replace("J", card4, 1)
                            return (True, cards)
    return (False, cards)

def three_of_a_kind(cards: str) -> (bool, str):
    # where three cards have the same label, and the remaining two cards are each different from any other card in the hand
    for card in cards:
        if cards.count(card) == 3:
            return (True, cards)
    for card2 in cards:
        if cards.count(card2) == 2 and cards.count("J") == 1:
            cards = cards.replace("J", card2, 1)
            return (True, cards)
    return (False, cards)

def two_pair(cards: str) -> (bool, str):
    # where two cards share one label, two other cards share a second label, and the remaining card has a third label
    for card in cards:
        if cards.count(card) == 2:
            for card2 in cards:
                if cards.count(card2) == 2 and card != card2:
                    return (True, cards)
    for card in cards:
        if cards.count(card) == 1 and cards.count("J") == 1:
            cards = cards.replace("J", card, 1)
            for card2 in cards:
                if cards.count(card2) == 2:
                    return (True, cards)
                else:
                    for card3 in cards:
                        if cards.count(card3) == 1 and cards.count("J") == 1 and card3 != card:
                            cards = cards.replace("J", card3, 1)
                            return (True, cards)
    return (False, cards)

def one_pair(cards: str) -> (bool, str):
    # where two cards share one label, and the other three cards have a different label from the pair and each other
    for card in cards:
        if cards.count(card) == 2:
            return (True, cards)
    for card in cards:
        if cards.count(card) == 1 and cards.count("J") == 1:
            cards = cards.replace("J", card, 1)
            return (True, cards)
    return (False, cards)

def high_gard(cards: str) -> (bool, str):
    if cards.count("J") == 1:
        cards = cards.replace("J", "A", 1)
        return (True, cards)
    return (True, cards)

def type_of_hand(cards: str) -> str:
    if five_of_a_kind(cards)[0]:
        return ("five_of_a_kind", five_of_a_kind(cards)[1])
    elif four_of_a_kind(cards)[0]:
        return ("four_of_a_kind", four_of_a_kind(cards)[1])
    elif full_house(cards)[0]:
        return ("full_house", full_house(cards)[1])
    elif three_of_a_kind(cards)[0]:
        return ("three_of_a_kind", three_of_a_kind(cards)[1])
    elif two_pair(cards)[0]:
        return ("two_pair", two_pair(cards)[1])
    elif one_pair(cards)[0]:
        return ("one_pair", one_pair(cards)[1])
    else:
        return ("high_gard", high_gard(cards)[1])
    
    
def same_type(dict: dict) -> None:
    labeled_cards_dict: dict = {
        "A": "a",
        "K" : "b",
        "Q" : "c",
        "T" : "d",
        "9" : "e",
        "8" : "f",
        "7" : "g",
        "6" : "h",
        "5" : "i",
        "4" : "j",
        "3" : "k",
        "2" : "l",
        "J" : "m"
    }
    for key in dict:
        for hand in dict[key]:
            card2int: str = ""
            for card in hand[0]:
                card2int += labeled_cards_dict[card]
            hand.append(card2int)
    for key in dict:
        dict[key].sort(key=lambda x: x[2], reverse=True)

def dict_to_list(dict: dict) -> list:
    list: list = []
    for hand in dict["high_gard"]:
        list.append(hand)
    for hand in dict["one_pair"]:
        list.append(hand)
    for hand in dict["two_pair"]:
        list.append(hand)
    for hand in dict["three_of_a_kind"]:
        list.append(hand)
    for hand in dict["full_house"]:
        list.append(hand)
    for hand in dict["four_of_a_kind"]:
        list.append(hand)
    for hand in dict["five_of_a_kind"]:
        list.append(hand)
    return list

def main1() -> int:
    answer: int = 0
    type: dict = {
        "five_of_a_kind": [],
        "four_of_a_kind": [],
        "full_house": [],
        "three_of_a_kind": [],
        "two_pair": [],
        "one_pair": [],
        "high_gard": []
    }
    input_text_file = open("test.txt", "r")
    input_list : list  = input_text_file.read().splitlines()
    for line in input_list:
        line_list: list = parse_input(line)
        line_list[0] = type_of_hand(line_list[0])[1]
        type[type_of_hand(line_list[0])[0]].append(line_list)
    same_type(type)
    print(type)
    for i, j in enumerate(dict_to_list(type)):
        answer += (i+1)*int(j[1])
    return answer


if __name__ == "__main__": 
    print("--- Day 7: Camel Cards ---")
    print(f"Part One: {main1()}")
    # print(f"Part Two: {main2()}")