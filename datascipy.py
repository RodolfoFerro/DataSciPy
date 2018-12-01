# ===============================================================
# Author: Rodolfo Ferro
# Email: ferro@cimat.mx
# Twitter: @FerroRodolfo
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script was originally created by Rodolfo Ferro, for
# his workshop in PythonDay Mexico 2018 at CUCEA in Gdl, Mx.
# Any explicit usage of this script or its contents is granted
# according to the license provided and its conditions.
# ===============================================================

# -*- coding: utf-8 -*-

# Importamos paquetes:
import matplotlib.pyplot as plt
import scipy.stats as st
import seaborn as sns
import numpy as np

# Fijamos semilla aleatoria:
np.random.seed(11)

# Muestra de tiempos:
tiempos = np.array([2.50, 4.93, 5.01, 1.11, 4.93, 3.51,
                    1.86, 0.10, 0.10, 0.05, 1.06, 1.06,
                    3.86, 0.75, 0.48, 1.53, 0.48, 1.18,
                    1.25, 2.78, 0.66, 5.36, 0.05, 2.13,
                    0.25, 2.28, 6.88, 18.45, 1.06, 2.5,
                    1.88
                    ])
tiempos = sorted(tiempos)

# PASO 1 - Creamos histograma.
breaks = 20
x = np.linspace(0.5, breaks, 1000)
plt.figure(1, figsize=(7, 7))
plt.hist(tiempos, breaks, normed=True, facecolor='blue',
         alpha=0.75, ec='white', label="Histograma de tiempos")
plt.title("Histograma de tiempos")
plt.xlabel("Tiempos")
plt.ylabel("Frecuencia de tiempos")
plt.savefig("assets/fig_1.png")

# PASO 2 - Proponemos un modelo.
dist_name = 'weibull_min'

# PASO 3 - Estimamos parámetros.
# Estimador de parámetros:
dist = getattr(st, dist_name)
param = dist.fit(tiempos)
pdf_fitted = dist.pdf(x, *param[:-2], loc=param[-2], scale=param[-1])
cdf_fitted = dist.cdf(x, *param[:-2], loc=param[-2], scale=param[-1])
print("Parámetros obtenidos: {}".format(param))

# PASO 4 - Validamos nuestro modelo.
# Función de Distribución Empírica (FDE):


def ecdf(x):
    xs = np.sort(x)
    ys = np.arange(1, len(xs) + 1) / float(len(xs))
    return xs, ys


x_cdf, y_cdf = ecdf(tiempos)
plt.figure(2, figsize=(7, 7))
plt.plot(x, cdf_fitted, label="FDT")
plt.plot(x_cdf, y_cdf, label="FDE")
plt.title("FDE vs FDT")
plt.xlabel("X")
plt.ylabel("pweibull(params)")
plt.savefig("assets/fig_2.png")
# plt.show()

# Gráfica cuantil-cuantil:
N = len(tiempos)
gen = np.arange(1 / (N + 1), N / (N + 1), 1 / (N + 1))
vec = dist.ppf(gen, *param[:-2], loc=param[-2], scale=param[-1])
plt.figure(3, figsize=(7, 7))
plt.plot(np.linspace(0, breaks), np.linspace(0, breaks))
plt.plot(tiempos[:-1], vec, ".r")
plt.xlabel("sort(tiempos)")
plt.ylabel("sort(vec)")
plt.title("Gráfica cuantil-cuantil (Q-Q)")
plt.savefig("assets/fig_3.png")
# plt.show()

# Densidad sobre histograma:
plt.figure(4, figsize=(7, 7))
plt.hist(tiempos, breaks, normed=True, facecolor='blue',
         alpha=0.75, ec='white', label="Histograma de tiempos")
plt.plot(x, pdf_fitted)
plt.xlabel("Tiempos")
plt.ylabel("Frecuencia de tiempos")
plt.title("Histograma de tiempos \nDensidad ajustada")
plt.savefig("assets/fig_4.png")
# plt.show()

# PASO 5 - Simular datos.
# Validar con nube de puntos:
unif = np.random.uniform
plt.figure(5, figsize=(7, 7))
for sim in range(50):
    row = dist.ppf(unif(size=N), *param[:-2], loc=param[-2], scale=param[-1])
    plt.plot(tiempos, sorted(row), ".c", alpha=0.3)
plt.plot(np.linspace(0, breaks), np.linspace(0, breaks))
plt.plot(tiempos[:-1], vec, ".r")
plt.title("Nube de puntos en Q-Q")
plt.savefig("assets/fig_5.png")
# plt.show()

# Simulamos una muestra de 100 datos:
n = 100
datos_unif = np.random.uniform(size=n)
simulados = dist.ppf(datos_unif, *param[:-2], loc=param[-2], scale=param[-1])
print("Datos simulados: \n{}".format(simulados))

# Media y suma total:
print("Media: {}".format(np.mean(simulados)))
print("Suma total: {}".format(np.sum(simulados)))

# Mostramos todos los plots:
plt.show()
