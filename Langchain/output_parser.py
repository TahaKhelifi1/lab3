# output_parser.py
from pydantic import BaseModel, Field

# Modèle de film
class Movie(BaseModel):
    title: str = Field(description="The title of the movie.")
    genre: list[str] = Field(description="The genre of the movie.")
    year: int = Field(description="The year the movie was released.")

# Parser de sortie utilisant Pydantic
from langchain.output_parsers import PydanticOutputParser

parser = PydanticOutputParser(pydantic_object=Movie)

def parse_movie_output(output: str):
    return parser.parse(output)
