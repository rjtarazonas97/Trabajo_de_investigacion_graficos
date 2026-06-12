import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

# ── Configuración global de estilo ──────────────────────────────────────────
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.titlesize": 12,
    "axes.titleweight": "bold",
    "axes.titlepad": 15, # Aumentado para separar más el título de la gráfica
    "figure.dpi": 150,
    "savefig.dpi": 200,
    "savefig.bbox": "tight", # Clave para que no se corte nada al guardar
})

COLORS = {
    "purple":  "#534AB7",
    "purple2": "#7F77DD",
    "purple3": "#AFA9EC",
    "teal":    "#0F6E56",
    "teal2":   "#1D9E75",
    "teal3":   "#5DCAA5",
    "teal4":   "#9FE1CB",
    "blue":    "#3B8BD4",
    "blue2":   "#85B7EB",
    "coral":   "#D85A30",
    "amber":   "#EF9F27",
    "red":     "#E24B4A",
    "green":   "#639922",
    "gray":    "#888780",
}

# ════════════════════════════════════════════════════════════════════════════
# OE1 — Amenazas de ciberseguridad e IA ofensiva identificadas
# ════════════════════════════════════════════════════════════════════════════
def grafica_oe1():
    categorias = [
        "IA ofensiva\nautomatizada",
        "APIs\nexpuestas",
        "Supply chain\nLLM",
        "Envenenamiento\nde datos",
        "Phishing\navanzado",
        "MitM en\nmicroservicios",
    ]
    valores = [14, 13, 11, 10, 8, 7]
    colores = [
        COLORS["coral"], COLORS["purple2"], COLORS["amber"],
        COLORS["red"],   COLORS["blue"],    COLORS["green"],
    ]

    # Lienzo más ancho
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(categorias, valores, color=colores, edgecolor="white",
                  linewidth=0.6, width=0.6, zorder=3)

    for bar, val in zip(bars, valores):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.3,
                str(val), ha="center", va="bottom", fontsize=10, fontweight="bold")

    ax.set_ylim(0, 17)
    ax.set_ylabel("N° de artículos que identifican la amenaza", fontsize=10)
    ax.set_title("OE1 — Amenazas de ciberseguridad e IA ofensiva identificadas\n"
                 "(Vectores de ataque documentados en la literatura revisada, 2020–2026)",
                 fontsize=11, fontweight="bold")
    ax.yaxis.grid(True, color="#e0e0e0", linewidth=0.7, zorder=0)
    ax.set_axisbelow(True)
    ax.spines["left"].set_color("#cccccc")
    ax.spines["bottom"].set_color("#cccccc")

    leyenda = [mpatches.Patch(color=c, label=l.replace('\n', ' '))
               for c, l in zip(colores, categorias)]
    # Leyenda fuera del gráfico a la derecha
    ax.legend(handles=leyenda, fontsize=9, loc="upper left",
              bbox_to_anchor=(1.02, 1), framealpha=0.4)

    plt.tight_layout()
    plt.savefig("OE1_amenazas_ciberseguridad.png", bbox_inches='tight')
    print("✓ OE1_amenazas_ciberseguridad.png guardado")
    return fig

# ════════════════════════════════════════════════════════════════════════════
# OE2 — Factores de deuda técnica y degradación arquitectónica
# ════════════════════════════════════════════════════════════════════════════
def grafica_oe2():
    etiquetas = [
        "Cambios no coordinados\nen APIs externas",
        "Acoplamiento\narquitectónico excesivo",
        "Falta de versionado\ny backward compat.",
        "Dependencias con\nservicios IA",
        "Ausencia de planes\nde deprecación",
    ]
    valores = [28, 24, 20, 17, 11]
    colores = [
        COLORS["purple"], COLORS["purple2"], COLORS["purple3"],
        COLORS["blue"],   COLORS["blue2"],
    ]

    # Lienzo más ancho para acomodar la leyenda lateral
    fig, ax = plt.subplots(figsize=(9, 6))
    wedges, texts, autotexts = ax.pie(
        valores,
        labels=None,
        colors=colores,
        autopct="%1.0f%%",
        pctdistance=0.75,
        startangle=120,
        wedgeprops={"edgecolor": "white", "linewidth": 2},
    )
    for at in autotexts:
        at.set_fontsize(10)
        at.set_fontweight("bold")
        at.set_color("white")

    centro = plt.Circle((0, 0), 0.50, color="white")
    ax.add_artist(centro)
    ax.text(0, 0, "Deuda\nTécnica", ha="center", va="center",
            fontsize=12, fontweight="bold", color=COLORS["purple"])

    ax.set_title("OE2 — Factores de deuda técnica y degradación arquitectónica\n"
                 "(Incidencia relativa documentada en la muestra analizada)",
                 fontsize=11, fontweight="bold")

    leyenda = [mpatches.Patch(color=c, label=l.replace('\n', ' '))
               for c, l in zip(colores, etiquetas)]
    # Leyenda movida al centro-derecha para evitar cortes abajo
    ax.legend(handles=leyenda, fontsize=9, loc="center left",
              bbox_to_anchor=(1.05, 0.5), framealpha=0.3)

    plt.tight_layout()
    plt.savefig("OE2_deuda_tecnica.png", bbox_inches='tight')
    print("✓ OE2_deuda_tecnica.png guardado")
    return fig

