from typing import List

import numpy as np

# input
f = open('input.txt')

lines = f.readlines()
lines = [line.replace('\n', '').split(' | ') for line in lines]
signals, outputs = [line[0] for line in lines], [line[1] for line in lines]

len_outputs = np.array([list(map(len, output.split())) for output in outputs])
len_signals = np.array([list(map(len, signal.split())) for signal in signals])

print(np.sum(np.isin(len_outputs, [2, 3, 4, 7])))


# part 2

class signal():
    SIGNAL_TO_DIGIT = {
        2: 1,
        3: 7,
        4: 4,
        7: 8
    }

    def __init__(self, string):
        self.string: set= set(string)
        self.length = len(string)
        self.digit = self.recognise_digit()

    def recognise_digit(self):
        try:
            return self.SIGNAL_TO_DIGIT[self.length]
        except:
            return None

    def __str__(self):
        return str(self.digit)

    def __eq__(self, other):
        return self.string.issuperset(other.string)

decoded_signals=[]

for i in signals:
    signal_pattern = [signal(j) for j in i.split()]
    decoded_pattern: List[signal] = np.zeros(10, dtype=object)
    for j in signal_pattern:
        if j.digit:
            decoded_pattern[j.digit] = j

    for j in signal_pattern:
        if j.length == 5:
            if decoded_pattern[1].string.issubset(j.string):
                j.digit = 3
                decoded_pattern[3] = j
            elif len(decoded_pattern[4].string.intersection(j.string)) == 2:
                j.digit = 2
                decoded_pattern[2] = j
            elif len(decoded_pattern[4].string.difference(decoded_pattern[7].string).intersection(j.string)) == 2:
                j.digit = 5
                decoded_pattern[5] = j
        elif j.length == 6:
            if len(decoded_pattern[7].string.intersection(j.string)) == 2:
                j.digit = 6
                decoded_pattern[6] = j
            elif decoded_pattern[4].string.issubset(j.string):
                j.digit = 9
                decoded_pattern[9] = j
            elif len(decoded_pattern[4].string.difference(decoded_pattern[7].string).intersection(j.string)) == 1:
                j.digit = 0
                decoded_pattern[0] = j

    decoded_signals.append(decoded_pattern)

decoded_outputs = []

for i in range(len(outputs)):
    decoded_output = []
    for j in outputs[i].split():
        for k in decoded_signals[i]:
            if set(j) == k.string:
                decoded_output.append(k.digit)
    decoded_outputs.append(decoded_output)

# print(decoded_outputs)

digits = []

for output in decoded_outputs:
    digits.append(int(''.join([str(i) for i in output])))

print(sum(digits))




