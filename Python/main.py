import time

from rsmapy import RSMA

def main():
    #connecting to RSMA
    RSMA.connect("RSMApy")

    #waiting 1 second
    time.sleep(1)

    #sending message to RSMA
    RSMA.message("Hello RSMA!")

    time.sleep(1)

    #sending command to RSMA
    RSMA.execute("help")

    time.sleep(1)

    #disconnecting to RSMA
    RSMA.disconnect()

    input("Press any key to Exit")

if __name__ == '__main__':
    main()