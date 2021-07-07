import os


def clr():
    os.system('cls' if os.name == 'nt' else 'clear')


def saveFile(data, fileName):
    open(fileName, 'w').write(str(data))
    print("\nFile was saved [+]")


def main(fileName="untitled"):
    clr()
    num = 0
    try:
        data = open(fileName).read()
        print(fileName+' [+]\n'+60*'_'+'\n')
        for i in data.split('\n'):
            num+=1
            print(str(num)+'  | '+i if num<10 else ' | '+i)
    except:
        data = ""
        print(fileName+' [+]\n'+60*'_'+'\n')
    while True:
        num+=1
        data+=input(str(num)+'  | ' if num<10 else ' | ')+'\n'
        if data.split('\n')[-2] == "!!quit":
            saveFile(data.replace('\n!!quit\n', ''), fileName)
            input("[Press Enter To Exit]")
            clr()
            exit()


if __name__ == '__main__':
    clr()
    print(30*'_'+'\n\nText Editor Py V1.0\n'+30*'_')
    file = str(input("\nEnter file name : "))
    main(file)



