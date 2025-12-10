import pandas as pd
import matplotlib.pyplot as plt

años = [2020, 2021, 2022, 2023]
ventas = [40000, 42000, 39500, 45000]

df = pd.DataFrame({
    "Año": años,
    "Ventas": ventas
})

df['Crecimiento'] = df['Ventas'].diff()

fig, ax1 = plt.subplots()

ax1.plot(df['Año'], df['Ventas'], marker='o', color='blue', label='Ventas')
ax1.set_xlabel('Año')
ax1.set_ylabel('Ventas', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.grid(True)

ax2 = ax1.twinx()
ax2.plot(df['Año'], df['Crecimiento'], marker='s', color='red', linestyle='--', label='Crecimiento')
ax2.set_ylabel('Crecimiento', color='red')
ax2.tick_params(axis='y', labelcolor='red')

plt.title('Evolución de ventas y crecimiento anual')
fig.tight_layout()
plt.show()

# El gráfico permite ver claramente la tendencia de las ventas y cuánto cambian cada año.
# La línea azul muestra las ventas de cada año, y la roja el crecimiento de las ventas y cuanto cambian cada año.