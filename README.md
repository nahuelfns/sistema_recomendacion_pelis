Tabla de contenido
1.	Descripción
2.	Instalación y Requisitos
3.	Estructura del Proyecto
4.	Uso y Ejecución
5.	Datos y Fuentes
6.	Metodología
7.	Resultados y Conclusiones
Descripción
Este proyecto tiene como objetivo analizar títulos de películas y sus promedios de votos para recomendarle al usuario largometrajes parecidos según la búsqueda del mismo. Usando técnicas de ciencia de datos, se genera una lista de cinco posibles películas que el espectador pueda encontrar de su gusto.
Instalación y Requisitos
Requisitos:
•	Python 3.9 o superior
•	pandas
•	numpy
•	matplotlib
•	scikit-learn
Pasos de instalación:
1.	Clonar el repositorio: git clone https://github.com/nahuelfns/Primer_proyecto_individual
2.	Crear un entorno virtual: python -m venv venv
3.	Activar el entorno virtual:
o	Windows: venv\Scripts\activate
o	macOS/Linux: source venv/bin/activate
4.	Instalar las dependencias: pip install -r requirements.txt

Estructura del Proyecto
•	Datasets: Contiene los archivos de datos.
•	notebooks: Jupyter notebooks con el análisis.
•	Main.py: contiene las funciones que se ejecutaran
•	Requirements.txt: contiene las dependencias a instalar 
•	README.md: descripción del proyecto
Uso y Ejecución
1.	Ejecutar Transformaciones.ipynb en notebooks/ para transformaciones.
2.	Ejecutar EDA.ipynb en notebooks/ para análisis.
Datos y Fuentes
Datos proporcionados dentro del mismo proyecto que incluyen datos de películas, sus elencos y equipos técnicos
Metodología
Se aplicaron conversión a vectores y similitud de cosenos para recomendar títulos de películas
Resultados y Conclusiones
•	Según el peso que se le asignen a los títulos y puntuaciones y la cantidad de peliculas en el data set las recomendaciones varían para mejor o no.
•	A mayor cantidad de datos, mas precisas son las recomendaciones.
•	A mayor peso en los títulos mas parecidos son estos con el ingresado.
Autores
Facundo Serqueira - Contacto: LinkedIn.
