import pandas as pd

# Cargar los datos de clasificación desde el archivo CSV
df_clasificacion = pd.read_csv('clasificacion.csv', delimiter=';', encoding='utf-8')

# Convertir los datos de clasificación en un diccionario
diccionario_clasificacion = dict(zip(df_clasificacion['PREGUNAT'], df_clasificacion['TIPOAPRENDIZAGE']))

# Cargar los datos de los estudiantes desde el archivo CSV
df_estudiantes = pd.read_csv('datos_estudiantes.csv', delimiter=';', encoding='utf-8')


#verificacion de datos
print ("----------------------------Tipos Columnas-----------------------------------")
print (df_estudiantes.dtypes)
print ("----------------------------Cantidad de Nulos--------------------------------")
print (df_estudiantes.isnull().sum())
print ("----------------------------Cantidad de Duplicados---------------------------")
print (df_estudiantes.duplicated().sum())

print("-------------------------------------------------------------------------------")



# Asignar nombres de columna adecuados
column_names = ['ID', 'Genero'] + list(df_estudiantes.columns[2:])
df_estudiantes.columns = column_names

# Convertir las respuestas a valores numéricos
df_estudiantes[column_names[2:]] = df_estudiantes[column_names[2:]].astype(int)

# Función para evaluar el tipo de aprendizaje de un estudiante según las sumatorias de las respuestas
def evaluar_tipo_aprendizaje(row):
    tipo_aprendizaje = []
    sumatorias_tipo = {}

    for i, respuesta in enumerate(row[2:]):
        pregunta = column_names[i+2]
        tipo = diccionario_clasificacion.get(pregunta)

        if tipo:
            if tipo not in sumatorias_tipo:
                sumatorias_tipo[tipo] = 0
            sumatorias_tipo[tipo] += respuesta

    max_sumatoria = max(sumatorias_tipo.values())

    for tipo, sumatoria in sumatorias_tipo.items():
        if sumatoria == max_sumatoria:
            tipo_aprendizaje.append(tipo)

    return ', '.join(tipo_aprendizaje)

# Aplicar la función evaluar_tipo_aprendizaje a cada fila del DataFrame de estudiantes
df_estudiantes['TipoAprendizaje'] = df_estudiantes.apply(evaluar_tipo_aprendizaje, axis=1)

# Imprimir el DataFrame de estudiantes con los tipos de aprendizaje asignados

print(df_estudiantes)

# Guardar el DataFrame de estudiantes con los tipos de aprendizaje asignados en un nuevo archivo CSV
df_estudiantes.to_csv('estudiantes_procesado.csv', index=False)
print("Archivo generado Exitosamente C:\SP\estudiantes_procesado.csv")