
> #### Quick info:
>
> **Charla:** *Data Science con SciPy* <br>
> **Tallerista:** Rodolfo Ferro <br>
> **Twitter:** [@rodo_ferro](https://twitter.com/rodo_ferro) <br>
> **Contacto:** [https://rodolfoferro.xyz](https://rodolfoferro.xyz) <br>
  > **Slides:** [¡Click aquí!](https://goo.gl/5Q3BZ8)
------
![DataSciPy](assets/DataSciPy.png)

# Data Science con SciPy

En esta charla se ilustrará una técnica de ciencia de datos para estimar distribuciones probabilísticas de datos y con ello poder simular nuevos datos que sean válidos, aleatorios y se distribuyan de igual manera que los datos originales. Todo ello con el poder de SciPy.

La idea es que a partir de una muestra de datos (*variables aleatorias*) utilicemos `scipy.stats` para estimar la distribución de probabilidad, así como los parámetros de dicha distribución y con ello utilizar el [*Teorema de la Transformada Inversa*](https://es.wikipedia.org/wiki/M%C3%A9todo_de_la_transformada_inversa) para generar nuevas variables aleatorias con dicha distribución. De esta manera se generan nuevos datos aleatorios pertenecientes a la misma familia que los datos originales.

Para este taller necesitas conocimientos básicos sobre programación en Python. Parte de los objetivos es que posterior a la charla se cuente con una nueva técnica para generación de datos aleatorios bien distribuidos; con Python, obviamente.

**Slides:** [¡Click aquí!](https://goo.gl/5Q3BZ8)

## ⚙️ Instalación

La versión más reciente de [Anaconda](https://www.anaconda.com/download/) (3.7) con [Python >= 3.6](https://www.python.org/downloads/) va a ser requerida. Trabajaremos utilizando un entorno de Anaconda para este taller.

Para crear el `conda env` e instalar los requerimientos sólo clona el repo:
```bash
# Clona el repo de GitHub:
git clone https://github.com/RodolfoFerro/DataSciPy.git
cd DataSciPy
```

Y corre lo siguiente:
```bash
# Crea el entorno de Anaconda:
conda env create -f environment.yml
```

Para activar/desactivar el entorno:
```bash
# Activar entorno:
conda activate DataSciPy

# Desactivar entorno:
conda deactivate
```

## 👾 Contenido

El repositorio y charla están autocontenidos, a través de los [slides](https://goo.gl/5Q3BZ8) y el script `datascipy.py`.


***

### SOBRE EL USO DE INFORMACIÓN TOTAL O PARCIAL: 🔐
* Estos documentos fueron originalmente creados por el autor.
* Cualquier uso de estos documentos o sus contenidos están permitidos a través de la licencia provista y sus condiciones.
* Para cualquier aclaración, puedes contactar al autor: https://rodolfoferro.xyz/

**Copyright (c) 2018 Rodolfo Ferro**
