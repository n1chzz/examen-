productos={
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['Lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'TjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'Integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['Lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'Integrada'],
    '342FHD': ['Lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}
stock={
    '8475HD': [387990, 10],
    '2175HD': [327990, 41],
    'TjfFHD': [424990, 11],
    'fgdxFHD': [664990, 0],
    'GF75HD': [749990, 2],
    '123FHD': [290890, 321],
    '342FHD': [444990, 71],
    'UWU131HD': [349990, 11],
}
def stock_marca(marca):
    marca=marca.lower()
    total=0
    for modelo, datos in productos.items():
        if datos[0].lower()==marca:
            total+=stock.get(modelo, [0, 0])[1]
    print(f"El stock es: {total}")

def busqueda_precio(p_min, p_max):
    resultados=[]
    for modelo, datos_stock in stock.items():
        precio, cantidad = datos_stock
        if p_min<=precio<=p_max and cantidad>0:
            marca = productos[modelo][0]
            resultados.append(f"{marca}--{modelo}")
    if resultados:
        print("Los notebooks entre los precios consultados son:")
        print(sorted(resultados))
    else:
        print("No hay notebooks en ese rango de precios.")
def actualizar_precio(modelo, nuevo_precio):
    if modelo in stock:
        stock[modelo][0] = nuevo_precio
        return True
    else:
        return False
