import numpy as np
from cargar_datos import obtener_datos_sii


def redondear_dos_cifras(precios):

    #con el logaritmo medimos un n que nos servira para saber en que orden de magnitud (potencia de 10) esta cada numero
    magnitud = np.floor(np.log10(precios))

    #luego creamos el factor que hara que se desplace la coma decimal

    factor = 10**(1 - magnitud)

    # Tomamos en cuenta solo las dos cifras significativas

    return np.round(precios * factor) / factor

def calcular_errores_a1():
    anios, nombres_meses, precios = obtener_datos_sii()
    
    precios_aprox = redondear_dos_cifras(precios)
    error_absoluto = np.abs(precios - precios_aprox)
    error_relativo = (error_absoluto / precios) * 100
    
    #guardamos el indice del peor error relativo
    indice_max_error = np.argmax(error_relativo)
    

    return precios_aprox, error_absoluto, error_relativo

def calcular_a2(idx_compra, idx_venta):
    anios, nombres_meses, precios = obtener_datos_sii()
    
    M = 1000000.0
    
    precios_aprox = redondear_dos_cifras(precios)
    
    p_compra_real = precios[idx_compra]
    p_compra_aprox = precios_aprox[idx_compra]
    
    p_venta_real = precios[idx_venta]
    p_venta_aprox = precios_aprox[idx_venta]
    
    #errores relativos de representacion
    er_compra =(abs(p_compra_real - p_compra_aprox) /  p_compra_real) * 100
    er_venta = (abs(p_venta_real - p_venta_aprox) / p_venta_real) * 100
    
    # Operacion con valores aproximados, es decir como lo haria la maquina con dos cifras
    usd_comprados = M / p_compra_aprox
    pesos_final = usd_comprados * p_venta_aprox
    ganancia = pesos_final - M
    
    # propagacion de errores
    # multiplicacion y division los errores relativos se suman
    er_total_operacion = er_compra + er_venta
    
    # Convertir error relativo total a error absoluto en pesos para la ganancia
    ea_ganancia = (er_total_operacion / 100) * abs(pesos_final)
    
    return ganancia, ea_ganancia, er_total_operacion

def calcular_a3():
    anios, nombres_meses, precios = obtener_datos_sii()
    
    filtro_diciembre_2022 = (anios == 2022) & (nombres_meses == 'Diciembre')
    filtro_diciembre_2023 = (anios == 2023) & (nombres_meses == 'Diciembre')
    
    p22 = precios[filtro_diciembre_2022]
    p23 = precios[filtro_diciembre_2023]
    
    #funcion para el redondeo a 3 cifras 
    def redondear_3_cifras(val):
        mag = np.floor(np.log10(val))
        factor = 10**(2-mag)
        return np.round(val * factor) / factor
    
    p22_aprox = redondear_dos_cifras(p22)
    p23_aprox = redondear_dos_cifras(p23)
    
    
    #errores absolutos individuales
    ea22 = abs(p22 - p22_aprox)
    ea23 = abs(p23 - p23_aprox)
    
    #La variacion de valores aproximados
    delta_p = p23_aprox - p22_aprox
    
    #Propagacion de error en la resta
    ea_propagado = ea22 + ea23
    error_porcentual = (ea_propagado / abs(p23 - p22)) * 100
    # booleano que nos dice si realmente si la diferencia es mas grande que el margen de error
    es_confiable = abs(delta_p) > ea_propagado
    
    return delta_p, ea_propagado, error_porcentual, es_confiable

def calcular_a5():
    anios, nombres_meses, precios = obtener_datos_sii()
    M = 1000000.0
    
    precios_aprox = redondear_dos_cifras(precios)
    
    idx_min = np.argmin(precios)
    idx_max = np.argmax(precios)
    
    p_min_real = precios[idx_min]
    p_max_real = precios[idx_max]
    
    p_min_aprox = precios_aprox[idx_min]
    p_max_aprox = precios_aprox[idx_max]
    
    er_min = (abs(p_min_real - p_min_aprox) / p_min_real) * 100
    er_max = (abs(p_max_real - p_max_aprox) / p_max_real) * 100
    
    # Simulacion completa
    
    usd = M / p_min_real
    pesos_final =  usd * p_max_aprox
    ganancia = pesos_final - M
    rentabilidad = (ganancia / M) * 100
    
    er_total = er_min + er_max
    ea_ganancia = (er_total / 100) * abs(pesos_final)
    
    #La conclusion sobrevive al error?
    
    sobrevive = ganancia > ea_ganancia
    
    return ganancia, ea_ganancia, rentabilidad, sobrevive
    
        
if __name__ == "__main__":
    
    pass