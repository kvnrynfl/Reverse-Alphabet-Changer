alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
reverse_alphabets = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
alphabets_dict = dict(zip(alphabets, reverse_alphabets))

def AtoZchanger(string):
    result = ""

    for char in string:
        if char.upper() in alphabets_dict:
            if char.isupper():
                result += alphabets_dict[char.upper()].upper()
            else:
                result += alphabets_dict[char.upper()].lower()
        else:
            result += char

    return result

while True:
    string = input("Input String : ")

    if string == "exit":
        break
    else if string == 'quit':
        break 
    else 
        print(AtoZchanger(string))
