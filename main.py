import pandas as pd
from fastapi import FastAPI
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.preprocessing import StandardScaler
import numpy as np

app = FastAPI()

df = pd.read_csv(r'C:\Users\nahue\Searches\Escritorio\CARRERA HENRY\Primer_proyecto_individual\Datasets\movies_dataset_transf.csv',low_memory=False) 
df_get_actor = pd.read_csv(r'Datasets/df_para_funcion_get_actor.csv',low_memory=False)
df_get_director = pd.read_csv(r'Datasets/df_para_funcion_get_director.csv',low_memory=False)
df_para_recomendacion = pd.read_csv(r'C:\Users\nahue\Searches\Escritorio\CARRERA HENRY\Primer_proyecto_individual\Datasets\df_para_recomendacion.csv', low_memory=False)

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matriz = tfidf.fit_transform(df_para_recomendacion['title'].str.lower())

sim_coseno = linear_kernel(tfidf_matriz, tfidf_matriz)
scaler = StandardScaler()
votos_norm = scaler.fit_transform(df_para_recomendacion[['vote_average']])

@app.get("/cantidad_filmaciones_mes/{mes}")
def cantidad_filmaciones_mes(mes: str) -> int:
    df['release_date'] = pd.to_datetime(df['release_date'])
    
    meses = {
        'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4,
        'mayo': 5, 'junio': 6, 'julio': 7, 'agosto': 8,
        'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12
    }
    mes_num = meses.get(mes.lower())
   
    if mes_num:
        return len(df[df['release_date'].dt.month == mes_num])
    return 0

@app.get("/cantidad_filmaciones_dia/{dia}")
def cantidad_filmaciones_dia(dia: str):
    df['release_date'] = pd.to_datetime(df['release_date'])
    
    dias_semana = {
        'lunes': 0, 'martes': 1, 'miercoles': 2, 'jueves': 3,
        'viernes': 4, 'sabado': 5, 'domingo': 6
    }
    dia_num = dias_semana.get(dia.lower())
    if dia_num is not None:
        return len(df[df['release_date'].dt.dayofweek == dia_num])
    return 0

@app.get("/score_titulo/{titulo}")
def score_titulo(titulo: str):
    df['release_date'] = pd.to_datetime(df['release_date'])
    
    pelicula = df[df['title'].str.lower() == titulo.lower()]
    
    if not pelicula.empty:
        titulo = pelicula['title'].values[0]
        anio_estreno = pelicula['release_date'].dt.year.values[0]
        popularidad = pelicula['popularity'].values[0]
        
        return f"La película {titulo} fue estrenada en el año {anio_estreno} con un score/popularidad de {popularidad}"
    else:
        return f"No se encontró la película con el título {titulo}"

@app.get("/votos_titulo/{titulo}")
def votos_titulo(titulo: str):
    pelicula = df[df['title'].str.lower() == titulo.lower()]
    
    if not pelicula.empty:
        titulo = pelicula['title'].values[0]
        cantidad_votos = pelicula['vote_count'].values[0]
        promedio_votos = pelicula['vote_average'].values[0]
        
        if cantidad_votos >= 2000:
            return f"La película {titulo} cuenta con un total de {cantidad_votos} valoraciones, con un promedio de {promedio_votos}"
        else:
            return f"La película {titulo} no cumple con la condición de tener al menos 2000 valoraciones. Tiene un total de {cantidad_votos} valoraciones."
    else:
        return f"No se encontró la película con el título {titulo}"

@app.get("/get_actor/{nombre_actor}")
def get_actor(nombre_actor):
    df_actor = df_get_actor[df_get_actor['actor'].str.lower() == nombre_actor.lower()]
    cantidad_peliculas = df_actor.shape[0]
    retorno_total = df_actor['return'].sum()
    promedio_retorno = df_actor['return'].mean()
    
    resultado = (
        f"El actor {nombre_actor} ha participado de {cantidad_peliculas} cantidad de filmaciones, "
        f"el mismo ha conseguido un retorno de {retorno_total} con un promedio de {promedio_retorno:.2f} por filmación"
    )
    
    return resultado

@app.get("/get_director/{nombre_director}")
def get_director(nombre_director):
    df_director = df_get_director[df_get_director['director'].str.lower() == nombre_director.lower()]
    retorno_total = df_director['return'].sum()
    
    peliculas_info = []
    for index, row in df_director.iterrows():
        pelicula = {
            'title': row['title'],
            'release_date': row['release_date'],
            'return': row['return'],
            'budget': row['budget'],
            'revenue': row['revenue']
        }
        peliculas_info.append(pelicula)
    
    peliculas_str = "\n".join([f"Película: {p['title']}, Fecha de lanzamiento: {p['release_date']}, Retorno: {p['return']}, Costo: {p['budget']}, Ganancia: {p['revenue']}" for p in peliculas_info])
    
    resultado = (
        f"El director {nombre_director} ha conseguido un retorno total de {retorno_total}.\n"
        f"Ha dirigido las siguientes películas:\n{peliculas_str}"
    )
    
    return resultado

@app.get("/recomendacion/{titulo}")
def recomendacion(titulo: str):
    titulo = titulo.lower()
    idx = df_para_recomendacion[df_para_recomendacion['title'].str.lower() == titulo].index[0]
    sim_scores = list(enumerate(sim_coseno[idx]))

    sim_scores = [(i, score * 0.5 + votos_norm[i] * 0.5 + np.random.normal(0, 0.01)) for i, score in sim_scores]
    
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
 
    sim_scores = sim_scores[1:6]
    pelicula_indices = [i[0] for i in sim_scores]

    return df_para_recomendacion['title'].iloc[pelicula_indices].values.tolist()
