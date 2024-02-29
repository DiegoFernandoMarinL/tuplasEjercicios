panaderia = {
    'Panes_salados': {
        "productos":list([
            {"nombre":"Baguette","valor":3000,"cod":"01"},
            {"nombre":"Pan de campo","valor":2500,"cod":"02"},
            {"nombre":"Pan de centeno","valor":3500,"cod":"03"},
            {"nombre":"Pan de ajo","valor":1000,"cod":"04"},
            {"nombre":"Pan de molde integral","valor":3000,"cod":"05"},
            {"nombre":"Pan de queso","valor":1500,"cod":"06"},
            {"nombre":"Pan de aceitunas","valor":3000,"cod":"07"},
            {"nombre":"Bollos de pizza","valor":3500,"cod":"08"},
            {"nombre":"Pan de cebolla","valor":2000,"cod":"09"},
            {"nombre":"Pan de maíz","valor":2000,"cod":"010"}]),
        "promociones":list([
            {"indice": 0, "nombre": "Descuento del 7% en la compra de 7", "unidades": 7, "descuento":0.07},
            {"indice": 0, "nombre": "Descuento del 10% en la compra de 10", "unidades": 10, "descuento":0.10},
            {"indice": 5, "nombre": "Descuento del 2% en la compra de 3", "unidades": 3, "descuento":0.02}])},   
    'Panes_dulces': {
        "productos":list([
            {"nombre":"Croissant","valor":3000,"cod":"11"},
            {"nombre":"Rosca de Reyes","valor":4000,"cod":"12"},
            {"nombre":"Pan de muerto","valor":1500,"cod":"13"},
            {"nombre":"Pan de canela","valor":1700,"cod":"14"},
            {"nombre":"Pan de banana","valor":2300,"cod":"15"},
            {"nombre":"Pan de zanahoria","valor":3000,"cod":"16"},
            {"nombre":"Donas","valor":2100,"cod":"17"},
            {"nombre":"Pan de jengibre","valor":1900,"cod":"18"},
            {"nombre":"Conchas","valor":2000,"cod":"19"},
            {"nombre":"Churros","valor":1000,"cod":"110"}]),
        "promociones":list([
            {"indice": 1, "nombre": "Descuento del 7% en la compra de 7", "unidades": 7, "descuento":0.07},
            {"indice": 6, "nombre": "Descuento del 10% en la compra de 10", "unidades": 10, "descuento":0.10},
            {"indice": 6, "nombre": "Descuento del 2% en la compra de 3", "unidades": 3, "descuento":0.02}])},
    'Reposteria': {
        "productos":list([
            {"nombre":"Tarta de manzana","valor":3000,"cod":"21"},
            {"nombre":"Cupcakes","valor":3000,"cod":"22"},
            {"nombre":"Galletas decoradas","valor":3000,"cod":"23"},
            {"nombre":"Pastel de zanahoria","valor":3000,"cod":"24"},
            {"nombre":"Brownies","valor":3000,"cod":"25"},
            {"nombre":"Cheesecake","valor":3000,"cod":"26"},
            {"nombre":"Macarons","valor":3000,"cod":"27"},
            {"nombre":"Éclairs","valor":3000,"cod":"28"},
            {"nombre":"Tarta de frutas","valor":3000,"cod":"29"},
            {"nombre":"Donas","valor":3000,"cod":"210"}]),
        "promociones":list([
            {"indice": 2, "nombre": "Descuento del 7% en la compra de 7", "unidades": 7, "descuento":0.07},
            {"indice": 7, "nombre": "Descuento del 10% en la compra de 10", "unidades": 10, "descuento":0.10},
            {"indice": 8, "nombre": "Descuento del 2% en la compra de 3", "unidades": 3, "descuento":0.02}])}
}
carrito = 0
x = "1"
while x == "1":
    print("-------PANADERIA PYTHON-------.")

    listaCategoria = panaderia.keys()
    listaCategoria = list(listaCategoria)
    for i, val in enumerate(listaCategoria):
        print(f"{i}. {val}")

    op = int(input("Seleccione categoria a comprar: "))
    categoria = panaderia.get(listaCategoria[op])
    producto = categoria["productos"]

    for i, val in enumerate(producto):
        print(f"{i}. {val}")

    op2 = int(input("Seleccione producto a comprar: "))

    categoria = panaderia.get(listaCategoria[op])
    promociones = categoria["promociones"]
    promocion = list()
    for val in promociones:
        if (val.get("indice") == op2):
            promocion.append(val)

    if (len(promocion) != 0):
        print(f""" Promociones del producto {categoria["productos"][op2]}""")
        for i, val in enumerate(promocion):
            print(f"{i}. {val}")

        op3 = int(input("Seleccione promocion que desea (NOTA: 9 para no aplicar ninguna promocion): "))
        if (op3 != 9):
            promo = categoria["promociones"][op3]
            descuento = promo["descuento"]
            unidades = promo["unidades"]

            producto = categoria["productos"][op2]
            descuento = producto["valor"] * unidades * descuento 
            valTotal = producto["valor"] * unidades - descuento
            print(f"El valor a cancelar es de: ${valTotal}")
        else:
            valTotal = categoria["productos"][op2]
            producto = valTotal["nombre"]
            valTotal = valTotal["valor"]
            cantidad = int(input(f"Cuanta cantidad del producto {producto} desea comprar: "))
            valTotal = valTotal * cantidad
            print(f"El valor a cancelar es de: ${valTotal}")      
    else:
        valTotal = categoria["productos"][op2]
        producto = valTotal["nombre"]
        valTotal = valTotal["valor"]  
        cantidad = int(input(f"Cuanta cantidad del producto {producto} desea comprar: "))
        valTotal = valTotal * cantidad
        print(f"El valor a cancelar es de: ${valTotal}") 
    
    carrito = carrito + valTotal
    x = input(f"Desea escojer otro producto (Si=1 No=0) Carrito:{carrito}: ")

b = 1
while b == 1:
    pago = int(input("Ingrese dinero para el pago: $"))
    if (pago >= carrito):
        vueltos = pago - carrito
        print(f"Sus vueltos son: {vueltos}")
        b = 0
    else:
        print(f"El dinero ingresado no alcanza para el pago: Carrito:{carrito}  Pago:{pago}") 
        b = 1  