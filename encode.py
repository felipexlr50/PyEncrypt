
import hashlib
import sys
import base64
import argparse

UNICODE_LIMIT = 65533


def shaToInt(sha):
    return int(sha, 16)


def saveFile(path, toWrite):
    with open(path, 'wb') as f:
        toSave = toWrite.encode('utf-8', errors='ignore')
        # print(toWrite)
        f.write(toSave)
    f.closed


def saveFileHex(path, toWrite):
    with open(path, 'w') as f:
        toSave = toWrite
        # print(toWrite)
        f.write(toSave)
    f.closed


def readFile(path):
    content = ''
    with open(path, 'rb') as f:
        content = f.read().decode('utf-8', errors='ignore')
        # print(content)
    f.closed
    return content


def readFileHex(path):
    content = ''
    with open(path, 'r') as f:
        content = f.read()
        # print(content)
    f.closed
    return content


def myEncoder(text, key):
    text = str(text)
    textList = list(text)
    key = str(key)
    key = hashlib.sha3_512(bytes(key, 'utf-8')).hexdigest()
    # print(key)
    keyList = list(key)
    keyAux = 0

    for k in keyList:
        keyAux += ord(k)

    keyAux += len(textList)

    # print(keyAux)
    for j in range(0, len(textList)):

        currentCharInt = ord(textList[j])

        if(j == 0):
            newChar = currentCharInt ^ int((keyAux / 3))

        if(j % 2 == 0):
            newChar = currentCharInt ^ int(((keyAux + j) / 2))

        else:
            newChar = currentCharInt ^ int((keyAux + j))

        if(newChar > UNICODE_LIMIT):
            while True:
                newChar -= UNICODE_LIMIT
                if(newChar <= UNICODE_LIMIT):
                    break

        if(newChar < 0):
            while True:
                newChar += UNICODE_LIMIT
                if(newChar > 0):
                    break

        textList[j] = chr(int(newChar))

    return ''.join(textList)


def encode(text, key):
    encString = myEncoder(text, key)
    hexString = bytes(encString, "utf-8").hex()
    return hexString


def decode(hexString, key):
    hexBytes = bytes.fromhex(hexString)
    encString = hexBytes.decode("utf-8")
    return myEncoder(encString, key)


def setupArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--encode", help="encode text/file",
                        action="store_true")
    parser.add_argument("--decode", help="decode text/file",
                        action="store_true")
    parser.add_argument("-f", help="file O/I mode", action="store_true")
    parser.add_argument("-v", help="verbode I/O mode", action="store_true")
    parser.add_argument("--hex", help="hex I/O mode", action="store_true")
    parser.add_argument("--fileOutput", help="filename output ", type=str)
    parser.add_argument("text", help="input text", type=str)
    parser.add_argument("key", help="input key", type=str)

    return parser.parse_args()


def parseArgs(args):

    if(args.encode and args.hex):
        if(args.v):
            print(encode(args.text, args.key))

        if(args.f):
            file = readFileHex(args.text)
            enc = encode(file, args.key)
            if(args.fileOutput):
                saveFileHex(args.fileOutput, enc)
            else:
                saveFileHex(args.text, enc)

    elif(args.decode and args.hex):
        if(args.v):
            print(decode(args.text, args.key))

        if(args.f):
            file = readFileHex(args.text)
            enc = decode(file, args.key)
            if(args.fileOutput):
                saveFileHex(args.fileOutput, enc)
            else:
                saveFileHex(args.text, enc)

    elif(args.encode):
        if(args.v):
            print(myEncoder(args.text, args.key))

        if(args.f):
            file = readFile(args.text)
            enc = myEncoder(file, args.key)
            if(args.fileOutput):
                saveFile(args.fileOutput, enc)
            else:
                saveFile(args.text, enc)

    elif(args.decode):
        if(args.v):
            print(myEncoder(args.text, args.key))

        if(args.f):
            file = readFile(args.text)
            enc = myEncoder(file, args.key)
            if(args.fileOutput):
                saveFile(args.fileOutput, enc)
            else:
                saveFile(args.text, enc)


parseArgs(setupArgs())
