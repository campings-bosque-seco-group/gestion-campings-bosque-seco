from business_logic import RedCampings


def mostrar_menu():
    print("\n--- RED DE CAMPINGS BOSQUE SECO ---")
    print("1. Crear un camping")
    print("2. Registrar los campistas del día siguiente")
    print("3. Simular días")
    print("4. Ver el informe de un camping")
    print("5. Ver el camping con el porcentaje de ocupación más alto y el más bajo")
    print("6. Cargar los campings y los campistas desde archivos")
    print("7. Salir")


def opcion_crear_camping(red):
    nombre = input("Nombre del camping: ")
    plazas = input("Número de plazas: ")
    anio = input("Año de inicio: ")
    mes = input("Mes de inicio: ")
    dia = input("Día de inicio: ")

    try:
        camping = red.crear_camping(nombre, plazas, anio, mes, dia)
        print(f"Camping '{camping.nombre}' creado correctamente.")
    except ValueError as error:
        print(error)


def opcion_registrar_dia(red):
    nombre = input("Nombre del camping: ")
    try:
        camping = red.obtener_camping(nombre)
    except ValueError as error:
        print(error)
        return

    fecha_siguiente = camping.obtener_fecha_siguiente()
    print(f"Fecha a registrar: {fecha_siguiente}")

    while True:
        dato_campistas = input("Número de campistas: ")
        try:
            camping.registrar_dia(dato_campistas)
            print("Día registrado correctamente.")
            break
        except ValueError as error:
            print(error)


def opcion_simular_dias(red):
    nombre = input("Nombre del camping: ")
    try:
        camping = red.obtener_camping(nombre)
    except ValueError as error:
        print(error)
        return

    dias = input("Número de días a simular: ")
    try:
        camping.validar_dias_simulacion(dias)
    except ValueError as error:
        print(error)
        return

    minimo = input("Campistas mínimos: ")
    try:
        camping.validar_campistas(minimo)
    except ValueError as error:
        print(error)
        return

    maximo = input("Campistas máximos: ")
    try:
        camping.simular_dias(dias, minimo, maximo)
        print(f"Se simularon {int(str(dias).strip())} días correctamente.")
    except ValueError as error:
        print(error)


def opcion_ver_informe(red):
    nombre = input("Nombre del camping: ")
    try:
        camping = red.obtener_camping(nombre)
    except ValueError as error:
        print(error)
        return

    print(f"\nCamping: {camping.nombre}")
    print(f"Plazas: {camping.plazas}")

    if not camping.tiene_registros():
        print("El camping no tiene días registrados.")
        return

    dias_registrados = len(camping.campistas)
    pernoctaciones = camping.calcular_pernoctaciones()
    promedio = round(camping.calcular_promedio(), 2)
    porcentaje = round(camping.calcular_porcentaje_ocupacion(), 2)
    desviacion = round(camping.calcular_desviacion_estandar(), 2)
    fecha_max, _, fecha_min, _ = camping.obtener_dias_extremos()
    niveles = camping.contar_niveles_ocupacion()
    racha_dias, racha_inicio = camping.obtener_racha_plena_mas_larga()
    ultimo_dia, dias_sin_registrar = camping.calcular_dias_sin_registrar()

    print(f"Días registrados: {dias_registrados}")
    print(f"Pernoctaciones: {pernoctaciones}")
    print(f"Promedio de campistas por día: {promedio}")
    print(f"Porcentaje de ocupación: {porcentaje} %")
    print(f"Desviación estándar: {desviacion}")
    print(f"Día de más campistas: {fecha_max}")
    print(f"Día de menos campistas: {fecha_min}")
    print("Días en cada nivel de ocupación:")
    print(f"  Baja: {niveles['Baja']}")
    print(f"  Media: {niveles['Media']}")
    print(f"  Alta: {niveles['Alta']}")
    print(f"  Plena: {niveles['Plena']}")

    if racha_dias == 0:
        print("El camping no tuvo ningún día en ocupación plena.")
    else:
        print(
            f"Racha más larga en ocupación plena: {racha_dias} días "
            f"(inició el {racha_inicio})"
        )

    print(f"Último día registrado: {ultimo_dia}")
    if dias_sin_registrar == 0:
        print("El registro está al día.")
    else:
        print(f"Días sin registrar: {dias_sin_registrar}")


def opcion_extremos_ocupacion(red):
    try:
        camping_mayor, camping_menor = red.obtener_extremos_ocupacion()
        porcentaje_mayor = round(camping_mayor.calcular_porcentaje_ocupacion(), 2)
        porcentaje_menor = round(camping_menor.calcular_porcentaje_ocupacion(), 2)
        print(
            f"Camping con porcentaje de ocupación más alto: "
            f"{camping_mayor.nombre} ({porcentaje_mayor} %)"
        )
        print(
            f"Camping con porcentaje de ocupación más bajo: "
            f"{camping_menor.nombre} ({porcentaje_menor} %)"
        )
    except ValueError as error:
        print(error)


def opcion_cargar_archivos(red):
    if red.tiene_campings():
        print("La carga solo se hace con el programa sin campings.")
        return

    ruta_campings = input("Ruta del archivo de campings: ")
    try:
        cargados_campings, errores_campings = red.cargar_campings_desde_archivo(
            ruta_campings
        )
    except FileNotFoundError as error:
        print(error)
        return

    for error in errores_campings:
        print(error)
    print(f"Se cargaron {cargados_campings} campings.")

    ruta_campistas = input("Ruta del archivo de campistas: ")
    try:
        cargados_dias, errores_campistas = red.cargar_campistas_desde_archivo(
            ruta_campistas
        )
    except FileNotFoundError as error:
        print(error)
        return

    for error in errores_campistas:
        print(error)
    print(f"Se cargaron {cargados_dias} días.")


def main():
    red = RedCampings()

    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            opcion_crear_camping(red)
        elif opcion == "2":
            opcion_registrar_dia(red)
        elif opcion == "3":
            opcion_simular_dias(red)
        elif opcion == "4":
            opcion_ver_informe(red)
        elif opcion == "5":
            opcion_extremos_ocupacion(red)
        elif opcion == "6":
            opcion_cargar_archivos(red)
        elif opcion == "7":
            print("Programa terminado.")
            break
        else:
            print("La opción no es válida.")


if __name__ == "__main__":
    main()