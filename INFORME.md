# INFORME: ANÁLISIS DE ERROR Y CANCELACIÓN EN EL DÓLAR OBSERVADO (2022-2025)

## Conclusiones y Recomendaciones Financieras

### 1. ¿Cuándo conviene comprar?

* **Mes más barato (Mínimo histórico):** Febrero de 2023 con un valor real de $798.26 CLP (aproximado a 2 cifras significativas como $800.0 CLP, con un error absoluto individual de $1.74 CLP).
* **Análisis de confianza frente a meses vecinos:**
  * **Respecto a Enero 2023 ($826.34 CLP):** La diferencia real es de $28.08 CLP, superando ampliamente el error absoluto propagado ($5.40 CLP).
  * **Respecto a Marzo 2023 ($809.50 CLP):** La diferencia real es de $11.24 CLP, superando también con claridad el error propagado ($2.24 CLP).
* **Matiz de confianza global:**
  Frente a sus vecinos temporales inmediatos, el mínimo de Febrero 2023 es completamente seguro. No obstante, al comparar con Marzo de 2022 ($799.19 CLP), la diferencia real es de apenas $0.93 CLP, mientras que la incertidumbre propagada entre ambos es de $2.55 CLP. Por lo tanto, numéricamente cae dentro del intervalo de incertidumbre, compartiendo la condición de "zona óptima de compra" con Marzo de 2022.

---

### 2. ¿Cuándo conviene vender?

* **Mes más caro (Máximo histórico):** Enero de 2025 con un valor real de $1000.76 CLP (aproximado a 2 cifras como $1000.0 CLP, con un error absoluto de $0.76 CLP).
* **Análisis de confianza:**
  * **Respecto a Diciembre 2024 ($982.30 CLP):** La diferencia real es de $18.46 CLP, superando sólidamente el error propagado de $3.06 CLP.
  * **Respecto a Febrero 2025 ($956.62 CLP):** La diferencia real es de $44.14 CLP, muy superior al error propagado de $4.14 CLP.
* **Conclusión de confianza:** El máximo de Enero de 2025 es un pico estadísticamente sólido e indiscutible, ya que la variación cambiaria real supera por más de 6 veces la incertidumbre del redondeo.

---

### 3. La mejor jugada completa

* **Estrategia óptima:** Comprar en Febrero de 2023 ($800.0 CLP aprox.) y vender en Enero de 2025 ($1000.0 CLP aprox.) con un capital inicial de $1.000.000 CLP.
* **Resultados numéricos:**
  * **Capital final estimado:** $1.250.000,00 CLP.
  * **Ganancia neta estimada:** $250.000,00 CLP (Ganancia real exacta: $253.676,75 CLP).
  * **Rentabilidad estimada:** 25.00% (Rentabilidad real: 25.37%).
  * **Error relativo en operaciones (compra + venta):** 0.22% + 0.08% = 0.29%.
  * **Margen de incertidumbre absoluto en pesos:** ± $3.673,95 CLP.
  * **Error relativo sobre la ganancia:** 1.47% (± $3.673,95 / $250.000,00).
* **¿Es una recomendación sólida?:**
  **Sí, es extremadamente sólida.** La ganancia neta supera al margen de error por más de 68 veces ($250.000,00 CLP frente a ± $3.673,95 CLP), demostrando que la rentabilidad sobrevive holgadamente a la propagación del error numérico.

---

### 4. Los tramos donde NO se puede recomendar operar

Existen periodos donde la variación real del precio es menor o comparable al error propagado del redondeo, provocando un efecto de cancelación donde cualquier conclusión carece de validez:

1. **Diciembre 2022 vs Diciembre 2023 (Ejercicio A3):**
   * **Precios reales:** Diciembre 2022 ($875.66 CLP) vs Diciembre 2023 ($874.67 CLP). Variación real: -0.99 CLP.
   * **Con 3 cifras significativas (enunciado A3):** Redondeados a $876.0 CLP y $875.0 CLP. $\Delta P = -1.00 \pm 0.67$ CLP (Error relativo: 67.68%). La incertidumbre consume más de dos tercios del cambio.
   * **Con 2 cifras significativas:** Redondeados a $880.0 CLP y $870.0 CLP. $\Delta P = -10.0 \pm 9.01$ CLP. El error propagado casi iguala a la diferencia estimada, tornando el análisis altamente impreciso.
2. **Mayo 2023 a Junio 2023:**
   * **Precios reales:** $798.64 CLP a $799.87 CLP ($\Delta P = +1.23$ CLP).
   * **Incertidumbre propagada:** ± $1.49 CLP. El error supera a la variación real, por lo que no es posible asegurar si el precio realmente subió o bajó.
3. **Febrero 2024 a Marzo 2024:**
   * **Precios reales:** $963.44 CLP a $967.93 CLP ($\Delta P = +4.49$ CLP).
   * **Incertidumbre propagada:** ± $5.51 CLP. La diferencia queda completamente absorbida por el error de representación.

---

### 5. La lección de método

> "Restar dos números grandes y muy cercanos entre sí amplifica drásticamente el error relativo (cancelación catastrófica), por lo que una diferencia calculada solo es confiable si su magnitud es estrictamente mayor que la suma de los errores absolutos de los datos originales."