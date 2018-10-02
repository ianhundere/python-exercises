def alphabet_position(text):
    text = text.lower()
    abc = "abcdefghijklmnopqrstuvwxyz"
    indexes = []

    for letter in text:
        index = abc.find(letter)
        if index >= 0:
            indexes.append(index + 1)
    return str(indexes)
