
productos={"8475HD": ["HP", 15.6, "8 GB", "DD", "1 TB", "Intel Core i5", "Nvidia GTX 1050"],
           "2175HD": ["Lenovo", 14, "4 GB", "SSD", "512 GB", "Intel Core i5", "Nvidia GTX 1050"],
           "JjfFHD": ["Asus", 14, "16 GB", "SSD", "256 GB", "Intel Core i7", "Nvidia RTX 2080 Ti"],
           "fgdxFHD": ["HP", 15.6, "8 GB", "DD", "1 TB", "Intel Core i3", "Integrada"],
           "GF75HD": ["Asus", 15.6, "8 GB", "DD", "1 TB", "Intel Core i7", "Nvidia GTX 1050"],
           "123FHD": ["Lenovo", 14, "6 GB", "DD", "1 TB", "AMD Ryzen 5", "Integrada"],
           "342FHD": ["Lenovo", 15.6, "8 GB", "DD", "1 TB", "AMD Ryzen 7", "Nvidia GTX 1050"],
           "UWU131HD": ["Dell", 15.6, "8 GB", "DD", "1 TB", "AMD Ryzen 3", "Nvidia GTX 1050"]
           }

stock={"8475HD": [387990, 10], "2175HD": [327990, 4], "JjfFHD": [424990, 1],
       "fgdxFHD": [664990, 21], "GF75HD": [749990, 2], "123FHD": [290890, 32],
       "342FHD": [444990, 7], "UWU131HD": [349990, 1]
       }

def menu():
    print("***MENU PRINCIPAL***")
    print("1. Stock Marca")
    print("2. Búsqueda por precio")
    print("3. Actualizar precio")
    print("4. Salir")
    
def stock_marca(marca):
    total=0
    listas=[]
    marca=input("Ingrese la marca a consultar: ").lower()
    for productos_modelo, listas in productos.items():
        if listas[0].lower() == marca.lower():
            total += stock[productos_modelo][1]
            print(f"El stock es {total}")
            
def búsqueda_precio(p_min, p_max):
    while(True):
        try:
            precio=0
            resultado=[]
            p_min=int(input("Ingrese el precio mínimo: "))
            p_max=int(input("Ingrese el precio máximo: "))
            for productos_modelo, listas in productos.items():
                if p_min <= precio <= p_max and stock > 0:
                    resultado.append(f"{listas[0]}--{productos_modelo}")
            if resultado:
                resultado.sort()
                print(f"Los notebooks entre los precios consultados son: {resultado}")
                break
            else:
                print("No hay notebooks en ese rango de precio")
        except ValueError:
            print("Debe ingresar valores enteros")
            
def actualizar_precio(modelo, p):
    while(True):
        try:    
            modelo=input("Ingrese modelo a actualizar: ")
            p=int(input("Ingrese el nuevo precio: "))
            if modelo == productos:
                for producto_modelo in stock:
                    print("Precio actualizado")
                    return True
            else:
                print("El modelo no existe")
                return False
            actualizar=input("¿Desea actualizar a otro precio? (si/no): ").lower
            if actualizar != "si":
                break
        except ValueError:
            print("Debe ingresar valores enteros")