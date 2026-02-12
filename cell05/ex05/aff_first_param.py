import sys
def ilove42():
    if len(sys.argv) > 1:
        print(sys.argv[1])
    else:
        print("none")
ilove42()