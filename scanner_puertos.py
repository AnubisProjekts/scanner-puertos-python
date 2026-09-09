import socket

print("=" * 45)
print("        ESCÁNER DE PUERTOS TCP")
print("=" * 45)

# Ingreso de dirección IP
ip = input("Ingrese la dirección IP: ").strip()

# Validar dirección IP
try:
    socket.inet_aton(ip)
except socket.error:
    print("\nError: La dirección IP ingresada no es válida.")
    exit()

# Ingreso de puertos
try:
    puerto_inicial = int(input("Ingrese el puerto inicial: "))
    puerto_final = int(input("Ingrese el puerto final: "))
except ValueError:
    print("\nError: Los puertos deben ser números enteros.")
    exit()

# Validar rango de puertos
if puerto_inicial < 1 or puerto_final > 65535:
    print("\nError: Los puertos deben estar entre 1 y 65535.")
    exit()

if puerto_inicial > puerto_final:
    print("\nError: El puerto inicial no puede ser mayor que el puerto final.")
    exit()

puertos_abiertos = []

print("\nEscaneando...\n")

for puerto in range(puerto_inicial, puerto_final + 1):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.5)

        resultado = sock.connect_ex((ip, puerto))

        if resultado == 0:
            print(f"Puerto {puerto} - ABIERTO")
            puertos_abiertos.append(puerto)

total_puertos = puerto_final - puerto_inicial + 1

print("\n" + "=" * 45)
print("               RESUMEN")
print("=" * 45)

print(f"IP analizada: {ip}")
print(f"Rango analizado: {puerto_inicial} - {puerto_final}")
print(f"Puertos analizados: {total_puertos}")
print(f"Puertos abiertos: {len(puertos_abiertos)}")

if puertos_abiertos:
    print(f"Lista de puertos abiertos: {puertos_abiertos}")
else:
    print("No se encontraron puertos abiertos.")

print("=" * 45)