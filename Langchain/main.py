# main.py
from groq_model import get_response
from prompt_template import create_prompt
from output_parser import parse_movie_output
from agent import run_agent

# Exemple de test de génération de titres de repas
prompt = create_prompt(n=5, cuisine="Italian")
response = get_response(prompt)
print("Meal Titles Response:", response.content)

# Exemple de test d'agent pour calculs et recherches
query = "What is the population difference between TUN and ALG?"
result = run_agent(query)
print("Agent Response:", result)
