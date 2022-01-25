# Mert TÜRKER 280201097
# Berke TINAS 270201079

import string
from timeit import default_timer as timer


lowerAlphabet = string.ascii_lowercase
upperAlphabet = string.ascii_uppercase


def encoder(message, keyword):
    index = 0
    keyword_phrase = ""
    coded_message = ""

    for char in message:
        if char in lowerAlphabet:
            # Add keyword character to keyword_phrase
            keyword_phrase = keyword_phrase + keyword[index]

            # Shift message character by its keyword_phrase character
            charIndex = lowerAlphabet.find(char)
            keyIndex = lowerAlphabet.find(keyword[index].lower())
            newIndex = (charIndex + keyIndex) % len(lowerAlphabet)

            # Add character to coded message
            coded_message = coded_message + lowerAlphabet[newIndex]

            # Update index
            index = (index + 1) % len(keyword)
        elif char in upperAlphabet:
            # Add keyword character to keyword_phrase
            keyword_phrase = keyword_phrase + keyword[index]

            # Shift message character by its keyword_phrase character
            charIndex = upperAlphabet.find(char)
            keyIndex = upperAlphabet.find(keyword[index].upper())
            newIndex = (charIndex + keyIndex) % len(upperAlphabet)

            # Add character to coded message
            coded_message = coded_message + upperAlphabet[newIndex]

            # Update index
            index = (index + 1) % len(keyword)
        else:

            coded_message = coded_message + char

            continue

    return coded_message


def decoder(message, keyword):
    index = 0
    keyword_phrase = ""
    decoded_message = ""

    for char in message:

        if char in lowerAlphabet:
            # Add keyword character to keyword_phrase

            keyword_phrase = keyword_phrase + keyword[index]

            # Unshift message character by its keyword_phrase character
            charIndex = lowerAlphabet.find(char)
            keyIndex = lowerAlphabet.find(keyword[index].lower())
            newIndex = (charIndex - keyIndex) % len(lowerAlphabet)

            # Add character to decoded message
            decoded_message = decoded_message + lowerAlphabet[newIndex]

            # Update index
            index = (index + 1) % len(keyword)
        elif char in upperAlphabet:
            # Add keyword character to keyword_phrase
            keyword_phrase = keyword_phrase + keyword[index]

            # Unshift message character by its keyword_phrase character
            charIndex = upperAlphabet.find(char)

            keyIndex = upperAlphabet.find(keyword[index].upper())
            newIndex = (charIndex - keyIndex) % len(upperAlphabet)

            # Add character to decoded message
            decoded_message = decoded_message + upperAlphabet[newIndex]

            # Update index
            index = (index + 1) % len(keyword)
        else:
            # Deal with non-alphabet characters
            decoded_message = decoded_message + char

            continue


    return decoded_message


def decoderForCracker(message, keyword):
    index = 0
    keyword_phrase = ""
    decoded_message = ""
    message = ''.join(e for e in message if e.isalpha()).lower()  # format the message
    keyword = ''.join(e for e in keyword if e.isalpha()).lower()  # format the keyword
    for char in message:
        # Add keyword character to keyword_phrase

        keyword_phrase = keyword_phrase + keyword[index]

        # Unshift message character by its keyword_phrase character
        charIndex = lowerAlphabet.find(char)
        keyIndex = lowerAlphabet.find(keyword[index])
        newIndex = (charIndex - keyIndex) % len(lowerAlphabet)

        # Add character to decoded message
        decoded_message = decoded_message + lowerAlphabet[newIndex]

        # Update index
        index = (index + 1) % len(keyword)

    return decoded_message


def vigenereCracker(cipherText, plainText):
    possibleKey = decoderForCracker(cipherText, plainText)

    for i in range(1, len(plainText) + 1):
        if plainText == decoder(cipherText, possibleKey[0:i]):
            print("key: ", possibleKey[0:i])
            return possibleKey[0:i]


loop = True
while loop:
    print('Select mode:')

    print('1 - Encoder')
    print('2 - Decoder')
    print('3 - Key finder')
    print('enter 0 to exit')
    mode = input('Mode: ')

    if mode == '1':
        msg = input('plain text:')
        key = input(' key:')
        print(encoder(msg, key))
    elif mode == '2':
        msg = input('cipher text:')
        key = input('Key:')
        print(decoder(msg, key))
    elif mode == '3':
        msg = input('Plain text:')
        cipher = input('cipher text:')
        start = timer()
        vigenereCracker(cipher, msg)
        end = timer()
        print('elapsed time: ', end - start, ' seconds')
    elif mode == '0':
        loop = False
        exit(1)
    else:
        print('unknown mode entry. Please enter valid mode number.')
