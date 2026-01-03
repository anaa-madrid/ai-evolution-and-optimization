# Genetic Schedule Optimizer

**Project:** Class Schedule Optimization using Genetic Algorithms (GA)  
**Author:** Ana Madrid Serrano  
 

This project is part of a growing collection of **optimization problems** solved using **evolutionary algorithms**. Each problem demonstrates how to use **SALGA** or other genetic algorithms to **iteratively search for the optimal chromosome or solution**.

---

## Problem Description

`genetic_schedule_optimizer.py` optimizes a **school timetable**:

- 30 classes per week, 6 hours per day  
- A fitness function that prioritizes:
  - Preferred placement of certain subjects (e.g., Mathematics first thing in the morning)  
  - Minimizing repeated subjects in the same time slot/day  
  - Ensuring mandatory subjects appear in specific days (e.g., MAE on Monday, Tutoring on Friday)

The program uses **permutation-based chromosomes** and a **fitness evaluation** to guide the search for an optimal schedule.

---

## Example Output

Creating random population
gen:     0; meanf: 1.859; bestf:51.90833; div: 0.745; time: 0.01
Target fitness reached
gen:    38; meanf:36.628; bestf:65.34722; div: 0.277; time: 8.65

Global historical best chromosome:
['Mat', 'Mat', 'Mat', 'Bio', 'EdF', 'Len', 'Len', 'Len', 'EdF', 'Len', 
 'MAE', 'Soc', 'Soc', 'Fis', 'Fis', 'Qui', 'Ing', 'Mus', 'Mus', 'Ing', 
 'Soc', 'Qui', 'Tec', 'Tec', 'Tec', 'Pla', 'Bio', 'Pla', 'Ing', 'Tut']
fitness: 65.3472

Global historical best phenotype:
Mat  Mat  Mat  Bio  EdF
Len  Len  Len  EdF  Len
MAE  Soc  Soc  Fis  Fis
Qui  Ing  Mus  Mus  Ing
Soc  Qui  Tec  Tec  Tec
Pla  Bio  Pla  Ing  Tut

---

## Interpretation of Results

- **Generation 0**: Initial random population. Mean fitness is low (`1.859`), best fitness `51.91`. Diversity is high (`0.745`), meaning the population is varied.

- **Generation 38**: Target fitness reached. Mean fitness improved (`36.63`), best fitness `65.35`. Diversity decreased (`0.277`), indicating convergence towards good solutions.

- **Global historical best chromosome** represents the sequence of classes that achieved the highest fitness found.

- **Phenotype** is the human-readable timetable, showing the distribution of subjects across the 5-day week.

- The algorithm successfully places key subjects in **preferred time slots** (e.g., MAE on Monday, Tutoring on Friday).

- It also reduces repeated subjects per day, producing a balanced and feasible schedule.

- **Fitness (`65.35`)** shows how well the schedule meets the defined preferences and constraints.

> In summary: the algorithm demonstrates that SALGA can efficiently explore the search space and converge to valid, optimized schedules within a reasonable number of generations.




