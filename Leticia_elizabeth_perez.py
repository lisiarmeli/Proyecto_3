import numpy as np
import matplotlib.pyplot as plt
from random import randint


def galton():
    niveles = 12
    if niveles >= 1:
        etapas = [0] * (niveles)
    else:
        print("The value of levels can't be lower than 1.")
        exit()
    pelotas = 3000
    for h in range(pelotas):
        stored = -1
        for j in range(niveles):
            stored += randint(0, 1)
        etapas[stored] += 1

    return etapas


def plotear(etapas):
    X = np.arange(-((len(etapas) / 2) - .5), (len(etapas) / 2) + .5)
    plt.title('Simulacion De La Máquina De Galton')
    plt.xlabel('Distribucion de canicas')
    plt.ylabel('Cantidad de canicas')
    plt.bar(X + 0.00, etapas, width=0.25)
    plt.show()
    plt.savefig("BellCurve.png")


plotear(galton())