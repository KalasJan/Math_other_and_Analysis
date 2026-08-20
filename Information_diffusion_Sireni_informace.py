# rychlost sireni iformace

import networkx as nx
import matplotlib.pyplot as plt
import random

# 1) vytvoreni zakladni site
n = 270 # velikost skupiny
k = 20 # pocet sousedu
p = 0.1 # pravdepodobnost prenosu ze Skupiny 1 do skupiny 2

G = nx.watts_strogatz_graph(n=n, k=k, p=p)

# 2) pacient 0, majitel informace
infected_nodes = {0}
recovered_nodes = set()

# 3) rychlost sireni
beta = 0.2 # pravdepodobnost, ze to clovek posle dal
steps = 5 # iterace sireni informace

for step in range(steps):
    new_infections = set()
    for node in infected_nodes: # sousedy daneho cloveka
        for neighbor in G.neighbors(node):
            if neighbor not in infected_nodes and neighbor not in recovered_nodes:
                if random.random() < beta: # napr. flegmatismus
                    new_infections.add(neighbor)
    infected_nodes.update(new_infections) # aktualizace stavu
    
# kolik lidi to vi
total_known = len(infected_nodes)
total_unknown = n - total_known

procento_vi = (total_known / n) * 100
procento_vi_str = f"{procento_vi:.1f}".replace('.', ',')

procento_nevi = 100 - procento_vi
procento_nevi_str = f"{procento_nevi:.1f}".replace('.', ',')


# 4) graf a vizualizace
pos = nx.spring_layout(G, seed=42) # seed = opakovatelnost

plt.figure(figsize=(10, 6))
nx.draw_networkx_nodes(G, pos, nodelist=list(infected_nodes), node_color='red', node_size=50, label=f"Ví to {total_known} lidí ({procento_vi_str} %)")
nx.draw_networkx_nodes(G, pos, nodelist=list(set(G.nodes) - infected_nodes), node_color='lightblue', node_size=50, label=f"Neví to {total_unknown} $({procento_nevi_str}$ %)")
nx.draw_networkx_edges(G, pos, alpha=0.3, width=0.5)

plt.title(f"Simulace šíření v sociální síti o {n} lidech", fontsize=12)
plt.legend(loc="upper left")
plt.axis('off')
plt.tight_layout()
plt.show()