import numpy as np
import matplotlib.pyplot as plt
import os
from cargar_datos import obtener_datos_sii
from errores import redondear_dos_cifras

anios, nombres_meses, precios = obtener_datos_sii()
n_total = len(precios)
eje_temporal = np.arange(n_total)

# GRÁFICO 1: Serie mensual del dólar observado (2022-2025)
plt.figure(figsize=(10, 5))
plt.plot(eje_temporal, precios, marker='o', color='b', linestyle='-', linewidth=1.5, markersize=3)
plt.title('1. Serie Mensual del Dólar Observado (2022-2025)')
plt.xlabel('Meses (Secuenciales)')
plt.ylabel('Precio (CLP)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('graficos/serie_mensual.png', dpi=300)
plt.close()