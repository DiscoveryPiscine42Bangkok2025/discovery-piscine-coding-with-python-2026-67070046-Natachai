import sys
def main():
    para = sys.argv[1:]
    if len(para) >= 1:
        for param in para:
            if not param.endswith("ism"):
                print(param + "ism")
    else:
        print("none")
main()