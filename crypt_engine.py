
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


def readByteFile(path):
    content = None
    with open(path, 'rb') as f:
        content = f.read()
    f.closed
    return content


def saveByteFile(path, toWrite):
    with open(path, 'wb') as f:
        f.write(toWrite)
    f.closed


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


def XORBytesV3(encString, key, isDec=False):
    keys = []

    keyHex = hashlib.sha3_512(bytes(key, 'utf-8')).hexdigest()
    keys.append(keyHex[:42])
    keys.append(keyHex[42:-42])
    keys.append(keyHex[-42:])

    if(isDec):
        keys = reversed(keys)

    for key in keys:
        encString = XORBytes(encString, key)

    return encString


def XORBytes(encString, key):
    byteSum = 0
    encBytes = []
    encArr = []
    if(type(encString) == bytes):
        encArr = list(encString)
    else:
        encArr = list(bytes(encString, "utf-8", errors="ignore"))

    for b in key.encode():
        byteSum += b

    for item in encArr:
        if(byteSum > 256):
            byteSum = (byteSum * len(encArr)) % (len(encArr) - 1)
        encBytes.append(item ^ byteSum)

    return bytes(encBytes)


def encodeByteFile(byte, key, V3=False):
    if(V3):
        return bytes(XORBytesV3(byte, key))
    else:
        return bytes(XORBytes(byte, key))


def decodeByteFile(encByte, key, V3=False):
    if(V3):
        return bytes(XORBytesV3(encByte, key, True))
    else:
        return bytes(XORBytes(encByte, key))


def encode(text, key, V3=False):
    encString = myEncoder(text, key)
    if(V3):
        return bytes(XORBytesV3(encString, key)).hex()
    else:
        return bytes(XORBytes(encString, key)).hex()


def decode(hexString, key, V3=False):
    hexBytes = bytes.fromhex(hexString)
    encString = None
    if(V3):
        encString = XORBytesV3(hexBytes, key).decode("utf-8", errors="ignore")
    else:
        encString = XORBytes(hexBytes, key).decode("utf-8", errors="ignore")

    return myEncoder(encString, key)
