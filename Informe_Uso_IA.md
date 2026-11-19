# Informe de Uso de Inteligencia Artificial
## Proyecto: Sistema de Gestión de la Red de Campings Bosque Seco (Alternativa H)

---

### 1. Herramientas de IA Utilizadas
* *Modelo de Lenguaje (Gemini):* Utilizado como asistente de apoyo para estructurar la documentación de análisis, revisar la lógica de los algoritmos estadísticos, diseñar casos de prueba y depurar errores de sintaxis y ejecución en Visual Studio Code.

---

### 2. Etapas en las que se Empleó IA y Tipo de Interacción

| Etapa del Proyecto | Uso de la IA | Validación y Aporte del Equipo |
| :--- | :--- | :--- |
| *Análisis de Requisitos* | Organización de las entradas, salidas y reglas del dominio de los 14 requisitos en formato estructurado. | Se contrastó cada regla con el enunciado oficial de la Alternativa H (orden de validaciones, desempates y formatos de salida). |
| *Codificación (business_logic.py y user_interface.py)* | Apoyo en la estructura de las clases Camping y RedCampings, manejo de fechas con datetime y captura de excepciones. | Se revisó que el código usara exclusivamente estructuras vistas en las sesiones 10 a 20 del curso, eliminando construcciones ajenas y corrigiendo problemas de rutas e importación local en Windows. |
| *Pruebas y Depuración* | Generación de datos de prueba para campings.csv y campistas.csv con errores intencionales. | Se ejecutó el programa en consola verificando manualmente los cálculos estadísticos (pernoctaciones, promedio, ocupación y desviación estándar) contra los ejemplos de referencia. |
| *Documentación* | Redacción base de los informes técnicos y tablas de verificación. | Se ajustó el contenido a la estructura real del repositorio en GitHub (Milestones, Issues y Commits). |

---

### 3. Ejemplos de Prompts Utilizados
1. "Guíame paso a paso para estructurar el documento de análisis con entradas, salidas y reglas del dominio para los 14 requisitos de la Alternativa H."
2. "Revisa si el código de business_logic.py y user_interface.py utiliza únicamente estructuras vistas en clase y cumple con la separación entre lógica e interfaz."
3. "Ayúdame a diagnosticar un AttributeError en la clase RedCampings y errores de importación entre archivos en Visual Studio Code."

---

### 4. Verificación, Correcciones y Compromiso Académico
* *Control de calidad:* Ningún fragmento de código o documento fue incorporado sin pruebas previas. Durante la ejecución local se detectaron y corrigieron errores de formato en los métodos __init__ y en la ubicación de los archivos .csv dentro del entorno de trabajo.
* *Comprensión total:* Todos los integrantes del equipo revisaron y comprendieron la lógica de cada clase, método y excepción implementada, garantizando plena autonomía para la sustentación oral individual del código.