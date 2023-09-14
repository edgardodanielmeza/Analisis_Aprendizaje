import dash
import pandas as pd
from dash import dcc, html
from dash.dependencies import Input, Output

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.subplots as sp
import webbrowser


def open_browser():
  webbrowser.open('http://localhost:8050/')
  app.run_server(port=8050, debug=True)

# Cargar los datos de los archivos CSV
df_estudiantes = pd.read_csv('estudiantes_procesado.csv')
otros_datos_estudiantes = pd.read_csv("otrosdatosestudiantes.csv", sep=";")
df_evaluacion_areas = pd.read_csv("resultadoevaluacionareas.csv", sep=";")

# Combinar los datos de los estudiantes y los resultados de evaluación
datos_combinados = pd.merge(df_evaluacion_areas, otros_datos_estudiantes, left_on="idestudiante", right_on="idestudiante")
datos_combinados = pd.merge(datos_combinados, df_estudiantes, left_on="idestudiante", right_on="ID")





#1
def plot_tipo_aprendizaje():
    fig = px.histogram(df_estudiantes, x='TipoAprendizaje', title='Distribución de los tipos de aprendizaje', color='TipoAprendizaje')
    fig.update_layout(xaxis_title='Tipo de Aprendizaje', yaxis_title='Cantidad de Estudiantes')
    return fig 

#2
def plot_tipo_aprendizaje_genero():
    fig = px.histogram(df_estudiantes, x='TipoAprendizaje', color='Genero', title='Distribución de los tipos de aprendizaje por género')
    fig.update_layout(xaxis_title='Tipo de Aprendizaje', yaxis_title='Cantidad de Estudiantes')
    return fig 

#3
def plot_calificaciones_tipo_aprendizaje():
    fig = px.scatter(df_estudiantes, x='TipoAprendizaje', y='Aprendo mejor leyendo lo que el maestro escribe en la pizarra', title='Calificaciones según el tipo de aprendizaje')
    fig.update_layout(xaxis_title='Tipo de Aprendizaje', yaxis_title='Calificaciones')
    return fig 

#4


def plot_proporcion_tipo_aprendizaje():
    fig = px.pie(df_estudiantes, names='TipoAprendizaje', title='Proporción de tipos de aprendizaje')
    fig.update_layout(showlegend=False)
    return fig 
#5

def plot_distribucion_edades():
    fig = px.histogram(df_estudiantes, x='Edad', title='Distribución de Edades',color='Edad')
    fig.update_layout(xaxis_title='Edad', yaxis_title='Cantidad de Estudiantes')
    return fig 

#6
def plot_tipo_aprendizaje_por_edad():
    fig = px.bar(df_estudiantes, x='TipoAprendizaje', y='Edad', title='Tipo de Aprendizaje por Edad',color='TipoAprendizaje')
    fig.update_layout(xaxis_title='Tipo de Aprendizaje', yaxis_title='Edad')
    return fig 
#7


def plot_combinado_distribucion_edades_tipo_aprendizaje():
    # Crear la cuadrícula de subtramas
    fig = sp.make_subplots(rows=1, cols=2, subplot_titles=('Distribución de Edades', 'Tipo de Aprendizaje por Edad'))

    # labde distribución de edades
    fig.add_trace(go.Histogram(x=df_estudiantes['Edad'], nbinsx=10, name='Edades', marker_color='blue'), row=1, col=1)

    # Gráfico de tipo de aprendizaje por edad
    fig.add_trace(go.Bar(x=df_estudiantes['Edad'], y=df_estudiantes['TipoAprendizaje'], name='Tipo de Aprendizaje', marker_color='green'), row=1, col=2)

    fig.update_layout(
        title='Distribución de Edades y Tipo de Aprendizaje por Edad',
        xaxis=dict(title='Edad'),
        yaxis=dict(title='Cantidad de Estudiantes'),
        xaxis2=dict(title='Edad'),
        yaxis2=dict(title='Tipo de Aprendizaje'),
        showlegend=False
    )

    return fig 


