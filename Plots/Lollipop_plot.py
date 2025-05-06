import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("responses_form_binario.csv")
cols_pais = [col for col in df.columns if col.startswith("País_")]
cols_impacto = [
    'Impacto_Poco importante', 'Impacto_Medianamente importante',
    'Impacto_Muy importante', 'Impacto_Fundamental'
]
df['Pais'] = df[cols_pais].idxmax(axis=1).str.replace("País_", "")
impacto_map = {
    'Impacto_Poco importante': 2,
    'Impacto_Medianamente importante': 3,
    'Impacto_Muy importante': 4,
    'Impacto_Fundamental': 5
}
df['Impacto'] = sum(df[col] * val for col, val in impacto_map.items())
resumen = df.groupby('Pais').agg(ImpactoPromedio=('Impacto', 'mean')).sort_values('ImpactoPromedio')

# Lollipop chart
fig, ax = plt.subplots(figsize=(9, 6))
ax.hlines(y=resumen.index, xmin=0, xmax=resumen['ImpactoPromedio'], color='gray', alpha=0.7, linewidth=2)
ax.plot(resumen['ImpactoPromedio'], resumen.index, "o", markersize=9, color='dodgerblue')
ax.set_xlabel("Impacto promedio percibido")
ax.set_title("Impacto promedio por país (Lollipop Chart)")
plt.tight_layout()
plt.show()
