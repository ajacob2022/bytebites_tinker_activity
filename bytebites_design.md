# ByteBites Design (final)

Four classes, exactly as in the spec. Every attribute and method below traces back to a sentence in
`bytebites_spec.md` (or to a task the activity explicitly asks for), following the rules in
`ByteBites_Design_Reference.md`.

```mermaid
classDiagram
    class Customer {
        +str name
        +list~Order~ purchase_history
        +is_verified() bool
    }
    class FoodItem {
        +str name
        +float price
        +str category
        +float popularity_rating
    }
    class Menu {
        +list~FoodItem~ items
        +add_item(item) None
        +filter_by_category(category) list~FoodItem~
        +sort_by_popularity() list~FoodItem~
    }
    class Order {
        +list~FoodItem~ items
        +add_item(item) None
        +calculate_total() float
    }

    Menu "1" o-- "*" FoodItem : holds
    Order "1" o-- "*" FoodItem : groups selected
    Customer "1" o-- "*" Order : purchase_history
```

## One sentence per class

- **Customer**: a user of the app, identified by name, with a record of past orders that lets the system verify they are real.
- **FoodItem**: one sellable thing (e.g. "Spicy Burger") with a name, price, category, and popularity rating.
- **Menu**: the full collection of `FoodItem`s, able to filter by category and sort by popularity.
- **Order**: a single transaction grouping the items a user picked and computing their total cost.

## Spec traceability

| Spec sentence | Design element |
|---|---|
| "tracking their names and their past purchase history" | `Customer.name`, `Customer.purchase_history` |
| "so the system can verify they are real users" | `Customer.is_verified()` |
| "track the name, price, category, and popularity rating" | the four `FoodItem` attributes |
| "a digital list that holds all items" | `Menu.items`, `Menu.add_item()` |
| "lets us filter by category" | `Menu.filter_by_category()` |
| "store the selected items and compute the total cost" | `Order.items`, `Order.add_item()`, `Order.calculate_total()` |
| Activity Part 3: "filtering, sorting, and computing totals" | `Menu.sort_by_popularity()` |
| Activity goals: "sorting, filtering, and validation" | `ValueError` on blank names or negative prices |

## Design decisions

- **Category is a plain string**, not a class: the spec only ever uses it as a label to filter on.
- **Purchase history is a plain list of `Order`s**, not a separate class, and there is no `add_purchase` method; callers append to the list.
- **`Order` has no `customer` field**, so there is no circular reference; the customer owns the order via `purchase_history`.
- **Verification is not authentication.** No passwords, tokens, or login. A customer is verified if they have at least one past order.
- **Behaviors:** category matching ignores case; an empty order totals `0`; sorting returns a new list.
- **One sort only.** Popularity is the one ranking attribute the spec calls out; a price sort was dropped as not requested.

## What changed vs `draft_from_copilot.md`

Removed ids, email, timestamps, status, availability, `apply_discount`, `checkout`, `search`,
`update_price`, `remove_item`, `get_total_spent`, and the `Order.customer` back-reference.
Kept `is_verified()` (spec-driven) and sorting (activity-driven).
