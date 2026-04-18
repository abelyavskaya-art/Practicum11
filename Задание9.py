lines = []

while True:
    line = input()
    if line == "":
        break
    lines.append(line)

text = "\n".join(lines)

# Delete punctuation.
punctuation = ".,!?;:()[]{}«»\"'"
for symbol in punctuation:
    text = text.replace(symbol, " ")

words = text.lower().split()

count = {}
order = []

for word in words:
    if word not in count:
        count[word] = 0
        order.append(word)
    count[word] += 1

# Sort words.
sorted_words = sorted(order, key=lambda w: (-count[w], order.index(w)))

for word in sorted_words:
    print(word)
