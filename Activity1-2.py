import matplotlib.pyplot as plt

noms = ["Anna", "Jordi", "Marta", "Pol", "Laia"]
notes = [7.5, 8.0, 6.0, 5.5, 9.0]

plt.bar(noms, notes, color="red")
plt.title("Notas por alumno")
plt.xlabel("Alumnos")
plt.ylabel("Notas")
plt.show()

# Según el gráfico, podemos observar que todos los alumnos de la clase han aprobado, la mayor nota ha sido un 9 de Laia, la menor nota ha sido un 5 de Pol.