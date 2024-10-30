# -*- coding: utf-8 -*-
"""Ejemplos_Carlos_Llanos.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QT9sxT-yjZxsLcIVSg-UhS99tdE6QOIn
"""

from pyspark.context import SparkContext

sc = SparkContext('local', 'test')

# flatMap
"""
Contexto:
Se tiene un RDD con una lista de frases y se quiere tener
todas las palabras de estas frases en un solo RDD
"""

# RDD con frases
frases = sc.parallelize(["Hola mundo", "Apache Spark es genial", "Usa flatMap"])

# Usar flatMap para obtener todas las palabras
palabras = frases.flatMap(lambda frase: frase.split(" "))

# Mostrar el resultado
palabras.collect()

# distinc
"""
Contexto:
Se tiene un RDD con datos repetidos, se desea obtener
otro RDD con todos los datos únicos(Sin valores repetidos)
"""

# RDD con artículos de compra duplicados
articulos = sc.parallelize(["leche", "pan", "huevos", "pan", "queso", "leche", "frutas"])

# Usar distinct para obtener artículos únicos
articulos_unicos = articulos.distinct()

# Mostrar el resultado
articulos_unicos.collect()

#sortByKey
"""
Contexto:
Se tiene un RDD que posee el nombre de cada estudiante y su calificaión en un examen,
se desea obtener el nombre de los estudiantes ordenados en orden ascendente y descendente.
"""
# RDD con nombres de estudiantes y sus calificaciones
estudiantes = [('Carlos', 85), ('Ana', 92), ('Luis', 78), ('María', 95), ('Elena', 88)]

# Usar sortByKey para ordenar por nombre
estudiantes_asc = sc.parallelize(estudiantes).sortByKey(True) #Ascentente
estudiantes_desc = sc.parallelize(estudiantes).sortByKey(False) #Descendente

# Mostrar el resultado
print(estudiantes_asc.collect())
print(estudiantes_desc.collect())

#coalesce
"""
Contexto:
Se tiene un RDD que posee el nombre de cada estudiante y su calificaión en un examen,
se desea obtener el nombre de los estudiantes ordenados en orden ascendente y descendente.
"""
# RDD con registros de ventas (por simplicidad, solo números)
ventas = sc.parallelize(range(1, 101), 10)  # Crea un RDD con 10 particiones

# Ver el número de particiones antes de coalesce
print("Número de particiones antes de coalesce:", ventas.getNumPartitions())

# Procesar los datos de ventas (ejemplo: filtrar ventas mayores a 50)
ventas_procesadas = ventas.filter(lambda x: x > 50)

# Ahora queremos reducir el número de particiones a 3 para optimizar la escritura
ventas_reducidas = ventas_procesadas.coalesce(3)

# Ver el número de particiones después de coalesce
print("Número de particiones después de coalesce:", ventas_reducidas.getNumPartitions())

# Recoger el resultado y mostrarlo
resultado = ventas_reducidas.collect()
print("Ventas procesadas:", resultado)

#count
"""
Contexto:
Se tiene un RDD de estudiantes registrados,
se quiere saber cuántos estudiantes hay en total.
"""
# RDD con los nombres de los estudiantes
estudiantes = sc.parallelize(["Ana", "Luis", "Carlos", "María", "Elena", "Carlos", "Pedro"])

# Usar count para contar el número total de estudiantes
total_estudiantes = estudiantes.count()

# Mostrar el resultado
print("Número total de estudiantes:", total_estudiantes)

#saveAsTextFile
"""
Contexto:
Se tiene un RDD con las ventas del día y
se desea exportar en un archivo txt
"""
# RDD con registros de ventas
ventas = sc.parallelize([
    "Venta 1: $100",
    "Venta 2: $200",
    "Venta 3: $150",
    "Venta 4: $300"
])

ventas.saveAsTextFile("/content/ventas.txt")

print("Informe de ventas guardado en ventas.txt.")

#saveAsTextFile
"""
Contexto:
Se tiene un RDD con las ventas del día y
se desea saber si se envió una notificación
"""
# RDD con registros de ventas
ventas = sc.parallelize([
    "Venta 1: $100",
    "Venta 2: $200",
    "Venta 3: $150",
    "Venta 4: $300"
])

# Función simulada para enviar una notificación
def enviar_notificacion(venta):
    print(f"Notificación enviada: {venta}")

# Usar foreach para enviar notificaciones para cada venta
ventas.foreach(enviar_notificacion)

print("Todas las notificaciones han sido enviadas.")