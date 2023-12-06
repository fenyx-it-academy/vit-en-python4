# This is the third exercise
# This is a translation for Morse Code

MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                   'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
                   'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---',
                   '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                   '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}
morse00len = len(MORSE_CODE_DICT)

inputtype = input("""Please enter type of your sentence, <<< "M" for morse or "T" for text >>> : """)
inputtype = inputtype.lower()

morseword = ""
txtword = ""

if inputtype == 'm':
    morse01 = input("Please enter your morse code: ")
    morselen = len(morse01)
    for i in range(0, morselen, 1):
        if morse01[i] == '.' or morse01[i] == '-':
            morseword += morse01[i]
        elif morse01[i] == ' ':
            for x, y in MORSE_CODE_DICT.items():
                if morseword == y:
                    txtword +=  x
                    morseword =""
        else:
            print("Your MorseCode that you entered is invalid!")
    for x, y in MORSE_CODE_DICT.items():
        if morseword == y:
            txtword += x
elif inputtype == 't':
    text01 = input("Please enter your text: ")
    text01 = text01.upper()
    textlen = len(text01)
    for i in range(0, textlen, 1):
        for x, y in MORSE_CODE_DICT.items():
            if x == text01[i]:
                morseword = morseword + " " + y


if inputtype == 'm':
    print(txtword)
elif inputtype == 't':
    print(morseword)
else:
    print("Error")

# End of the Exercise
