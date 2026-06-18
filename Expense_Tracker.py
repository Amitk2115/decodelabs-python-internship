# Expense Tracker - DecodeLabs Python Internship 2026

expenses = []  # List of dicts: {category, description, amount}
total = 0.0    # Accumulator initialized outside the loop

CATEGORIES = ["Food", "Transport", "Shopping", "Bills", "Other"]

def select_category():
    print("\nCategories:")
    for i, cat in enumerate(CATEGORIES, start=1):
        print(f"  {i}. {cat}")
    while True:
        try:
            choice = int(input("Select category (1-5): "))
            if 1 <= choice <= 5:
                return CATEGORIES[choice - 1]
            print("Enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input.")

def add_expense():
    global total
    print("\nEnter expenses one by one. Type 'done' to stop.\n")
    while True:
        entry = input("Amount: ").strip()

        if entry.lower() == "done":  # Kill switch
            break

        try:
            amount = float(entry)
            if amount <= 0:
                print("Amount must be positive.")
                continue

            description = input("Description: ").strip() or "No description"
            category = select_category()

            expenses.append({
                "amount": amount,
                "description": description,
                "category": category
            })

            total += amount  # Accumulator pattern
            print(f"Saved under {category} | Running Total: {total:.2f}\n")

        except ValueError:  # Catches non-numeric input
            print("Invalid amount. Enter a number.")

def view_summary():
    if not expenses:
        print("No expenses recorded.")
        return

    # Group totals by category
    category_totals = {}
    for exp in expenses:
        cat = exp["category"]
        category_totals[cat] = category_totals.get(cat, 0) + exp["amount"]

    print("\n======= EXPENSE SUMMARY =======")
    for i, exp in enumerate(expenses, start=1):
        print(f"  {i}. {exp['category']:<12} | {exp['description']:<20} | {exp['amount']:.2f}")

    print("\n--- By Category ---")
    for cat, amt in category_totals.items():
        print(f"  {cat:<12}: {amt:.2f}")

    print(f"\n  TOTAL SPENT : {total:.2f}")
    
    if expenses:
        avg = total / len(expenses)
        highest = max(expenses, key=lambda x: x["amount"])
        print(f"  AVERAGE     : {avg:.2f}")
        print(f"  HIGHEST     : {highest['description']} ({highest['amount']:.2f})")
    print("================================\n")

def main():
    while True:
        print("\n1. Add expenses\n2. View summary\n3. Quit")
        choice = input("Choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            view_summary()  # Show final total before quitting
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
