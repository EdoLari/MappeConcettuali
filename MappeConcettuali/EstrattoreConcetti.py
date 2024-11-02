import openai
import networkx as nx # type: ignore
import matplotlib.pyplot as plt # type: ignore

openai.api_key = "#YOUR_CHAT-GTP_KEYS"  # Sostituisci con la tua chiave API

def estrai_concetti_e_relazioni(testo):
    prompt = f"Analizza il seguente testo e identifica i concetti principali e le relazioni tra essi in formato lista di coppie. Testo: {testo}"
    
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=150,
        temperature=0.3,
        n=1,
        stop=None
    )
    
    # Parsing the response for pairs of concepts
    result = response.choices[0].text.strip()
    concept_pairs = eval(result)  # Converte la stringa in una lista di coppie
    
    return concept_pairs
