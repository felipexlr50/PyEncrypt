import argparse
import crypt_engine
import crypt_files


def setupArgs2():
    # main parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    parser.set_defaults(which='main')

    # encfiles parser
    parser_encfiles = subparsers.add_parser(
        "encfiles", help=" encrypt folder files")
    parser_encfiles.add_argument(
        "folderpath", type=str, help="folder system path")
    parser_encfiles.add_argument("key", type=str, help="input key")
    parser_encfiles.set_defaults(which='encfiles')

    # decfiles parser
    parser_decfiles = subparsers.add_parser(
        "decfiles", help=" decrypt folder files")
    parser_decfiles.add_argument(
        "folderpath", type=str, help="folder system path")
    parser_decfiles.add_argument("key", type=str, help="input key")
    parser_decfiles.set_defaults(which='decfiles')

    # crypt engine functions
    parser_engine = subparsers.add_parser(
        "engine", help="crypt engine functions")
    engineSubparser = parser_engine.add_subparsers()
    parser_engine.set_defaults(which='engine')

    # encode functions
    parser_encode = engineSubparser.add_parser(
        "encode", help="encode functions")
    parser_encode.add_argument(
        "text", type=str, help="input text or file path")
    parser_encode.add_argument("key", type=str, help="input key")
    parser_encode.set_defaults(which='encode')

    # decode functions
    parser_decode = engineSubparser.add_parser(
        "decode", help="decode functions")
    parser_decode.add_argument(
        "text", type=str, help="input text or file path")
    parser_decode.add_argument("key", type=str, help="input key")
    parser_decode.set_defaults(which='decode')

    # optionals
    parser_engine.add_argument("-b", "--byteFile",
                               help="byte file", action="store_true")
    parser_engine.add_argument(
        "--V3", help="new XOR version", action="store_true")
    parser_engine.add_argument("-f", help="file O/I mode", action="store_true")
    parser_engine.add_argument(
        "--hex", help="hex I/O mode", action="store_true")
    parser_engine.add_argument(
        "-o", "--fileOutput", help="filename output", type=str)

    return parser.parse_args()


def setupArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--encode", help="encode text/file",
                        action="store_true")
    parser.add_argument("-d", "--decode", help="decode text/file",
                        action="store_true")
    parser.add_argument("-b", "--byteFile", help="byte file",
                        action="store_true")
    parser.add_argument("--V3", help="new XOR version",
                        action="store_true")
    parser.add_argument("-f", help="file O/I mode", action="store_true")
    parser.add_argument("-v", help="verbode I/O mode", action="store_true")
    parser.add_argument("--hex", help="hex I/O mode", action="store_true")
    parser.add_argument("-o", "--fileOutput", help="filename output", type=str)
    parser.add_argument("text", help="input text", type=str)
    parser.add_argument("key", help="input key", type=str)

    return parser.parse_args()


