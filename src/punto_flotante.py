import numpy as np
from cargar_datos import obtener_datos_sii


def mantisa_corta_b1():
    valor_real = 1000.76  # valor real del dataset
    valor_aprox_3cifras = 1000.0  # queda asi porque solo se usan 3 cifras significativas, truncando la mantisa, seria 1.00 x 10**3
    ea = abs(valor_real - valor_aprox_3cifras)  # calculo del error absoluto
    er = (ea / valor_real) * 100  # calculo del error relativo porcentual

    
    return valor_real, valor_aprox_3cifras, ea, er


def cancelacion_maquina_b4():
    p_dic2023 = 874.67  # numeros casi identicos
    p_dic2022 = 875.66
    valor_teorico = p_dic2023 - p_dic2022  # = -0.99

    # Este bloque combierte ambos numeros al estandar IEEE 754 de precision simple
    f32_dic2023 = np.float32(p_dic2023)
    f32_dic2022 = np.float32(p_dic2022)
    resta_f32 = f32_dic2023 - f32_dic2022

    # Este bloque combierte ambos numeros al estandar IEEE 754 de precision doble
    f64_dic2023 = np.float64(p_dic2023)
    f64_dic2022 = np.float64(p_dic2022)
    resta_f64 = f64_dic2023 - f64_dic2022

  
    return valor_teorico, float(resta_f32), float(resta_f64)


def ejercicio_b2_ida_vuelta():
    # Obtener los datos del dataset
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
    max_deriva_32 = float(np.max(np.abs(deriva_f32)))
    max_deriva_64 = float(np.max(np.abs(deriva_f64)))

    
    return precios, deriva_f32, deriva_f64, max_deriva_32, max_deriva_64


if __name__ == "__main__":
    pass