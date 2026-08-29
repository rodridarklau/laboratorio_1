# orquestador.py
import numpy as np
from cargar_datos import obtener_datos_sii
from anualidad import calcular_a4
from errores import calcular_errores_a1, calcular_a2, calcular_a3, calcular_a5
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
   