#8
def varios_tortas():
    #preparo datos para graficos
    values1 = datos_combinados['Genero'].value_counts()
    labels1 = 'Masculino', 'Femenino'

    values2 = datos_combinados['Raza/etnia'].value_counts()
    labels2 = 'Group C', 'Group D', 'Group B', 'Group E', 'Group A'

    values3 = datos_combinados['almuerzo'].value_counts()
    labels3 = 'Pago/Premiun', 'Gratis/Reducido'

    # Gráfico 5: Nivel de educacion de los padres
    values4 = datos_combinados['Nivel de educacion de los padres'].value_counts()
    labels4 = 'alguna educación superior', 'grado asociado', 'escuela secundaria', 'algún instituto', 'licenciatura', 'maestría'

    values5 = datos_combinados['Curso de preparacion para examenes'].value_counts()
    labels5 = 'ninguna', 'completado'


    values6= datos_combinados['TipoAprendizaje'].value_counts()
    labels6 = values6.index


    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']



    # Crear subplots

                    
    fig = make_subplots(rows=2, cols=3, subplot_titles=(' Por Genero', 'Por Etnia', 'Por Tipo Amuerzo',
                                                        'Por Nivel  educacion PAdres', 'Por Curso Preparacion', 'Por Tipo Aprendizaje'), specs=[[{'type':'pie'}, {'type':'pie'}, {'type':'pie'}],
                            [{'type':'pie'}, {'type':'pie'}, {'type':'pie'}]]) 

    # Agregar gráficos de torta

    fig.add_trace(go.Pie(labels=labels1, values=values1, showlegend=False, textinfo='label+percent'), row=1, col=1)
    fig.add_trace(go.Pie(labels=labels2, values=values2, showlegend=False, textinfo='label+percent'), row=1, col=2)
    fig.add_trace(go.Pie(labels=labels3, values=values3, showlegend=False, textinfo='label+percent'), row=1, col=3)
    fig.add_trace(go.Pie(labels=labels4, values=values4, showlegend=False, textinfo='label+percent'), row=2, col=1)
    fig.add_trace(go.Pie(labels=labels5, values=values5, showlegend=False, textinfo='label+percent'), row=2, col=2)
    fig.add_trace(go.Pie(labels=labels6, values=values6, marker=dict(colors=colors), showlegend=False, textinfo='label+percent'), row=2, col=3)


    fig.update_layout(height=800, width=1200, title_text="<b>Varios gráficos de torta</b>", title_font=dict(size=18), title_x=0.5)

    return fig 









#9



def promedio_de_notas_de_areas_por_tipo_de_aprendisaje ():

    # Obtener las áreas de evaluación únicas y los tipos de aprendizaje únicos
    areas_evaluacion = datos_combinados['area'].unique()
    tipos_aprendizaje = datos_combinados['TipoAprendizaje'].unique()


    # Obtener las áreas de evaluación únicas y los tipos de aprendizaje únicos
    areas_evaluacion = datos_combinados['area'].unique()
    tipos_aprendizaje = datos_combinados['TipoAprendizaje'].unique()

    # Crear el gráfico de barras
    fig = go.Figure()

    for area in areas_evaluacion:
        df_area = datos_combinados[datos_combinados['area'] == area]
        
        # Crear lista vacía para almacenar los valores de cada tipo de aprendizaje
        valores_tipos = []
        
        for tipo_aprendizaje in tipos_aprendizaje:
            df_tipo = df_area[df_area['TipoAprendizaje'] == tipo_aprendizaje]
            
            # Obtener el promedio de puntuación para el tipo de aprendizaje y área actual
            promedio_puntuacion = df_tipo['Puntuacion'].mean()
            
            # Agregar el promedio de puntuación a la lista de valores de tipos de aprendizaje
            valores_tipos.append(promedio_puntuacion)
        
        # Agregar las barras para el área de evaluación actual
        fig.add_trace(go.Bar(x=tipos_aprendizaje,
                            y=valores_tipos,
                            name=area,
                            text=[f'{round((v/sum(valores_tipos))*100, 2)}%' for v in valores_tipos],
                            textposition='auto'))
        
    # Actualizar etiquetas de los ejes
    fig.update_xaxes(title_text='Tipo de Aprendizaje')
    fig.update_yaxes(title_text='Puntuación promedio')

    # Actualizar diseño de la figura
    fig.update_layout(title='<b>Puntuaciones promedio por Tipo de Aprendizaje y Área de Evaluación</b>', title_font=dict(size=18), title_x=0.5,
                    barmode='group')

    # Mostrar el gráfico
    return fig 



