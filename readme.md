# Personal Expense Tracker

A simple command line expense tracker built with Python that helps you keep track of your spending without any complicated setup or external dependencies.

## What is this?

This is a terminal based application I built to manage personal expenses. It runs entirely in your command line and stores everything in a local SQLite database. No internet required, no fancy installations needed just Python and you're good to go.

I made this because I wanted something quick and straightforward for tracking my daily expenses without opening a browser or dealing with ads and subscriptions. Plus, it's always nice to have your financial data stored locally on your own machine.

## What can it do?

The tracker has all the basic features you'd expect:

- Add new expenses with details like date, category, amount, and payment method
- View all your expenses in a nice formatted table
- Filter expenses by category or date range
- Search for specific expenses using keywords
- Get summaries showing where your money goes
- See monthly breakdowns of your spending
- Update or delete expenses if you made a mistake
- Everything saves automatically to a database file

## Getting started

You'll need Python 3.7 or newer installed on your computer. That's literally it.

Download the expense_tracker.py file, open your terminal, navigate to where you saved it, and run:

```bash
python expense_tracker.py
```

The first time you run it, the program will automatically create a database file to store your expenses. After that, just run the same command whenever you want to track your spending.

## How to use it

When you start the program, you'll see a menu with numbered options. Just type the number of what you want to do and hit enter.

### Adding expenses

Pick option 1 from the menu. The program will ask you for:
- The date (just press enter to use today's date)
- A category (like Food, Transportation, Shopping, etc.)
- How much you spent
- How you paid (Cash, Card, UPI, etc.)
- Any notes you want to add

### Viewing your expenses

There are several ways to look at your expenses:

Option 2 shows everything you've recorded, newest first. You'll see a table with all the details plus a total at the bottom.

Option 3 lets you filter by category if you want to see just your food expenses or transportation costs.

Option 4 is for checking expenses between specific dates, which is handy for monthly reviews.

Option 5 lets you search for expenses by typing keywords.

### Getting insights

Option 6 gives you a category breakdown showing what percentage of your money goes where. It's eye-opening to see how much you're actually spending on different things.

Option 7 shows you statistics for any month you choose - total spent, number of transactions, and average expense.

Option 8 displays your overall spending across all time.

### Editing and deleting

Option 9 lets you update an expense if you entered something wrong. Just provide the expense ID and the new information.

Option 10 deletes an expense. The program will ask you to confirm before actually removing it.

## Categories included

The tracker comes with eight categories that cover most common expenses:
- Food & Dining
- Transportation
- Shopping
- Entertainment
- Bills & Utilities
- Healthcare
- Education
- Others

## Payment methods

You can track expenses across five different payment types:
- Cash
- Credit Card
- Debit Card
- UPI
- Net Banking

This helps you see not just what you're spending on, but how you're spending it.

## About the database

All your data gets stored in a file called expenses.db that sits right next to the Python script. It's a SQLite database, which is super reliable and doesn't need any special software to work with.

The database has one main table that stores:
- A unique ID for each expense
- The date
- Category
- Amount
- Description
- Payment method

If you ever want to back up your data, just copy that expenses.db file somewhere safe.
## Some notes

This is a fairly simple tool that does what it's designed to do well. It's not trying to be a full-featured accounting system or compete with fancy budgeting apps. It's just a straightforward way to track your spending from your terminal.

The code doesn't have external dependencies on purpose. I wanted something that would just work without having to install a bunch of packages. Everything uses Python's standard library.

If you find bugs or have suggestions, feel free to open an issue or submit a pull request. I built this for myself but I'm happy to improve it if others find it useful.

## Technical stuff

Built with Python 3.7+. Uses only standard library modules - sqlite3 for the database, datetime for handling dates, os and sys for basic system operations. Works on Windows, Mac, and Linux.

The whole thing is in a single Python file to keep it simple. The database gets created automatically on first run.

## License

This project is open source under the MIT License. Feel free to use it, modify it, or learn from it however you want.

## Final thoughts

I've been using this to track my expenses for a while now and it's been genuinely helpful for understanding where my money goes. There's something satisfying about keeping your financial data local and having a tool you can use entirely from the keyboard.
