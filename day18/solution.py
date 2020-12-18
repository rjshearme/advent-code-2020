with open("input.txt") as fh:
    input_lines = fh.read().split("\n")

def parse_tokens(string_input):
    tokens = [char for char in string_input if char != " "]
    for idx, token in enumerate(tokens):
        try:
            tokens[idx] = int(token)
        except ValueError:
            pass
    return tokens


def top_level_brackets(tokens):
    top_level_brackets = []
    level = 0
    start_idx = -1
    for idx, token in enumerate(tokens):
        if token == "(":
            start_idx = idx if level == 0 else start_idx
            level += 1
        elif token == ")":
            level -= 1

        if level == 0 and start_idx != -1:
            top_level_brackets.append((start_idx, idx))
            start_idx = -1
    return top_level_brackets


def calculate_output(tokens):
    if isinstance(tokens, int):
        return tokens
    tokens = tokens_generator(tokens)
    total = next(tokens)

    while True:
        try:
            operator = next(tokens)
            value = next(tokens)
        except StopIteration:
            break
        if operator == "+":
            total += value
        elif operator == "*":
            total *= value
    return total


def flatten_tokens(tokens):
    if "(" in tokens and ")" in tokens:
        brackets = top_level_brackets(tokens)
        brackets_substitutions = [flatten_tokens(tokens[start_bracket+1:end_bracket]) for start_bracket, end_bracket in brackets]
        lshift = 0
        for brackets, brackets_substitutions in zip(brackets, brackets_substitutions):
            start_pos = brackets[0] - lshift
            end_pos = brackets[1] - lshift
            tokens[start_pos:end_pos + 1] = [brackets_substitutions]
            lshift += brackets[1] - brackets[0]

    return calculate_output(tokens)


def tokens_generator(tokens):
    for token in tokens:
        yield token


def evaluate(string_input):
    tokens = parse_tokens(string_input)
    flat_tokens = flatten_tokens(tokens)
    return calculate_output(flat_tokens)


def reverse_polish_notation(tokens):
    output = []
    operators = []
    for token in tokens:
        if isinstance(token, int):
            output.append(token)
        elif token == "(":
            operators.append("(")
        elif token == ")":
            operators_str = "".join(operators)
            open_par_idx = operators_str.rindex("(")
            operators, poperators = operators[:open_par_idx], operators[open_par_idx+1:][::-1]
            output.extend(poperators)
        elif not operators:
            operators.append(token)
        elif token == "+":
            poperator = operators.pop()
            if poperator == "(":
                operators.append("(")
                operators.append(token)
            elif poperator == "*":
                operators.append("*")
                operators.append("+")
            else:
                output.append("+")
                operators.append("+")
        elif token == "*":
            poperator = operators.pop()
            if poperator == "(":
                operators.append("(")
                operators.append(token)
            else:
                output.append(poperator)
                operators.append(token)

    output.extend(operators[::-1])
    return output


def first_op_ind(rpn):
    for idx, tok in enumerate(rpn):
        if str(tok) in "+*":
            return idx


def calculate_rpn(rpn):
    while len(rpn) != 1:
        print(rpn)
        op_ind = first_op_ind(rpn)
        val = rpn[op_ind-1] * rpn[op_ind-2] if rpn[op_ind] == "*" else rpn[op_ind-1] + rpn[op_ind-2]
        rpn = rpn[:op_ind-2] + [val] + rpn[op_ind+1:]
    return rpn.pop()


def evaluate2(line):
    tokens = parse_tokens(line)
    rpn = reverse_polish_notation(tokens)
    return calculate_rpn(rpn)


def part2(input_lines):
    sum = 0
    for line in input_lines:
        sum += evaluate2(line)
    return sum


def part1(input_lines):
    sum = 0
    for line in input_lines:
        sum += evaluate(line)
    return sum

print(part2(input_lines))