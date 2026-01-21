# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 13:04:50 2026

@author: Patrycja Głuszek
"""

#Programowanie w Python zestaw numer 3

# Zadanie 1
podatek_dochod = 0.17
skl_emeryt, skl_rentow, skl_chorob = 0.0976, 0.0150, 0.0245
ubezp_zdrow_staw1, ubezp_zdrow_staw2 = 0.09, 0.0775
koszt_uzyskania = 250.00
kwota_wolna = 43.76
placa_brutto = 3200

emeryt = skl_emeryt * placa_brutto
rentow = skl_rentow * placa_brutto
chorob = skl_chorob * placa_brutto
spoleczn = emeryt + rentow + chorob

przychod = placa_brutto - spoleczn
zdrow = ubezp_zdrow_staw1 * przychod

podst_opod = przychod - koszt_uzyskania
podatek = podatek_dochod * podst_opod - kwota_wolna
podatek -= ubezp_zdrow_staw2 * przychod

placa_netto = placa_brutto - spoleczn - zdrow - podatek

print('''
Płaca brutto: %f
* Ub. społeczne: %f
*** Ub. emeryt.: %f
*** Ub. rentow.: %f
*** Ub. chorob.: %f
* Ub. zdrowotne: %f
* Podatek doch.: %f
Płaca netto: %f
''' % (
    placa_brutto, spoleczn, emeryt, rentow, chorob, zdrow, podatek, placa_netto
))

# Zadanie 2

pts1 = [3, 1, 3, 2, 1, 3, 2, 3, 2, 1, 3, 2, 1, 3, 3]

pres2 = [
    True, True, True, True, False, True, True, True, True,
    True, False, False, True, False, True
]

home2 = [
    'perf', 'perf', 'perf', 'good', 'good', 'good', 'perf',
    'none', 'good', 'good', 'good', 'none', 'good', 'perf',
    'good'
]

# Kopia, aby nie modyfikować pts1
pts2 = pts1.copy()

# Słownik punktów za pracę domową
home_points = {'perf': 2, 'good': 1}

for i in range(len(pts2)):
    # 1 punkt za obecność (True=1, False=0)
    pts2[i] += pres2[i]

    # Punkty za pracę domową (domyślnie 0)
    pts2[i] += home_points.get(home2[i], 0)

print(pts2)
print(pts1)

# Zadanie 2 punkt 1
# Uproszczenie linii 15
pts2[i] += pres2[i]   # bo True == 1, False == 0

# Zadanie 2 punkt 2
# Uproszczenie linii 17–22 do jednej linijki:
pts2[i] += {'perf': 2, 'good': 1}.get(home2[i], 0)

# Zadanie 2 punkt 3
# Dlaczego pts1 się zmienia?
# Bo pts2 = pts1, obie zmienne wskazują na tę samą listę (przypisanie przez referencję)

# Jak temu zapobiec? Trzeba zrobić kopię listy:
pts2 = pts1.copy()        # poprawne
# albo:
pts2 = list(pts1)         # poprawne
# albo:
pts2 = [x for x in pts1]  # poprawne

# Zadanie 3

# 1. Wczytanie pliku
with open(r"C:\Users\patry\OneDrive\Pulpit\3_programowanie_w_python\frankenstein.txt",
          "r", encoding="utf-8") as f:
    text = f.read()

# 2. Zliczanie wystąpień każdego symbolu
counts = {}
for ch in text:
    counts[ch] = counts.get(ch, 0) + 1

# 3. Sortowanie od najczęściej do najrzadziej
sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

# 4. Wyświetlenie wyników
for symbol, freq in sorted_counts:
    print(repr(symbol), ":", freq)

# Zadanie 4
# HOSPITALIZACJE OSÓB CHORYCH NA COVID-19
hosp = (15444, 16144, 16427, 17223, 18160, 18654, 19114)

def transform2(ts, func):
    return [func(v0, v1) for v0, v1 in zip(ts[:-1], ts[1:])]

# 1. Dobowa zmiana liczby hospitalizowanych
daily_change = transform2(
    hosp,
    lambda x0, x1: x1 - x0
)

print("Dobowa zmiana liczby hospitalizowanych:")
print(daily_change)

# 2. Dobowa zmiana procentowa
daily_pct_change = transform2(
    hosp,
    lambda x0, x1: (x1 - x0) / x0 * 100
)

print("\nDobowa zmiana procentowa:")
print(daily_pct_change)

# Zadanie 5
# Klasa Sample reprezentująca jednowymiarową próbkę statystyczną
class Sample:
    def __init__(self, vals):
        # przechowujemy kopię listy, aby uniknąć modyfikacji oryginału
        self._vals = list(vals)

    def get_vals(self):
        # zwraca całą próbkę
        return self._vals

    def get_val(self, i):
        # zwraca i-tą obserwację (indeksowanie od 0)
        return self._vals[i]

    def set_val(self, i, new_val):
        # ustawia nową wartość i-tej obserwacji
        self._vals[i] = new_val

    def add_val(self, new_val):
        # dodaje nową obserwację na koniec próbki
        self._vals.append(new_val)


# Klasa ExtSample rozszerza Sample o funkcje statystyczne
class ExtSample(Sample):
    def sum(self):
        # suma wszystkich wartości
        return sum(self._vals)

    def mul(self):
        # iloczyn wszystkich wartości
        result = 1
        for v in self._vals:
            result *= v
        return result

    def avg(self):
        # średnia wartości
        return sum(self._vals) / len(self._vals)

# TEST
es = ExtSample([1, 2, 3, 4])

print(es.get_vals())      # [1, 2, 3, 4]

es.add_val(5)
print(es.get_vals())      # [1, 2, 3, 4, 5]

print(es.sum())           # 15
print(es.mul())           # 120
print(es.avg())           # 3.0


# Zadanie 7
# Klasa Vector reprezentująca wektor matematyczny
class Vector:
    def __init__(self, vals):
        # przechowujemy kopię listy
        self._vals = list(vals)

    def get_vals(self):
        return self._vals

    def __add__(self, other):
        # dodawanie wektorów element po elemencie
        result = [v1 + v2 for v1, v2 in zip(self._vals, other._vals)]
        return Vector(result)

    def __mul__(self, other):
        # mnożenie skalarne (iloczyn wektorowy)
        return sum(v1 * v2 for v1, v2 in zip(self._vals, other._vals))

# TEST
v1 = Vector([1, 2, 1, 5])
v2 = Vector([2, 3, 1, 4])

# [1+2, 2+3, 1+1, 5+4]
v3 = v1 + v2
print(v3.get_vals())     # [3, 5, 2, 9]

# 1*2 + 2*3 + 1*1 + 5*4
print(v1 * v2)           # 29
 