#10
def repercute_las_notas_el_nivel_de_los_prades():
    # Obtener los niveles de educación de los padres únicos
    niveles_educacion_padres = datos_combinados["Nivel de educacion de los padres"].unique()

    # Asignar un color a cada nivel de educación de los padres
    colores = ['rgb(31, 119, 180)', 'rgb(255, 127, 14)', 'rgb(44, 160, 44)', 'rgb(214, 39, 40)', 'rgb(148, 103, 189)']

    # Crear una lista vacía para almacenar los promedios de notas por nivel de educación de los padres
    promedios_notas = []

    # Crear el gráfico de barras
    fig = go.Figure()

    for nivel_educacion, color in zip(niveles_educacion_padres, colores):
        df_nivel_educacion = datos_combinados[datos_combinados["Nivel de educacion de los padres"] == nivel_educacion]
        
        # Calcular el promedio de notas para el nivel de educación de los padres actual
        promedio_notas = df_nivel_educacion["Puntuacion"].mean()
        
        # Agregar el promedio de notas a la lista de promedios
        promedios_notas.append(promedio_notas)
        
        # Configurar el texto para mostrar en la punta de la barra
        text = f'Promedio: {promedio_notas:.2f}'
        
        # Agregar la barra al gráfico sin leyenda
        fig.add_trace(go.Bar(x=[nivel_educacion], y=[promedio_notas], marker=dict(color=color), text=text, textposition='outside', showlegend=False))

    # Actualizar etiquetas de los ejes
    fig.update_xaxes(title_text='Nivel de Educación de los Padres')
    fig.update_yaxes(title_text='Promedio de Notas')

    # Actualizar diseño de la figura
    fig.update_layout(title='<b>Promedio de Notas en Relación al Nivel de Educación de los Padres</b>',title_font=dict(size=18), title_x=0.5)

    # Mostrar el gráfico
    return fig 


#11
def Distribución_de_tipos_de_alumnos_por_tipo_de_almuerzo():
    fig = px.histogram(datos_combinados, x="almuerzo", color="almuerzo", title="Distribución de tipos de alumnos por tipo de almuerzo")
    fig.update_layout(barmode="group")
    return fig 

#12

    
def almerzo_en_relacion_a_notas():
    # Obtener los tipos de almuerzo únicos
    tipos_almuerzo = datos_combinados["almuerzo"].unique()

    # Asignar un color a cada tipo de almuerzo
    colores = ['rgb(31, 119, 180)', 'rgb(255, 127, 14)', 'rgb(44, 160, 44)', 'rgb(214, 39, 40)', 'rgb(148, 103, 189)']

    # Crear una lista vacía para almacenar los promedios de notas por tipo de almuerzo
    promedios_notas = []

    # Crear el gráfico de barras
    fig = go.Figure()

    for tipo_almuerzo, color in zip(tipos_almuerzo, colores):
        df_tipo_almuerzo = datos_combinados[datos_combinados["almuerzo"] == tipo_almuerzo]
        
        # Calcular el promedio de notas para el tipo de almuerzo actual
        promedio_notas = df_tipo_almuerzo["Puntuacion"].mean()
        
        # Agregar el promedio de notas a la lista de promedios
        promedios_notas.append(promedio_notas)
        
        # Configurar el texto para mostrar en la punta de la barra
        text = f'Promedio: {promedio_notas:.2f}'
        
        # Agregar la barra al gráfico sin leyenda
        fig.add_trace(go.Bar(x=[tipo_almuerzo], y=[promedio_notas], marker=dict(color=color), text=text, textposition='outside', showlegend=False))

    # Actualizar etiquetas de los ejes
    fig.update_xaxes(title_text='Tipo de Almuerzo')
    fig.update_yaxes(title_text='Promedio de Notas')

    # Actualizar diseño de la figura
    fig.update_layout(title='<b>Promedio de Notas en Relación al Tipo de Almuerzo</b>', title_font=dict(size=18), title_x=0.5)

    # Mostrar el gráfico
    return fig 


