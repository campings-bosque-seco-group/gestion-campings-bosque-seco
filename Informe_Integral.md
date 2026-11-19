# Informe Integral del Trabajo Realizado
## Sistema de Gestión de la Red de Campings Bosque Seco (Alternativa H)

---

### 1. Introducción y Enfoque de Desarrollo
El presente documento describe el proceso de análisis, diseño, codificación y verificación del sistema desarrollado en Python para administrar la ocupación diaria y los indicadores estadísticos de la red de campings *Bosque Seco. El proyecto se construyó de manera incremental utilizando GitHub como plataforma de control de versiones y planificación mediante *Milestones e Issues.

### 2. Desarrollo por Incrementos
* *Incremento 1 (Análisis y Especificación):* Se definieron las entradas, salidas y reglas del dominio para los 14 requisitos funcionales de la Alternativa H, priorizando el orden estricto de validación y los criterios de desempate.
* *Incremento 2 (Lógica del Negocio):* Se implementó el módulo business_logic.py aplicando Programación Orientada a Objetos (POO), encapsulando los datos y cálculos matemáticos sin interacción directa con la consola.
* *Incremento 3 (Interfaz de Usuario):* Se desarrolló el módulo user_interface.py con el menú interactivo de 7 opciones y el manejo estructurado de excepciones (try / except).
* *Incremento 4 (Pruebas y Verificación):* Se diseñaron los archivos campings.csv y campistas.csv con registros válidos y líneas con errores intencionales para comprobar la tolerancia a fallos y la exactitud estadística.

---

### 3. Arquitectura y Diseño de Clases
Para garantizar la separación de responsabilidades exigida en el curso, el sistema se dividió en dos módulos independientes:

```text
+-----------------------------------+       importa       +-----------------------------------+
|        user_interface.py          | ------------------> |         business_logic.py         |
|-----------------------------------|                     |-----------------------------------|
| - mostrar_menu()                  |                     | [Clase RedCampings]               |
| - opcion_crear_camping()          |                     |  - campings: list[Camping]        |
| - opcion_registrar_dia()          |                     |  + crear_camping()                |
| - opcion_simular_dias()           |                     |  + buscar_camping()               |
| - opcion_ver_informe()            |                     |  + obtener_extremos_ocupacion()   |
| - opcion_extremos_ocupacion()     |                     |  + cargar_campings_desde_archivo()|
| - opcion_cargar_archivos()        |                     |  + cargar_campistas_desde_archivo()|
| - main()                          |                     |                                   |
+-----------------------------------+                     | [Clase Camping]                   |
                                                          |  - nombre: str                    |
                                                          |  - plazas: int                    |
                                                          |  - fecha_inicio: date             |
                                                          |  - campistas: list[int]           |
                                                          |  + registrar_dia()                |
                                                          |  + simular_dias()                 |
                                                          |  + calcular_promedio()            |
                                                          |  + calcular_desviacion_estandar() |
                                                          |  + contar_niveles_ocupacion()     |
                                                          |  + obtener_racha_plena_mas_larga()|
                                                          |  + calcular_dias_sin_registrar()  |
                                                          +-----------------------------------+