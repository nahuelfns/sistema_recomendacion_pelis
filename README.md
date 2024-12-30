# Sistema de recomendación de películas

## Tabla de contenido

1.	Descripción
2.	Requisitos, Instalación y ejecución
3.	Estructura del Proyecto
4.	Uso
5.	Datos y Fuentes
6.	Metodología
7.	Resultados y Conclusiones
8.	Visualizaciones
9.	Licencia
10.	Despliegue en Render
11.	Autor

## Descripción

Este proyecto desarrolla un sistema de recomendación de películas que combina técnicas de análisis de datos, visualizaciones y modelos de Machine Learning para ofrecer recomendaciones personalizadas basadas en la similitud de películas. Además, se implementa una API con FastAPI para disponibilizar datos clave y funcionalidades relacionadas con películas, actores y directores.

## Requisitos, Instalación y ejecución

Requisitos:
+	Python 3.8 o superior
+	pandas
+	numpy
+	matplotlib
+	scikit-learn
+	fastapi
+	uvicorn
+	wordcloud
+	seaborn

Pasos de instalación y ejecución

1.	Clonar el repositorio: git clone https://github.com/nahuelfns/Primer_proyecto_individual.git
cd Primer_proyecto_individual
2.	Crear un entorno virtual: python -m venv venv
3.	Activar el entorno virtual:
o	Windows: venv\Scripts\activate
o	macOS/Linux: source venv/bin/activate
4.	Instalar las dependencias: pip install -r requirements.txt
5. Inicia el servidor FastAPI con uvicorn: uvicorn main:app --reload
6. Accede a la documentación interactiva de la API en http://127.0.0.1:8000/docs

## Estructura del Proyecto

+	Datasets: Contiene los archivos de datos.
+	notebooks: Jupyter notebooks con el análisis de datos y desarrollos de las funciones para la API.
+	Main.py: contiene los endpoints de la API
+	Requirements.txt: contiene las dependencias a instalar 
+	README.md: descripción del proyecto

## Uso

1. cantidad_filmaciones_mes(mes)
Devuelve la cantidad de películas estrenadas en el mes especificado (en español).

Ejemplo:

Entrada: mes = "Enero"
Salida: "X películas fueron estrenadas en el mes de Enero"

2. cantidad_filmaciones_dia(dia)
Devuelve la cantidad de películas estrenadas en el día especificado (en español).

Ejemplo:

Entrada: dia = "Lunes"
Salida: "X películas fueron estrenadas en los días Lunes"

3. score_titulo(titulo)
Devuelve el título, año de estreno y score de una película.

Ejemplo:

Entrada: titulo = "Hamlet"
Salida: "La película Hamlet fue estrenada en el año 1996 con un score/popularidad de 9.994088"

4. votos_titulo(titulo)
Devuelve el título, cantidad de votos y promedio de votaciones. Si tiene menos de 2000 votos, se emite un mensaje indicando que no cumple con el criterio.

Ejemplo:

Entrada: titulo = "Toy Story"
Salida: "La película Toy Story cuenta con un total de 5415.0 valoraciones, con un promedio de 7.7"

5. get_actor(nombre_actor)
Devuelve el número de películas en las que participó un actor, su retorno total y el promedio de retorno por película.

Ejemplo:

Entrada: nombre_actor = "Frank Welker"
Salida: "El actor Frank Welker ha participado de 33 cantidad de filmaciones, el mismo ha conseguido un retorno de 158.51834432334533 con un promedio de 4.80 por filmación"

6. get_director(nombre_director)
Devuelve el éxito de un director, mostrando el nombre de cada película, fecha de lanzamiento, retorno individual, costo y ganancia.

Ejemplo:

Entrada: nombre_director = "Joe Johnston"
El director Joe Johnston ha conseguido un retorno total de 12.985677228968255.
Ha dirigido las siguientes películas:
Película: Jumanji, Fecha de lanzamiento: 1995-12-15, Retorno: 4.0430346, Costo: 65000000.0, Ganancia: 262797249.0
Película: The Pagemaster, Fecha de lanzamiento: 1994-11-23, Retorno: 0.5063217777777778, Costo: 27000000.0, Ganancia: 13670688.0
Película: Honey, I Shrunk the Kids, Fecha de lanzamiento: 1989-06-22, Retorno: 6.960130375, Costo: 32000000.0, Ganancia: 222724172.0
Película: The Rocketeer, Fecha de lanzamiento: 1991-06-21, Retorno: 1.4761904761904765, Costo: 42000000.0, Ganancia: 62000000.0

7. recomendacion(titulo)
Recomienda 5 películas similares al título ingresado, ordenadas por similitud de puntuación.

Ejemplo:

Entrada: titulo = "Batman"
Salida: ["Batman Returns", "Batman Forever", "Batman & Robin", "Girl in the Cadillac", "Reckless"]

## Datos y Fuentes

Datos proporcionados dentro del mismo proyecto que incluyen datos de películas, sus elencos y equipos técnicos

## Metodología

Se aplicaron conversión a vectores y similitud de cosenos para recomendar títulos de películas

## Resultados y Conclusiones

+	Según el peso que se le asignen a los títulos y puntuaciones y la cantidad de peliculas en el data set las recomendaciones varían para mejor o no.
+	A mayor cantidad de datos, mas precisas son las recomendaciones.
+	A mayor peso en los títulos mas parecidos son estos con el ingresado.

## Visualizaciones

El EDA incluye:

+ Nubes de palabras: Palabras más frecuentes en los títulos de las películas.
+ Distribuciones: Tendencias de puntuación, votaciones, y géneros más populares.
+ Gráficos interactivos: Análisis en profundidad del dataset.

## Licencia

Este proyecto está bajo la MIT License, permitiendo su uso, modificación y distribución.

## Despliegue en Render

La API ha sido desplegada en Render, asegurando su disponibilidad para consultas y aplicaciones de terceros.

## Despliegue en Render 🚀

La API ha sido desplegada en Render y está disponible en el siguiente enlace:

**https://primer-proyecto-individual-henry.onrender.com**

### Cómo desplegar la API en Render

Para desplegar esta API en Render, sigue los pasos a continuación:

1. **Crea una cuenta en [Render](https://render.com)**.
2. **Conecta tu repositorio** de GitHub o GitLab con Render.
3. **Configura el servicio**:
   - Elige la opción **"Web Service"**.
   - Selecciona el repositorio del proyecto.
   - Especifica el comando de inicio en "Start Command":
     ```bash
     uvicorn main:app --host 0.0.0.0 --port 10000
     ```
   - Configura el entorno como `Python 3.x` y selecciona el archivo `requirements.txt` para las dependencias.
4. **Despliega**: Render configurará automáticamente el entorno y desplegará la API.
5. Una vez desplegada, obtendrás un enlace público donde estará disponible la API.

Puedes acceder a la documentación interactiva en:  
`https://primer-proyecto-individual-henry.onrender.com/docs`


## Autor
Facundo Serqueira - Contacto: https://www.linkedin.com/in/facundo-nahuel-serqueira-aba554b/
