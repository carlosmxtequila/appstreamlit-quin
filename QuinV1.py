import streamlit as st
import pandas as pd
import csv
from datetime import datetime
import os

# --------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# --------------------------------------------------

st.set_page_config(
    page_title="Quiniela Mundial FIFA 2026",
    page_icon="🏆",
    layout="wide"
)

# --------------------------------------------------
# ESTILOS
# --------------------------------------------------

st.markdown("""
<style>

.main-title{
    text-align:center;
    color:#004aad;
    font-size:40px;
    font-weight:bold;
}

.match-row{
    padding:10px;
    border-radius:10px;
    background-color:#f7f7f7;
    margin-bottom:10px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# PARTIDOS DE LA SEMANA
# --------------------------------------------------
# Sustituir por los juegos reales de cada jornada

SEMANA_1 = [
{"fecha":"Jueves 11 de junio","local":" México","visitante":"Sudáfrica "},
{"fecha":"Jueves 11 de junio","local":" República de Corea","visitante":"República Checa "},
{"fecha":"Viernes 12 de junio","local":" Canadá","visitante":"Bosnia y Herzegovina "},
{"fecha":"Viernes 12 de junio","local":" Estados Unidos","visitante":"Paraguay "},
{"fecha":"Sábado 13 de junio","local":" Catar","visitante":"Suiza "},
{"fecha":"Sábado 13 de junio","local":" Brasil","visitante":"Marruecos "},
{"fecha":"Sábado 13 de junio","local":" Haití","visitante":"Escocia "},
{"fecha":"Sábado 13 de junio","local":" Australia","visitante":"Turquía "},
{"fecha":"Domingo 14 de junio","local":" Alemania","visitante":"Curazao "},
{"fecha":"Domingo 14 de junio","local":" Países Bajos","visitante":"Japón "},
{"fecha":"Domingo 14 de junio","local":" Costa de Marfil","visitante":"Ecuador "},
{"fecha":"Domingo 14 de junio","local":" Suecia","visitante":"Túnez "}
]
SEMANA_2 = [
{"fecha":"Lunes 15 de junio","local":" España","visitante":"Cabo Verde "},
{"fecha":"Lunes 15 de junio","local":" Bélgica","visitante":"Egipto "},
{"fecha":"Lunes 15 de junio","local":" Arabia Saudí","visitante":"Uruguay "},
{"fecha":"Lunes 15 de junio","local":" Irán","visitante":"Nueva Zelanda "},
{"fecha":"Martes 16 de junio","local":" Francia","visitante":"Senegal "},
{"fecha":"Martes 16 de junio","local":" Irak","visitante":"Noruega "},
{"fecha":"Martes 16 de junio","local":" Argentina","visitante":"Argelia "},
{"fecha":"Martes 16 de junio","local":" Austria","visitante":"Jordania "},
{"fecha":"Miércoles 17 de junio","local":" Portugal","visitante":"RD Congo "},
{"fecha":"Miércoles 17 de junio","local":" Inglaterra","visitante":"Croacia "},
{"fecha":"Miércoles 17 de junio","local":" Ghana","visitante":"Panamá "},
{"fecha":"Miércoles 17 de junio","local":" Uzbekistán","visitante":"Colombia "},
{"fecha":"Jueves 18 de junio","local":" República Checa","visitante":"Sudáfrica "},
{"fecha":"Jueves 18 de junio","local":" Suiza","visitante":"Bosnia y Herzegovina "},
{"fecha":"Jueves 18 de junio","local":" Canadá","visitante":"Catar "},
{"fecha":"Jueves 18 de junio","local":" México","visitante":"República de Corea "},
{"fecha":"Viernes 19 de junio","local":" Estados Unidos","visitante":"Australia "},
{"fecha":"Viernes 19 de junio","local":" Escocia","visitante":"Marruecos "},
{"fecha":"Viernes 19 de junio","local":" Brasil","visitante":"Haití "},
{"fecha":"Viernes 19 de junio","local":" Turquía","visitante":"Paraguay "},
{"fecha":"Sábado 20 de junio","local":" Países Bajos","visitante":"Suecia "},
{"fecha":"Sábado 20 de junio","local":" Alemania","visitante":"Costa de Marfil "},
{"fecha":"Sábado 20 de junio","local":" Ecuador","visitante":"Curazao "},
{"fecha":"Sábado 20 de junio","local":" Túnez","visitante":"Japón "},
{"fecha":"Domingo 21 de junio","local":" España","visitante":"Arabia Saudí "},
{"fecha":"Domingo 21 de junio","local":" Bélgica","visitante":"Irán "},
{"fecha":"Domingo 21 de junio","local":" Uruguay","visitante":"Cabo Verde "},
{"fecha":"Domingo 21 de junio","local":" Nueva Zelanda","visitante":"Egipto "}
]
SEMANA_3 = [
{"fecha":"Lunes 22 de junio","local":" Argentina","visitante":"Austria "},
{"fecha":"Lunes 22 de junio","local":" Francia","visitante":"Irak "},
{"fecha":"Lunes 22 de junio","local":" Noruega","visitante":"Senegal "},
{"fecha":"Lunes 22 de junio","local":" Jordania","visitante":"Argelia "},
{"fecha":"Martes 23 de junio","local":" Portugal","visitante":"Uzbekistán "},
{"fecha":"Martes 23 de junio","local":" Inglaterra","visitante":"Ghana "},
{"fecha":"Martes 23 de junio","local":" Panamá","visitante":"Croacia "},
{"fecha":"Martes 23 de junio","local":" Colombia","visitante":"RD Congo "},
{"fecha":"Miércoles 24 de junio","local":" Suiza","visitante":"Canadá "},
{"fecha":"Miércoles 24 de junio","local":" Bosnia y Herzegovina","visitante":"Catar "},
{"fecha":"Miércoles 24 de junio","local":" Escocia","visitante":"Brasil "},
{"fecha":"Miércoles 24 de junio","local":" Marruecos","visitante":"Haití "},
{"fecha":"Miércoles 24 de junio","local":" República Checa","visitante":"México "},
{"fecha":"Miércoles 24 de junio","local":" Sudáfrica","visitante":"República de Corea "},
{"fecha":"Jueves 25 de junio","local":" Curazao","visitante":"Costa de Marfil "},
{"fecha":"Jueves 25 de junio","local":" Ecuador","visitante":"Alemania "},
{"fecha":"Jueves 25 de junio","local":" Japón","visitante":"Suecia "},
{"fecha":"Jueves 25 de junio","local":" Túnez","visitante":"Países Bajos "},
{"fecha":"Jueves 25 de junio","local":" Turquía","visitante":"Estados Unidos "},
{"fecha":"Jueves 25 de junio","local":" Paraguay","visitante":"Australia "},
{"fecha":"Viernes 26 de junio","local":" Noruega","visitante":"Francia "},
{"fecha":"Viernes 26 de junio","local":" Senegal","visitante":"Irak "},
{"fecha":"Viernes 26 de junio","local":" Cabo Verde","visitante":"Arabia Saudí "},
{"fecha":"Viernes 26 de junio","local":" Uruguay","visitante":"España "},
{"fecha":"Viernes 26 de junio","local":" Egipto","visitante":"Irán "},
{"fecha":"Viernes 26 de junio","local":" Nueva Zelanda","visitante":"Bélgica "},
{"fecha":"Sábado 27 de junio","local":" Panamá","visitante":"Inglaterra "},
{"fecha":"Sábado 27 de junio","local":" Croacia","visitante":"Ghana "},
{"fecha":"Sábado 27 de junio","local":" Colombia","visitante":"Portugal "},
{"fecha":"Sábado 27 de junio","local":" RD Congo","visitante":"Uzbekistán "},
{"fecha":"Sábado 27 de junio","local":" Argelia","visitante":"Austria "},
{"fecha":"Sábado 27 de junio","local":" Jordania","visitante":"Argentina "}
]
DIECISEISAVOS = [
{"fecha":"Domingo 28 de junio","local":" 2° Grupo A","visitante":"2° Grupo B "},
{"fecha":"Lunes 29 de junio","local":" 1° Grupo E","visitante":"Mejor Tercero "},
{"fecha":"Lunes 29 de junio","local":" 1° Grupo F","visitante":"2° Grupo C "},
{"fecha":"Lunes 29 de junio","local":" 1° Grupo C","visitante":"2° Grupo F "},
{"fecha":"Martes 30 de junio","local":" 1° Grupo I","visitante":"Mejor Tercero "},
{"fecha":"Martes 30 de junio","local":" 2° Grupo E","visitante":"2° Grupo I "},
{"fecha":"Martes 30 de junio","local":" 1° Grupo A","visitante":"Mejor Tercero "},
{"fecha":"Miércoles 1 de julio","local":" 1° Grupo L","visitante":"Mejor Tercero "},
{"fecha":"Miércoles 1 de julio","local":" 1° Grupo D","visitante":"Mejor Tercero "},
{"fecha":"Miércoles 1 de julio","local":" 1° Grupo G","visitante":"Mejor Tercero "},
{"fecha":"Jueves 2 de julio","local":" 2° Grupo K","visitante":"2° Grupo L "},
{"fecha":"Jueves 2 de julio","local":" 1° Grupo H","visitante":"2° Grupo J "},
{"fecha":"Jueves 2 de julio","local":" 1° Grupo B","visitante":"Mejor Tercero "},
{"fecha":"Viernes 3 de julio","local":" 1° Grupo J","visitante":"2° Grupo H "},
{"fecha":"Viernes 3 de julio","local":" 1° Grupo K","visitante":"Mejor Tercero "},
{"fecha":"Viernes 3 de julio","local":" 2° Grupo D","visitante":"2° Grupo G "}
]
OCTAVOS = [
{"fecha":"Sábado 4 de julio","local":" Ganador 74","visitante":"Ganador 77 "},
{"fecha":"Sábado 4 de julio","local":" Ganador 73","visitante":"Ganador 75 "},
{"fecha":"Domingo 5 de julio","local":" Ganador 76","visitante":"Ganador 78 "},
{"fecha":"Domingo 5 de julio","local":" Ganador 79","visitante":"Ganador 80 "},
{"fecha":"Lunes 6 de julio","local":" Ganador 83","visitante":"Ganador 84 "},
{"fecha":"Lunes 6 de julio","local":" Ganador 81","visitante":"Ganador 82 "},
{"fecha":"Martes 7 de julio","local":" Ganador 86","visitante":"Ganador 88 "},
{"fecha":"Martes 7 de julio","local":" Ganador 85","visitante":"Ganador 87 "},
]
CUARTOS = [
{"fecha":"Jueves 9 de julio","local":" Ganador 89","visitante":"Ganador 90 "},
{"fecha":"Viernes 10 de julio","local":" Ganador 93","visitante":"Ganador 94 "},
{"fecha":"Sábado 11 de julio","local":" Ganador 91","visitante":"Ganador 92 "},
{"fecha":"Sábado 11 de julio","local":" Ganador 95","visitante":"Ganador 96 "},
]
SEMIFINALES_FINALES = [
{"fecha":"Martes 14 de julio","local":" Ganador 97","visitante":"Ganador 98 "},
{"fecha":"Miércoles 15 de julio","local":" Ganador 99","visitante":"Ganador 100 "},
{"fecha":"Sábado 18 de julio","local":" Perdedor 101","visitante":"Perdedor 102 "},
{"fecha":"Domingo 19 de julio","local":" Ganador 101","visitante":"Ganador 102 "}
]

# --------------------------------------------------
# TÍTULO
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🏆 Quiniela 2026</div>',
    unsafe_allow_html=True
)

st.write("")
st.write("")

st.subheader("Visita el sitio web oficial")
st.markdown("[FIFA](https://www.fifa.com/es/tournaments/mens/worldcup/canadamexicousa2026/scores-fixtures?country=MX&wtw-filter=ALL).")


# --------------------------------------------------
# DATOS DEL PARTICIPANTE
# --------------------------------------------------
st.write("SI ya eres participante búscate en la lista y selecciona tu nombre, SI NO, date de alta abajo ")

df=pd.read_csv('quinielas/Acumulado.csv')

participantes_activos= df['Participante'].unique()
nombre="---"
nombre = st.selectbox("Selecciona tu nombre",participantes_activos)

if nombre == "---":
    nombre = st.text_input(
        "Nombre del participante",
        placeholder="Escribe tu nombre completo"
)

st.divider()

# --------------------------------------------------
# CAPTURA DE PRONÓSTICOS
# --------------------------------------------------

st.subheader("Quiniela por Semana/Fase")

# --------------------------------------------------
# CAPTURA DE ETAPA
# --------------------------------------------------

# Lista de opciones
etapas = ("SEMANA 1", "SEMANA 2", "SEMANA 3", "DIECISEISAVOS","OCTAVOS","CUARTOS","SEMIFINALES Y FINALES" )

semana_seleccionada = st.selectbox("Selecciona la Semana o Fase",etapas)

pronosticos = []
# --------------------------------------------------
# SEMANA 1
# --------------------------------------------------

if semana_seleccionada == "SEMANA 1":

    for indice, partido in enumerate(SEMANA_1):

        fecha = partido["fecha"]
        local = partido["local"]
        visitante = partido["visitante"]

        col1, col2 = st.columns([1,5])

        with col1:
            st.write(fecha)

        with col2:

            seleccion = st.radio(
                label=f"{local} vs {visitante}",
                options=[
                    "Local",
                    "Empate",
                    "Visita"
                ],
                horizontal=True,
                key=f"partido_{indice}"
            )

        pronosticos.append({
            "Fecha": fecha,
            "Local": local,
            "Visitante": visitante,
            "Pronostico": seleccion
        })
# --------------------------------------------------
# SEMANA 2
# --------------------------------------------------

if semana_seleccionada == "SEMANA 2":

    for indice, partido in enumerate(SEMANA_2):

        fecha = partido["fecha"]
        local = partido["local"]
        visitante = partido["visitante"]

        col1, col2 = st.columns([1,5])

        with col1:
            st.write(fecha)

        with col2:

            seleccion = st.radio(
                label=f"{local} vs {visitante}",
                options=[
                    "Local",
                    "Empate",
                    "Visita"
                ],
                horizontal=True,
                key=f"partido_{indice}"
            )

        pronosticos.append({
            "Fecha": fecha,
            "Local": local,
            "Visitante": visitante,
            "Pronostico": seleccion
        })
# --------------------------------------------------
# SEMANA 3
# --------------------------------------------------

if semana_seleccionada == "SEMANA 3":

    for indice, partido in enumerate(SEMANA_3):

        fecha = partido["fecha"]
        local = partido["local"]
        visitante = partido["visitante"]

        col1, col2 = st.columns([1,5])

        with col1:
            st.write(fecha)

        with col2:

            seleccion = st.radio(
                label=f"{local} vs {visitante}",
                options=[
                    "Local",
                    "Empate",
                    "Visita"
                ],
                horizontal=True,
                key=f"partido_{indice}"
            )

        pronosticos.append({
            "Fecha": fecha,
            "Local": local,
            "Visitante": visitante,
            "Pronostico": seleccion
        })
# --------------------------------------------------
# DIECISEISAVOS
# --------------------------------------------------

if semana_seleccionada == "DIECISEISAVOS":

    for indice, partido in enumerate(DIECISEISAVOS):

        fecha = partido["fecha"]
        local = partido["local"]
        visitante = partido["visitante"]

        col1, col2 = st.columns([1,5])

        with col1:
            st.write(fecha)

        with col2:

            seleccion = st.radio(
                label=f"{local} vs {visitante}",
                options=[
                    "Local",
                    "Empate",
                    "Visita"
                ],
                horizontal=True,
                key=f"partido_{indice}"
            )

        pronosticos.append({
            "Fecha": fecha,
            "Local": local,
            "Visitante": visitante,
            "Pronostico": seleccion
        })
# --------------------------------------------------
# OCTAVOS
# --------------------------------------------------

if semana_seleccionada == "OCTAVOS":

    for indice, partido in enumerate(OCTAVOS):

        fecha = partido["fecha"]
        local = partido["local"]
        visitante = partido["visitante"]

        col1, col2 = st.columns([1,5])

        with col1:
            st.write(fecha)

        with col2:

            seleccion = st.radio(
                label=f"{local} vs {visitante}",
                options=[
                    "Local",
                    "Empate",
                    "Visita"
                ],
                horizontal=True,
                key=f"partido_{indice}"
            )

        pronosticos.append({
            "Fecha": fecha,
            "Local": local,
            "Visitante": visitante,
            "Pronostico": seleccion
        })

# --------------------------------------------------
# CUARTOS
# --------------------------------------------------

if semana_seleccionada == "CUARTOS":

    for indice, partido in enumerate(CUARTOS):

        fecha = partido["fecha"]
        local = partido["local"]
        visitante = partido["visitante"]

        col1, col2 = st.columns([1,5])

        with col1:
            st.write(fecha)

        with col2:

            seleccion = st.radio(
                label=f"{local} vs {visitante}",
                options=[
                    "Local",
                    "Empate",
                    "Visita"
                ],
                horizontal=True,
                key=f"partido_{indice}"
            )

        pronosticos.append({
            "Fecha": fecha,
            "Local": local,
            "Visitante": visitante,
            "Pronostico": seleccion
        })

# --------------------------------------------------
# SEMIFINALES_FINALES
# --------------------------------------------------

if semana_seleccionada == "SEMIFINALES Y FINALES":

    for indice, partido in enumerate(SEMIFINALES_FINALES):

        fecha = partido["fecha"]
        local = partido["local"]
        visitante = partido["visitante"]

        col1, col2 = st.columns([1,5])

        with col1:
            st.write(fecha)

        with col2:

            seleccion = st.radio(
                label=f"{local} vs {visitante}",
                options=[
                    "Local",
                    "Empate",
                    "Visita"
                ],
                horizontal=True,
                key=f"partido_{indice}"
            )

        pronosticos.append({
            "Fecha": fecha,
            "Local": local,
            "Visitante": visitante,
            "Pronostico": seleccion
        })

st.divider()

# --------------------------------------------------
# NOMBRE DE CARPETA Y ARCHIVO
# --------------------------------------------------

carpeta = "quinielas"
archivo = (f"{carpeta}/Acumulado.csv")
# --------------------------------------------------
# BOTÓN GUARDAR
# --------------------------------------------------

if st.button("Guardar Quiniela"):

    if nombre.strip() == "":
        st.error("Debes capturar el nombre del participante.")
        st.stop()

    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    df = pd.DataFrame(pronosticos)

    df.insert(
        0,
        "Participante",
        nombre
    )
    df.insert(
        1,
        "Semana",
        semana_seleccionada
    )

    df.to_csv(
        archivo,
        mode='a', 
        header=False,
        index=False,
        encoding="utf-8-sig"
    )

    st.success("Quiniela registrada correctamente.")

    st.dataframe(
        df,
        use_container_width=True
    )

# Info Personal
    archivo_personal=f"{nombre.replace(' ','_')}_{timestamp}.csv"
    df=pd.read_csv(archivo)
    df=pd.read_csv(archivo)
    filtrado=df.query("Participante == @nombre")
    csv=filtrado.to_csv(index=False).encode('utf-8-sig')
#
#    with open(archivo_personal,"w") as csv:

    st.download_button(
        label="Descargar Quiniela",
        data=csv,
        file_name=os.path.basename(archivo_personal),
        mime="text/csv"
        )

# --------------------------------------------------
# DESPLIEGUE DE RESULTADOS
# --------------------------------------------------

st.subheader("Resultados")
st.write("")
st.write("")
# 1. Cargar el archivo CSV
# Reemplaza 'tus_datos.csv' por la ruta de tu archivo
df = pd.read_csv(archivo)
#df['Resultado'] = df['Resultado'].astype('Int64')

#df_filtrado = df[df['Resultado'] != 0]

# 2. Generar la tabla resumen
# Agrupar por 'Participante' y sumar los valores de 'Ventas'
subtotales = df.groupby('Participante')['Resultado'].agg(lambda x: x.astype(float).sum())

st.write(subtotales)

