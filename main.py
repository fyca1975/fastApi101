from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
# control de validaciones importar Field
from pydantic import BaseModel, Field	
from typing import Optional, List


app = FastAPI()
# para la documentacion de fastAPI, cambiar titulo y version
app.title = 'Aprendiendo fastapi'
app.version = '0.0.1'

class Movie(BaseModel):
	#id: int | None = None 
	#con typing se puede remplzar por ->
	id: Optional[int] = None
	title: str = Field(default='pelicula', min_length=5, max_length=15)
	overview: str = Field(default='Descripcion de la pelicula', min_length=15, max_length=51)
	year: int = Field(default=2001, le=2024)
	rating: float = Field(ge=1, le=10)  # abreviatura ge =  mayor igual, le =menor igual
	category: str =Field(min_length=5, max_length=20)

	# class Config:
    #     schema_extra = {
    #         "example": {
    #             "id": 1,
    #             "title": "Mi pelÃ­cula",
    #             "overview": "DescripciÃ³n de la pelÃ­cula",
    #             "year": 2022,
    #             "rating": 9.8,
    #             "category" : "AcciÃ³n"
    #         }
    #     }


# datos de prueba
movies = [
    {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	},
    {
		"id": 2,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	}
]


@app.get('/', tags=['home'])
def message():
    # return {'Hello': 'world'}
    # Si utilizamos HTMLResponse
    return HTMLResponse ('<h1>hellooo </h1> ')

# Con typing puedo devolver una lista  response_model
@app.get('/movies', tags=['movies'], response_model=List[Movie])
def get_movies() -> List[Movie]:
	#return movies
	# Lo cambio por el Jsonresponse
	return JSONResponse(content=movies)


@app.get('/movies/{id}', tags=['movie id'], response_model=Movie )
def get_movie(id: int = Path( ge=1, le=2000)) ->Movie:	
	for item in movies:
		if item['id'] == id:
			# cambio por json
			#return item
			return JSONResponse(content=item)
	return JSONResponse(content=[])

# al no colocar el parametro el lo coloca como parametro query
@app.get('/movies/', tags=['movie categoria'], response_model=Movie)
def get_movie_by_categ(categoria: str = Query(min_length=5, max_length=15 )) -> List[Movie]:
	retorna = []
	for item in movies:
		if item['category'] == categoria:
			retorna.append(item)
	return retorna

# Utilizar post
@app.post('/movies/', tags=['movies post create'], response_model=dict)
# como cambiar por esquema por pydantic
#def create_movie(id: int = Body(), title: str= Body(), overview: str= Body(), year: int= Body(), rating: float= Body() , category: str= Body() ):
def create_movie(movie: Movie)->dict:

# al utilizar el esquema con pydantic ya no va esto ->
#	movies.append({
#		"id": id,
#		"title": title,
#		"overview":overview,
#		"year": year,
#		"rating": rating,
#		"category": category
#	})
	movies.append(movie)
	return JSONResponse(content={"message":"Se registro la pelicula"})
# Utilizar put update
@app.put('/movies/{id}', tags=['movies put update'], response_model=dict)
# por pyndatic ya no ->
#def update_movie(id: int, title: str= Body(), overview: str= Body(), year: int= Body(), rating: float= Body() , category: str= Body() ):
def update_movie(id: int, movie: Movie)->dict:
	for item in movies:
		if item['id'] == id:
			item['title'] = movie.title
			item['overview'] = movie.overview
			item['year'] = movie.year
			item['rating'] = movie.rating
			item['category'] = movie.category
			return JSONResponse(content={"message":"Se modifico la pelicula"})

# Utilizar delete
@app.delete('/movies/{id}', tags=['movies delete'], response_model=dict)
def delete_movie(id: int )->dict:
	for item in movies:
		if item['id'] == id:
			movies.remove(item)
			return JSONResponse(content={"message":"Se elimino al pelicula"})