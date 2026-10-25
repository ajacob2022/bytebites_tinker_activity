# Draft 1: standard chat, spec only (no reference file)

> Prompt: "Here is my spec (bytebites_spec.md) and my four candidate classes: Customer,
> FoodItem, Menu, Order. Generate a UML-style class diagram."
>
> Note: file name kept from the activity template. This draft was produced by Claude from
> the spec alone, with no ground rules, to compare against the guided version.

```mermaid
classDiagram
    class Customer {
        +int customer_id
        +str name
        +str email
        +list~Order~ purchase_history
        +verify() bool
        +add_order(order) void
        +get_total_spent() float
    }
    class FoodItem {
        +int item_id
        +str name
        +float price
        +str category
        +float popularity_rating
        +bool is_available
        +update_price(new_price) void
    }
    class Menu {
        +list~FoodItem~ items
        +add_item(item) void
        +remove_item(item_id) void
        +filter_by_category(category) list
        +sort_by_popularity() list
        +search(keyword) list
    }
    class Order {
        +int order_id
        +Customer customer
        +list~FoodItem~ items
        +datetime created_at
        +str status
        +add_item(item) void
        +remove_item(item) void
        +calculate_total() float
        +apply_discount(code) float
        +checkout() void
    }
    Customer "1" --> "*" Order : places
    Menu "1" o-- "*" FoodItem : contains
    Order "1" o-- "*" FoodItem : includes
```

## Review against the spec

| Issue | Where | Verdict |
|---|---|---|
| Invented attributes: `customer_id`, `email`, `item_id`, `is_available`, `order_id`, `created_at`, `status` | all classes | Not in the request. Remove. |
| Invented methods: `get_total_spent`, `update_price`, `remove_item`, `search`, `apply_discount`, `checkout` | all classes | Not requested. `apply_discount` and `checkout` are real scope creep. |
| `Order.customer` back-reference | Order | Creates a circular dependency with `Customer.purchase_history`. Unneeded. |
| `verify()` | Customer | Reasonable, since the spec says history verifies real users. Keep, simplified. |
| `sort_by_popularity()` | Menu | Not stated explicitly, but the activity (Part 3) asks for sorting. Keep. |

**Takeaway:** with no guardrails the assistant added roughly 15 things the product manager
never asked for. The guided draft (`bytebites_design.md`) removes them.
