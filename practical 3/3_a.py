sentence = input("Enter the sentence: ")
d = 0
u = 0
l = 0
space = 0
symbol = 0
for s in sentence:
    if s.isdigit():
        d = d+1
    elif s.isupper():
        u = u+1
    elif s.islower():
        l = l+1
    elif s.isspace():
        space = space + 1
    else:
        symbol = symbol + 1
print("Digit: ", d)
print("letters: ", len(sentence))
print("Uppercase: ", u)
print("Lowercase: ", l)
print("Space: ", space)
print("Extra symbol: ", symbol)