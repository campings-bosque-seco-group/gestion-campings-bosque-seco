from datetime import date, timedelta
import math
import random


class Camping:
    def _init_(self, nombre, plazas, fecha_inicio):
        self.nombre = nombre
        self.plazas = plazas
        self.fecha_inicio = fecha_inicio
        self.campistas = []

    def obtener_fecha_siguiente(self):
        return self.fecha_inicio + timedelta(days=len(self.campistas))

    def validar_campistas(self, valor):
        try:
            cantidad = int(str(valor).strip())
        except ValueError:
            raise ValueError("Los campistas deben ser un número entero.")

        if cantidad < 0 or cantidad > self.plazas:
            raise ValueError(f"Los campistas van de 0 a {self.plazas}.")
        return cantidad

    def registrar_dia(self, valor_campistas):
        cantidad = self.validar_campistas(valor_campistas)
        self.campistas.append(cantidad)

    def validar_dias_simulacion(self, valor_dias):
        try:
            dias = int(str(valor_dias).strip())
        except ValueError:
            raise ValueError("El número de días debe ser un número entero.")

        if dias < 1:
            raise ValueError("Se debe simular al menos un día.")
        return dias

    def simular_dias(self, valor_dias, valor_minimo, valor_maximo):
        dias = self.validar_dias_simulacion(valor_dias)
        minimo = self.validar_campistas(valor_minimo)
        maximo = self.validar_campistas(valor_maximo)

        if minimo > maximo:
            raise ValueError("El mínimo no puede ser mayor que el máximo.")

        for _ in range(dias):
            campistas_azar = random.randint(minimo, maximo)
            self.campistas.append(campistas_azar)

    def tiene_registros(self):
        return len(self.campistas) > 0

    def calcular_pernoctaciones(self):
        return sum(self.campistas)

    def calcular_promedio(self):
        return self.calcular_pernoctaciones() / len(self.campistas)

    def calcular_porcentaje_ocupacion(self):
        return (self.calcular_promedio() / self.plazas) * 100

    def calcular_desviacion_estandar(self):
        promedio = self.calcular_promedio()
        suma_cuadrados = 0.0
        for cantidad in self.campistas:
            suma_cuadrados += (cantidad - promedio) ** 2
        return math.sqrt(suma_cuadrados / len(self.campistas))

    def obtener_dias_extremos(self):
        max_campistas = self.campistas[0]
        indice_max = 0
        min_campistas = self.campistas[0]
        indice_min = 0

        for i in range(1, len(self.campistas)):
            if self.campistas[i] > max_campistas:
                max_campistas = self.campistas[i]
                indice_max = i
            if self.campistas[i] < min_campistas:
                min_campistas = self.campistas[i]
                indice_min = i

        fecha_max = self.fecha_inicio + timedelta(days=indice_max)
        fecha_min = self.fecha_inicio + timedelta(days=indice_min)
        return fecha_max, max_campistas, fecha_min, min_campistas

    def contar_niveles_ocupacion(self):
        baja = 0
        media = 0
        alta = 0
        plena = 0

        for cantidad in self.campistas:
            porcentaje_dia = (cantidad / self.plazas) * 100
            if porcentaje_dia < 35:
                baja += 1
            elif porcentaje_dia < 65:
                media += 1
            elif porcentaje_dia < 85:
                alta += 1
            else:
                plena += 1

        return {
            "Baja": baja,
            "Media": media,
            "Alta": alta,
            "Plena": plena,
        }

    def obtener_racha_plena_mas_larga(self):
        mejor_racha = 0
        mejor_inicio = 0
        racha_actual = 0
        inicio_actual = 0

        for i in range(len(self.campistas)):
            porcentaje_dia = (self.campistas[i] / self.plazas) * 100
            if porcentaje_dia >= 85:
                if racha_actual == 0:
                    inicio_actual = i
                racha_actual += 1
                if racha_actual > mejor_racha:
                    mejor_racha = racha_actual
                    mejor_inicio = inicio_actual
            else:
                racha_actual = 0

        if mejor_racha == 0:
            return 0, None

        fecha_inicio_racha = self.fecha_inicio + timedelta(days=mejor_inicio)
        return mejor_racha, fecha_inicio_racha

    def calcular_dias_sin_registrar(self, fecha_actual=None):
        if fecha_actual is None:
            fecha_actual = date.today()

        ultimo_dia = self.fecha_inicio + timedelta(days=len(self.campistas) - 1)
        ayer = fecha_actual - timedelta(days=1)

        if ultimo_dia >= ayer:
            return ultimo_dia, 0

        dias_faltantes = (ayer - ultimo_dia).days
        return ultimo_dia, dias_faltantes


