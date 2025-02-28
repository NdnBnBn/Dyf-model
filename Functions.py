#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 13:56:35 2025

@author: nadine
"""
from pyboolnet.model_checking import model_checking
from pyboolnet.temporal_logic import subspace2proposition
from pyboolnet import prime_implicants
from pyboolnet.prime_implicants import find_predecessors
from pyboolnet.state_space import state2dict
from pyboolnet.boolean_logic import minimize_espresso
from pyboolnet.boolean_normal_forms import get_dnf

def bn_to_mv(states, primes):
    mv_states = states.copy()  # Copy to avoid modifying the original dictionary
    processed_nodes = set()

    for n in primes.keys():
        if n not in states.keys():
            mv_states[n] = "-"


    for k in sorted(states.keys()):  # Sort keys to process b1, b2, ... in order
        if "_b" in k:
            node, _ = k.rsplit("_b", 1)  # Extract base node name

            if node not in processed_nodes:
                # Collect all Boolean levels
                levels = []
                i = 1
                while f"{node}_b{i}" in states:
                    levels.append(states[f"{node}_b{i}"])
                    i += 1

                # Compute MV value as the count of leading 1s
                mv_states[node] = sum(levels)  # Number of consecutive ones

                # Remove Booleanized variables
                for j in range(1, i):
                    del mv_states[f"{node}_b{j}"]

                # Mark as processed
                processed_nodes.add(node)

    return mv_states

def reachability(reach, model, attr_state):
    """
    Assess the existence of a trajectory from an initial state to a fixed point.

    """
    init = {}
    for key, value in reach.items():
        init[key] = f"INIT {subspace2proposition(model, value)}"

    answer = {}
    for key, value in reach.items():
        answer[key] = []
        specification = f"CTLSPEC EF({subspace2proposition(model, attr_state)})"
        res = model_checking(model, "asynchronous", init[key], specification)
        answer[key].append(res)
    return answer

