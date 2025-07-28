import random
import time

words = [
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "I",
    "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
    "this", "but", "his", "by", "from", "they", "we", "say", "her", "she",
    "my", "yours", "never", "except"
]

word_list = []

number_of_words = int(input("How many words would you like?\n"))

for _ in range(number_of_words):
    word_list.append(random.choice(words))

string_words = ' '.join(word_list)

start_time = time.time()

user_input = input(f"{string_words}\n")

end_time = time.time()

final_time = round(end_time-start_time,2)
wpm = round(number_of_words/final_time*60,2)

if user_input==string_words:
    print(f"You completed {number_of_words} words in {final_time} seconds or {wpm} words per minute.")
else:
    print("You have failed the typing test, please try again.")

