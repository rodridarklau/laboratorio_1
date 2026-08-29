# RESULTADOS

## 1. Análisis de Errores y Operaciones Financieras (A1 - A5)

### A1. Error de Representación Mes a Mes
- **Mes con mayor error relativo:** Abril 2022 (Error Relativo: 0.5987%)

### A2. Evaluación de Compra y Venta (Ejemplo: Marzo 2022 -> Julio 2022)
- **Ganancia Calculada:** $187,500.00 CLP
- **Margen de Incertidumbre Absoluto:** ± $5,823.02 CLP
- **Error Porcentual Propagado:** 0.4904%

### A3. Efecto Cancelación (Diciembre 2022 vs Diciembre 2023)
- **Variación Calculada (ΔP):** -1.0 CLP
- **Error Absoluto Propagado:** ± 0.6700 CLP
- **Error Relativo:** 67.68%
- **¿Es confiable?:** SÍ

### A4. Anualidad Ordenada por Confiabilidad (Enero a Diciembre)
| Año | Variación Real (ΔP) | Error Absoluto Propagado (±Ea) | Error Relativo (%) | Nivel de Confianza |
| :--- | :---: | :---: | :---: | :--- |
| 2025 | -84.60 CLP | ±4.60 CLP | 5.44% | Más Confiable |
| 2024 | 74.31 CLP | ±4.31 CLP | 5.80% | Intermedio |
| 2022 | 53.61 CLP | ±6.39 CLP | 11.92% | Intermedio |
| 2023 | 48.33 CLP | ±8.33 CLP | 17.24% | Menos Confiable |

### A5. La Mejor Jugada Global (Óptimo Histórico)
- **Compra:** Febrero 2023 | **Venta:** Enero 2025
- **Ganancia Neta:** $252,724.68 CLP (**Rentabilidad: 25.27%**)
- **Error Propagado:** ± $3,681.96 CLP
- **¿Sobrevive al error?:** SÍ. La ganancia supera holgadamente a la incertidumbre.

---

## 2. Aritmética de Punto Flotante y Máquina (B1 - B4)

### B1. Mantisa Corta y Representación
- **Valor Real:** 1000.76 | **Valor Aprox (3 cifras):** 1000.0 (Error Relativo: 0.0759%)

### B4. Cancelación en la Máquina (`float32` vs `float64`)
- **Valor Teórico:** -0.9900000000000091 | `float32`: `-0.989990234375` | `float64`: `-0.9900000000000091`

### B2. Deriva de la Ida y Vuelta en Punto Flotante
- **Máxima desviación (`float32`):** 0.0625 CLP
- **Máxima desviación (`float64`):** 0.0000 CLP
