import random
words = ["colleage", "university", "bridge", "temperature", "overtime"]
a = random.choice(words)
ind = words.index(a)
length = len(a)
while True:
    i = 1
    while i <= length:
        print("_", end=" ")
        i += 1
    c = input("\nGuess the letter (L) or Press (* ) if you got the word : ")
    if c == '*':
        b = input("Enter a word  : ")
        if a == b:
            print("Yahooo!! You got a word")
            break
        else:
            print("Oops!! Try again")
    elif c == 'L':
        le = input("Enter a Letter  : ")
        if le in a:
            print(le, "is in word")
            ls = []
            for index, a in enumerate(a):
                if a == le:
                    ls.append(index)
                    print("index of ", le, "is", ls)
                    break












