import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ventas.csv')

print(df.head())
print(df.describe())

plt.figure(figsize=(8,5))
plt.bar(df['Producto'], df['Ventas'], color='skyblue')
plt.xlabel('Producto')
plt.ylabel('Ventas')
plt.title('Ventas por producto')
plt.show()

plt.figure(figsize=(8,5))
plt.scatter(df['Precio'], df['Ventas'], color='green')
plt.xlabel('Precio')
plt.ylabel('Ventas')
plt.title('Precio vs Ventas')
plt.grid(True)
plt.show()

# Los productos más baratos, como Agua y Pan, tienen las ventas más altas, eso muestra una relación inversa entre precio y unidades vendidas.
# Productos con precios intermedios o altos, como Sandwich y Chocolate, tienen menos ventas, indicando menor demanda.
# Algunos productos con precio medio, como Café y Zumo, tienen buenas ventas, lo que puede indicar popularidad o preferencia del cliente.