def parseArgs2(args):

    # encfiles option
    if(args.which == 'encfiles'):
        if(args.folderpath and args.key):
            files = crypt_files.getItems(args.folderpath)
            crypt_files.encFiles(files, args.key)

    # decfiles option
    if(args.which == 'decfiles'):
        if(args.folderpath and args.key):
            files = crypt_files.getItems(args.folderpath)
            crypt_files.decFiles(files, args.key)

    # encode option
    elif(args.which == 'encode'):
        if(args.byteFile):
            file = crypt_engine.readByteFile(args.text)
            enc = crypt_engine.encodeByteFile(args.text, args.key, args.V3)
            if(args.fileOutput):
                crypt_engine.saveByteFile(args.fileOutput, enc)
            else:
                crypt_engine.saveByteFile(args.text, enc)
        elif(args.hex):
            if(args.f):
                file = crypt_engine.readFileHex(args.text)
                enc = crypt_engine.encode(file, args.key, args.V3)
                if(args.fileOutput):
                    crypt_engine.saveFileHex(args.fileOutput, enc)
                else:
                    crypt_engine.saveFileHex(args.text, enc)
            else:
                print(crypt_engine.encode(args.text, args.key, args.V3))
        elif(args.f):
            file = crypt_engine.readFileHex(args.text)
            enc = crypt_engine.decode(file, args.key, args.V3)
            if(args.fileOutput):
                crypt_engine.saveFileHex(args.fileOutput, enc)
            else:
                crypt_engine.saveFileHex(args.text, enc)
        else:
            enc = crypt_engine.myEncoder(args.text, args.key)
            if(args.fileOutput):
                crypt_engine.saveFile(args.fileOutput, enc)

            print(enc)

    # decode option
    elif(args.which == "decode"):
        if(args.byteFile):
            file = crypt_engine.readByteFile(args.text)
            enc = crypt_engine.decodeByteFile(args.text, args.key, args.V3)
            if(args.fileOutput):
                crypt_engine.saveByteFile(args.fileOutput, enc)
            else:
                crypt_engine.saveByteFile(args.text, enc)

        elif(args.hex):
            if(args.f):
                file = crypt_engine.readFileHex(args.text)
                enc = crypt_engine.decode(file, args.key, args.V3)
                if(args.fileOutput):
                    crypt_engine.saveFileHex(args.fileOutput, enc)
                else:
                    crypt_engine.saveFileHex(args.text, enc)
            else:
                print(crypt_engine.decode(args.text, args.key, args.V3))

        elif(args.f):
            file = crypt_engine.readFileHex(args.text)
            enc = crypt_engine.decode(file, args.key, args.V3)
            if(args.fileOutput):
                crypt_engine.saveFileHex(args.fileOutput, enc)
            else:
                crypt_engine.saveFileHex(args.text, enc)
        else:
            enc = crypt_engine.myEncoder(args.text, args.key)
            if(args.fileOutput):
                crypt_engine.saveFile(args.fileOutput, enc)

            print(enc)

    else:
        print("No avaiable!")

    # print(args)


def parseArgs(args):

    if(args.byteFile and args.f):
        if(args.encode):
            file = crypt_engine.readByteFile(args.text)
            enc = crypt_engine.encodeByteFile(args.text, args.key, args.V3)
            if(args.fileOutput):
                crypt_engine.saveByteFile(args.fileOutput, enc)
            else:
                crypt_engine.saveByteFile(args.text, enc)

        elif(args.decode):
            file = crypt_engine.readByteFile(args.text)
            enc = crypt_engine.decodeByteFile(args.text, args.key, args.V3)
            if(args.fileOutput):
                crypt_engine.saveByteFile(args.fileOutput, enc)
            else:
                crypt_engine.saveByteFile(args.text, enc)

    if(args.encode and args.hex):
        if(args.v):
            print(crypt_engine.encode(args.text, args.key, args.V3))

        if(args.f):
            file = crypt_engine.readFileHex(args.text)
            enc = crypt_engine.encode(file, args.key, args.V3)
            if(args.fileOutput):
                crypt_engine.saveFileHex(args.fileOutput, enc)
            else:
                crypt_engine.saveFileHex(args.text, enc)

    elif(args.decode and args.hex):
        if(args.v):
            print(crypt_engine.decode(args.text, args.key, args.V3))

        if(args.f):
            file = crypt_engine.readFileHex(args.text)
            enc = crypt_engine.decode(file, args.key, args.V3)
            if(args.fileOutput):
                crypt_engine.saveFileHex(args.fileOutput, enc)
            else:
                crypt_engine.saveFileHex(args.text, enc)

    elif(args.encode):
        if(args.v):
            print(crypt_engine.myEncoder(args.text, args.key))

        if(args.f):
            file = crypt_engine.readFile(args.text)
            enc = crypt_engine.myEncoder(file, args.key)
            if(args.fileOutput):
                crypt_engine.saveFile(args.fileOutput, enc)
            else:
                crypt_engine.saveFile(args.text, enc)

    elif(args.decode):
        if(args.v):
            print(crypt_engine.myEncoder(args.text, args.key))

        if(args.f):
            file = crypt_engine.readFile(args.text)
            enc = crypt_engine.myEncoder(file, args.key)
            if(args.fileOutput):
                crypt_engine.saveFile(args.fileOutput, enc)
            else:
                crypt_engine.saveFile(args.text, enc)
    else:
        print("Option not avaiable")


try:
    # parseArgs(setupArgs())
    parseArgs2(setupArgs2())
except Exception as e:
    print(str(e))
