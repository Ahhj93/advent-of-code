def main2() -> int:
    input_text_file = open("test.txt", "r")
    input_list : list  = input_text_file.read().splitlines()
    nb_card = [1] * len(input_list)
    for i, line in enumerate(input_list):
        first, my_number = line.split(" | ")
        print(first)
        print(my_number)
        _, winning_number = first.split(": ")
        winning_number = winning_number.split()
        my_number = my_number.split()
        total_matches = 0
        for number in my_number:
            if number in winning_number:
                total_matches += 1
                nb_card[i + total_matches] += nb_card[i]
    return sum(nb_card)

if __name__ == "__main__":
    print("--- Day 4: Scratchcards ---")
    print(f"Part Two: {main2()}")