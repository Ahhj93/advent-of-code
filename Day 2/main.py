bag: dict = {"red": 12, "blue": 14, "green": 13}

def parse_input(input: str) -> list:
    id_game: int = int(input[5:input.find(":")])
    input = input[input.find(":")+2:]
    list: list = input.split(";")
    for i in range(len(list)):
        list[i] = list[i].split(",")
        for j in range(len(list[i])):
            list[i][j] = list[i][j].split()
            list[i][j][0] = int(list[i][j][0])
    return (id_game, list)

def main1() -> int:
    input_text_file = open("input.txt", "r")
    input_list : list  = input_text_file.read().split("\n")
    possible_games: list = []
    for line in input_list:
        id_game, list = parse_input(line)
        possible: bool = True
        for item in list:
            revealed_bag = {"red": 0, "blue": 0, "green": 0}
            for color in item:
                revealed_bag[color[1]] += color[0]
            for color in revealed_bag:
                if revealed_bag[color] > bag[color]:
                    possible = False
        if possible:
            possible_games.append(id_game)
    return sum(possible_games)

def main2() -> int:
    input_text_file = open("input.txt", "r")
    input_list: list  = input_text_file.read().split("\n")
    ensemble: list = []
    for line in input_list:
        _, list = parse_input(line)
        revealed_bag = {"red": 0, "blue": 0, "green": 0}
        for item in list:
            revealed_bag_temp = {"red": 0, "blue": 0, "green": 0}
            for color in item:
                revealed_bag_temp[color[1]] += color[0]
            if revealed_bag_temp["red"] > revealed_bag["red"]:
                revealed_bag["red"] = revealed_bag_temp["red"]
            if revealed_bag_temp["blue"] > revealed_bag["blue"]:
                revealed_bag["blue"] = revealed_bag_temp["blue"]
            if revealed_bag_temp["green"] > revealed_bag["green"]:
                revealed_bag["green"] = revealed_bag_temp["green"]
        ensemble.append(revealed_bag["red"]*revealed_bag["blue"]*revealed_bag["green"])
    return sum(ensemble)

if __name__ == "__main__":
    print("--- Day 2: Cube Conundrum ---")
    print(f"Part One: {main1()}")
    print(f"Part Two: {main2()}")