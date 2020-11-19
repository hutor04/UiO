# The test of Motorsykkel class

from motorsykkel import Motorsykkel


def hovedprogram():
    mot1 = Motorsykkel('BMW', '9204-IT-7', 15000)
    mot2 = Motorsykkel('Yamaha', '1155-IT-7', 94000)
    mot3 = Motorsykkel('Honda', '5319-IT-7', 54000)
    mots = [mot1, mot2, mot3]
    for mot in mots:
        mot.skrivUt()
    mot3.kjor(10)
    print(mot3.hentKilometerstand)


if __name__ == '__main__':
    hovedprogram()
