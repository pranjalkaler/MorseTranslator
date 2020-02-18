MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
        'C':'-.-.', 'D':'-..', 'E':'.', 
        'F':'..-.', 'G':'--.', 'H':'....', 
        'I':'..', 'J':'.---', 'K':'-.-', 
        'L':'.-..', 'M':'--', 'N':'-.', 
        'O':'---', 'P':'.--.', 'Q':'--.-', 
        'R':'.-.', 'S':'...', 'T':'-', 
        'U':'..-', 'V':'...-', 'W':'.--', 
        'X':'-..-', 'Y':'-.--', 'Z':'--..', 
        '1':'.----', '2':'..---', '3':'...--', 
        '4':'....-', '5':'.....', '6':'-....', 
        '7':'--...', '8':'---..', '9':'----.', 
        '0':'-----', ',':'--..--', '.':'.-.-.-', 
        '?':'..--..', '/':'-..-.', '-':'-....-', 
        '(':'-.--.', ')':'-.--.-', ' ':'/'} 

def textToMorse(message):
    morse = ""
    for char in message:
        morse += MORSE_CODE_DICT[char] + ' '
    return morse

def morseToText(morse):
    morse += ' '
    keyList = list(MORSE_CODE_DICT.keys())
    valList = list(MORSE_CODE_DICT.values())
    text = ""
    letter = ""
    for char in morse:
        if char == '.' or char == '-':
            letter += char
        elif char == ' ':
            if letter != '':
                text += keyList[valList.index(letter)]
                letter = ""
        elif char == '/':
            text += ' '
    return text

def main():
    text = input("Enter a string: ")
    print(textToMorse(text.upper()))
    print(morseToText(".... . .-.. .-.. --- / .-- --- .-. .-.. -.."))

if __name__ == "__main__":
    main()
