#Author = Varfolomeev Nikita Denisovich
#Group = P3112
#Date = 05.10.2025
#1

from re import*

num = int(input("Номер: "))
with open("Informatics_Lab3_Task3_test", "r") as file:
    text = file.readlines()

words = findall(r"\b\w+\b|[^\w]", text[0])

adjectives = []
for i, word in enumerate(words):
    if match(r"^[А-Яа-я]+(ый|ий|ой|ая|яя|ое|ее|ого|его|ому|ему|ей|ую|юю|ым|им|ем|ых|их|ыми|ими)$", word):
        adjectives.append((i, word))

if 0 < num <= len(adjectives):
    sample_idx, sample_word = adjectives[num - 1]
    sample_ending = sample_word[-2:]
    for i, (idx, adj) in enumerate(adjectives):
        if i != num - 1:
            base = sub(r"(ый|ий|ая|яя|ое|ее|ого|его|ому|ему|ой|ей|ую|юю|ым|им|ем|ых|их|ыми|ими)$", "", adj)
            new_adj = base + sample_ending
            words[idx] = new_adj

result = ''
for i, word in enumerate(words):
    result += word

print("Результат:")
print(result)