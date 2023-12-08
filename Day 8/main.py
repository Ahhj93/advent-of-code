def parse_input(input: str) -> (str, dict):
    """
    Parse the input into a list of instructions and a dictionary of nodes.
    :param input: The input string.
    :return: A tuple of the instructions and nodes.
    """
    input: str = input.split("\n\n")
    instructions: str = (input[0].split("\n"))[0]
    rules: str = input[1].split("\n")
    nodes: dict = {}
    for rule in rules:
        rule = rule.split(" = ")
        nodes[rule[0]] = rule[1].replace("(", "").replace(")", "").split(", ")
    return instructions, nodes

def to_zzz(instructions: str, nodes: dict) -> int:
    """
    Find the number of steps to get from AAA to ZZZ.
    :param instructions: The instructions.
    :param nodes: The nodes.
    :return: The number of steps.
    """
    count: int = 0
    i: int = 0
    current: str = "AAA"
    while (current != "ZZZ"):
        if i == len(instructions):
            i = -1
        elif instructions[i] == "R":
            current = nodes[current][1]
            count += 1
        else:
            current = nodes[current][0]
            count += 1
        i += 1
    return count

def main() -> int:
    """
    Execute the program.
    :return: The number of steps to get from AAA to ZZZ.
    """
    input_text_file = open("input.txt", "r")
    input_text: str = input_text_file.read()
    instructions, nodes = parse_input(input_text)
    return to_zzz(instructions, nodes)

if __name__ == "__main__":
    print("--- Day 8: Haunted Wasteland ---")
    print(f"Part One: {main()}")