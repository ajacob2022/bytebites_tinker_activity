# ByteBites Design Reference

Ground rules for any AI assistant working on this project. Attach this file to every chat.

## Project Context

ByteBites is a campus food ordering backend. This tinker activity builds only the
**core domain model**: Python classes plus simple algorithms (filter, sort, total).
There is no UI, database, network, or AI recommendation engine in scope.

## Behavioral Instructions

**Scope**
- Model exactly four classes: `Customer`, `FoodItem`, `Menu`, `Order`. Do not add others
  (no `Payment`, `Restaurant`, `Recommender`, `Cart`, `Address`, etc.).
- Only include attributes and methods that the client feature request implies.
  If something is not in `bytebites_spec.md`, leave it out and mention it as an optional idea instead.
- Do not invent features: no discounts, taxes, delivery, inventory, authentication, or persistence.

**Design style**
- Prefer the simplest thing that works: plain Python classes, lists, and built-in
  `sorted()` / list comprehensions. No inheritance hierarchies, abstract base classes,
  design patterns, metaclasses, or third-party libraries.
- Standard library only. Type hints are welcome; `dataclasses` are fine for plain data holders.
- Keep each method short and single-purpose, with a one-line docstring.

**Attributes (from the spec)**
- `Customer`: `name`, `purchase_history` (past orders).
- `FoodItem`: `name`, `price`, `category`, `popularity_rating`.
- `Menu`: a collection of `FoodItem` objects, filterable by category.
- `Order`: the selected `FoodItem`s for one transaction, with a computed total.

**Behavior**
- Category matching is case-insensitive (`"drinks"` matches `"Drinks"`).
- An empty `Order` has a total of `0`, not an error.
- Sorting returns a new list and never mutates the stored collection.
- Validate obvious bad data (negative price, blank name) with a clear `ValueError`.
- A customer is "verified" when they have a non-empty name and a purchase history
  (the spec says history is used "to verify they are real users"), kept as a tiny helper.

**Output format**
- UML diagrams are Mermaid `classDiagram` blocks inside Markdown.
- Show relationships with cardinality (e.g. `Menu "1" o-- "*" FoodItem`).
- Explain each class in one sentence beneath the diagram.
- When asked to review code, review one class at a time and list only changes that
  keep the code aligned with the spec.

**Process**
- Treat AI output as a draft. Flag anything you added that is not in the spec.
- Prefer small, reviewable changes over large rewrites.
