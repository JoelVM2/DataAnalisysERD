import matplotlib.pyplot as plt

temperatures = [12, 13, 11, 15, 16, 14, 10]
days = ["Lun.", "Mar.", "Mie.", "Jue.", "Vie.", "Sab.", "Dom."]

plt.plot( days,temperatures, marker="o", color="red")
plt.title("Temperatures per day")
plt.xlabel("Days")
plt.ylabel("Temperatures")
plt.show()

# Según el gráfico la temperatura máxima se dio el viernes y fue de 16ºC, la temperatura minima fue el domingo y fue de 10ºC, la media de la semana es de es de 13.