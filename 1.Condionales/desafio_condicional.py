CARGO_FIJO = 7000
COSTO_METRO = 200
IVA = 0.21

print("TIPOS DE CLIENTE:")
print("1 - Residencial")
print("2 - Comercial")
print("3 - Industrial")

cliente = int(input("Ingrese el tipo de cliente: "))
consumo = float(input("Ingrese la cantidad de m³ consumidos: "))

bonificacion = 0
recargo = 0
descuento = 0

costo_consumo = consumo * COSTO_METRO
subtotal_consumo = costo_consumo + CARGO_FIJO


match cliente:
    # RESIDENCIAL
    case 1:
        match consumo:
            case consumo if consumo < 30:
                bonificacion = costo_consumo * 0.1
            case consumo if consumo > 80:
                recargo = costo_consumo * 0.15

        match subtotal_consumo:
            case subtotal_consumo if subtotal_consumo < 35000:
                descuento = subtotal_consumo * 0.5

    # COMERCIAL
    case 2:
        match consumo:
            case consumo if consumo > 300:
                bonificacion = costo_consumo * 0.12
            case consumo if consumo > 150:
                bonificacion = costo_consumo * 0.08
            case consumo if consumo < 50:
                recargo = costo_consumo * 0.05

    # INDUSTRIAL
    case 3:
        match consumo:
            case consumo if consumo > 1000:
                bonificacion = costo_consumo * 0.3
            case consumo if consumo > 500:
                bonificacion = costo_consumo * 0.2
            case consumo if consumo < 200:
                recargo = costo_consumo * 0.1

subtotal = subtotal_consumo + recargo - bonificacion - descuento
monto_iva = subtotal * IVA
total = subtotal + monto_iva   

print("Total Facturado:")
print(f"Consumo: ${costo_consumo}")
print(f"Subtotal consumi: ${subtotal_consumo}")

print(f"Bonificacion: ${bonificacion}")
print(f"Recargo: ${recargo}")
print(f"Descuento: ${descuento}")

print(f"Subtotal: ${subtotal}")
print(f"IVA: ${monto_iva}")
print(f"TOTAL: ${total}")