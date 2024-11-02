from EstrattoreConcetti import estrai_concetti_e_relazioni

def crea_mappa_concettuale(concept_pairs):
    G = nx.Graph() # type: ignore
    
    # Aggiunge i nodi e gli archi al grafo
    for pair in concept_pairs:
        G.add_edge(pair[0], pair[1])

    # Visualizza il grafo
    plt.figure(figsize=(12, 8)) # type: ignore
    pos = nx.spring_layout(G) # type: ignore
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=2000, font_size=10, font_weight="bold", edge_color="gray") # type: ignore
    plt.title("Mappa Concettuale") # type: ignore
    plt.show() # type: ignore

# Esempio di utilizzo
testo = "La fotosintesi è un processo attraverso il quale le piante trasformano la luce solare in energia. Include la trasformazione dell'anidride carbonica e dell'acqua in ossigeno e glucosio."
concetti_relazioni = estrai_concetti_e_relazioni(testo)
crea_mappa_concettuale(concetti_relazioni)
