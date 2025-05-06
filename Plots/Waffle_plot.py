import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Datos de los tres gráficos tipo tarjeta
cards = [
    {"title": "Estilo de juego diverso", "percent": 5.3, "color": "#66b3ff"},
    {"title": "Apoyo a campañas sociales", "percent": 100.0, "color": "#99ff99"},
    {"title": "País más mencionado: Serbia", "percent": 30.0, "color": "#ff9999"}
]

# Función para dibujar una tarjeta waffle con el relleno desde abajo
def draw_waffle_bottom_up(ax, percent, color, title):
    total_squares = 100
    filled = int(percent)
    count = 0
    for i in range(10):  # recorrer de abajo hacia arriba
        for j in range(10):  # de izquierda a derecha
            facecolor = color if count < filled else 'white'
            edgecolor = 'lightgray'
            rect = patches.Rectangle((j, i), 1, 1, linewidth=0.5,
                                     edgecolor=edgecolor, facecolor=facecolor)
            ax.add_patch(rect)
            count += 1

    # Ajustes de visualización
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 11.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Título superior
    ax.text(5, 10.5, f"{title}", ha='center', va='center', fontsize=11, weight='bold')

    # Porcentaje inferior en negrilla
    ax.text(5, -0.8, f"{percent:.1f}%", ha='center', va='top',
            fontsize=11, weight='bold', color='black')

# Crear figura y subgráficos
fig, axs = plt.subplots(1, 3, figsize=(12, 5))

# Dibujar cada tarjeta
for ax, card in zip(axs, cards):
    draw_waffle_bottom_up(ax, card["percent"], card["color"], card["title"])

plt.tight_layout()
plt.show()