class RedCampings:
    def _init_(self):
        self.campings = []

    def tiene_campings(self):
        return len(self.campings) > 0

    def buscar_camping(self, nombre):
        nombre_limpio = str(nombre).strip()
        for camping in self.campings:
            if camping.nombre == nombre_limpio:
                return camping
        return None

    def obtener_camping(self, nombre):
        camping = self.buscar_camping(nombre)
        if camping is None:
            raise ValueError("No hay un camping con ese nombre.")
        return camping

    def crear_camping(self, nombre, plazas, anio, mes, dia):
        nombre_limpio = str(nombre).strip()
        if nombre_limpio == "":
            raise ValueError("El nombre no puede estar vacío.")
        if self.buscar_camping(nombre_limpio) is not None:
            raise ValueError("Ya existe un camping con ese nombre.")

        try:
            plazas_int = int(str(plazas).strip())
        except ValueError:
            raise ValueError("Las plazas deben ser un número entero.")

        if plazas_int < 1:
            raise ValueError("El camping debe tener al menos una plaza.")

        try:
            anio_int = int(str(anio).strip())
            mes_int = int(str(mes).strip())
            dia_int = int(str(dia).strip())
            fecha_inicio = date(anio_int, mes_int, dia_int)
        except ValueError:
            raise ValueError("La fecha no es válida.")

        nuevo_camping = Camping(nombre_limpio, plazas_int, fecha_inicio)
        self.campings.append(nuevo_camping)
        return nuevo_camping

    def obtener_extremos_ocupacion(self):
        campings_con_datos = []
        for camping in self.campings:
            if camping.tiene_registros():
                campings_con_datos.append(camping)

        if len(campings_con_datos) == 0:
            raise ValueError("Ningún camping tiene días registrados.")

        camping_mayor = campings_con_datos[0]
        mayor_ocupacion = camping_mayor.calcular_porcentaje_ocupacion()
        camping_menor = campings_con_datos[0]
        menor_ocupacion = camping_menor.calcular_porcentaje_ocupacion()

        for i in range(1, len(campings_con_datos)):
            actual = campings_con_datos[i]
            ocupacion_actual = actual.calcular_porcentaje_ocupacion()
            if ocupacion_actual > mayor_ocupacion:
                mayor_ocupacion = ocupacion_actual
                camping_mayor = actual
            if ocupacion_actual < menor_ocupacion:
                menor_ocupacion = ocupacion_actual
                camping_menor = actual

        return camping_mayor, camping_menor

    def cargar_campings_desde_archivo(self, ruta):
        if self.tiene_campings():
            raise ValueError("La carga solo se hace con el programa sin campings.")

        cargados = 0
        errores = []

        try:
            with open(ruta, mode="r", encoding="utf-8") as archivo:
                for num_linea, linea in enumerate(archivo, start=1):
                    if num_linea == 1:
                        continue
                    if linea.strip() == "":
                        continue

                    campos = linea.rstrip("\r\n").split(";")
                    if len(campos) != 5:
                        errores.append(f"Línea {num_linea}: no tiene cinco campos.")
                        continue

                    try:
                        self.crear_camping(
                            campos[0], campos[1], campos[2], campos[3], campos[4]
                        )
                        cargados += 1
                    except ValueError as error:
                        errores.append(f"Línea {num_linea}: {error}")
        except FileNotFoundError:
            raise FileNotFoundError("El archivo no existe.")

        return cargados, errores

    def cargar_campistas_desde_archivo(self, ruta):
        cargados = 0
        errores = []

        try:
            with open(ruta, mode="r", encoding="utf-8") as archivo:
                for num_linea, linea in enumerate(archivo, start=1):
                    if num_linea == 1:
                        continue
                    if linea.strip() == "":
                        continue

                    campos = linea.rstrip("\r\n").split(";")
                    if len(campos) != 2:
                        errores.append(f"Línea {num_linea}: no tiene dos campos.")
                        continue

                    try:
                        camping = self.obtener_camping(campos[0])
                        camping.registrar_dia(campos[1])
                        cargados += 1
                    except ValueError as error:
                        errores.append(f"Línea {num_linea}: {error}")
        except FileNotFoundError:
            raise FileNotFoundError("El archivo no existe.")

        return cargados, errores