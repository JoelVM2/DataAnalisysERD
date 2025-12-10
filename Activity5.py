import matplotlib.pyplot as plt

categorias = ["Comida", "Transporte", "Ocio", "Otras"]
gasto = [300, 70, 120, 50]

explode = (0.1, 0, 0, 0)
fig, ax = plt.subplots()
ax.pie(gasto, explode=explode, labels=categorias, 
autopct='%1.1f%%',shadow=True, startangle=90)
plt.title("Distribución del gasto mensual")
plt.show()

# El gráfico muestra cómo se distribuyen los gastos mensuales entre cuatro categorías: Comida, Transporte, Ocio y Otras.
# El sector destacado indica que Comida es el mayor gasto, representando aproximadamente 60% del total.
# Transporte, Ocio y Otras tienen un peso mucho menor, siendo Otras la categoría menos significativa.
# El gráfico permite ver rápidamente que la mayor parte del presupuesto mensual se destina a comida y que el resto de categorías tienen un impacto mucho más pequeño.