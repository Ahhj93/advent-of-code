import re

def problem1():
    input_text_file = open("puzzle.txt", "r")
    input_list : list  = input_text_file.read().split("\n")
    somme_calibration : int = 0

    for item in input_list:
        nombre_str: str = ""
        for elt in item:
            if elt.isdigit():
                nombre_str += elt
        nombre_str = nombre_str[0] + nombre_str[-1]
        somme_calibration += int(nombre_str)

    print(somme_calibration)

number : list = [None, "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def problem2():
    input_text_file = open("puzzle2.txt", "r")
    input_list : list  = input_text_file.read().split("\n")
    somme_calibration : int = 0
    for item in input_list:
        number_str : str = ""
        number1 : list = [-1] * 10
        number2 : list = [-1] * 10
        for i in range (1,10):
            n11 = re.search(rf'\b{number[i]}\b', item)
            n12 = re.search(rf'\b{str(i)}\b', item)
            if n11 and n12:
                number1[i] = min([n11.start(), n12.start()])
            if n11:
                number1[i] = n11.start()
            else:
                number1[i] = n12.start()
            number1[i] = min([re.search(rf'\b{number[i]}\b', item), re.search(rf'\b{str(i)}\b', item)])
            number2[i] = max([item.rfind(number[i]), item.rfind(str(i))])
        number_str += str(number1.index(min([i for i in number1 if i>=0])))
        number_str += str(number2.index(max([i for i in number2 if i>=0])))
        somme_calibration += int(number_str)

    print(somme_calibration)

if __name__ == "__main__":
    problem1()
    problem2()