import random
import string
import plotly.graph_objects as plot


# Se crea la función para generar una cadena aleatoria
def generar_cadena_aleatoria(longitud):
    letras = string.ascii_lowercase
    return ''.join(random.choice(letras) for i in range(longitud))

# Se listan los dominios comunes, para generar correos aleatorios con cada dominio
dominios_correo = ['@outlook.com','@gmail.com', '@hotmail.com', '@live.com','@yahoo.com']

# Cadena aleatoria, que será el nombre del usuario y el correo.
def generar_cadena_aleatoria(longitud):
    letras = string.ascii_lowercase
    return ''.join(random.choice(letras) for i in range(longitud))
# Lista para almacenar los datos
datos = []

# Se generan los 500.000 registros al azar
for _ in range(500000):
    nombre = generar_cadena_aleatoria(5)
    correo = generar_cadena_aleatoria(5) + random.choice(dominios_correo)
    longitud_contraseña = random.randint(5, 12)  # Generar longitud aleatoria entre 5 y 12
    contraseña = generar_cadena_aleatoria(longitud_contraseña)  # Usar longitud aleatoria
    datos.append({'name': nombre, 'email': correo, 'password': contraseña})



# Se toman los datos almacenados en la funcion datos para hacer el analisis
# print(datos[:10])
# print (len(datos))


# Se separan los correos tomando como delimitador el @, para asi poder determinar cuantos dominos unicos hay.
dominios_unicos = set(correo.split('@')[-1] for correo in [registro['email'] for registro in datos])

# Contar la frecuencia de cada dominio
frecuencia_dominios = {dominio: sum(1 for registro in datos if registro['email'].endswith(dominio)) for dominio in dominios_unicos}
print(frecuencia_dominios)
# Se realiza el gráfico con la frecuencia de cada dominio.
figdominios = plot.Figure(data=[plot.Bar(x=list(frecuencia_dominios.keys()), y=list(frecuencia_dominios.values()), marker_color='darkturquoise')])
figdominios.update_layout(title='Frecuencia de Dominios de Correo Electrónico',
                  xaxis_title='Dominios',
                  yaxis_title='Cantidad de veces que aparece el dominio',
                  xaxis=dict(type='category'),
                  yaxis=dict(type='log')
                  )

# Mostrar el gráfico
figdominios.show()