import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar datos
df = pd.read_csv("responses_form_binario.csv")

# Columnas
cols_pais = [col for col in df.columns if col.startswith("País_")]
cols_impacto = [
    'Impacto_Poco importante', 'Impacto_Medianamente importante',
    'Impacto_Muy importante', 'Impacto_Fundamental'
]

# Procesamiento
df['Pais'] = df[cols_pais].idxmax(axis=1).str.replace("País_", "")
impacto_map = {
    'Impacto_Poco importante': 2,
    'Impacto_Medianamente importante': 3,
    'Impacto_Muy importante': 4,
    'Impacto_Fundamental': 5
}
df['Impacto'] = 0
for col, val in impacto_map.items():
    df['Impacto'] += df[col] * val

resumen = df.groupby('Pais').agg(
    Frecuencia=('Pais', 'count'),
    ImpactoPromedio=('Impacto', 'mean')
).reset_index()

# Bubble chart
sizes = resumen['Frecuencia'] * 300
colors = plt.cm.viridis(np.linspace(0, 1, len(resumen)))

fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(resumen['Frecuencia'], resumen['ImpactoPromedio'],
           s=sizes, c=colors, edgecolors='black', alpha=0.85)
for i in range(len(resumen)):
    ax.text(resumen['Frecuencia'][i], resumen['ImpactoPromedio'][i], resumen['Pais'][i],
            ha='center', va='center', fontsize=9, color='black', weight='bold')
ax.set_xlabel("Frecuencia de menciones del país")
ax.set_ylabel("Impacto promedio percibido")
ax.set_title("Aporte de países vs. Impacto percibido")
plt.tight_layout()
plt.show()
    