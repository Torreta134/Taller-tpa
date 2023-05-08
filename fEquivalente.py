from ingreso_datos import Divisa   

# vDivisa = float
#eqA1USD = float
# vEquivalente: float float -> float

def vEquivalente_eur(vDivisa):
    eqA1USD = 0.90567
    return vDivisa / eqA1USD
print(f"El valor equivalente de euro/s a dólar/es americano/s, es {vEquivalente_eur()}")

def vEquivalente_lib(vDivisa):
    eqA1USD = 0.79043
    return vDivisa / eqA1USD
print(f"El valor equivalente de libra/s esterlina/s a dólar/es americano/s, es {vEquivalente_lib()}")

