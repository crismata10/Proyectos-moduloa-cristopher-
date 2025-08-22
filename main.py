# Proyecto: [Nombre del Proyecto]
# Estudiante: [Nombre del Estudiante]
# Fecha de Inicio: [dd/mm/aaaa]
# Fecha de Entrega: [dd/mm/aaaa]
# Descripción: Este archivo contiene el punto de entrada principal del proyecto.
# Recuerda incluir tu nombre completo, la fecha en la que iniciaste el proyecto y la fecha estimada de entrega.
# Esto ayuda a mantener un registro claro del trabajo realizado.
from analisis_datos.carga_datos import generar_lista_compras
from analisis_datos.estadisticas import media

def saludar():
    print("hola desde la funcion")

       
if __name__=="__main__":
    compras = generar_lista_compras()
    print(compras)
    media = media(list(compras.values()))
    print("promedio de costo por articulo:",media)
    
        
    # mediana = mediana(list(compras.values()))
     #print("mediana de costo por articulo: ",mediana)
     