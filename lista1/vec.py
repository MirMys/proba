'''Moduł tworzący i wykonujący operacje na wektorach'''
import random
import numpy as np
import math
class vector:
    '''klasa vector'''
    def __init__(self,args=3):
        '''
        Funkcja:
        Tworzy wektor w postaci listy. Ilość współrzędnych wektora zależy od args. Początkowo wszystkie współrzędne wektora są równe 0
        '''
        self.v = list(np.zeros(args))
    def generate(self):
        '''Funkcja:
        Generuje losowo współrzędne wektora od -100 do 100 wykorzystując funckje random.uniform z biblioteki random
        '''
        for i in range(len(self.v)):
            self.v[i]= random.uniform(-100,100)
    def load(self,list):
        '''
        Funkcja:
        Nadpisuje współrzędne wektora elementami z listy
        INPUT:
        list (list) - lista z współrzędnymi którymi chcemy nadpisać wektor
        OUTPUT:
        self.v (list) - wektor z nadpisanymi współrzędnymi
        '''
        if len(self.v) != len(list):
            raise ValueError("rozna ilosc elementow w wektorze")
        else:
                self.v = list
        return self.v
    def __add__(self,list):
        '''
        Funkcja:
        Dodaje liste do wektora
        INPUT:
        list (list) - lista z elementami które chcemy dodać do wektora
        OUTPUT:
        self.v (list) - wektor z dodanymi elementami z listy
        '''
        if len(self.v) != len(list):
            raise ValueError("rozna ilosc elementow w wektorze")
        for i in range(len(self.v)):
            self.v[i] = self.v[i]+list[i]
        return self.v
    def __sub__(self,list):
        '''
        Funkcja:
        Od wektora odejmuje liste
        INPUT:
        list (list) - lista z elementami które chcemy odjąć od wektora
        OUTPUT:
        self.v (list) - wektor z odjętymi elementami z listy
        '''
        if len(self.v) != len(list):
            raise ValueError("rozna ilosc elementow w wektorze")
        for i in range(len(self.v)):
            self.v[i] = self.v[i]-list[i]
        return self.v
    def __mul__(self,x):
        '''
        Funkcja:
        Mnoży wektor razy skalar
        INPUT:
        x (list) - skalar przez który chcemy pomnożyć
        OUTPUT:
        self.v (list) - wektor z wspolrzednymi pomnożonymi przez skalar x
        '''
        for i in range(len(self.v)):
            self.v[i] = self.v[i]*x
        return self.v
    def lenght(self):
        '''
        Funkcja:
        Wylicza długość wektora
        OUTPUT:
        l (float) - długość wektora
        '''
        l=0
        for i in range(0,len(self.v)):
            l+=self.v[i]**2
        l = math.sqrt(l)
        return l
    def sum(self):
        '''
        Funkcja:
        Wylicza sume elementów wektora
        OUTPUT:
        s (float) - suma elementów wektora
        '''
        s=0
        for i in range(0,len(self.v)):
            s+=self.v[i]
        return(s)
    def dot_product(self,list):
        '''
        Funkcja:
        Wylicza iloczyn skalarny wektora i listy
        INPUT:
        list (lista) - lista której ilocznyn skalarny z wektorem chcemy policzyć
        OUTPUT:
        l (float) - Iloczyn skalarny wektora i listy
        '''
        l=0
        if len(self.v) != len(list):
            raise ValueError("rozna ilosc elementow w wektorze")
        for i in range(len(self.v)):
            l=l+(self.v[i]*list[i])
        return(l)
    def __str__(self):
        '''
        Funkcja:
        Podaje wektor jako string
        OUTPUT:
        a (str) - wektor zapoisany jako string
        '''
        return str(self.v)
    def __getitem__(self,a):
        '''
        Funkcja:
        Podaje określoną współrzędną wektora
        INPUT:
        a (int) - numer pozycji współrzędnej którą chcemy wywołać
        OUTPUT:
        self.v[a] (float) - określona współrzędna wektora
        '''
        return self.v[a]
    def __contains__(self, a):
        '''
        Funkcja:
        Sprawdza czy określony element należy do wektora
        INPUT:
        a (int/float) - element który chcemy sprawdzić czy należy do wektora
        OUTPUT:
        a in self.v (True/False)
        '''
        return a in self.v
