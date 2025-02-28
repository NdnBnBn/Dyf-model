#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:05:44 2025

@author: nadine
"""

import pystablemotifs as sm
import pyboolnet
import pystablemotifs.export as ex
import networkx as nx
import matplotlib.pyplot as plt
from pyboolnet import file_exchange, attractors, basins_of_attraction, commitment_diagrams, phenotypes, state_space


# Load the model
model_path = "/home/nadine/Documents/7. Dysferlinopathy_model/7. GINsim model/Dysferlinopathy_CellModelV5.bnet"
primes = file_exchange.bnet2primes(model_path)

# Mutation to test
mut = ["Dysferlin", "SERCA", "MCU", "leaky_RyR1", "NCLX"]

# Initial states
ZEROS = {key: 0 for key in primes.keys()}

BASAL = ZEROS.copy()
BASAL["Dysferlin_b1"] = 1
BASAL["srCa_b1"] = 1
BASAL["srCa_b2"] = 1

AP = BASAL.copy()
AP["AP"] = 1

LESION = BASAL.copy()
LESION["LESION"] = 1

AP_LESION = BASAL.copy()
AP_LESION["LESION"] = 1
AP_LESION["AP"] = 1

inits = {"BASAL": BASAL, "AP": AP, "LESION": LESION, "AP_LESION": AP_LESION}

# Compute the attractors
attrs = attractors.compute_attractors(primes, update="asynchronous")

# Print the attractors
print("The attractors are:")
attractor_states = []
for i, a in enumerate(attrs["attractors"]):
    state = a["min_trap_space"]["dict"]
    attractor_states.append(state)
    print(f"Attracteur {i+1}: {state}")
    


# Loop over each attractor and assess reachability from every initial state.
for idx, at in enumerate(attractor_states):
    print(f"\nAssessing reachability for Attractor {idx+1}: {at}")
    result = reachability(inits, primes, at)
    for init_name, res in result.items():
        print(f"  From initial state '{init_name}': {res}")



# Compute the comitment diagram
diagram = commitment_diagrams.compute_commitment_diagram(attrs)
commitment_diagrams.commitment_diagram2image(diagram, "diagram.pdf")
commitment_diagrams.create_commitment_piechart(diagram, "commitment_piechart.pdf")

# Compute the phenotype diagram
markers = ["NECROSIS", "CONTRACTION", "cpxREPAIR", "leaky_RyR1", "LESION"]
phenos = phenotypes.compute_phenotypes(attrs, markers)
phenotypes.compute_phenotype_diagram(phenos, fname_image="phenos.pdf")

# Compute the size of the basins of attractions, using the asynchronous updating scheme
weak_sizes = []
strong_sizes = []
for state in attractor_states:
    weak = basins_of_attraction.weak_basin(primes, "asynchronous", state)
    strong = basins_of_attraction.strong_basin(primes, "asynchronous", state)

    weak_size = weak.get("perc", 0)
    strong_size = strong.get("perc", 0)
    weak_sizes.append(weak_size)
    strong_sizes.append(strong_size)

    # Print the results
    print(f"\n Weak basin of the attractor {state}:")
    for key, value in weak.items():
        print(f"{key} = {value}")

    print(f"\n Strong basin of the attractor {state}:")
    for key, value in strong.items():
        print(f"{key} = {value}")

# Plot the basins
labels = [f"Attracteur {i+1}\n{state_space.state2str(bn_to_mv(state, primes))}" for i, state in enumerate(attractor_states)]
x = range(len(attractor_states))
width = 0.3
plt.figure(figsize=(10, 6))
plt.bar(x, weak_sizes, width=width, label="Weak basin", color="forestgreen", align="center")
plt.bar([i + width for i in x], strong_sizes, width=width, label="Strong basin", color="darkorange", align="center")
plt.xlabel("Attractors")
plt.ylabel("Basin size (%)")
plt.title("Basins of attractions sizes")
plt.xticks([i + width / 2 for i in x], labels, rotation=45, ha="center")
plt.legend()
plt.tight_layout()
plt.show()

initial_state = BASAL

ar = sm.AttractorRepertoire.from_primes(primes)
GR=ex.networkx_succession_diagram(ar,include_attractors_in_diagram=True)
ex.plot_nx_succession_diagram(GR,draw_edge_labels=True,
                              nx_node_label_kwargs={'font_size':10},
                              nx_edge_label_kwargs={'font_size':12,'rotate':False})


