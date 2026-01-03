# AI-EVOLUTION-AND-OPTIMIZATION

**Author:** Ana Madrid Serrano  
**Focus:** Evolutionary Computation · Genetic Algorithms · Optimization  
**Tools:** SALGA · Python  

This repository contains a collection of **classic optimization problems solved using Genetic Algorithms (GA)**.  
Each project demonstrates how **evolutionary techniques** can be applied to complex search spaces where traditional or brute-force approaches are inefficient.

The goal of this repository is to **experiment, learn, and showcase practical applications of Genetic Algorithms**, with a strong emphasis on **fitness design, chromosome representation, and convergence behavior**.

---

## Repository Structure

ga_N-Queens_optimizer --> https://github.com/anaa-madrid/ai-evolution-and-optimization/tree/main/ga_N-Queens_optimizer

ga_knapsack_optimizer --> https://github.com/anaa-madrid/ai-evolution-and-optimization/tree/main/ga_knapsack_optimizer

ga_schedule_optimizer --> https://github.com/anaa-madrid/ai-evolution-and-optimization/tree/main/ga_schedule_optimizer

Each folder contains:
- A Python implementation of the problem
- A dedicated README explaining the problem, fitness function, and results

---

## Implemented Optimization Problems

### N-Queens Problem
**Folder:** `ga_N-Queens_optimizer`

- Objective: Place `N` queens on an `N×N` chessboard with no conflicts
- Representation: One queen per column
- Fitness: Number of non-attacking queen pairs
- Demonstrates scalability to large `N` (e.g., `N = 64`)

---

### Knapsack Problem
**Folder:** `ga_knapsack_optimizer`

- Objective: Maximize total value without exceeding knapsack capacity
- Representation: Boolean chromosome (item selected / not selected)
- Fitness: Total value with penalties for overweight solutions
- Demonstrates constraint handling in GA

---

### Class Schedule Optimization
**Folder:** `ga_schedule_optimizer`

- Objective: Optimize a weekly school timetable
- Representation: Permutation-based chromosome
- Fitness: Encodes domain-specific constraints and preferences
- Demonstrates real-world combinatorial optimization

---

## Genetic Algorithm Approach

All problems follow a common GA workflow:

1. Random population initialization  
2. Fitness evaluation  
3. Selection and reproduction  
4. Mutation and elitism  
5. Iterative evolution until convergence or target fitness  

The implementations are compatible with **SALGA**, but the fitness functions are designed to be reusable with other GA frameworks.

---

## Key Concepts Demonstrated

- Fitness function design  
- Chromosome encoding strategies  
- Constraint handling via penalties  
- Exploration vs exploitation trade-off  
- Convergence and population diversity  

---
