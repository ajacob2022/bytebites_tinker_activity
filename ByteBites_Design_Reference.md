# ByteBites Reference File

## About This Project
You are building the backend logic for a campus food ordering app called ByteBites
using Python classes and simple algorithms.

## Project Scope
Do not add authentication logic, a database layer, or any features not described 
in the spec.

## Behavioral Instructions
**Stay within four classes.** Model only `Customer`, `FoodItem`, `Menu`, and `Order`.
Do not add other classes (no `Payment`, `Restaurant`, `Cart`, `Recommender`, `Category`,
`PurchaseHistory`, etc.). Category is a plain string; purchase history is a plain list of `Order`s.

**Only what the spec describes.** Every attribute and method must trace to a sentence in
`bytebites_spec.md`, or to a task the activity explicitly asks for (filtering, sorting, totals,
light validation). If something is not covered, leave it out and mention it as an optional idea
instead of adding it. No ids, emails, timestamps, status fields, discounts, taxes, delivery,
inventory, checkout, search, or persistence.

**"Verify real users" is not authentication.** It means a simple check of the customer's
purchase history. Do not add passwords, tokens, login, or sessions.

**Keep it simple.** Plain Python classes, lists, list comprehensions, and built-in `sorted()`.
Standard library only. No inheritance, abstract classes, design patterns, or third-party
libraries. Short methods with a one-line docstring each.

**Predictable behavior.** Category matching ignores case. An empty `Order` totals `0`, not an
error. Sorting returns a new list and never reorders the stored menu. Bad data (blank name,
negative price) raises `ValueError`.

**How to respond.** Treat AI output as a draft. Flag anything you added that is not in the spec.
Draw UML as a Mermaid `classDiagram` with cardinality, followed by one sentence per class.
When reviewing code, go one class at a time and propose only changes that keep it aligned with
the spec. Prefer small, reviewable changes over rewrites.
