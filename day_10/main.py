import numpy as np


class BracketSyntaxChecker():
    CLOSE_TO_OPEN = {  # Create dictionary to map closing brackets to opening brackets
        "}": "{",
        ")": "(",
        "]": "[",
        ">": "<"
    }

    OPEN_TO_CLOSE = {  # Create dictionary to map closing brackets to opening brackets
        "{": "}",
        "(": ")",
        "[": "]",
        "<": ">"
    }

    def __init__(self, string):
        self.string = string

    def check_syntax(self):
        self.stack = []
        for s in self.string:
            if s in self.CLOSE_TO_OPEN.keys():
                if self.CLOSE_TO_OPEN[s] == self.stack[-1]:
                    self.stack.pop(-1)
                else:
                    return s
            elif s in self.CLOSE_TO_OPEN.values():
                self.stack.append(s)
            else:
                raise Exception('invalid bracket')
        return None

    def complete_brackets(self):
        error = self.check_syntax()
        additional_brackets = []
        if not error and self.stack:
            for s in self.stack[::-1]:
                additional_brackets.append(self.OPEN_TO_CLOSE[s])
            return additional_brackets


# input
f = open("input.txt")
lines = f.readlines()
lines = [line.replace('\n', '') for line in lines]

# part 1
bracket_to_points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
points = 0
for line in lines:
    checker = BracketSyntaxChecker(line)
    error = checker.check_syntax()
    if error:
        points += bracket_to_points[error]

print(points)

# part 2
bracket_to_points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}
list_points = []
for line in lines:
    points = 0
    checker = BracketSyntaxChecker(line)
    additional_brackets = checker.complete_brackets()
    if additional_brackets:
        for b in additional_brackets:
            points = points * 5 + bracket_to_points[b]
        list_points.append(points)

print(list_points)
print(int(np.median(list_points)))
