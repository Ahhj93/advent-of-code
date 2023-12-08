def parse_input(input):
    input = input.split("\n\n")
    instructions = (input[0].split("\n"))[0]
    rules = input[1].split("\n")
    nodes = {}
    for rule in rules:
        rule = rule.split(" = ")
        nodes[rule[0]] = rule[1].replace("(", "").replace(")", "").split(", ")
    return instructions, nodes

def to_zzz(instructions, nodes):
    count = 0
    i = 0
    current = "AAA"
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

def main():
    input_text_file = open("input.txt", "r")
    input_text = input_text_file.read()
    instructions, nodes = parse_input(input_text)
    return to_zzz(instructions, nodes)

if __name__ == "__main__":
    print(main())