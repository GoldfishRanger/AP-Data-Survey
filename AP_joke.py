## User Input
## At least one list
## A function
# if loop
## for/while loop
## call the function
## output something

word = str(input("Enter a word or sentence: "))
word = list(word.upper())

if len(word) == 0:
    print("you didn't input anything")
elif len(word) >= 100:
    print("that is too many characters")

def count(word):
    number = 0
    for x in word:
        number += 1
    return(number)

print(count(word))