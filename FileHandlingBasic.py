file = open("data.txt", "r")

content = file.read()

print(content)

lines = content.splitlines()
words = content.split()
characters = len(content)

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", characters)

file.close()
