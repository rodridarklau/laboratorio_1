import numpy as np
import matplotlib.pyplot as plt
from cargar_datos import obtener_datos_sii
from errores import redondear_dos_cifras
from punto_flotante import ejercicio_b2_ida_vuelta

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

# GRÁFICO 2: Variación mes a mes en barras
delta_mensual = np.diff(precios) # Resta entre mes t+1 y mes t
plt.figure(figsize=(10, 5))
colores = np.where(delta_mensual >= 0, 'g', 'r')
plt.bar(eje_temporal[1:], delta_mensual, color=colores, alpha=0.7)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.title('2. Variación Mes a Mes (ΔP) - Evidencia de Cancelación')
plt.xlabel('Meses (Secuenciales)')
plt.ylabel('ΔP (CLP)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('graficos/2_variacion_mes_a_mes.png', dpi=300)
plt.close()


# GRÁFICO 3: Error de representación por mes (2 cifras significativas)
precios_aprox = redondear_dos_cifras(precios)
error_absoluto = np.abs(precios - precios_aprox)
plt.figure(figsize=(10, 5))
plt.bar(eje_temporal, error_absoluto, color='purple', alpha=0.6)
plt.title('3. Error de Representación Absoluto por Mes (Mantisa Corta)')
plt.xlabel('Meses (Secuenciales)')
plt.ylabel('Error Absoluto (CLP)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('graficos/3_error_representacion.png', dpi=300)
plt.close()

# GRÁFICO 4: Rentabilidad comprando en el mínimo histórico

M = 1000000.0
idx_min = np.argmin(precios)
p_min_aprox = precios_aprox[idx_min]
er_min = (abs(precios[idx_min] - p_min_aprox) / precios[idx_min]) * 100

usd_comprados = M / p_min_aprox
rentabilidades = []
errores_rentabilidad = []

for i in range(n_total):
    p_venta_aprox = precios_aprox[i]
    pesos_final = usd_comprados * p_venta_aprox
    ganancia = pesos_final - M
    rent = (ganancia / M) * 100
    rentabilidades.append(rent)
    
    # Propagación de error para la rentabilidad
    er_venta = (abs(precios[i] - p_venta_aprox) / precios[i]) * 100
    er_total = er_min + er_venta
    errores_rentabilidad.append(er_total)

plt.figure(figsize=(10, 5))
plt.errorbar(eje_temporal, rentabilidades, yerr=errores_rentabilidad, fmt='-o', color='teal', ecolor='salmon', elinewidth=1, capsize=2, markersize=3)
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.title('4. Rentabilidad Comprando en el Mínimo Global (con Error Propagado)')
plt.xlabel('Meses (Secuenciales)')
plt.ylabel('Rentabilidad (%)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('graficos/rentabilidad_minimo.png', dpi=300)
plt.close()

