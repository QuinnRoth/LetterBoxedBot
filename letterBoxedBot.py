import nltk
import re
from nltk import word_tokenize


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


    for c in i:

        if c == 0:
            p = c
            # get the list that c is from
            prev_lists = letterFinder(c, letter_list)
            continue
        curr_lists = letterFinder(c, letter_list)
        # if either of the lists have multiple sides or are different from each other continue to next letter
        # and update variables
        if not (len(curr_lists) == 1 and len(prev_lists) == 1 and curr_lists == prev_lists):

            p = c
            prev_lists = curr_lists



print("Please Enter the letters on the top separated by a space:")
lettersT = input().split()
letters = input().replace(" ", "|")
print("Please Enter the letters on the bottom separated by a space:")
lettersB = input().split()
letters = letters + "|" + input().replace(" ", "|")
print("Please Enter the letters on the left side separated by a space:")
lettersL = input().split()
letters = letters + "|" + input().replace(" ", "|")
print("Please Enter the letters on the right side separated by a space:")
lettersR = input().split()
letters = letters + "|" + input().replace(" ", "|")

letter_list = {lettersT, lettersB, lettersL, lettersR}
words = wordFinder(letters)

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



print("Here is your board:")
print("  " + " ".join(lettersT))
for i in range(len(lettersL)):
    print(lettersL[i] + "      " + lettersR[i])
print("  " + " ".join(lettersB))
