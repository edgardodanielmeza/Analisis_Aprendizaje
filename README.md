#Proyecto Analytica de Estudiantes.

### Objetivo y Preguntas:

- Analizar a los estudiantes de acuerdo a una encuesta para identificar el tipo de aprendizaje y analizar su rendimiento.
- Rendimiento académico de estudiantes según su tipo de
- ¿Cómo se distribuyen los estudiantes según tipos de aprendizaje?
- ¿Existen diferencias en el rendimiento académico entre los tipos de aprendizaje?
- aprendizaje 


### Fuente de Datos(Datos públicos libres)

- Sistema académico de la institución educativa
- Se extrajeron datos de:
- Encuesta aplicada a estudiantes (datos_estudiantes.csv)
- Resultados de evaluaciones por área (resultadoevaluacionareas.csv)
- Información adicional de estudiantes (otrosdatosestudiantes.csv)

### Recolección y Preprocesamiento de Datos( analizarestudiantes.bat):
- datos_estudiantes.csv (encuesta)
- resultadoevaluacionareas.csv (pruebas)
- otrosdatosestudiantes.csv (datos adicionales)
- Limpieza y unificación de datos
- Generar archivo estudiantes_procesado.csv

### Exploración de Datos(analítica_estudiantes.bat,  Graficos con POWER BI):
- Visualización gráfica para identificar tendencias
- Estadísticos descriptivos

### Modelado Predictivo:
- Asignar tipo de aprendizaje mediante analizarestudiantes.bat
- Modelos de regresión/clasificación para predecir rendimiento

### Interpretación de Resultados:
- Analisis de la distribución de tipos de aprendizaje
- Variables que mejor predicen el rendimiento
- Hallazgos pedagógicos

### Documentación y Exposición:
- Informe con el proceso
- Aplicación analítica_estudiantes.bat
- Presentación de resultados

### Herramientas
- Python: Pandas, Scikit-learn
- Dash: Aplicación dashboard
- Power BI: Tableros interactivos

# PROGRAMAS
## procesarEstudiante.bat        (categorizarestudiantes.py)
####Analizador y clasificador de tipo de aprendizaje

Importa la librería Pandas para trabajar con datos estructurados en DataFrames.
Carga los datos de clasificación de preguntas a tipos de aprendizaje desde el archivo CSV "clasificacion.csv". Estos datos mapean cada pregunta de la encuesta a un tipo de aprendizaje.
Convierte esta información a un diccionario, donde la pregunta es la clave y el tipo de aprendizaje es el valor.
Carga los datos de los estudiantes desde el archivo CSV "datos_estudiantes.csv". Este contiene la información base de cada estudiante.
Realiza validaciones iniciales sobre los datos, verificando tipos de columnas, nulos y duplicados.
Renombra las columnas de las respuestas de la encuesta.
Convierte las respuestas a valores numéricos para poder sumarlas.
Define una función que evaluará el tipo de aprendizaje por fila. Suma las respuestas por tipo y elige el máximo.
Aplica esta función para cada fila del DataFrame de estudiantes, asignando el tipo resultado.
Imprime el DataFrame con los tipos de aprendizaje clasificados.
Guarda este DataFrame procesado en un nuevo CSV "estudiantes_procesado.csv" para su análisis posterior.
En resumen, carga los datos, procesa las respuestas numéricamente, clasifica el tipo aplicando lógica y guarda el resultado en un nuevo archivo limpio y clasificado.

## Analitica_estudiantest,bat	(analítica_estudiantes.py)
#### Aplicación dashboard para visualizar datos estudiantiles 


Importamos las librerías necesarias como Dash, Pandas, Plotly para graficar.
Cargamos los datos desde diferentes CSV usando Pandas y los combinamos.
Definimos funciones para generar cada gráfico, uso diferentes tipos de graficas como barras, distribuciones, combinados, etc.

Graficar distribución de tipos: Muestra distribución de tipos de aprendizaje.
Graficar por género: Distribución de tipos agrupados por género.
Graficar calificaciones: Relación de calificaciones con tipos de aprendizaje.
Distribuciones
Promedios
Combinados
Gráficos de torta
Relación de variables
![](https://github.com/edgardodanielmeza/Analisis_Aprendizaje/blob/main/analisis_estudiantes.png?raw=true)
## Tablero power by	(analiticas estudiantes.pbix)
Realizamos analíticas parecidas a las desarrolladas pero con una interfaz mas intuitiva y caracterizarle para la presentación de los datos.

![](https://github.com/edgardodanielmeza/Analisis_Aprendizaje/blob/main/analisis_powerBI.png?raw=true)

## En resumen

El proyecto aplica técnicas de datos, modelo predictivo y visualización para analizar el perfil y rendimiento de estudiantes según su estilo de aprendizaje.
En resumen, el proyecto aplica técnicas de datos, modelo predictivo y visualización para analizar el perfil y rendimiento de estudiantes según su estilo de aprendizaje.
La metodología propuesta permite caracterizar la distribución de tipos de aprendizaje entre los estudiantes y explorar su relación con el rendimiento académico, lo que apoyaría el análisis y la toma de decisiones pedagógicas. Los scripts y herramientas de análisis de datos facilitan el procesamiento, modelado y comunicación de los hallazgos.


#Autores Grupo 3

###- Jonathan Bernal 
###- Micheli De Almeida Bareiro 
###- Lourdes Beatriz Delgado Gonzalez 
###- Vladimir Lopez Maldonado 
###- Edgardo Daniel Meza Fleitas 

