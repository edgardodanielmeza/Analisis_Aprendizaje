import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el archivo procesado con los tipos de aprendizaje asignados
df_estudiantes = pd.read_csv('estudiantes_procesado.csv')

def plot_tipo_aprendizaje():
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df_estudiantes, x='TipoAprendizaje')
    plt.title('Distribución de los tipos de aprendizaje')
    plt.xlabel('Tipo de Aprendizaje')
    plt.ylabel('Cantidad de Estudiantes')
    plt.xticks(rotation=45)
    plt.show()

def plot_tipo_aprendizaje_genero():
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df_estudiantes, x='TipoAprendizaje', hue='Genero')
    plt.title('Distribución de los tipos de aprendizaje por género')
    plt.xlabel('Tipo de Aprendizaje')
    plt.ylabel('Cantidad de Estudiantes')
    plt.xticks(rotation=45)
    plt.legend(title='Género')
    plt.show()

def plot_calificaciones_tipo_aprendizaje():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df_estudiantes, x='TipoAprendizaje', y='Aprendo mejor leyendo lo que el maestro escribe en la pizarra')
    plt.title('Calificaciones según el tipo de aprendizaje')
    plt.xlabel('Tipo de Aprendizaje')
    plt.ylabel('Calificaciones')
    plt.xticks(rotation=45)
    plt.show()

def plot_calificaciones_distribucion():
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df_estudiantes, x='TipoAprendizaje', y='Aprendo mejor leyendo lo que el maestro escribe en la pizarra')
    plt.title('Distribución de las calificaciones por tipo de aprendizaje')
    plt.xlabel('Tipo de Aprendizaje')
    plt.ylabel('Calificaciones')
    plt.xticks(rotation=45)
    plt.show()

def menu():
    while True:
        print("------ MENÚ ------")
        print("1. Gráfico de distribución de los tipos de aprendizaje")
        print("2. Gráfico de distribución de los tipos de aprendizaje por género")
        print("3. Gráfico de dispersión de las calificaciones según el tipo de aprendizaje")
        print("4. Gráfico de caja de las calificaciones por tipo de aprendizaje")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            plot_tipo_aprendizaje()
        elif opcion == "2":
            plot_tipo_aprendizaje_genero()
        elif opcion == "3":
            plot_calificaciones_tipo_aprendizaje()
        elif opcion == "4":
            plot_calificaciones_distribucion()
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menu()