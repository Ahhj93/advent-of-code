def parse_input(input: str) -> list:
    id_game: int = int(input[5:input.find(":")])
    input = input[input.find(":")+2:]
    list: list = input.split("|")
    winning_number: list = list[0].split()
    card_number: list = list[1].split()
    return (id_game, winning_number, card_number)

def main1() -> int:
    input_text_file = open("input.txt", "r")
    input_list : list  = input_text_file.read().split("\n")
    score: int = 0
    for line in input_list:
        _, winning_number, card_number = parse_input(line)
        card_score: int = 0
        for number in card_number:
            if number in winning_number:
                if card_score == 0:
                    card_score = 1
                else :
                    card_score *= 2
        score += card_score
    return score

def main2() -> int:
    input_text_file = open("input.txt", "r")
    input_list: list  = input_text_file.read().splitlines()
    nb_card: list = [1] * len(input_list)
    for i, line in enumerate(input_list):
        _, winning_number, card_number = parse_input(line)
        total_played: int = 0
        for number in card_number:
            if number in winning_number:
                total_played += 1
                nb_card[i + total_played] += nb_card[i]
    return sum(nb_card)

if __name__ == "__main__":
    print("--- Day 4: Scratchcards ---")
    print(f"Part One: {main1()}")
    print(f"Part Two: {main2()}")
