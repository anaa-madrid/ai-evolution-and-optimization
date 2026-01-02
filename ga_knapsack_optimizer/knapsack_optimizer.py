#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
knapsack_optimizer.py

Project: Knapsack Problem Optimization using Genetic Algorithms (GA)
Author: Ana Madrid Serrano
Date: 2026-01-02

Description:
This script implements a simple genetic algorithm fitness function
for the classic Knapsack Problem. Given a set of items with weights
and values, the goal is to select a subset of items that maximizes
the total value without exceeding the knapsack capacity.

The chromosome is represented as a list of Booleans, where True
indicates that the corresponding item is included in the knapsack.
"""

# -------------------------------------------------------------------
# Knapsack parameters
knapsack_capacity = 80

weights = [10, 50, 5, 20, 35]
values  = [70, 90, 10, 40, 30]

# -------------------------------------------------------------------
# Fitness function for GA
def fitness(chromosome):
    """
    Evaluate total value of selected items.
    Returns a single number (total value) for GA optimization.
    """
    total_weight = 0
    total_value  = 0
    selected_items = []

    for i in range(len(chromosome)):
        if chromosome[i] and i not in selected_items:
            total_weight += weights[i]
            total_value  += values[i]
            selected_items.append(i)
        elif chromosome[i] and i in selected_items:
            # Penalize duplicate selection
            total_value *= 0.8

    # Penalize overweight
    if total_weight > knapsack_capacity:
        return 0

    return total_value

# -------------------------------------------------------------------
# Evaluation function for inspection
def evaluate(chromosome):
    """
    Returns fitness, total weight, and list of selected items.
    Useful for printing results after optimization.
    """
    total_weight = 0
    total_value  = 0
    selected_items = []

    for i in range(len(chromosome)):
        if chromosome[i] and i not in selected_items:
            total_weight += weights[i]
            total_value  += values[i]
            selected_items.append(i)
        elif chromosome[i] and i in selected_items:
            total_value *= 0.8

    if total_weight > knapsack_capacity:
        return 0, total_weight, selected_items

    return total_value, total_weight, selected_items

# -------------------------------------------------------------------
# Genetic algorithm parameters
alphabet = [False, True]
parameters = {
    'alphabet': alphabet,
    'chromsize': len(weights),
    'pmut': 0.2
}

# -------------------------------------------------------------------
# Example usage
if __name__ == "__main__":
    example_chromosome = [True, True, False, True, False]

    # Only fitness (for GA)
    fit = fitness(example_chromosome)
    print("Fitness for GA:", fit)

    # Full evaluation (for inspection)
    fit_val, weight_val, items = evaluate(example_chromosome)
    print("Full evaluation:")
    print("  Fitness:", fit_val)
    print("  Total weight:", weight_val)
    print("  Selected items:", items)
