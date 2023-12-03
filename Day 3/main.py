input_text_file = open("input.txt", "r")
input_list : list  = input_text_file.read().splitlines()

def is_symbol(char: str) -> bool:
    return not char == '.' and not char.isdigit()

def is_valid_index(i: int, j: int, rows: int, cols: int) -> bool:
    return 0 <= i < rows and 0 <= j < cols

def calculate_part_numbers(input_list : list) -> int:
    rows: int = len(input_list)
    cols: int = len(input_list[0])

    part_numbers_sum: int = 0

    i: int = 0
    while i < rows:
        j: int = 0
        while j < cols:
            current_char = input_list[i][j]

            if current_char.isdigit():
                is_part_number: bool = False

                # Check all adjacent positions (including diagonals)
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if is_valid_index(i + x, j + y, rows, cols) and is_symbol(input_list[i + x][j + y]):
                            is_part_number = True
                            break

                if is_part_number:
                    #Récupérer le nombre
                    num1: bool = False
                    begin_num: int = j
                    while not num1 and begin_num >= 0:
                        if input_list[i][begin_num].isdigit():
                            begin_num -= 1
                        else:
                            num1 = True
                    num2: bool = False
                    end_num: int = j
                    while not num2 and end_num < cols:
                        if input_list[i][end_num].isdigit():
                            end_num += 1
                        else:
                            num2 = True
                    if input_list[i][begin_num + 1:end_num] != '':
                        part_numbers_sum += int(input_list[i][begin_num + 1:end_num])
                    j = end_num
            j += 1
        i += 1

    return part_numbers_sum

if __name__ == "__main__":
    print("--- Day 3: Gear Ratios ---")
    print(f"Part One: {calculate_part_numbers(input_list)}")