#13
def promedio_de_notas_segun_cursos_preparacion ():

    # Obtener los cursos de preparación para exámenes únicos
    cursos_preparacion = datos_combinados["Curso de preparacion para examenes"].unique()

    # Asignar un color a cada curso de preparación para exámenes
    colores = ['rgb(31, 119, 180)', 'rgb(255, 127, 14)', 'rgb(44, 160, 44)', 'rgb(214, 39, 40)', 'rgb(148, 103, 189)']

    # Crear una lista vacía para almacenar los promedios de notas por curso de preparación
    promedios_notas = []

    # Crear el gráfico de barras
    fig = go.Figure()

    for curso, color in zip(cursos_preparacion, colores):
        df_curso = datos_combinados[datos_combinados["Curso de preparacion para examenes"] == curso]
        
        # Calcular el promedio de notas para el curso de preparación actual
        promedio_notas = df_curso["Puntuacion"].mean()
        
        # Agregar el promedio de notas a la lista de promedios
        promedios_notas.append(promedio_notas)
        
        # Configurar el texto para mostrar en la punta de la barra
        text = f'Promedio: {promedio_notas:.2f}'
        
        # Agregar la barra al gráfico sin leyenda
        fig.add_trace(go.Bar(x=[curso], y=[promedio_notas], marker=dict(color=color), text=text, textposition='outside', showlegend=False))

    # Actualizar etiquetas de los ejes
    fig.update_xaxes(title_text='Curso de Preparación para Exámenes')
    fig.update_yaxes(title_text='Promedio de Notas')

    # Actualizar diseño de la figura
    fig.update_layout(title='<b>Promedio de Notas en Relación al Curso de Preparación para Exámenes</b>', title_font=dict(size=18), title_x=0.5)

    # Mostrar el gráfico
    return fig 


lab1="Distribución de los tipos de aprendizaje"
lab2="Distribución de los tipos de aprendizaje por género"
lab3="Dispersión de las calificaciones según el tipo de aprendizaje"
lab4="Distribucion de Tipos de aprendizaje"
lab5="Distribucion de Estudiantes por Edad"
lab6="Distribucion de Aprendizaje por Edad"
lab7="Combinado distribucion edades tipo aprendizaje"
lab8="Tortas Varios"
lab9="Promedio de notas por area  segun aprendizaje"
lab10="Promedio notas segun grado de aprendisaje de Padres"
lab11="Distribucion alumnos segun tipo de almuerzo"
lab12="Promedio de notas tipo de almuerzo"
lab13="Graficco Promedio de notas hicieron o  no   Segun Curso de Preparacion"



 # backgroundColor: #ccc;  fontSize: 14px;   textAlign: center;



# Crear una aplicación Dash
app = dash.Dash(__name__)

# Define el diseño del tablero
app.layout = html.Div([
     
    html.H1("Dashboard Estudiantes",style={"text-align": "center"} ),

    dcc.Tabs(id='tabs', value='tab-1', children=[
        dcc.Tab(label=lab1, value='tab-1' , style={"font-size": "11px",'text-align': 'center','backgroundColor': '#A5CAF9'}),
        dcc.Tab(label=lab2, value='tab-2', style={"font-size": "11px",'text-align':  'center','backgroundColor': '#A5CAF9'}),
        dcc.Tab(label=lab3, value='tab-3', style={"font-size": "11px",'text-align':  'center','backgroundColor': '#A5CAF9'}),
        dcc.Tab(label=lab4, value='tab-4', style={"font-size": "11px",'text-align':  'center','backgroundColor': '#A5CAF9'}),
        dcc.Tab(label=lab5, value='tab-5', style={"font-size": "11px",'text-align':  'center','backgroundColor': '#A5CAF9'}),
        dcc.Tab(label=lab6, value='tab-6', style={"font-size": "11px",'text-align':  'center','backgroundColor': '#A5CAF9'}),
        dcc.Tab(label=lab7, value='tab-7', style={"font-size": "11px",'text-align':  'center','backgroundColor': '#A5CAF9'}),
        dcc.Tab(label=lab8, value='tab-8', style={"font-size": "11px",'text-align':  'center','backgroundColor': '#A5CAF9'}),
        dcc.Tab(label=lab9, value='tab-9', style={"font-size": "11px",'text-align':  'center','backgroundColor': '#A5CAF9'}),
        dcc.Tab(label=lab6, value='tab-10', style={"font-size": "11px",'text-align':  'center','backgroundColor': '#A5CAF9'}),
        dcc.Tab(label=lab7, value='tab-11', style={"font-size": "11px",'text-align':  'center','backgroundColor': '#A5CAF9'}),
        dcc.Tab(label=lab8, value='tab-12', style={"font-size": "11px",'text-align':  'center','backgroundColor': '#A5CAF9'}),
        dcc.Tab(label=lab9, value='tab-13', style={"font-size": "11px",'text-align':  'center','backgroundColor': '#A5CAF9'})
    ]),

    html.Div(id='tabs-content')
 
])



