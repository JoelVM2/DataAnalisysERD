import pandas as pd
import matplotlib.pyplot as plt

datos = {
    "Edad": [18, 19, 20, 21, 22, 23, 24, 25],
    "Altura": [160, 162, 165, 168, 170, 172, 175, 178]
}
df = pd.DataFrame(datos)

plt.scatter(df['Edad'], df['Altura'], color='blue')
plt.xlabel('Edad')
plt.ylabel('Altura (cm)')
plt.title('Gráfico de dispersión: Edad vs Altura')
plt.grid(True)
plt.show()
# Observando el gráfico, a medida que la edad aumenta tambien aumenta la edad. En este caso hay una correlacion positiva entre edad y altura.