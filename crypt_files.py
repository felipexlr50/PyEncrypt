import os
import sys
import crypt_engine

#dir = "C:/Users/ezbapfe/Downloads/crawler/"
#itemList = []


def getItems(path):
    itemList = []
    with os.scandir(path) as listOfEntries:
        for entry in listOfEntries:
            if(entry.is_file()):
                itemObj = {'path': path, 'item': entry.name, 'type': 'file'}
                itemList.append(itemObj)
            else:
                itemObj = {'path': path, 'item': entry.name, 'type': 'folder'}
                itemList.append(itemObj)
                itemList += getItems(path+"\\"+entry.name)
    return itemList


def encFiles(items, key):
    count = 0

    for item in reversed(items):
        try:
            path = item['path']
            name = item['item']
            typefile = item['type']
            pathItem = path+'\\'+name
            itemEncName = crypt_engine.encode(name, key)

            if(typefile == "file"):
                file = crypt_engine.readByteFile(pathItem)
                encFile = crypt_engine.encodeByteFile(file, key)
                crypt_engine.saveByteFile(path+'\\'+itemEncName, encFile)
                print("Enc " + path+'\\'+itemEncName)
                os.remove(pathItem)

            elif(typefile == "folder"):
                encpath = path+'\\'+itemEncName
                os.rename(pathItem, encpath)

        except IOError as ioe:
            print("some error: "+str(ioe))
            continue

        except Exception as e:
            print("some error: "+str(e))
            return False
    return True


def decFiles(items, key):
    count = 0

    for item in reversed(items):
        try:
            path = item['path']
            name = item['item']
            typefile = item['type']
            pathItem = path+'\\'+name
            itemEncName = crypt_engine.decode(name, key)

            if(typefile == "file"):
                file = crypt_engine.readByteFile(pathItem)
                encFile = crypt_engine.decodeByteFile(file, key)
                crypt_engine.saveByteFile(path+'\\'+itemEncName, encFile)
                print("Enc " + path+'\\'+itemEncName)
                os.remove(pathItem)

            elif(typefile == "folder"):
                encpath = path+'\\'+itemEncName
                os.rename(pathItem, encpath)

        except IOError as ioe:
            print("some error: "+str(ioe))
            continue

        except Exception as e:
            print("some error: "+str(e))
            return False
    return True


#lista = getItems("C:\\Users\\ezbapfe\\first-app")

#decFiles(lista, "123")

# print(lista)
