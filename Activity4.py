import pandas as pd
import matplotlib.pyplot as plt

productos = ["Café", "Té", "Sandwich", "Galleta", "Zumo"]
ventas = [120, 85, 45, 60, 95]

df = pd.DataFrame({
    "Producto": productos,
    "Ventas": ventas
})

df_filtrado = df[df['Ventas'] > 80]

plt.bar(df_filtrado['Producto'], df_filtrado['Ventas'], color='blue')
plt.xlabel('Producto')
plt.ylabel('Ventas')
plt.title('Productos con más de 80 unidades vendidas')
plt.show()
# Observando el gráfico puedes ver los los producton con más de 80 unidades vendidas, primeros el café con bastante diferencia y depues el zumo y el té.
# Este gráfico muestra los productos con mejor rendimiento en ventas.