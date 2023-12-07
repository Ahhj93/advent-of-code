def parse_input(input: str) -> list:
    hand = input.split(" ")
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
        "2" : "l"
    }
    card2int: str = ""
    for card in hand[0]:
        card2int += labeled_cards_dict[card]
    hand.append(card2int)
    return hand


def five_of_a_kind(cards: str) -> bool:
    # where all five cards have the same label
    if cards.count(cards[0]) == 5:
        return (True, cards)
    else:
        for card in cards:
            if cards.count(card) == 4 and cards.count("J") == 1:
                cards = cards.replace("J", card)
                return (True, cards)

def four_of_a_kind(cards: str) -> bool:
    # where four cards have the same label and one card has a different label
    for card in cards:
        if cards.count(card) == 4:
            return True
    return False

def full_house(cards: str) -> bool:
    # where three cards have the same label, and the remaining two cards share a different label
    for card in cards:
        if cards.count(card) == 3:
            for card2 in cards:
                if cards.count(card2) == 2:
                    return True
    return False

def three_of_a_kind(cards: str) -> bool:
    # where three cards have the same label, and the remaining two cards are each different from any other card in the hand
    for card in cards:
        if cards.count(card) == 3:
            return True
    return False

def two_pair(cards: str) -> bool:
    # where two cards share one label, two other cards share a second label, and the remaining card has a third label
    for card in cards:
        if cards.count(card) == 2:
            for card2 in cards:
                if cards.count(card2) == 2 and card != card2:
                    return True
    return False

def one_pair(cards: str) -> bool:
    # where two cards share one label, and the other three cards have a different label from the pair and each other
    for card in cards:
        if cards.count(card) == 2:
            return True
    return False

def type_of_hand(cards: str) -> str:
    if five_of_a_kind(cards):
        return "five_of_a_kind"
    elif four_of_a_kind(cards):
        return "four_of_a_kind"
    elif full_house(cards):
        return "full_house"
    elif three_of_a_kind(cards):
        return "three_of_a_kind"
    elif two_pair(cards):
        return "two_pair"
    elif one_pair(cards):
        return "one_pair"
    else:
        return "high_gard"
    
def same_type(dict: dict) -> None:
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
    input_text_file = open("input.txt", "r")
    input_list : list  = input_text_file.read().splitlines()
    for line in input_list:
        line_list: list = parse_input(line)
        type[type_of_hand(line_list[0])].append(line_list)
    same_type(type)
    for i, j in enumerate(dict_to_list(type)):
        answer += (i+1)*int(j[1])
    return answer


if __name__ == "__main__": 
    print("--- Day 7: Camel Cards ---")
    print(f"Part One: {main1()}")
    # print(f"Part Two: {main2()}")