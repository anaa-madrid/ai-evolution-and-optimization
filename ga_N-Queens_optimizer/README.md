# N-Queens Problem Optimizer

**Project:** N-Queens Optimization using Genetic Algorithms (GA)  
**Author:** Ana Madrid Serrano  

This project is part of a broader collection of **optimization problems solved using evolutionary algorithms**. It demonstrates how **SALGA** can be applied to the classic **N-Queens problem**, scaling to large board sizes.

---

## Problem Description

The **N-Queens problem** consists of placing **N queens on an N×N chessboard** such that no two queens attack each other.

A queen can attack another queen if they share:
- The same **row**
- The same **column**
- The same **diagonal**

In this implementation:
- Each chromosome represents a board configuration.
- The **index** of the chromosome corresponds to a column.
- The **value** at each index corresponds to the row where the queen is placed.

---

## Chromosome Representation

Example for `N = 8`:

Chromosome: [1, 5, 8, 6, 3, 7, 2, 4]


- Column 0 → Queen in row 1  
- Column 1 → Queen in row 5  
- Column 2 → Queen in row 8  
- …  

This representation guarantees **one queen per column**.

---

## Fitness Function

The fitness function evaluates how good a configuration is by:

- Counting the number of **conflicting queen pairs**
- Subtracting conflicts from the **maximum possible number of non-attacking pairs**

Maximum pairs = N × (N − 1) / 2
Fitness = Maximum pairs − conflicts

- **Maximum fitness** is achieved when there are **zero conflicts**
- Higher fitness → better solution

---



