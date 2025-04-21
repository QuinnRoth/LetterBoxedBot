

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



print("Please Enter the letters on the top separated by a space:")
lettersT = input().split()
print("Please Enter the letters on the bottom separated by a space:")
lettersB = input().split()
print("Please Enter the letters on the left side separated by a space:")
lettersL = input().split()
print("Please Enter the letters on the right side separated by a space:")
lettersR = input().split()

print("Here is your board:")
print("  " + " ".join(lettersT))
for i in range(len(lettersL)):
    print(lettersL[i] + "      " + lettersR[i])
print("  " + " ".join(lettersB))


