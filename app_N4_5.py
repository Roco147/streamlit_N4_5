import streamlit as st

st.title('Sistema de calificaciones')

if 'alumnos' not in st.session_state:
    st.session_state.alumnos = []
if 'notas' not in st.session_state:
    st.session_state.notas = []

st.header('Registrar alumno')
nombre = st.text_input('Nombre del alumno')
nota = st.number_input('Nota', min_value=1, max_value=10)

if st.button('Registrar'):
    nombre_limpio = nombre.strip()
    if nombre_limpio == '':
        st.error('El nombre no puede estar vacio')
    else:
        existe = False
        for a in st.session_state.alumnos:
            if a.lower() == nombre_limpio.lower():
                existe = True
        if existe:
            st.warning('El alumno ya esta registrado')
        else:
            st.session_state.alumnos.append(nombre_limpio)
            st.session_state.notas.append(nota)
            st.success('Alumno registrado')

st.header('Listado de alumnos')
if len(st.session_state.alumnos) > 0:
    st.table({
        'alumno': st.session_state.alumnos,
        'nota': st.session_state.notas
    })

    st.header('Estadisticas')
    promedio = sum(st.session_state.notas) / len(st.session_state.notas)
    nota_max = max(st.session_state.notas)
    nota_min = min(st.session_state.notas)

aprobados = 0 
desaprobados = 0
for n in st.session_state.notas:
    if n >= 7:
        aprobados += 1
    else:
        desaprobados += 1

st.write('primedio general: ', round(promedio, 2))
st.write('nota mas alta: ', nota_max)
st.write('nota mas baja: ', nota_min)
st.write('aprobados: ', aprobados)
st.write('desaprobados: ', desaprobados)

st.header("Buscar alumno")
buscar = st.text_input("Nombre a buscar")
if st.button("Buscar"):
    encontrado = False
    for i in range(len(st.session_state.alumnos)):
        if st.session_state.alumnos[i].lower() == buscar.strip().lower():
            st.write("Nota de", st.session_state.alumnos[i], ":", st.session_state.notas[i])
            encontrado = True
    if not encontrado:
        st.warning("Alumno no encontrado")

st.header("Eliminar alumno")
eliminar = st.selectbox("Seleccionar alumno", st.session_state.alumnos)
if st.button("Eliminar"):
    indice = st.session_state.alumnos.index(eliminar)
    st.session_state.alumnos.pop(indice)
    st.session_state.notas.pop(indice)
    st.success("Alumno eliminado")
    st.rerun()

else:
    st.info("Todavía no hay alumnos registrados")