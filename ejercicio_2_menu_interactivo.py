ejecutando = True

while ejecutando:
    print("\n--- MENÚ DE CONTROL DE ROBOT ---")
    print("A. Mover a la derecha")
    print("B. Mover a la izquierda")
    print("C. Mover hacia el frente")
    print("D. Mover hacia atrás")
    print("E. Apagar")

    comando = input("\nIngrese el código de comando (A, B, C, D o E): ").strip().upper()

    match comando:
        case "A":
            print("El robot se desplazó a la derecha")
        case "B":
            print("El robot se desplazó a la izquierda")
        case "C":
            print("El robot se desplazó hacia adelante")
        case "D":
            print("El robot se desplazó hacia atrás")
        case "E":
            ejecutando = False
        case _:
            print("Comando no reconocido. Intente de nuevo.")