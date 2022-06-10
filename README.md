# PyEncrypt


### Usage

#### Main options
```bash
positional arguments:
  {encfiles,decfiles,engine}
    encfiles            encrypt folder files
    decfiles            decrypt folder files
    engine              crypt engine functions

options:
  -h, --help            show this help message and exit
```
#### Encode engine
```bash
positional arguments:
  {encode,decode}
    encode              encode functions
    decode              decode functions

options:
  -h, --help            show this help message and exit
  -b, --byteFile        byte file
  --V3                  new XOR version
  -f                    file O/I mode
  --hex                 hex I/O mode
  -o FILEOUTPUT, --fileOutput FILEOUTPUT
                        filename output
```
#### Encode files
```bash
positional arguments:
  folderpath  folder system path
  key         input key

options:
  -h, --help  show this help message and exit
```
