# Knapsack Problem Optimizer

**Project:** Knapsack Problem Optimization using Genetic Algorithms (GA)  
**Author:** Ana Madrid Serrano  


This project is part of a growing collection of **optimization problems** solved using **evolutionary algorithms**. Each problem demonstrates how to use **SALGA** or other genetic algorithms to **iteratively search for the optimal solution**.

---

## Problem Description

`knapsack_optimizer.py` solves the **classic Knapsack Problem**:

- A set of items, each with a **weight** and **value**.  
- A knapsack with a **maximum capacity**.  
- The goal is to select a subset of items that **maximizes total value** without exceeding the capacity.  

The **chromosome** is represented as a list of Booleans:

- `True` → the item is included in the knapsack  
- `False` → the item is excluded  

The algorithm uses a **fitness function** to evaluate chromosomes and guide the search for the optimal selection.

---