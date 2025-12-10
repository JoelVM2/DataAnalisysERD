import pandas as pd
import matplotlib.pyplot as plt

datos = {
    "Dia": ["Dl","Dl","Dt","Dt","Dc","Dc","Dj","Dj"],
    "Visitas": [120, 150, 130, 160, 140, 170, 110, 180]
}

df = pd.DataFrame(datos)

df_agrupado = df.groupby("Dia")["Visitas"].mean().reset_index()

plt.bar(df_agrupado['Dia'], df_agrupado['Visitas'], color='skyblue')
plt.xlabel('Día')
plt.ylabel('Media de visitas')
plt.title('Media de visitas por día')
plt.show()
# Se puede observar en el gráfico que La media de visitas muestra que el miércoles tiene el mayor promedio con 155 visitas, 
# seguido de el jueves y el martes con 145 visitas cada uno.
# El lunes tiene el menor promedio, con 135 visitas.
# El gráfico de barras permite ver rápidamente el tráfico semanal en la web.