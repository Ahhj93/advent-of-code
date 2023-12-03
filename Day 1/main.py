def problem1():
    input_text_file = open("input.txt", "r")
    input_list : list  = input_text_file.read().split("\n")
    somme_calibration : int = 0

    for item in input_list:
        nombre_str: str = ""
        for elt in item:
            if elt.isdigit():
                nombre_str += elt
        nombre_str = nombre_str[0] + nombre_str[-1]
        somme_calibration += int(nombre_str)

    return somme_calibration

def problem2():
    input_text_file = open("input.txt", "r")
    input_list : list  = input_text_file.read().split("\n")

    somme_calibration: int = 0
    numbers_spelled: dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    digits: str = "0123456789"

    for item in input_list:
        numbers: list = []
        for value in digits:
            index = item.find(value)
            if index != -1:
                numbers.append((index, value))
            index = item.rfind(value)
            if index != -1:
                numbers.append((index, value))
        for spelled, value in numbers_spelled.items():
            index = item.find(spelled)
            if index != -1:
                numbers.append((index, value))
            index = item.rfind(spelled)
            if index != -1:
                numbers.append((index, value))

        numbers.sort()
        somme_calibration += int(f"{numbers[0][1]}{numbers[-1][1]}")

    return somme_calibration

if __name__ == "__main__":
    print("--- Day 1: Trebuchet?! ---")
    print(f"Part One: {problem1()}")
    print(f"Part Two: {problem2()}")