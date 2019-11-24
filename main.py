from bank_entries.bank_entries import get_people_entered
import sys


def main():
    if len(sys.argv) != 2:
        print('usage: ./main.py file')
        sys.exit(1)

    print(get_people_entered(sys.argv[1]))


if __name__ == '__main__':
    main()
