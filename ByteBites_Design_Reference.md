# ByteBites Reference File

## About This Project
You are building the backend logic for a campus food ordering app called ByteBites
using Python classes and simple algorithms.

## Project Scope
Do not add authentication logic, a database layer, or any features not described 
in the spec.

## Behavioral Instructions
<!-- Write a short set of instructions guiding how your AI assistant should behave 
when helping with this project — for example, which classes to stay within, 
what complexity to avoid, or any preferences for how suggestions are structured. -->

1. **Strict Scope Control**: Only implement the four core candidate classes (`Customer`, `FoodItem`, `Menu`, `Transaction`). Do NOT introduce extraneous concepts such as payment gateways, database ORM models, inventory depletion, user authentication tokens, or web frameworks unless explicitly instructed.
2. **Encapsulation & Type Hints**: Use Python type annotations (`str`, `float`, `list[FoodItem]`, etc.) on all constructors and method signatures.
3. **Immutability & Pure Calculations**: Financial totals inside `Transaction` must be calculated dynamically over the current list of items rather than stored as a hardcoded mutable float.
4. **Defensive Defaults**: Collections (like purchase histories or transaction item lists) must default to empty lists without using mutable default arguments (use `None` and initialize inside `__init__`).
5. **Standard Output**: Provide clean, idiomatic Python code with minimal docstrings describing intent rather than boilerplate comments.