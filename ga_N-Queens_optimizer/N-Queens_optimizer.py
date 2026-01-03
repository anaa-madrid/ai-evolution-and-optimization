#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
n_queens_optimizer.py

Project: N-Queens Problem Optimization using Genetic Algorithms (GA)
Author: Ana Madrid Serrano
Date: 2026-01-02

Description:
This script defines a fitness function for the classic N-Queens problem.
The goal is to place N queens on an N×N chessboard such that no two queens
attack each other.

Each chromosome represents a board configuration where:
- The index represents the column.
- The value at that index represents the row of the queen in that column.

The fitness function rewards configurations with fewer conflicts.
"""

# -------------------------------------------------------------------
# Problem size
N = 64

# -------------------------------------------------------------------
# Fitness function
def fitness(chromosome):
    """
    Compute the fitness of a chromosome by counting the number of
    non-attacking queen pairs.

    Maximum fitness is achieved when there are zero conflicts.
    """
    conflicts = 0

    for i in range(len(chromosome)):
        for j in range(i + 1, len(chromosome)):
            # Same row or same diagonal
            if chromosome[i] == chromosome[j] or \
               abs(chromosome[i] - chromosome[j]) == abs(i - j):
                conflicts += 1

    # Maximum possible number of non-attacking pairs
    max_pairs = (N * (N - 1)) // 2

    # Fitness = number of non-conflicting pairs
    fitness_value = max_pairs - conflicts
    return fitness_value

# -------------------------------------------------------------------
# Genetic algorithm parameters
alphabet = list(range(1, N + 1))

parameters = {
    'alphabet': alphabet,
    'type': 'classic',
    'elitism': True,
    'target': 80,
    'norm': True,
    'chromsize': N
}