import time
from datetime import datetime
from random import random

def main():

    interval = 3

    while True:
        time.sleep(interval)

        with open("test.log", "a") as f:
            f.write(str(datetime.now()) + " File read: " + str(random()) + '\n')

if __name__ == '__main__':
    main()
