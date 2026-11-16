# --- SISTEMA BANCO MYOWNMONEY ---
# Definición de Constantes
BANCO_NOMBRE = "Banco MyOwnMoney"

# Inicialización de la variable para el ciclo while del menú principal
opcion = 0

# Bucle principal que mantiene el programa en ejecución hasta que el usuario elija salir (opción 7)
while opcion != 7:
    # --- MENÚ PRINCIPAL ---
    print("\n" + "="*40)
    print(f"--- MENÚ PRINCIPAL - {BANCO_NOMBRE} ---")
    print("="*40)
    print("1. Ingreso de Clientes")
    print("2. Ingreso de Movimientos")
    print("3. Ingreso de Transferencias Electrónicas (TEF)")
    print("4. Ingreso de Pagos Digitales")
    print("5. Ingreso de Reclamos")
    print("6. Consultar")
    print("7. Salir")
    print("="*40)
    
    # Captura de la opción seleccionada por el usuario
    opcion_str = input("Seleccione una opción (1-7): ")
    
    # Validación simple: verifica si la entrada contiene solo dígitos usando isdigit()
    if opcion_str.isdigit():
        # Si es un dígito, lo convierte a entero para usarlo en las condiciones lógicas
        opcion = int(opcion_str)
        
        # OPCIÓN 1: Ingreso de Clientes
        if opcion == 1:
            print("\n--- 1. REGISTRO DE CLIENTE ---")
            nombre = input("Ingrese nombre del cliente: ")
            
            # Validación simple: verifica que la cadena no esté vacía (ignorando espacios en blanco)
            if nombre.strip() != "":
                rut = input("Ingrese RUT del cliente: ")
                numero_cuenta = input("Ingrese numero de cuenta corriente: ")
                
                print("\n-> Cliente registrado correctamente.")
                print(f"Nombre: {nombre} | RUT: {rut} | Cuenta corriente: {numero_cuenta}")
            else:
                print("Error: Debe ingresar un nombre válido (no puede estar vacío).")

        # OPCIÓN 2: Ingreso de Movimientos 
        elif opcion == 2:
            print("\n--- 2. REGISTRO DE MOVIMIENTO ---")
            numero_cuenta = input("Ingrese numero de cuenta corriente: ")
            
            # Validación de cadena no vacía para asegurar que se ingresó una cuenta
            if numero_cuenta.strip() != "":
                tipo_movimiento = input("Ingrese tipo de movimiento (ingreso o giro): ")
                fecha = input("Ingrese fecha del movimiento (DD/MM/AAAA): ")
                
                monto_str = input("Ingrese monto del movimiento: ")
                
                # Validación simple usando isdigit()
                if monto_str.isdigit():
                    monto = float(monto_str)
                    
                    # Validación de rango numérico (el monto debe ser mayor a 0)
                    if monto > 0:
                        glosa = input("Ingrese glosa del movimiento: ")
                        print("\n-> Movimiento registrado correctamente.")
                        print(f"Cuenta: {numero_cuenta} | Tipo: {tipo_movimiento} | Fecha: {fecha}")
                        print(f"Monto: ${monto} | Glosa: {glosa}")
                    else:
                        print("Error: El monto debe ser mayor a 0.")
                else:
                    print("Error: Debe ingresar un valor numérico válido para el monto.")
            else:
                print("Error: El número de cuenta no puede estar vacío.")

        # OPCIÓN 3: Ingreso de Transferencias Electrónicas (TEF)
        elif opcion == 3:
            print("\n--- 3. REGISTRO DE TRANSFERENCIA TEF ---")
            numero_cuenta = input("Ingrese numero de cuenta del cliente afectado: ")
            
            if numero_cuenta.strip() != "":
                fecha = input("Ingrese fecha de la transferencia (DD/MM/AAAA): ")
                hora = input("Ingrese hora de la transferencia (HH:MM): ")
                monto_str = input("Ingrese monto de la transferencia: ")
                
                if monto_str.isdigit():
                    monto = float(monto_str)
                    banco_destino = input("Ingrese banco de destino: ")
                    rut_destinatario = input("Ingrese RUT del destinatario: ")
                    cuenta_destino = input("Ingrese numero de cuenta de destino: ")
                    comentario = input("Ingrese comentario de la transferencia: ")
                    
                    print("\n-> Transferencia registrada correctamente.")
                    print(f"Afectada: {numero_cuenta} | Monto: ${monto}")
                    print(f"Destino: {banco_destino} - Cuenta: {cuenta_destino} - RUT: {rut_destinatario}")
                else:
                    print("Error: El monto debe contener solo números.")
            else:
                 print("Error: El número de cuenta no puede estar vacío.")

        # OPCIÓN 4: Ingreso de Pagos Digitales
        elif opcion == 4:
            print("\n--- 4. REGISTRO DE PAGO DIGITAL ---")
            numero_cuenta = input("Ingrese numero de cuenta del cliente afectado: ")
            
            if numero_cuenta.strip() != "":
                tipo_pago = input("Ingrese tipo de pago (e-commerce, web, TerryPay, billetera): ")
                monto_str = input("Ingrese monto del pago: ")
                
                if monto_str.isdigit():
                    monto = float(monto_str)
                    fecha = input("Ingrese fecha del pago: ")
                    hora = input("Ingrese hora del pago: ")
                    rut_comercio = input("Ingrese RUT del comercio: ")
                    
                    print("\n-> Pago registrado correctamente.")
                    print(f"Cuenta: {numero_cuenta} | Tipo: {tipo_pago} | Monto: ${monto}")
                    print(f"Comercio RUT: {rut_comercio} | Fecha y Hora: {fecha} {hora}")
                else:
                    print("Error: El monto debe contener solo números.")
            else:
                 print("Error: El número de cuenta no puede estar vacío.")

        # OPCIÓN 5: Ingreso de Reclamos
        elif opcion == 5:
            print("\n--- 5. REGISTRO DE RECLAMO ---")
            nombre_cliente = input("Ingrese nombre del cliente: ")
            
            # Validación de cadena no vacía
            if nombre_cliente.strip() != "":
                rut_cliente = input("Ingrese RUT del cliente: ")
                numero_cuenta = input("Ingrese numero de cuenta corriente: ")
                movimiento_objetado = input("Describa el movimiento que reclama: ")
                descripcion_deteccion = input("Indique como se dio cuenta del posible fraude: ")
                
                print("\n-> Reclamo registrado correctamente.")
                print(f"Cliente: {nombre_cliente} ({rut_cliente}) | Cuenta: {numero_cuenta}")
                print(f"Movimiento Objetado: {movimiento_objetado}")
                print(f"Detección: {descripcion_deteccion}")
            else:
                print("Error: El nombre del cliente no puede estar vacío.")
        
        # OPCIÓN 6: Consultar
        elif opcion == 6:

            while True:
                print("\n--- 6. CONSULTAR ---")
                print("="*40)
                print("1. Consultar clientes registrados")
                print("2. Consultar reclamos registrados")
                print("3. Volver")
                print("="*40)

                #CONTROL DE EXCEPCIÓN: Ingreso de variable no valida
                try:
                    tipo_consulta=int(input("Seleccione una opción (1-3): "))
                    if tipo_consulta == 1:
                        print("Muestra clientes registrados")

                    elif tipo_consulta == 2:
                        print("Muestra reclamos registrados")

                    elif tipo_consulta == 3:
                        break
                    
                    # VALIDACIÓN DE MENÚ: Opción fuera de rango
                    else:
                        print("Debe ingresar un numero entre 1 y 3")

                except ValueError:
                    print("Debe ingresar el numero de la opción que desee consultar")

        # OPCIÓN 7: Salir del programa
        elif opcion == 7:
            print("\nCerrando el sistema. ¡Hasta luego!")
            
        # VALIDACIÓN DE MENÚ: Opción fuera de rango
        else:
            # Esta validación se ejecuta si el usuario ingresa un número, pero no está entre 1 y 6
            print("\nError: Opción inválida. Por favor, seleccione un número del 1 al 6.")
            
    # VALIDACIÓN DE MENÚ: Entrada no numérica
    else:
         # Esta validación se ejecuta si isdigit() es False (ej: si el usuario ingresó letras)
         print("\nError: Debe ingresar un número válido (no letras ni símbolos).")