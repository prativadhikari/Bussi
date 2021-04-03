"""
The given program asks a user for a word and
tells how many vowels and consonants the word contains.
"""
def main():
    ask = input("Enter a word: ")
    vowels = 0
    consonants = 0
    for i in ask:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            vowels = vowels + 1
        else:
            consonants = consonants + 1

    print("Word",(ask),"contains",(vowels),"vowels and",(consonants),"Consonants")





