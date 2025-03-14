custos = [1000, 500 ,700 , 300]
ganho = [4500, 950]

def somatorio(lista):
    contador= 0
    soma= 0
    while (contador < len(lista)):
        soma= soma+ lista[contador]
        contador= contador+1 
    return soma 

somacusto = somatorio(custos)
somaganho = somatorio(ganho)

print ("O custos foi de:", somacusto)
print ("O ganho foi de: ", somaganho)
print ("O Saldo foi de: ", somaganho - somacusto)

/// Custo: 2500 ///
/// Ganho: 5450 ///
/// Saldo: 2950 ///
