# Gets user input
word = str(input("Enter a word or sentence: "))
# Turns input into a list
word = list(word.upper())

# Counts the number of characters in the input
def count(word):
    number = 0
    for x in word:
        number += 1
    return(number)

# Checks that the input isn't too short or too long
if len(word) == 0:
    print("You didn't input anything.")
elif len(word) >= 100:
    print("That is too many characters.")
# outputs the number of characters in the input
else:
    print("Your input has " + str(count(word)) + " characters.")