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

if __name__ == "__main__":
    calcular_errores_a1()