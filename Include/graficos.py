import pandas as pd
import matplotlib.pyplot as plt

def grafico_barra(respuestas, xlabel, ylabel, titulo, color_barra):
    preg = respuestas.plot.bar(color=color_barra)
    preg.set_xlabel(xlabel)
    preg.set_ylabel(ylabel)
    preg.set_title(titulo)
    return plt.show()

def grafico_comun(respuestas, xlabel, ylabel, titulo):
    preg = respuestas.plot()
    preg.set_xlabel(xlabel)
    preg.set_ylabel(ylabel)
    preg.set_title(titulo)
    return plt.show()