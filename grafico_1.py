import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# ==========================================
# CONFIGURACIÓN GENERAL ACADÉMICA
# ==========================================
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.size'] = 11
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.titleweight'] = 'bold'
# Usamos una tipografía sans-serif limpia (ideal para lectura rápida)
plt.rcParams['font.family'] = 'sans-serif' 

# Crear el documento PDF que contendrá todas las imágenes
with PdfPages('graficos_tesis.pdf') as pdf:

    # ==========================================
    # 1. Gráfico Circular (Pie Chart)
    # ==========================================
    fig1 = plt.figure(figsize=(8, 6))
    porcentajes_1 = [44, 32, 24]
    etiquetas_1 = [
        'Desafíos de Ciberseguridad y Superficie de Ataque',
        'Desafíos de Sostenibilidad Técnica y Deuda Técnica',
        'Estrategias Metodológicas y Resolución Integral'
    ]
    colores_1 = ['#5b9bd5', '#ed7d31', '#a5a5a5']
    # "explode" separa la primera rebanada (44%) para destacarla
    separacion = (0.05, 0, 0) 

    plt.pie(porcentajes_1, labels=None, autopct='%1.0f%%', colors=colores_1, 
            startangle=90, pctdistance=0.65, explode=separacion,
            wedgeprops={'edgecolor': 'black', 'linewidth': 0.8}, # Borde negro sutil
            textprops={'weight': 'bold', 'fontsize': 12}) # Números en negrita
            
    plt.legend(etiquetas_1, loc="lower center", bbox_to_anchor=(0.5, -0.15), frameon=False)
    plt.title("Distribución de Desafíos y Estrategias", pad=20)
    plt.tight_layout()
    
    # Guardar en PNG individual y luego en el PDF
    plt.savefig('grafico_1_circular.png', bbox_inches='tight')
    pdf.savefig(fig1, bbox_inches='tight')
    plt.close()

    # ==========================================
    # 2. Gráfico de Anillo (Donut Chart)
    # ==========================================
    fig2 = plt.figure(figsize=(9, 5))
    porcentajes_2 = [39, 31, 30] 
    etiquetas_2 = [
        'Falta de autenticación robusta y el mal uso de las APIs',
        'IA Ofensiva e Ingeniería Social',
        'Auge y susceptibilidad de LLMs'
    ]
    colores_2 = ['#3175b9', '#b88c00', '#ba590d'] 

    wedges, texts, autotexts = plt.pie(porcentajes_2, autopct='%1.0f%%', colors=colores_2, 
                                       startangle=140, pctdistance=0.75, 
                                       wedgeprops={'edgecolor': 'white', 'linewidth': 2.5},
                                       textprops=dict(color="white", weight="bold", fontsize=12))

    # Círculo blanco central
    centro_blanco = plt.Circle((0,0), 0.50, fc='white') # Centro un poco más amplio
    plt.gca().add_artist(centro_blanco)

    plt.legend(wedges, etiquetas_2, loc="center left", bbox_to_anchor=(1, 0.5), frameon=False)
    plt.title("Distribución de Vulnerabilidades Críticas", pad=20)
    plt.tight_layout()
    
    plt.savefig('grafico_2_anillo.png', bbox_inches='tight')
    pdf.savefig(fig2, bbox_inches='tight')
    plt.close()

    # ==========================================
    # 3. Gráfico de Barras Verticales
    # ==========================================
    fig3 = plt.figure(figsize=(8, 6))
    etiquetas_3 = [
        'Acoplamiento rígido,\nrendimiento y\ncomplejidad de red',
        'Evolución inconsistente,\nversionado y falta\nde gobernanza',
        'Falta de\ninteroperabilidad y\nbrechas en pruebas'
    ]
    valores_3 = [23, 20, 17]
    colores_3 = ['#456935', '#9dc183', '#c2ddb6']

    barras_3 = plt.bar(etiquetas_3, valores_3, color=colores_3, width=0.55, 
                       edgecolor='black', linewidth=0.8) # Borde añadido
    plt.ylim(0, 28) # Límite Y ajustado

    # Añadir valores exactos ENCIMA de cada barra
    for barra in barras_3:
        altura = barra.get_height()
        plt.annotate(f'{altura}',
                     xy=(barra.get_x() + barra.get_width() / 2, altura),
                     xytext=(0, 5),  # 5 puntos de elevación
                     textcoords="offset points",
                     ha='center', va='bottom', weight='bold', fontsize=12)

    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    plt.grid(axis='y', linestyle='--', color='lightgrey', alpha=0.7) # Grid punteado más sutil
    ax.set_axisbelow(True)
    plt.title("Problemas Técnicos de Arquitectura Evaluados", pad=20)

    plt.tight_layout()
    plt.savefig('grafico_3_barras_verticales.png', bbox_inches='tight')
    pdf.savefig(fig3, bbox_inches='tight')
    plt.close()

    # ==========================================
    # 4. Gráfico de Barras Horizontales
    # ==========================================
    fig4 = plt.figure(figsize=(10, 4.5))
    etiquetas_4 = [
        'Diseño Proactivo con IA, MLOps\ny Gobernanza Continua',
        'Arquitectura Zero Trust, Service Mesh\ny Criptografía',
        'Computación Asíncrona, Serverless,\nEdge y Pub/Sub'
    ]
    valores_4 = [24, 20, 13]
    colores_4 = ['#4f8135', '#ffcc55', '#9abce4']

    barras_4 = plt.barh(etiquetas_4, valores_4, color=colores_4, height=0.5, 
                        edgecolor='black', linewidth=0.8)

    # Añadir el número al final de cada barra en negrita
    for barra in barras_4:
        ancho = barra.get_width()
        plt.annotate(f'{ancho}',
                     xy=(ancho, barra.get_y() + barra.get_height() / 2),
                     xytext=(10, 0), # Reducida un poco la separación
                     textcoords="offset points",
                     ha='left', va='center', weight='bold', fontsize=12)

    plt.xlim(0, 28)

    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    plt.grid(axis='x', linestyle='--', color='lightgrey', alpha=0.7)
    ax.set_axisbelow(True)
    plt.title("Tendencias en Adopción Tecnológica", pad=20)

    plt.tight_layout()
    plt.savefig('grafico_4_barras_horizontales.png', bbox_inches='tight')
    pdf.savefig(fig4, bbox_inches='tight')
    plt.close()

print("¡Éxito! Se han generado las 4 imágenes PNG y 1 archivo PDF consolidado para tu tesis.")