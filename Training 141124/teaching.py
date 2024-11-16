from time import sleep

a = ""
words = ["cat", "dog", "bird", "fish", "horse", "cow", "sheep", "goat", "pig", "chicken"]
counter = 0

word = " ".join(words)
#print(word)

for i in word:
    if i == " ":
        print()
    else:
        if counter in [10, 20, 30, 40, 50]:
            a += "*"
        print(a + i)
        sleep(0.1)
        counter += 1
