import sqlite3
from datetime import datetime
import os
import sys

class ExpenseTracker:
    def __init__(self):
        self.conn = sqlite3.connect('expenses.db')
        self.cursor = self.conn.cursor()
        self.create_table()
        
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL,
                description TEXT,
                payment_method TEXT
            )
        ''')
        self.conn.commit()
    
    def add_expense(self, date, category, amount, description, payment_method):
        self.cursor.execute('''
            INSERT INTO expenses (date, category, amount, description, payment_method)
            VALUES (?, ?, ?, ?, ?)
        ''', (date, category, amount, description, payment_method))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def get_all_expenses(self):
        self.cursor.execute('SELECT * FROM expenses ORDER BY date DESC')
        return self.cursor.fetchall()
    
    def get_expenses_by_date_range(self, start_date, end_date):
        self.cursor.execute('''
            SELECT * FROM expenses 
            WHERE date BETWEEN ? AND ?
            ORDER BY date DESC
        ''', (start_date, end_date))
        return self.cursor.fetchall()
    
    def get_expenses_by_category(self, category):
        self.cursor.execute('''
            SELECT * FROM expenses 
            WHERE category = ?
            ORDER BY date DESC
        ''', (category,))
        return self.cursor.fetchall()
    
    def get_category_summary(self):
        self.cursor.execute('''
            SELECT category, SUM(amount) as total, COUNT(*) as count
            FROM expenses
            GROUP BY category
            ORDER BY total DESC
        ''')
        return self.cursor.fetchall()
    
    def get_monthly_summary(self, year, month):
        month_str = f"{year}-{month:02d}"
        self.cursor.execute('''
            SELECT SUM(amount) as total, COUNT(*) as count
            FROM expenses
            WHERE strftime('%Y-%m', date) = ?
        ''', (month_str,))
        return self.cursor.fetchone()
    
    def get_total_expenses(self):
        self.cursor.execute('SELECT SUM(amount) FROM expenses')
        result = self.cursor.fetchone()[0]
        return result if result else 0
    
    def delete_expense(self, expense_id):
        self.cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def update_expense(self, expense_id, date, category, amount, description, payment_method):
        self.cursor.execute('''
            UPDATE expenses 
            SET date = ?, category = ?, amount = ?, description = ?, payment_method = ?
            WHERE id = ?
        ''', (date, category, amount, description, payment_method, expense_id))
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def search_expenses(self, keyword):
        self.cursor.execute('''
            SELECT * FROM expenses 
            WHERE description LIKE ? OR category LIKE ?
            ORDER BY date DESC
        ''', (f'%{keyword}%', f'%{keyword}%'))
        return self.cursor.fetchall()
    
    def close(self):
        self.conn.close()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    print("\n" + "="*60)
    print(f"{title:^60}")
    print("="*60 + "\n")

def print_menu():
    clear_screen()
    print_header("PERSONAL EXPENSE TRACKER")
    print("1.  Add New Expense")
    print("2.  View All Expenses")
    print("3.  View Expenses by Category")
    print("4.  View Expenses by Date Range")
    print("5.  Search Expenses")
    print("6.  View Category Summary")
    print("7.  View Monthly Summary")
    print("8.  View Total Expenses")
    print("9.  Update Expense")
    print("10. Delete Expense")
    print("11. Exit")
    print("\n" + "-"*60)

def get_valid_date(prompt):
    while True:
        date_str = input(prompt)
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return date_str
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD")

def get_valid_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than zero")
        except ValueError:
            print("Invalid amount. Please enter a number")

def get_category():
    categories = [
        "Food & Dining",
        "Transportation",
        "Shopping",
        "Entertainment",
        "Bills & Utilities",
        "Healthcare",
        "Education",
        "Others"
    ]
    
    print("\nSelect Category:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")
    
    while True:
        try:
            choice = int(input("\nEnter choice (1-8): "))
            if 1 <= choice <= 8:
                return categories[choice - 1]
            else:
                print("Invalid choice. Please select 1-8")
        except ValueError:
            print("Invalid input. Please enter a number")

def get_payment_method():
    methods = [
        "Cash",
        "Credit Card",
        "Debit Card",
        "UPI",
        "Net Banking"
    ]
    
    print("\nSelect Payment Method:")
    for i, method in enumerate(methods, 1):
        print(f"{i}. {method}")
    
    while True:
        try:
            choice = int(input("\nEnter choice (1-5): "))
            if 1 <= choice <= 5:
                return methods[choice - 1]
            else:
                print("Invalid choice. Please select 1-5")
        except ValueError:
            print("Invalid input. Please enter a number")

def add_expense(tracker):
    clear_screen()
    print_header("ADD NEW EXPENSE")
    
    date = get_valid_date("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        date = datetime.now().strftime('%Y-%m-%d')
    
    category = get_category()
    amount = get_valid_amount("\nEnter amount: ₹")
    payment_method = get_payment_method()
    description = input("\nEnter description (optional): ")
    
    expense_id = tracker.add_expense(date, category, amount, description, payment_method)
    print(f"\n✓ Expense added successfully! (ID: {expense_id})")
    input("\nPress Enter to continue...")

def view_all_expenses(tracker):
    clear_screen()
    print_header("ALL EXPENSES")
    
    expenses = tracker.get_all_expenses()
    
    if not expenses:
        print("No expenses found.")
    else:
        print(f"{'ID':<5} {'Date':<12} {'Category':<20} {'Amount':>10} {'Payment':<15} {'Description':<30}")
        print("-" * 110)
        for exp in expenses:
            print(f"{exp[0]:<5} {exp[1]:<12} {exp[2]:<20} ₹{exp[3]:>9.2f} {exp[5]:<15} {exp[4]:<30}")
        
        total = sum(exp[3] for exp in expenses)
        print("-" * 110)
        print(f"{'Total:':<58} ₹{total:>9.2f}")
    
    input("\nPress Enter to continue...")

def view_expenses_by_category(tracker):
    clear_screen()
    print_header("VIEW EXPENSES BY CATEGORY")
    
    category = get_category()
    expenses = tracker.get_expenses_by_category(category)
    
    clear_screen()
    print_header(f"EXPENSES - {category}")
    
    if not expenses:
        print(f"No expenses found for category: {category}")
    else:
        print(f"{'ID':<5} {'Date':<12} {'Amount':>10} {'Payment':<15} {'Description':<30}")
        print("-" * 80)
        for exp in expenses:
            print(f"{exp[0]:<5} {exp[1]:<12} ₹{exp[3]:>9.2f} {exp[5]:<15} {exp[4]:<30}")
        
        total = sum(exp[3] for exp in expenses)
        print("-" * 80)
        print(f"{'Total:':<28} ₹{total:>9.2f}")
    
    input("\nPress Enter to continue...")

def view_expenses_by_date_range(tracker):
    clear_screen()
    print_header("VIEW EXPENSES BY DATE RANGE")
    
    start_date = get_valid_date("Enter start date (YYYY-MM-DD): ")
    end_date = get_valid_date("Enter end date (YYYY-MM-DD): ")
    
    expenses = tracker.get_expenses_by_date_range(start_date, end_date)
    
    clear_screen()
    print_header(f"EXPENSES FROM {start_date} TO {end_date}")
    
    if not expenses:
        print("No expenses found in this date range.")
    else:
        print(f"{'ID':<5} {'Date':<12} {'Category':<20} {'Amount':>10} {'Payment':<15} {'Description':<30}")
        print("-" * 110)
        for exp in expenses:
            print(f"{exp[0]:<5} {exp[1]:<12} {exp[2]:<20} ₹{exp[3]:>9.2f} {exp[5]:<15} {exp[4]:<30}")
        
        total = sum(exp[3] for exp in expenses)
        print("-" * 110)
        print(f"{'Total:':<58} ₹{total:>9.2f}")
    
    input("\nPress Enter to continue...")

def search_expenses(tracker):
    clear_screen()
    print_header("SEARCH EXPENSES")
    
    keyword = input("Enter keyword to search: ")
    expenses = tracker.search_expenses(keyword)
    
    clear_screen()
    print_header(f"SEARCH RESULTS FOR: {keyword}")
    
    if not expenses:
        print("No expenses found matching your search.")
    else:
        print(f"{'ID':<5} {'Date':<12} {'Category':<20} {'Amount':>10} {'Payment':<15} {'Description':<30}")
        print("-" * 110)
        for exp in expenses:
            print(f"{exp[0]:<5} {exp[1]:<12} {exp[2]:<20} ₹{exp[3]:>9.2f} {exp[5]:<15} {exp[4]:<30}")
        
        total = sum(exp[3] for exp in expenses)
        print("-" * 110)
        print(f"{'Total:':<58} ₹{total:>9.2f}")
    
    input("\nPress Enter to continue...")

def view_category_summary(tracker):
    clear_screen()
    print_header("CATEGORY SUMMARY")
    
    summary = tracker.get_category_summary()
    
    if not summary:
        print("No expenses found.")
    else:
        print(f"{'Category':<25} {'Total Amount':>15} {'Count':>10} {'Percentage':>12}")
        print("-" * 70)
        
        total = sum(cat[1] for cat in summary)
        
        for cat in summary:
            percentage = (cat[1] / total * 100) if total > 0 else 0
            print(f"{cat[0]:<25} ₹{cat[1]:>14.2f} {cat[2]:>10} {percentage:>11.1f}%")
        
        print("-" * 70)
        print(f"{'TOTAL:':<25} ₹{total:>14.2f}")
    
    input("\nPress Enter to continue...")

def view_monthly_summary(tracker):
    clear_screen()
    print_header("MONTHLY SUMMARY")
    
    try:
        year = int(input("Enter year (YYYY): "))
        month = int(input("Enter month (1-12): "))
        
        if not (1 <= month <= 12):
            print("Invalid month. Please enter 1-12")
            input("\nPress Enter to continue...")
            return
        
        result = tracker.get_monthly_summary(year, month)
        
        clear_screen()
        print_header(f"SUMMARY FOR {datetime(year, month, 1).strftime('%B %Y')}")
        
        if result[0] is None:
            print("No expenses found for this month.")
        else:
            print(f"Total Expenses: ₹{result[0]:.2f}")
            print(f"Number of Transactions: {result[1]}")
            print(f"Average per Transaction: ₹{result[0]/result[1]:.2f}")
        
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    
    input("\nPress Enter to continue...")

def view_total_expenses(tracker):
    clear_screen()
    print_header("TOTAL EXPENSES")
    
    total = tracker.get_total_expenses()
    expenses = tracker.get_all_expenses()
    
    print(f"Total Amount Spent: ₹{total:.2f}")
    print(f"Total Transactions: {len(expenses)}")
    
    if expenses:
        avg = total / len(expenses)
        print(f"Average per Transaction: ₹{avg:.2f}")
    
    input("\nPress Enter to continue...")

def update_expense(tracker):
    clear_screen()
    print_header("UPDATE EXPENSE")
    
    try:
        expense_id = int(input("Enter expense ID to update: "))
        
        print("\nEnter new details (press Enter to skip):")
        date = input("New date (YYYY-MM-DD): ")
        if date:
            try:
                datetime.strptime(date, '%Y-%m-%d')
            except ValueError:
                print("Invalid date format.")
                input("\nPress Enter to continue...")
                return
        
        category = input("Update category? (y/n): ")
        if category.lower() == 'y':
            category = get_category()
        else:
            category = None
        
        amount_input = input("New amount: ")
        amount = float(amount_input) if amount_input else None
        
        payment = input("Update payment method? (y/n): ")
        if payment.lower() == 'y':
            payment_method = get_payment_method()
        else:
            payment_method = None
        
        description = input("New description: ")
        
        if tracker.update_expense(expense_id, date or None, category, amount, description or None, payment_method):
            print("\n✓ Expense updated successfully!")
        else:
            print("\n✗ Expense not found or update failed.")
            
    except ValueError:
        print("Invalid input.")
    
    input("\nPress Enter to continue...")

def delete_expense(tracker):
    clear_screen()
    print_header("DELETE EXPENSE")
    
    try:
        expense_id = int(input("Enter expense ID to delete: "))
        confirm = input(f"Are you sure you want to delete expense {expense_id}? (y/n): ")
        
        if confirm.lower() == 'y':
            if tracker.delete_expense(expense_id):
                print("\n✓ Expense deleted successfully!")
            else:
                print("\n✗ Expense not found.")
        else:
            print("\nDeletion cancelled.")
            
    except ValueError:
        print("Invalid ID.")
    
    input("\nPress Enter to continue...")

def main():
    tracker = ExpenseTracker()
    
    while True:
        print_menu()
        
        try:
            choice = input("Enter your choice (1-11): ")
            
            if choice == '1':
                add_expense(tracker)
            elif choice == '2':
                view_all_expenses(tracker)
            elif choice == '3':
                view_expenses_by_category(tracker)
            elif choice == '4':
                view_expenses_by_date_range(tracker)
            elif choice == '5':
                search_expenses(tracker)
            elif choice == '6':
                view_category_summary(tracker)
            elif choice == '7':
                view_monthly_summary(tracker)
            elif choice == '8':
                view_total_expenses(tracker)
            elif choice == '9':
                update_expense(tracker)
            elif choice == '10':
                delete_expense(tracker)
            elif choice == '11':
                print("\nThank you for using Personal Expense Tracker!")
                print("Goodbye!\n")
                tracker.close()
                sys.exit(0)
            else:
                print("\nInvalid choice. Please select 1-11")
                input("\nPress Enter to continue...")
                
        except KeyboardInterrupt:
            print("\n\nThank you for using Personal Expense Tracker!")
            print("Goodbye!\n")
            tracker.close()
            sys.exit(0)

if __name__ == "__main__":
    main()
