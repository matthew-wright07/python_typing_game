import random

words = ["hello","the","no","yes","maybe","never","why","awesome","super","wow","go","get","my","your"]

word_list = []

for _ in range(15):
    word_list.append(random.choice(words))

string_words = ' '.join(word_list)

print(string_words)

user_input = input("type out the letters\n")

if user_input==string_words:
    print("Yay you did it")
else:
    print("Your trash kid")

