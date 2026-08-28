import numpy as np
from cargar_datos import obtener_datos_sii
from errores import redondear_dos_cifras

def calcular_a4():
    anios, nombres_meses, precios = obtener_datos_sii()
    anios_unicos = np.unique(anios)
    
    resultados = []
    for y in anios_unicos:
        p_enero = precios[(anios == y) & (nombres_meses == 'Enero')]
        p_diciembre = precios[(anios == y) & (nombres_meses == 'Diciembre')]
        
        p_enero_aprox = redondear_dos_cifras(p_enero)
        p_diciembre_aprox = redondear_dos_cifras(p_diciembre)
        
        ea_enero = abs(p_enero - p_enero_aprox)
        ea_diciembre = abs(p_diciembre - p_diciembre_aprox)
        
        delta_real = p_diciembre - p_enero
        ea_delta = ea_enero + ea_diciembre
        
        er_delta = (ea_delta / abs(delta_real)) * 100
        
        resultados.append((y, delta_real, ea_delta, er_delta))
    
    resultados_ordenados = sorted(resultados, key=lambda x: x[3])
    # retornamos los siguiente (el año, variacion real, error absoluto propagado, error relativo procentual)
    return resultados_ordenados

if __name__ == '__main__':
    pass