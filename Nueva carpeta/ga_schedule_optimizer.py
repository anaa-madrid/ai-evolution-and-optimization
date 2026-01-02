#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

"""
genetic_schedule_optimizer.py

Program for optimizing class schedules using Genetic Algorithms (GA).

Author: Ana Madrid Serrano
Date: 2026-01-02
Project: Class Schedule Optimization

Description:
This script automatically generates and evaluates class schedules
using genetic algorithms. The fitness function prioritizes:
    - Subjects in preferred time slots (e.g., Mathematics first thing in the morning)
    - Minimizing repeated subjects in the same time slot/day
    - Compliance with mandatory subjects on specific days (MAE, Tutoring)
    
This project is part of a collection of evolutionary and optimization
projects developed in Python.
"""

# -------------------------------------------------------------------
# Definition of the “alphabet” of subjects
alpha = [
    'Mat', 'Mat', 'Mat', 'Len', 'Len', 'Len', 'Len',
    'Ing', 'Ing', 'Ing', 'Soc', 'Soc', 'Soc',
    'Bio', 'Bio', 'Fis', 'Fis', 'Tec', 'Tec', 'Tec',
    'Qui', 'Qui', 'Pla', 'Pla', 'EdF', 'EdF',
    'Mus', 'Mus', 'MAE', 'Tut'
]

print(alpha)
print("Use permutation type")
print("Set Target Fitness to 50")

# -------------------------------------------------------------------
# Helper functions
def by_time_slots(chromosome):
    """Split a chromosome into 5-class time slots"""
    return [chromosome[0:5], chromosome[5:10], chromosome[10:15],
            chromosome[15:20], chromosome[20:25], chromosome[25:30]]

def phenotype(chromosome):
    """Convert a chromosome into a human-readable schedule by slots"""
    f = by_time_slots(chromosome)
    res = ""
    for e in f:
        for d in e:
            res += f"{d:4}"
        res += "\n"
    return res

def by_days(chromosome):
    """Organize the chromosome by weekdays"""
    res = []
    for i in range(5):
        day = []
        for j in range(6):
            day.append(chromosome[i + j*5])
        res.append(day)
    return res

# -------------------------------------------------------------------
# Fitness function
def fitness(chromosome):
    """Evaluate the quality of a schedule according to defined criteria"""
    slots = by_time_slots(chromosome)
    days = by_days(chromosome)

    score = 0.0
    # Prioritize Mathematics, Language, and Art in specific slots
    score += 50.0 * slots[0].count('Mat') / 5.0
    score += 50.0 * slots[5].count('Pla') / 5.0
    score += 50.0 * slots[1].count('Len') / 5.0

    # Prioritize diversity in the same slot
    for slot in slots:
        unique_subjects = set(slot)
        score += 1.0 / float(len(unique_subjects))

    # Prioritize diversity per day
    for day in days:
        unique_subjects = set(day)
        score += 10.0 * float(len(unique_subjects))

    # Mandatory subjects in specific days
    if 'Tut' not in days[4]:
        return 0.0
    if 'MAE' not in days[0]:
        return 0.0

    return score / len(slots)

# -------------------------------------------------------------------
# Genetic algorithm parameters
parameters = {
    'alphabet': alpha,
    'type': 'permutation',
    'target': 80,
    'elitism': True,
    'pmut': 1/25.0
}
