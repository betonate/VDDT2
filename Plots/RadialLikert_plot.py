import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("responses_form_binario.csv")

cols_impacto = [
    'Impacto_Poco importante',
    'Impacto_Medianamente importante',
    'Impacto_Muy importante',
    'Impacto_Fundamental'
]

frecuencias = df[cols_impacto].sum()
labels = [col.replace("Impacto_", "") for col in frecuencias.index]
values = frecuencias.values
angles = np.linspace(0, 2 * np.pi, len(values), endpoint=False)

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.bar(angles, values, width=0.6, color='teal', alpha=0.8)
ax.set_xticks(angles)
ax.set_xticklabels(labels)
ax.set_title("Percepción del impacto de jugadores extranjeros")
plt.tight_layout()
plt.show()
