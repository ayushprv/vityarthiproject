import os

# Function to initialize the data file
def initialize_system():
    """Creates the expense file if it doesn't exist"""
    if not os.path.exists('expenses.txt'):
        with open('expenses.txt', 'w') as file:
            file.write('')
        print("System initialized successfully!\n")

# Feature 1: Add New Expense
def add_expense():
    print("\n--- ADD EXPENSE ---")
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food/Transport/Bills/Shopping/Other): ")
    amount = float(input("Enter amount (₹): "))
    description = input("Enter description: ")
    
    # Write to file
    with open('expenses.txt', 'a') as file:
        file.write(f"{date}|{category}|{amount}|{description}\n")
    
    print("✓ Expense added successfully!")

# Feature 2: View All Expenses
def view_all_expenses():
    """Displays all recorded expenses"""
    print("\n" + "="*70)
    print("ALL EXPENSES")
    print("="*70)
    print(f"{'Date':<15} {'Category':<15} {'Amount':<12} {'Description':<25}")
    print("-"*70)
    
    try:
        with open('expenses.txt', 'r') as file:
            lines = file.readlines()
            if len(lines) == 0:
                print("No expenses recorded yet!")
            else:
                for line in lines:
                    date, category, amount, description = line.strip().split('|')
                    print(f"{date:<15} {category:<15} ₹{amount:<11} {description:<25}")
    except FileNotFoundError:
        print("No expense file found!")
    
    print("="*70)

# Feature 3: Search by Category
def search_by_category():
    """Search and display expenses of a specific category"""
    print("\n--- SEARCH BY CATEGORY ---")
    search_cat = input("Enter category to search: ").lower()
    
    print("\n" + "="*70)
    print(f"EXPENSES IN CATEGORY: {search_cat.upper()}")
    print("="*70)
    print(f"{'Date':<15} {'Category':<15} {'Amount':<12} {'Description':<25}")
    print("-"*70)
    
    found = False
    with open('expenses.txt', 'r') as file:
        for line in file:
            date, category, amount, description = line.strip().split('|')
            if category.lower() == search_cat:
                print(f"{date:<15} {category:<15} ₹{amount:<11} {description:<25}")
                found = True
    
    if not found:
        print("No expenses found in this category!")
    print("="*70)

# Feature 4: Calculate Total Expenses
def calculate_total():
    """Calculates and displays total expenses"""
    total = 0.0
    
    with open('expenses.txt', 'r') as file:
        for line in file:
            parts = line.strip().split('|')
            total += float(parts[2])
    
    print("\n" + "="*70)
    print(f"TOTAL EXPENSES: ₹{total:.2f}")
    print("="*70)

# Feature 5: Category-wise Summary
def category_summary():
    """Shows expense breakdown by category"""
    categories = {}
    
    with open('expenses.txt', 'r') as file:
        for line in file:
            parts = line.strip().split('|')
            category = parts[1]
            amount = float(parts[2])
            
            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount
    
    print("\n" + "="*70)
    print("CATEGORY-WISE SUMMARY")
    print("="*70)
    
    if len(categories) == 0:
        print("No expenses recorded!")
    else:
        total = sum(categories.values())
        for category, amount in categories.items():
            percentage = (amount / total) * 100
            print(f"{category:<20} : ₹{amount:>10.2f}  ({percentage:>5.1f}%)")
        print("-"*70)
        print(f"{'TOTAL':<20} : ₹{total:>10.2f}")
    
    print("="*70)

# Feature 6: Delete Last Expense
def delete_last_expense():
    """Deletes the most recent expense entry"""
    with open('expenses.txt', 'r') as file:
        lines = file.readlines()
    
    if len(lines) == 0:
        print("No expenses to delete!")
        return
    
    # Remove last line
    with open('expenses.txt', 'w') as file:
        file.writelines(lines[:-1])
    
    print("✓ Last expense deleted successfully!")

# Main Menu Function
def display_menu():
    """Displays the main menu"""
    print("\n" + "="*70)
    print("PERSONAL EXPENSE TRACKER".center(70))
    print("="*70)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search by Category")
    print("4. Calculate Total Expenses")
    print("5. Category-wise Summary")
    print("6. Delete Last Expense")
    print("7. Exit")
    print("="*70)

# Main Program
def main():
    """Main function to run the expense tracker"""
    initialize_system()
    
    print("\n" + "*"*70)
    print("WELCOME TO PERSONAL EXPENSE TRACKER".center(70))
    print("*"*70)
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_all_expenses()
        elif choice == '3':
            search_by_category()
        elif choice == '4':
            calculate_total()
        elif choice == '5':
            category_summary()
        elif choice == '6':
            delete_last_expense()
        elif choice == '7':
            print("\n" + "="*70)
            print("Thank you for using Expense Tracker!".center(70))
            print("="*70)
            break
        else:
            print("\n✗ Invalid choice! Please select 1-7.")

# Run the program
if _name== "main_":
    main()
