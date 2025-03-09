import argparse
from proj import f1, f2

def main():
    parser = argparse.ArgumentParser(description="Command-line tool for f1 and f2")
    parser.add_argument("function", choices=["f1", "f2"], help="Function to call")
    parser.add_argument("value", type=int, help="Input value")

    args = parser.parse_args()

    if args.function == "f1":
        print(f1(args.value))
    elif args.function == "f2":
        print(f2(args.value))

if __name__ == "__main__":
    main()
