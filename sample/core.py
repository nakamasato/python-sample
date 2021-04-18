from helper import add
from utils.database import get_database

def main():
    sum = add(1, 2)
    print(f'sum: {sum}')
    print(get_database())

if __name__ == '__main__':
    main()