import matplotlib.pyplot as plt
import numpy as np

notas = np.random.randint(0, 11, 30)

plt.hist(notas, bins=range(12), edgecolor='black', align='left')
plt.xticks(range(11))
plt.xlabel('Nota')
plt.ylabel('Número de alumnos')
plt.title('Histograma de notas')
plt.show()

# En la ejecución que he hecho los rangos de notas con más alumnos son de 2 y 5 con 5 alumnos, seguido de 0 con 4, 
# después 3, 7 y 10 con 3 alumnos, luego 1 y 6 con 2 alumnos y finalmente 4, 8 y 9 con 1 alumno.
# En general la mayoría de los alumnos sacaron notas bajas o medias, muy pocos sacaron notas altas.