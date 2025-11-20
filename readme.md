# Personal Expense Tracker 💰

A simple command-line application built with Python to help you track and manage your personal expenses efficiently.

## Features

- **Add Expenses** - Record new expenses with date, category, amount, and description
- **View All Expenses** - Display all recorded expenses in a formatted table
- **Search by Category** - Filter and view expenses by specific categories
- **Calculate Total** - Get the sum of all your expenses
- **Category-wise Summary** - See expense breakdown by category with percentages
- **Delete Last Expense** - Remove the most recent expense entry

## Categories

The tracker supports the following expense categories:
- Food
- Transport
- Bills
- Shopping
- Other

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker
```

2. Ensure you have Python 3.x installed:
```bash
python --version
```

## Usage

Run the program:
```bash
python expense_tracker.py
```

### Main Menu Options

1. **Add Expense** - Enter date (DD-MM-YYYY), category, amount (₹), and description
2. **View All Expenses** - See all your recorded expenses
3. **Search by Category** - Filter expenses by category
4. **Calculate Total Expenses** - View total amount spent
5. **Category-wise Summary** - See spending breakdown with percentages
6. **Delete Last Expense** - Remove the most recent entry
7. **Exit** - Close the application

## Data Storage

Expenses are stored in a text file (`expenses.txt`) in the following format:
```
DD-MM-YYYY|Category|Amount|Description
```

## Example Usage

```
--- ADD EXPENSE ---
Enter date (DD-MM-YYYY): 15-11-2024
Enter category (Food/Transport/Bills/Shopping/Other): Food
Enter amount (₹): 250
Enter description: Lunch at restaurant
✓ Expense added successfully!
```

## Requirements

- Python 3.x
- No external dependencies required

## File Structure

```
expense-tracker/
│
├── expense_tracker.py    # Main program file
├── expenses.txt          # Auto-generated data file
└── README.md            # This file
```

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## License

This project is open source and available under the MIT License.

## Author
Ayush Yadav

## Acknowledgments

Built as a simple Python project for learning file handling and basic CRUD operations.