# Callback para actualizar el contenido de las pestañas
@app.callback(Output('tabs-content', 'children'), [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3(lab1,style={"font-size": "14px",'text-align': 'center'}),
            dcc.Graph(
                figure=plot_tipo_aprendizaje()
            )
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3(lab2,style={"font-size": "14px",'text-align': 'center'}),
            dcc.Graph(
                figure=plot_tipo_aprendizaje_genero()
            )
        ])
        
    elif tab == 'tab-3':
        return html.Div([
            html.H3(lab3,style={"font-size": "14px",'text-align': 'center'}),
            dcc.Graph(
                figure=plot_calificaciones_tipo_aprendizaje()
            )
        ])
    elif tab == 'tab-4':
        return html.Div([
            html.H3(lab4,style={"font-size": "14px",'text-align': 'center'}),
            dcc.Graph(
                figure=plot_proporcion_tipo_aprendizaje()
            )
        ])
    elif tab == 'tab-5':
        return html.Div([
            html.H3(lab5,style={"font-size": "14px",'text-align': 'center'}),
            dcc.Graph(
                figure=plot_distribucion_edades()
            )
        ])
    elif tab == 'tab-6':
        return html.Div([
            html.H3(lab6,style={"font-size": "14px",'text-align': 'center'}),
            dcc.Graph(
                figure=plot_tipo_aprendizaje_por_edad()
            )
        ])
    elif tab == 'tab-7':
        return html.Div([
            html.H3(lab7,style={"font-size": "14px",'text-align': 'center'}),
            dcc.Graph(
                figure=plot_combinado_distribucion_edades_tipo_aprendizaje()
            )
        ])
    elif tab == 'tab-8':
        return html.Div([
            html.H3(lab8,style={"font-size": "14px",'text-align': 'center'}),
            dcc.Graph(
                figure=varios_tortas()
            )
        ])
    elif tab == 'tab-9':
        return html.Div([
            html.H3(lab9,style={"font-size": "14px",'text-align': 'center'}),
            dcc.Graph(
                figure=promedio_de_notas_de_areas_por_tipo_de_aprendisaje()
            )
        ])
    elif tab == 'tab-10':
        return html.Div([
            html.H3(lab10,style={"font-size": "14px",'text-align': 'center'}),
            dcc.Graph(
                figure=promedio_de_notas_de_areas_por_tipo_de_aprendisaje()
            )
        ])
    elif tab == 'tab-11':
        return html.Div([
            html.H3(lab11,style={"font-size": "14px",'text-align': 'center'}),
            dcc.Graph(
                figure=Distribución_de_tipos_de_alumnos_por_tipo_de_almuerzo()
            )
        ])
    elif tab == 'tab-12':
        return html.Div([
            html.H3(lab12,style={"font-size": "14px",'text-align': 'center'}),
            dcc.Graph(
                figure=almerzo_en_relacion_a_notas()
            )
        ])
    elif tab == 'tab-13':
        return html.Div([
            html.H3(lab13,style={"font-size": "14px",'text-align': 'center'}),
            dcc.Graph(
                figure=promedio_de_notas_segun_cursos_preparacion ()
            )
        ])

if __name__ == '__main__':
   open_browser()
    # app.run_server(debug=True)
