"""
Begin with a KNOWN table --> 256 ascii chars in a dictionary (letter_dict)
letter_dict = {i: chr(i) for i in range(256)}
print(letter_dict)

actually not needed...
add each character to a dictionary ( known chars)
add each unknown multi-character string to the dictionary


"""


class lzw:
    def __init__(self, text1):
        self.encode(text1)

    def encode(self, file1):
        # create a letter string from input file
        letter_string = ''
        with open(file1) as file:
            for letter in file.read():
                letter_string += letter
        counter = 0

        # create dictionary with each new-found letter string
        letter_dict = {}
        for letter in letter_string:
            if letter not in letter_dict.values():
                letter_dict[counter] = letter
                counter += 1

        # add each new multi-character string to dictionary
        for letter in letter_string:
            if letter in letter_dict.values():
                letter_dict[counter + 1] = letter

        print(letter_dict, len(letter_dict))

    def decode(self):
        pass
