import re
import itertools


#word rules:
#a word must not use the same side twice in a row
#must be atleast 3 letters long
#must start with the last letter of the previous word unless it is the first word

#game rules:
#the first word can start with any letter
#must use all the letters on the board

#game ends when player has used all the letters on the board
#player aims to use fewest words possible

#we have a 4 sets of letters, one for each side of the box
#when we use a letter from one set we can't use it again until we have used a letter from another set
#letters must make a word from the valid word text file

#we need to create a function that will take the letters from the box and return a list of words that can be made from those letters

#function that reads the txt and returns a list of words that can be spelled with our letters

def wordFinder(letters):
    f = open("validWords.txt")
    valid_words = []
    for line in f:
        if re.search(rf"[^{letters}]", line, re.IGNORECASE):
            continue
        valid_words.append(line)

    return valid_words


def letterFinder(l, l_lists):
    in_lists = set()
    for w in l_lists:
        if l in w:
            in_lists.add(w)
    return in_lists


def validFinder(w, l_lists):
    curr_lists = set()
    prev_lists = set()

    for c in w:
        if c == 0:
            # get the list that c is from
            prev_lists = letterFinder(c, l_lists)
            continue
        curr_lists = letterFinder(c, l_lists)
        # if either of the lists have multiple sides or are different from each other continue to next letter
        # and update variables
        if not (len(curr_lists) == 1 and len(prev_lists) == 1 and curr_lists == prev_lists):
            if c == len(w):
                return w
            prev_lists = curr_lists
            continue
        return


def is_valid_chain(words):
    # Generate all permutations of the three words
    for perm in itertools.permutations(words):
        w1, w2, w3 = perm
        if w1[-1] == w2[0] and w2[-1] == w3[0]:
            return perm
    return None

print("Please Enter the letters on the top separated by a space:")
top_input = input()
lettersT = top_input.split()
letters = top_input.replace(" ", "|")

print("Please Enter the letters on the bottom separated by a space:")
bottom_input = input()
lettersB = bottom_input.split()
letters += "|" + bottom_input.replace(" ", "|")

print("Please Enter the letters on the left side separated by a space:")
left_input = input()
lettersL = left_input.split()
letters += "|" + left_input.replace(" ", "|")

print("Please Enter the letters on the right side separated by a space:")
right_input = input()
lettersR = right_input.split()
letters += "|" + right_input.replace(" ", "|")

# Use a list or dictionary instead of a set
letter_lists = [lettersT, lettersB, lettersL, lettersR]
words = wordFinder(letters)

letters.replace("|", "")

# we have a large list of words that can be spelt using only the letters available
# now we need to take those words

# the word list approach

# create an algorithm that takes a word and goes letter by letter checking if the letter is valid,
# as in it is not from the same side
# iterate through words
# iterate through letters
# if first character skip for now
# if current character is from same string as last character : invalid
# if there are duplicate characters : valid
top = 1
bottom = 2
left = 3
right = 4

# exists in one list
# exists in a different list
# good
# exists in one list
# exists in the same list
# bad
# exists in two lists
# exists in one of the two lists
# good
# exists in two lists
# exists in the same two lists
# good

valid_words = set()

for i in words:
    valid_words.add(validFinder(i, letter_list))

valid_combos = []
low = 9999
# go through all the words making combination sets of words that
# B: start with the letter of the previous words last letter
# A: contain all letter (use regex?)

# A: iterate through all words
# take a word add it to the set, if the set uses all letters add set to combo set
# if not through it away and move to next word
# once through all the words add the next
# we have a max of 3 words per combo
# we add first word
#iterate through
# i   j   k
# w1  w2  w3
# w1  w2  w4
# w1  w2  w5

# w1  w3  w4
# w1  w3  w5

# w1  w4  w5
# w1  w4  w6

# w1  w5  w6
# w1  w5  w7

# w2  w3  w4
# w2  w3  w5
current_combo = []

for i in valid_words:
    current_combo[0] = i
    j = i + 1
    if all(x in current_combo for x in letters):
        valid_combos.append(current_combo)
    for j in valid_words:
        current_combo[1] = j
        k = j + 1
        if all(x in current_combo for x in letters):
            valid_combos.append(current_combo)
        for k in valid_words:
            current_combo[2] = k
            if all(x in current_combo for x in letters):
                valid_combos.append(current_combo)

shortest_combos = []

for combo in valid_combos:
    if len(combo) == 1:
        shortest_combos.append(combo)
if len(shortest_combos) > 0:
    print("Your shortest combo/s is: ")
    for combos in shortest_combos:
        for word in combos:
            print(word)
    print("\n")
    quit()

for combo in valid_combos:
    # if regex: capture the last letter of both words, match if captured letter is at start of word 1 or 2
    # capture both last letters into separate variables,
    # match if l1 is a start of word 2, match if l2 is at start of word 1
    # if there are 3 words
    # get all first letters
    # get all last letters
    # we don't want a word matching with itself
    # if [0] = /[1] or /[2]
    # if [1] = /[0] or /[2]
    # if [2] = /[0] or /[1]
    shortest_combos.append(is_valid_chain(combo))

done = False
while not done:
    done = True
    for current_combo in shortest_combos:
        # if it is equal to or lower than the current low add it to shortest
        # and remove no longer short combos
        if len(current_combo) < low:
            low = len(current_combo)
            done = False
        elif len(current_combo) > low:
            shortest_combos.remove(current_combo)




print("Here is your board:")
print("  " + " ".join(lettersT))
for i in range(len(lettersL)):
    print(lettersL[i] + "      " + lettersR[i])
print("  " + " ".join(lettersB))

print("Your shortest combo/s is: ")
for combos in shortest_combos:
    for word in combos:
        print(word)
    print("\n")
