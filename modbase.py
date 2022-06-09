import os

def main():
    print("script by @codingstorm")

    if os.path.exists("mods") == False:
        print("creating dir mods")
        print("dir made successfuly")
        os.mkdir("mods")
    else:
        print("dir already exists")
    os.system("pause")

main()