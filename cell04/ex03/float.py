def main():
    text = float(input("Give me a number: "))
    if text - (int(text)) == 0.00:
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
main()