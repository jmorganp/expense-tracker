# Alt-de-project-3 💻

## Description ℹ️:
An implementation of 'Expense' and 'ExpenseDatabase' python classes, to model and manage financial expenses.

### Expense 💳:
Represents an individual financial expense with the following attributes:
- id (str): A unique identifier generated as a UUID string.
- title (str): A string representing the title of the expense.
- amount (float): A float representing the amount of the expense.
- created_at (str): A timestamp indicating when the expense was created.
- updated_at (str): A timestamp indicating the last time the expense was updated.

### ExpenseDatabase 💳💾:
Manages a collection of Expense objects, and has the following attribute:
- expenses (list): A list storing Expense instances.

## Cloning 👯:
```
git clone https://github.com/jmorganp/alt-de-project-3.git
```
```
cd alt-de-project-3
```

## Usage ⚙️:
### You can import the Expense and ExpenseDatabase classes into your script (in the same directory) as follows:
```python
from main import Expense, ExpenseDatabase
```
### Then initialize them as follows:

```python
expense_db = ExpenseDatabase()
monthly_expense = Expense('Altschool Tuition (Monthly)', 30.0)
```
### Or for convenience, just run the following in the terminal (to see how it works) ⚡:
```
python main.py
```

### Main guard 💂‍♂️ (code executed if you ran the script directly as specified above):
![Main guard](https://i.imgur.com/ya7gjEu.png)

## Requires 🧾:
Python >= 3.10

## References 🔗:
- https://docs.python.org/3/library/uuid.html
- https://stackoverflow.com/questions/534839/how-to-create-a-guid-uuid-in-python#answer-534847
- https://docs.python.org/3/library/datetime.html#datetime.datetime.isoformat
- https://data.altschoolafrica.com/programs/data-engineering