# ════════════════════════════════════════════════════════════════════════════
# OE3 — Mecanismos de gobernanza de APIs y patrones arquitectónicos
# ════════════════════════════════════════════════════════════════════════════
def grafica_oe3():
    mecanismos = [
        "API Gateway centralizado",
        "Service Mesh / Istio",
        "Contratos API (OpenAPI)",
        "Event-driven / asíncrono",
        "Autenticación federada\n(OAuth2 / JWT)",
    ]
    valores = [17, 14, 13, 12, 10]
    colores = [
        COLORS["teal"],  COLORS["teal2"], COLORS["teal3"],
        COLORS["teal4"], COLORS["blue"],
    ]

    fig, ax = plt.subplots(figsize=(10, 6))
    y_pos = np.arange(len(mecanismos))
    bars = ax.barh(y_pos, valores, color=colores, edgecolor="white",
                   linewidth=0.6, height=0.6, zorder=3)

    for bar, val in zip(bars, valores):
        ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height() / 2,
                f"{val} arts.", ha="left", va="center",
                fontsize=10, fontweight="bold")

    ax.set_yticks(y_pos)
    ax.set_yticklabels(mecanismos, fontsize=10)
    ax.set_xlim(0, 22)
    ax.set_xlabel("N° de artículos que proponen el mecanismo", fontsize=10)
    ax.set_title("OE3 — Mecanismos de gobernanza de APIs y patrones arquitectónicos\n"
                 "(Soluciones para mitigar fallos lógicos y caídas de servicio)",
                 fontsize=11, fontweight="bold")
    ax.xaxis.grid(True, color="#e0e0e0", linewidth=0.7, zorder=0)
    ax.set_axisbelow(True)
    ax.spines["left"].set_color("#cccccc")
    ax.spines["bottom"].set_color("#cccccc")

    leyenda = [mpatches.Patch(color=c, label=l.replace('\n', ' '))
               for c, l in zip(colores, mecanismos)]
    # Leyenda a la derecha
    ax.legend(handles=leyenda, fontsize=9, loc="center left",
              bbox_to_anchor=(1.02, 0.5), framealpha=0.3)

    plt.tight_layout()
    plt.savefig("OE3_gobernanza_apis.png", bbox_inches='tight')
    print("✓ OE3_gobernanza_apis.png guardado")
    return fig

# ════════════════════════════════════════════════════════════════════════════
# OE4 — Contraste de marcos metodológicos: seguridad vs. sostenibilidad
# ════════════════════════════════════════════════════════════════════════════
def grafica_oe4():
    grupos = [
        {
            "label":  "Marcos de seguridad\n(Zero Trust, IA defensiva)",
            "puntos": [(85, 25, 14), (78, 30, 9)],
            "color":  COLORS["coral"],
        },
        {
            "label":  "Marcos arquitectónicos\n(Microservicios, IoT)",
            "puntos": [(30, 80, 11), (22, 72, 8)],
            "color":  COLORS["blue"],
        },
        {
            "label":  "Marcos de gobernanza\nde APIs",
            "puntos": [(50, 55, 10), (45, 48, 6)],
            "color":  COLORS["teal2"],
        },
        {
            "label":  "Propuestas integradoras\n(emergentes — brecha)",
            "puntos": [(62, 60, 3)],
            "color":  COLORS["purple2"],
        },
    ]

    fig, ax = plt.subplots(figsize=(10, 7))

    for g in grupos:
        for (x, y, s) in g["puntos"]:
            ax.scatter(x, y, s=s * 60, color=g["color"], alpha=0.65,
                       edgecolors=g["color"], linewidths=1.2, zorder=3)
            ax.text(x + 1.5, y + 1.5, f"n={s}", fontsize=9, color=g["color"])

    ax.axvline(50, color="#cccccc", linewidth=0.8, linestyle="--", zorder=1)
    ax.axhline(50, color="#cccccc", linewidth=0.8, linestyle="--", zorder=1)
    ax.text(52, 92, "Marco ideal\n(integrador)", fontsize=9,
            color="#999999", style="italic")

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_xlabel("Cobertura de seguridad / ciberseguridad (%)", fontsize=10)
    ax.set_ylabel("Cobertura de sostenibilidad técnica (%)", fontsize=10)
    ax.set_title("OE4 — Contraste de marcos metodológicos\n"
                 "Seguridad vs. sostenibilidad técnica en la literatura revisada",
                 fontsize=11, fontweight="bold")
    ax.grid(True, color="#eeeeee", linewidth=0.7, zorder=0)

    leyenda = [mpatches.Patch(color=g["color"], label=g["label"].replace('\n', ' '))
               for g in grupos]
    # Leyenda a la derecha, para evitar que tape puntos importantes (ej. n=14 o n=9)
    ax.legend(handles=leyenda, fontsize=9, loc="center left",
              bbox_to_anchor=(1.02, 0.5), framealpha=0.4, borderpad=0.8)

    plt.tight_layout()
    plt.savefig("OE4_contraste_marcos.png", bbox_inches='tight')
    print("✓ OE4_contraste_marcos.png guardado")
    return fig

