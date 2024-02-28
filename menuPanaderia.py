panaderia = {
    'panes_salados': {"productos":list([
        {"nombre":"Baguette","valor":3000,"cod":"01"},
        {"nombre":"Pan de campo","valor":2500,"cod":"02"},
        {"nombre":"Pan de centeno","valor":3500,"cod":"03"},
        {"nombre":"Pan de ajo","valor":1000,"cod":"04"},
        {"nombre":"Pan de molde integral","valor":3000,"cod":"05"},
        {"nombre":"Pan de queso","valor":1500,"cod":"06"},
        {"nombre":"Pan de aceitunas","valor":3000,"cod":"07"},
        {"nombre":"Bollos de pizza","valor":3500,"cod":"08"},
        {"nombre":"Pan de cebolla","valor":2000,"cod":"09"},
        {"nombre":"Pan de maíz","valor":2000,"cod":"010"}])},
    'panes_dulces': {"productos":list([
        {"nombre":"Croissant","valor":3000,"cod":"11"},
        {"nombre":"Rosca de Reyes","valor":2500,"cod":"12"},
        {"nombre":"Pan de muerto","valor":1500,"cod":"13"},
        {"nombre":"Pan de canela","valor":1700,"cod":"14"},
        {"nombre":"Pan de banana","valor":2300,"cod":"15"},
        {"nombre":"Pan de zanahoria","valor":3000,"cod":"16"},
        {"nombre":"Donas","valor":2100,"cod":"17"},
        {"nombre":"Pan de jengibre","valor":1900,"cod":"18"},
        {"nombre":"Conchas","valor":2000,"cod":"19"},
        {"nombre":"Churros","valor":1000,"cod":"110"}])},
    'reposteria': {"productos":list([
        {"nombre":"Tarta de manzana","valor":3000,"cod":"21"},
        {"nombre":"Cupcakes","valor":3000,"cod":"22"},
        {"nombre":"Galletas decoradas","valor":3000,"cod":"23"},
        {"nombre":"Pastel de zanahoria","valor":3000,"cod":"24"},
        {"nombre":"Brownies","valor":3000,"cod":"25"},
        {"nombre":"Cheesecake","valor":3000,"cod":"26"},
        {"nombre":"Macarons","valor":3000,"cod":"27"},
        {"nombre":"Éclairs","valor":3000,"cod":"28"},
        {"nombre":"Tarta de frutas","valor":3000,"cod":"29"},
        {"nombre":"Donas","valor":3000,"cod":"210"}])}
}

print("-------PANADERIA PYTHON-------.")
i = 0
for categoria, producto in panaderia.items():
    i = i + 1
    print(f"   {i}. {categoria}")

op = int(input("Digite categoria a comprar: "))
if op == 1:
    categoria = "panes_salados"
    print(f"""Haz seleccionado la categoria: {categoria}""")
elif op == 2:
    categoria = "panes_dulces"
    print(f"""Haz seleccionado la categoria: {categoria}""")
elif op == 3:
    categoria = "reposteria"   
    print(f"""Haz seleccionado la categoria: {categoria}""")  

producto = int(input("Digite producto a comprar: "))
pedido = panaderia[categoria]["productos"][producto]
nombre = pedido["nombre"]
valor = pedido["valor"]
cod = pedido["cod"]


print(f"El producto seleccionado es: {nombre} con un valor de ${valor}")
