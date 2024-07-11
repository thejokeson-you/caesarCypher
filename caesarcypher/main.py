# This is a sample Python script.

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"
    , "u", "v", "w", "x", "y", "z"]


def encrypt(inpstr, key):
    inp_list = list(inpstr)
    new_inp_list = []
    i = 0
    for x in inp_list:
        if x == " ":
            new_inp_list[i] == " "
        else:
            new_index = (alphabet.index(x) + key) % 26
            new_inp_list.append(alphabet[new_index])

        i += 1

    return str(new_inp_list)


print("CAESAR CYPHER")
print("----------------------")
inpString = input("Enter the string you want to encrypt: ")
inpKey = int(input("Enter the key which you want to shift by: "))
encrypt(inpString, inpKey)
