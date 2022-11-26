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