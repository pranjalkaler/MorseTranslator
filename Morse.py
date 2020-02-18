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
        morse += MORSE_CODE_DICT[char]
        morse += ' '
    return morse

def morseToText(morse):
    text = ""
    for char in morse:
        text += decrypt(morse)
    return text

def main():
    text = input("Enter a string: ")
    print(textToMorse(text.upper()))

if __name__ == "__main__":
    main()
