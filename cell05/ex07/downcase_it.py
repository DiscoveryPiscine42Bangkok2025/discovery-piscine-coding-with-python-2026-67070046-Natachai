import sys
def ilove42():
    if len(sys.argv) == 2:
        txt = sys.argv[1]
        print(txt.lower())
    else:
        print("none")
ilove42()