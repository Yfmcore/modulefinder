import os

def main():
    print("script by @codingstorm")
    print("creating dir mods")

    if os.path.exists("mods") == False:
        print("dir made successfuly")
        os.mkdir("mods")
    else:
        print("dir already exists")
    os.system("pause")

main()