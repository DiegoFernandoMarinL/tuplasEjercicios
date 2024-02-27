productos = tuple((
    "Coca-Cola", 
    "Pepsi", 
    "Sprite", 
    "Fanta", 
    "7UP", 
    "Mountain Dew", 
    "Dr Pepper", 
    "Schweppes", 
    "Mirinda", 
    "Lift"))
precios = tuple((
    4500, 
    3750, 
    3000, 
    3600, 
    5250, 
    6000, 
    5400, 
    3900, 
    4200, 
    4800))

print("Menu de seleccion de productos")

for i, val in enumerate(productos):
    print(f"""   {i}. {val} ${precios[i]} """)

a = "1"
valTotal = 0
while a == "1":
    opcion = int(input())
    print(f"Usuario usted selecciono el producto {productos[opcion]} con un valor de ${precios[opcion]}")
    valTotal = valTotal + precios[i]
    a = input("Desea seleccionar otro producto o finallizar la compra: Seleccionar=1 --- Finalizar=0")

dinero = int(input("Ingrese la cantidad de dinero disponible: "))
vueltos = dinero - valTotal

if dinero >= precios[opcion]:
    print(f"Usuario usted compro el producto {productos[opcion]} con un valor de ${precios[opcion]}, sus vueltos son ${vueltos}")
else:
    print(f"Usuario el producto que desea comprar {productos[opcion]} con un valor de ${precios[opcion]}, le falta un total de ${-vueltos} ")    