# Computational Thinking Exercise

## Smart School Canteen Queue

**Name:** Jake Aedaan A. Iglesia  
**Section:** 9 - Magnesium  
**Last Name:** Iglesia  
**Date:** August 13, 2026

---

## Step 1: Identify the Big Problem

### Main Problem

The main problem in the canteen scenario is the cascading effect of delays from customer indecision, manual cost calculation and giving change, and lack of an easy-to-use inventory system. These issues compound over time, resulting in long queuing times during lunch break.

---

## Step 2: Identify the Sub-Problems

1. Students take too long to decide what to order (e.g., chips, snacks, drinks) and whether they can afford them.

2. The cashier manually calculates the total and gives change to the customer, which takes precious seconds that compound into longer wait times when there is a backlog.

3. There is no inventory system that informs workers and cashiers whether a specific food item is still in stock. When an item is out of stock, students must choose another product, wasting more time.

---

## Step 3: Apply Computational Thinking Skills

| Sub-Problem | CT Skill | Proposed Solution |
|---|---|---|
| Students take too long to decide what to order and if they can afford it | Abstraction and Algorithm Design | Create a digital menu board that abstracts the products into categories (e.g., "Drinks," "Snacks," "Meals") with clear prices and images. Implement a simple "budget calculator" algorithm where students can input their budget and the system shows only items they can afford, reducing decision-making time. |
| Cashier manually calculates totals and gives change, causing delays | Algorithm Design and Automation | Replace manual computation with a Point-of-Sale (POS) system using a smartphone or tablet. The algorithm will automatically sum the items scanned/selected, compute the exact change, and display it instantly to both the cashier and the student. |
| No inventory system to track stock levels, causing students to re-select items | Data Representation and Analysis | Implement a simple real-time inventory system. Represent stock levels as numerical data (e.g., integer counts) in a database. Use an algorithm to automatically deduct items sold and trigger a visual alert (e.g., a red "OUT OF STOCK" overlay on the menu) when an item reaches zero, preventing students from choosing unavailable products. |

---

## Step 4: Algorithmic Solution

### Selected Sub-Problem

The cashier manually calculates totals and gives change, causing delays.

### Pseudocode


START POS_Transaction

// Step 1: Initialize total
SET total = 0

// Step 2: Loop to add items to the order
REPEAT
    DISPLAY "Scan or select an item (or type 'DONE' to finish):"
    INPUT item_code

    IF item_code == "DONE" THEN
        BREAK loop
    ELSE
        SET price = GET_ITEM_PRICE(item_code)
        total = total + price
        DECREMENT_STOCK(item_code)
    END IF
UNTIL (user finishes order)

// Step 3: Calculate change
DISPLAY "Total amount due: ", total
DISPLAY "Enter amount given by student:"
INPUT amount_given

SET change = amount_given - total

// Step 4: Finalize the transaction
DISPLAY "Change to return: ", change
PRINT_RECEIPT(total, change)

RESET total

END POS_Transaction

