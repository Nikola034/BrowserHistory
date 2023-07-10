"""
Modul sadrži implementaciju deka na osnovu liste.
Dek je cirkularno implementiran i sadrzi ogranicen broj elemenata.
Autor: Nikola Bandulaja SV74/2022
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
        self._data = [None] * max_capacity
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        """
        Metoda proverava da li je dek prazan.
        """
        return self._size == 0

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

    def __str__(self):
        return str(self._data)


if __name__ == '__main__': #testiranje deka
    d = Deque(10)
    d.add_last(5)
    d.add_first(7)
    d.add_first(3)
    print(d.first())

    d.delete_last()
    print(len(d))

    d.delete_last()
    d.delete_last()
    d.add_first(6)
    print(d.last())

    d.add_first(8)
    print(d.is_empty())
    print(d.last())