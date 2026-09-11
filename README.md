# python-set-friend-comparison
A beginner Python project that uses sets to compare friends between two people.

# 🧑‍🤝‍🧑 Friend Comparison Tool (Python Set Project)

## Description
A beginner-friendly Python project that compares the friends of two people using **sets**. The user enters each person's friends (separated by commas), and the program analyzes the relationship between the two lists using set operations.

This project is part of my Python learning journey, focused on mastering sets and their methods.

## Features
- Reads friends of two people from user input
- Cleans names (removes extra spaces, converts to lowercase)
- Displays:
  - All friends combined (union)
  - Mutual friends (intersection)
  - Friends only the first person knows (difference)
  - Friends only the second person knows (difference)
  - Non-mutual friends (symmetric difference)
  - Whether one person's friends are a subset/superset of the other's

## Example Run
```

First person friends are : Ali, Sara, Omar
Second person friends are : Sara, Omar, Zain

---

All friends are: {'ali', 'sara', 'omar', 'zain'}

The mutual friends are: {'sara', 'omar'}

The friends that only the first person knows: {'ali'}

The friends that only the second person knows: {'zain'}

The non-mutual friends are: {'ali', 'zain'}

Are all the friends of the second person also friends with the first? : False

Are all the friends of the first person also friends with the second? : False

```

## Concepts Practiced
- Sets in Python
- Set methods: `union()`, `intersection()`, `difference()`, `issubset()`, `issuperset()`
- Symmetric difference operator `^`
- User input with `input()` and `.split()`
- String cleaning with `.strip()` and `.lower()`
- F-strings and `.format()`
