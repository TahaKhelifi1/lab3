# prompt_template.py
from langchain.prompts import PromptTemplate

# Modèle d'invite pour générer des titres de repas
prompt_template = PromptTemplate.from_template(
    "List {n} cooking/meal titles for {cuisine} cuisine (name only)."
)

def create_prompt(n: int, cuisine: str):
    return prompt_template.format(n=n, cuisine=cuisine)
