"""
Drugi zadatak domaceg
Autor: Nikola Bandulaja SV74/2022
Zadatak omogucava simulaciju istorije web pregledaca uz upotrebu cirkularne implementacije deka iz prethodnog zadatka.
"""

class EmptyDequeException(Exception):
    """
    Klasa modeluje izuzetke vezane za klasu Deque.
    """
    pass

class FullDequeException(Exception):
    """
    Klasa modeluje izuzetke vezane za klasu Deque.
    """
    pass

class Deque(object):
    """
    Implementacija deka na osnovu liste.
    """

    def __init__(self, max_capacity):
        """
        Konstruktor.
        """
        self._data = [None] * max_capacity #maksimalan broj strana koje istorija pamti
        self._max_capacity = max_capacity #maksimalan kapacitet deka se dodaje u ovoj implementaciji
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        """
        Metoda proverava da li je dek prazan.
        """
        return self._size == 0

    def is_full(self):
        return self._size == self._max_capacity

    def first(self):
        """
        Metoda omogućava pristup prvom elementu deka.
        """
        if self.is_empty():
            raise EmptyDequeException('Dek je prazan.')
        return self._data[self._front]

    def last(self):
        """
        Metoda omogućava pristup poslednjem elementu deka.
        """
        if self.is_empty():
            raise EmptyDequeException('Dek je prazan.')

        return self._data[(self._front + self._size - 1) % len(self._data)]

    def add_first(self, e):
        """
        Metoda dodaje element na početak deka.

        Argument:
        - `e`: novi element
        """
        if self._size == len(self._data):
            raise FullDequeException("Dek je pun.")

        if self._front == 0 and self.is_empty():
            self._front = 0
        else:
            self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def add_last(self, e):
        """
        Metoda dodaje element na kraj deka.

        Argument:
        - `e`: novi element
        """
        if self._size == len(self._data):
            raise FullDequeException("Dek je pun.")

        back = (self._front + self._size) % len(self._data)
        self._data[back] = e
        self._size += 1

    def delete_first(self):
        """
        Metoda izbacuje prvi element iz deka.
        """
        if self.is_empty():
            raise EmptyDequeException('Dek je prazan.')

        retValue = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

        return retValue

    def delete_last(self):
        """
        Metoda izbacuje poslednji element iz deka.
        """
        if self.is_empty():
            raise EmptyDequeException('Dek je prazan.')

        back = (self._front + self._size - 1) % len(self._data)
        retValue = self._data[back]
        self._data[back] = None
        self._size -= 1

        return retValue

    def getMaxCapacity(self):
        return self._max_capacity

    def __str__(self):
        return str(self._data)

class BrowserHistory(object):

    def __init__(self, pocetna):    #pravljenje objekta klase BrowserHistory, u njoj se nalazi dek sa stranicama
        self._dek = Deque(3) #ova verzija skladisti 10 stranica
        self._dek.add_first(pocetna)
        self._napred = 0
        self._nazad = 0

    def visit(self, url):
        if self._napred != 0:
            while self._napred > 0:
                self._dek.delete_first()
                self._napred -= 1
            self._dek.add_last(url)
            self._nazad += 1
        elif self._napred == 0 and not self._dek.is_full():
            self._dek.add_last(url)
            self._nazad += 1
        else:
            self._dek.delete_first()
            self._dek.add_last(url)

    def back(self, steps):
        while steps > 0:
            if self._nazad == 0:
                break
            self._dek.add_first(self._dek.delete_last())
            steps -= 1
            self._nazad -= 1
            self._napred += 1
        return self._dek.last()

    def forward(self, steps):
        while steps > 0:
            if self._napred == 0:
                break
            self._dek.add_last(self._dek.delete_first())
            steps -= 1
            self._napred -= 1
            self._nazad += 1
        return self._dek.last()

if __name__ == '__main__':

    print("Unesite pocetnu web stranicu: ")
    pocetna = input()
    history = BrowserHistory(pocetna)

    kraj = False
    while not kraj: #meni koji radi dok se ne unese exit
        komanda = input(">>")
        if komanda == "exit": #prepoznavanje i provera ispravnosti komandi
            kraj = True
        elif "forward" in komanda:
            if len(komanda.split(" ")) == 1:
                print(history.forward(1))
            elif len(komanda.split(" ")) == 2:
                try:
                    print(history.forward(eval(komanda.split(" ")[1])))
                except:
                    print("Neispravan unos!")
                    pass
            else:
                print("Neispravan unos!")
                pass
        elif "back" in komanda:
            if len(komanda.split(" ")) == 1:
                print(history.back(1))
            elif len(komanda.split(" ")) == 2:
                try:
                    print(history.back(eval(komanda.split(" ")[1])))
                except:
                    print("Neispravan unos!")
                    pass
            else:
                print("Neispravan unos!")
                pass
        elif "." in komanda:
            history.visit(komanda)
        else:
            print("Program nije prepoznao komandu!")

