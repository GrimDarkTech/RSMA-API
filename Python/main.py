import time

from rsmapy import RSMA

from rsma_client import RSMAClient

def main():
    #connecting to RSMA
    RSMA.connect("127.0.0.1","RSMApy")
    time.sleep(0.1)

    RSMA.client.logger = True

    time.sleep(0.1)

    #sending message to RSMA
    RSMA.message("Hello RSMA!")
    RSMA.message("2")
    RSMA.message("1")
    RSMA.message("3")
    RSMA.message("4")


    time.sleep(2)
    #disconnecting to RSMA
    RSMA.disconnect()


if __name__ == '__main__':
    main()