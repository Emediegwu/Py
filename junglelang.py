'''
This little Python translator translates every word to a sort of language known as 'jungle language'.
It basically changes every vowel (a,e,i,o,u) in the English alphabet to a number ranging from 1 to 5.
That simply means: a=1, e=2, i=3, o=4, u=5.
An "a" is added to every consonant.
For instance, the name 'John' translates to 'Ja4hana', and 'America' translates to 1ma2ra3ca1.
'''
def translate(words):
    translation = ""
    for letters in words:
        if letters.lower() in "a":
            translation = translation + "1"
        elif letters.lower() in "e":
            translation = translation + "2"
        elif letters.lower() in "i":
            translation = translation + "3"
        elif letters.lower() in "o":
            translation = translation + "4"
        elif letters.lower() in "u":
            translation = translation + "5"
        elif letters.lower() in "bcdfghjklmnpqrstvwxyz":
            translation = translation + letters + "a"
        else:
            translation = translation + letters
    return translation

    print(translate(input("Enter word/sentence: ")))
