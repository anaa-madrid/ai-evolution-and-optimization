#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
knapsack_optimizer.py

Project: Knapsack Problem Optimization using Genetic Algorithms (GA)
Author: Ana Madrid Serrano

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
values = [70, 90, 10, 40, 30]

# -------------------------------------------------------------------
# Fitness function
def fitness(chromosome):
    """
    Evaluate the total value of selected items in the knapsack.
    Penalizes if the total weight exceeds capacity or if items are duplicated.
    """
    total_weight = 0
    total_value = 0
    selected_items = []

    for i in range(len(chromosome)):
        if chromosome[i] and i not in selected_items:
            total_weight += weights[i]
            total_value += values[i]
            selected_items.append(i)
        elif chromosome[i] and i in selected_items:
            # Penalize if an item is selected more than once
            total_value *= 0.8  # reduce total value by 20%

    # Penalize overweight
    if total_weight > knapsack_capacity:
        return 0

    return total_value

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
    # Example chromosome (selecting items 0, 1, and 3)
    example_chromosome = [True, True, False, True, False]
    print("Chromosome:", example_chromosome)
    print("Fitness:", fitness(example_chromosome))
