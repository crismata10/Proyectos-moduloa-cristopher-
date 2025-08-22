# estadisticas.py
def media(datos):
    media_arimetica = sum(datos) / len(datos)
    return media_arimetica

def mediana(datos):
    #mediana
    #paso #1 ordenar
    datos= sorted(datos)
    n = len(datos)
    mitad = n // 2
    if n % 2 == 0:
        mediana((datos[mitad -1]+ datos[mitad])/2)
    else:
        mediana = datos[mitad]
    return mediana

if __name__=="__main__":
    notas = [100,50,100,78,100]
    print(mediana(notas)) 