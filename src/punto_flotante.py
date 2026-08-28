import numpy as np
import os
import matplotlib.pyplot as plt
from cargar_datos import obtener_datos_sii

def mantisa_corta_b1():
    
    print("B1: Cifras significativas y mantisa corta")
    valor_real = 1000.76 #valor real del dataset
    valor_aprox_3cifras = 1000.0 #queda asi porque solo se usan 3 cifras significativas, truncando la mantisa, seria 1.00 x 10**3
    ea = abs(valor_real - valor_aprox_3cifras) # calculo del error absoluto
    er = (ea / valor_real) * 100 # calculo del error relativo porcentual
    
    print(f"Valor real (Enero 2025)   : {valor_real} CLP")
    print(f"Aproximación a 3 cifras   : {valor_aprox_3cifras} CLP")
    print(f"Error absoluto (Ea)       : {ea:.4f} CLP")
    print(f"Error relativo (Er)       : {er:.4f} %")
    print("\nExplicación:")
    print("Guardar con 2 o 3 cifras significativas equivale a truncar la mantisa")
    print("en el estándar IEEE 754 de punto flotante, descartando los bits de menor")
    print("peso y generando un error de representación intrínseco.")

def cancelacion_maquina_b4():
  
   
    print("B4: Cancelación en la máquina")
    

    p_dic2023 = 874.67 #numeros casi identicos
    p_dic2022 = 875.66
    valor_teorico = p_dic2023 - p_dic2022  # = -0.99

        #Este bloque combierte ambos numeros al estandar IEEE 754 de precision simple
    f32_dic2023 = np.float32(p_dic2023) 
    f32_dic2022 = np.float32(p_dic2022)
    resta_f32 = f32_dic2023 - f32_dic2022

        #Este bloque combierte ambos numeros al estandar IEEE 754 de precision doble
    f64_dic2023 = np.float64(p_dic2023)
    f64_dic2022 = np.float64(p_dic2022) 
    resta_f64 = f64_dic2023 - f64_dic2022
    print(f"Diferencia teórica exacta : {valor_teorico:.6f}")
    print(f"Resta en float32          : {resta_f32:.8f}")
    print(f"Resta en float64          : {resta_f64:.16f}")

def ejercicio_b2_ida_vuelta():
    print("B2: La ida y vuelta que no vuelve (float32 vs float64)")
    
    #Obtener los datos del dataset
    anios, nombres_meses, precios = obtener_datos_sii()
    M = 1000000.0  # $1.000.000 CLP de capital inicial

    # Simulación en presicion doble
    usd_f64 = M / precios
    clp_final_f64 = usd_f64 * precios
    deriva_f64 = clp_final_f64 - M

    # Simulación en presicion simple
    M_f32 = np.float32(M)
    precios_f32 = precios.astype(np.float32)
    usd_f32 = M_f32 / precios_f32
    clp_final_f32 = usd_f32 * precios_f32
    deriva_f32 = clp_final_f32 - M_f32

    # Maxima perdida o ganacia en ambos formatos
    max_deriva_32 = np.max(np.abs(deriva_f32))
    max_deriva_64 = np.max(np.abs(deriva_f64))
    print(f"Máxima deriva en float32 : {max_deriva_32:.6f} CLP")
    print(f"Máxima deriva en float64 : {max_deriva_64:.16e} CLP")

    return deriva_f32, deriva_f64
if __name__ == "__main__":
    mantisa_corta_b1()
    cancelacion_maquina_b4()
    ejercicio_b2_ida_vuelta()