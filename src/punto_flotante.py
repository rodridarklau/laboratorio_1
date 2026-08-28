import numpy as np

def ejercicio_b1():
    
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

if __name__ == "__main__":
    ejercicio_b1()