# ════════════════════════════════════════════════════════════════════════════
# OE5 — Brecha metodológica: cobertura aislada vs. integrada
# ════════════════════════════════════════════════════════════════════════════
def grafica_oe5():
    categorias = [
        "Solo\nseguridad",
        "Solo\nsostenibilidad",
        "Solo\ngobernanza APIs",
        "Seguridad +\narquitectura\n(parcial)",
        "Marco\nintegrador\n(seg. + sost.)",
    ]
    valores = [14, 10, 7, 6, 3]
    porcentajes = [v / 40 * 100 for v in valores]
    colores = [
        COLORS["coral"], COLORS["blue"], COLORS["amber"],
        COLORS["purple2"], COLORS["teal2"],
    ]

    fig, ax = plt.subplots(figsize=(10, 6.5))
    x_pos = np.arange(len(categorias))
    bars = ax.bar(x_pos, valores, color=colores, edgecolor="white",
                  linewidth=0.6, width=0.6, zorder=3)

    for bar, val, pct in zip(bars, valores, porcentajes):
        ax.text(bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.2,
                f"{val} ({pct:.0f}%)",
                ha="center", va="bottom", fontsize=10, fontweight="bold")

    ax.set_xticks(x_pos)
    ax.set_xticklabels(categorias, fontsize=10)
    ax.set_ylim(0, 18)
    ax.set_ylabel("N° de artículos (n = 40)", fontsize=10)
    ax.set_title("OE5 — Brecha metodológica: cobertura aislada vs. integrada\n"
                 "Justificación del marco metodológico propuesto (solo 3/40 con enfoque integrador)",
                 fontsize=11, fontweight="bold")
    ax.yaxis.grid(True, color="#e0e0e0", linewidth=0.7, zorder=0)
    ax.set_axisbelow(True)
    ax.spines["left"].set_color("#cccccc")
    ax.spines["bottom"].set_color("#cccccc")

    # Ajuste de las coordenadas para que la flecha no se solape con otras barras
    ax.annotate("← Solo 7.5% propone\nun marco integrador",
                xy=(4, 3.5), xytext=(3.1, 12),
                arrowprops=dict(arrowstyle="->", color=COLORS["teal2"],
                                lw=1.5),
                fontsize=10, color=COLORS["teal2"], fontstyle="italic")

    leyenda = [mpatches.Patch(color=c, label=l.replace('\n', ' '))
               for c, l in zip(colores, categorias)]
    # Leyenda a la derecha
    ax.legend(handles=leyenda, fontsize=9, loc="upper left",
              bbox_to_anchor=(1.02, 1), framealpha=0.3)

    plt.tight_layout()
    plt.savefig("OE5_brecha_metodologica.png", bbox_inches='tight')
    print("✓ OE5_brecha_metodologica.png guardado")
    return fig

# ════════════════════════════════════════════════════════════════════════════
# MAIN — generar todas las gráficas y un PDF consolidado
# ════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("\n=== Generando gráficas de investigación ===\n")

    figs = [
        grafica_oe1(),
        grafica_oe2(),
        grafica_oe3(),
        grafica_oe4(),
        grafica_oe5(),
    ]

    with PdfPages("graficas_investigacion_completo.pdf") as pdf:
        for fig in figs:
            # Replicar el bbox_inches='tight' al guardar en PDF
            pdf.savefig(fig, bbox_inches="tight")
    print("\n✓ graficas_investigacion_completo.pdf generado")

    plt.show()
    print("\nListo. Archivos generados:")
    print("  • OE1_amenazas_ciberseguridad.png")
    print("  • OE2_deuda_tecnica.png")
    print("  • OE3_gobernanza_apis.png")
    print("  • OE4_contraste_marcos.png")
    print("  • OE5_brecha_metodologica.png")
    print("  • graficas_investigacion_completo.pdf")