# Avoid adding a block of code for each question & answer by iterating the conditional statement through a single randomized list of lists.
# Randomize the list of lists using .shuffle() method. The order inside the nested lists won't change, so for example L[0][0] is the question and L[0][1] is the answer of the first element of the randomized list.
# Make the input case-insensitive with .lower() method.
# Optional: add a count of right and wrong answers.

import random

L = [["Who is Batman's sidekick ?: ", "Robin"], ["Which is the capital of North Ireland ?: ", "Belfast"], ["What do caterpillars turn into ?: ", "Butterflies"]]
random.shuffle(L)
r = 0 # right answers count
w = 0 # wrong answers count
for i in range(0, len(L), 1):
    user_input = input(L[i][0])
    if user_input.lower() == L[i][1].lower():
        print("That's right !")
        r = r + 1
    else:
        print("Wrong answer")
        w = w + 1
    print(str(r) + " right and " + str(w) + " wrong answers)")

    








