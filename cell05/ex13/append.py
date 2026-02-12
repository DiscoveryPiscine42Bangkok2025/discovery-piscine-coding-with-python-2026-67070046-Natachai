import sys
def main():
    if len(sys.argv) >= 2:
        for param in sys.argv[1:]:
            if not param.endswith("ism"):
                print(param + "ism")
    else:
        print("none")
main()