from collections import Counter


# input
f = open('input.txt')
template = f.readline().replace('\n', '')
f.readline()
rules = [line.replace('\n', '').split(' -> ') for line in f.readlines()]
rules = {pair: insertion for pair, insertion in rules}
print(rules)

# part 1
last_element = template[-1]
counts = Counter()
for j in range(len(template) - 1):
    pair = template[j: j + 2]
    counts[pair] += 1

print(counts)
for i in range(40):
    for pair, amount in list(counts.items()):
        new_mol = rules[pair]
        counts[pair] -= amount
        counts[pair[0] + new_mol] += amount
        counts[new_mol + pair[-1]] += amount
print(counts)

element_counts = Counter()
for pair, amount in counts.items():
    element_counts[pair[0]] += amount
max_element = max(element_counts, key=element_counts.get)
min_element = min(element_counts, key=element_counts.get)
element_counts[last_element] += 1

print(element_counts[max_element] - element_counts[min_element])
