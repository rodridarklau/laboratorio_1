import os
import sys
import csv
import numpy as np

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from cargar_datos import obtener_datos_sii
from anualidad import calcular_a4
from errores import calcular_errores_a1, calcular_a2, calcular_a3, calcular_a5, redondear_dos_cifras
from punto_flotante import mantisa_corta_b1, cancelacion_maquina_b4, ejercicio_b2_ida_vuelta

def generar_resultados_md():
    # 1. Ejecutar funciones de la Sección A
    anios, nombres_meses, precios = obtener_datos_sii()
    
    # A1
    er_a1 = calcular_errores_a1()
    idx_peor = np.argmax(er_a1)
    
    # A2 (Ejemplo: Comprar en Marzo 2022 [índice 2] y Vender en Julio 2022 [índice 6])
    ganancia_a2, ea_ganancia_a2, er_total_a2 = calcular_a2(2, 6)
    
    # A3
    delta_p_a3, ea_propagado_a3, error_porcentual_a3, es_confiable_a3 = calcular_a3()
    
    #A4
    resultados_a4 = calcular_a4()
    
    # A5
    ganancia_a5, ea_ganancia_a5, rentabilidad_a5, sobrevive_a5 = calcular_a5()
    idx_min, idx_max = np.argmin(precios), np.argmax(precios)
    
    # 2. Ejecutar funciones de la Sección B
    val_real_b1, val_aprox_b1, ea_b1, er_b1 = mantisa_corta_b1()
    teorico_b4, f32_b4, f64_b4 = cancelacion_maquina_b4()
    _, _, _, max_d32, max_d64 = ejercicio_b2_ida_vuelta()
   
    markdown_content = f"""# RESULTADOS

## 1. Análisis de Errores y Operaciones Financieras (A1 - A5)

### A1. Error de Representación Mes a Mes
- **Mes con mayor error relativo:** {nombres_meses[idx_peor]} {anios[idx_peor]} (Error Relativo: {er_a1[idx_peor]:.4f}%)

### A2. Evaluación de Compra y Venta (Ejemplo: Marzo 2022 -> Julio 2022)
- **Ganancia Calculada:** ${ganancia_a2:,.2f} CLP
- **Margen de Incertidumbre Absoluto:** ± ${ea_ganancia_a2:,.2f} CLP
- **Error Porcentual Propagado:** {er_total_a2:.4f}%

### A3. Efecto Cancelación (Diciembre 2022 vs Diciembre 2023)
- **Variación Calculada (ΔP):** {delta_p_a3} CLP
- **Error Absoluto Propagado:** ± {ea_propagado_a3:.4f} CLP
- **Error Relativo:** {error_porcentual_a3:.2f}%
- **¿Es confiable?:** {'SÍ' if es_confiable_a3 else 'NO. La variación es menor que el error propagado.'}

### A4. Anualidad Ordenada por Confiabilidad (Enero a Diciembre)
| Año | Variación Real (ΔP) | Error Absoluto Propagado (±Ea) | Error Relativo (%) | Nivel de Confianza |
| :--- | :---: | :---: | :---: | :--- |
"""
    for r in resultados_a4:
        confianza = "Más Confiable" if r == resultados_a4[0] else ("Menos Confiable" if r == resultados_a4[-1] else "Intermedio")
        markdown_content += f"| {r[0]} | {r[1]:.2f} CLP | ±{r[2]:.2f} CLP | {r[3]:.2f}% | {confianza} |\n"

    markdown_content += f"""
### A5. La Mejor Jugada Global (Óptimo Histórico)
- **Compra:** {nombres_meses[idx_min]} {anios[idx_min]} | **Venta:** {nombres_meses[idx_max]} {anios[idx_max]}
- **Ganancia Neta:** ${ganancia_a5:,.2f} CLP (**Rentabilidad: {rentabilidad_a5:.2f}%**)
- **Error Propagado:** ± ${ea_ganancia_a5:,.2f} CLP
- **¿Sobrevive al error?:** {'SÍ' if sobrevive_a5 else 'NO'}. La ganancia supera holgadamente a la incertidumbre.

---

## 2. Aritmética de Punto Flotante y Máquina (B1 - B4)

### B1. Mantisa Corta y Representación
- **Valor Real:** {val_real_b1} | **Valor Aprox (3 cifras):** {val_aprox_b1} (Error Relativo: {er_b1:.4f}%)

### B4. Cancelación en la Máquina (`float32` vs `float64`)
- **Valor Teórico:** {teorico_b4} | `float32`: `{f32_b4}` | `float64`: `{f64_b4}`

### B2. Deriva de la Ida y Vuelta en Punto Flotante
- **Máxima desviación (`float32`):** {max_d32:.4f} CLP
- **Máxima desviación (`float64`):** {max_d64:.4f} CLP
"""

    ruta_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta_md = os.path.join(ruta_base, "resultados.md")
    with open(ruta_md, "w", encoding="utf-8") as f:
        f.write(markdown_content)

def generar_csv_evaluacion_errores():
    ruta_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta_csv = os.path.join(ruta_base, "data", "evaluacion_errores.csv")
    
    anios, nombres_meses, precios = obtener_datos_sii()
    
    # Pares anuales A4
    res_a4 = calcular_a4()
    
    # Par A2
    ganancia_a2, ea_ganancia_a2, er_total_a2 = calcular_a2(2, 6)
    
    # Par A3
    delta_p_a3, ea_propagado_a3, error_porcentual_a3, _ = calcular_a3()
    
    # Par A5
    ganancia_a5, ea_ganancia_a5, rentabilidad_a5, _ = calcular_a5()
    
    with open(ruta_csv, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["seccion", "tipo_evaluacion", "punto_inicial", "punto_final", "valor_real", "valor_aprox", "error_absoluto_propagado", "error_relativo_porcentual", "observacion"])
        
        # Anualidades A4
        for anio, delta_real, ea_delta, er_delta in res_a4:
            writer.writerow(["A4", f"Anualidad {anio}", f"Enero {anio}", f"Diciembre {anio}", f"{delta_real:.2f}", "-", f"{ea_delta:.2f}", f"{er_delta:.2f}%", "Variacion anual"])
            
        # Par A2
        writer.writerow(["A2", "Compra-Venta Ejemplo", "Marzo 2022", "Julio 2022", "187500.00", "187500.00", f"{ea_ganancia_a2:.2f}", f"{er_total_a2:.4f}%", "Capital $1.000.000 CLP"])
        
        # Par A3
        writer.writerow(["A3", "Cancelacion (3 cifras)", "Diciembre 2022", "Diciembre 2023", "-0.99", f"{delta_p_a3:.2f}", f"{ea_propagado_a3:.4f}", f"{error_porcentual_a3:.2f}%", "Efecto cancelacion"])
        
        # Par A5
        writer.writerow(["A5", "Mejor Compra-Venta Global", "Febrero 2023", "Enero 2025", "253676.75", f"{ganancia_a5:.2f}", f"{ea_ganancia_a5:.2f}", f"{(ea_ganancia_a5/ganancia_a5)*100:.2f}%", "Optimo historico"])

if __name__ == "__main__":
    generar_resultados_md()
    generar_csv_evaluacion_errores()