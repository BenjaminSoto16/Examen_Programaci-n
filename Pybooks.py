
from Librería import menu, stock_marca, búsqueda_precio, actualizar_precio

marca=[]
p_min=0
p_max=0
modelo=[]
p=0

while(True):
    menu()
    try:
        op=int(input("Ingrese una opción: "))
        if op==1:
            stock_marca(marca)
        elif op==2:
            búsqueda_precio(p_min, p_max)
        elif op==3:
            actualizar_precio(modelo, p)
        elif op==4:
            print("Programa finalizado")
            break
        else:
            print("Debe seleccionar una opción válida")
    except ValueError:
        print("Debe ingresar un valor entero")
