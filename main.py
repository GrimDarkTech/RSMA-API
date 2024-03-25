import time

from rsmapy import RSMA

def main():
    RSMA.connect("RSMApy")

    time.sleep(1)

    RSMA.message("Hello RSMA!")

    time.sleep(1)

    RSMA.execute("help")

    time.sleep(1)

    RSMA.disconnect()

    input("Press any key to Exit")

if __name__ == '__main__':
    main()