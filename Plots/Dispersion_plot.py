import pandas as pd
import matplotlib.pyplot as plt

# Cargar y preparar
df = pd.read_csv("responses_form_binario.csv")

cols_contrib = [col for col in df.columns if col.startswith("Contribución_")]
cols_impacto = [
    'Impacto_Poco importante', 'Impacto_Medianamente importante',
    'Impacto_Muy importante', 'Impacto_Fundamental'
]
df['Contrib'] = df[cols_contrib].idxmax(axis=1).str.replace("Contribución_", "")
impacto_map = {
    'Impacto_Poco importante': 2,
    'Impacto_Medianamente importante': 3,
    'Impacto_Muy importante': 4,
    'Impacto_Fundamental': 5
}
df['Impacto'] = 0
for col, val in impacto_map.items():
    df['Impacto'] += df[col] * val

# Asignar número a cada categoría
mapa_contrib = {v: i+1 for i, v in enumerate(df['Contrib'].unique())}
df['Contrib_num'] = df['Contrib'].map(mapa_contrib)

# Gráfico de dispersión
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(df['Contrib_num'], df['Impacto'], alpha=0.7, c=df['Impacto'], cmap='plasma')
ax.set_xticks(list(mapa_contrib.values()))
ax.set_xticklabels(list(mapa_contrib.keys()), rotation=45, ha='right')
ax.set_ylabel("Impacto percibido")
ax.set_xlabel("Contribución percibida")
ax.set_title("Cruce entre impacto percibido y tipo de contribución")
plt.tight_layout()
plt.show()
