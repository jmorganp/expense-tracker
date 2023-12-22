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
expense_db = ExpenseDatabase() # create an expense database instance
monthly_expense = Expense('Altschool Tuition (Monthly)', 30.0)
```

### To add the sample expense to the database:
```python
expense_db.add_expense(monthly_expense)
```

### To update the title & amount of the expense:
```python
monthly_expense.update(title='Altschool Tuition (Monthly) (10% off)', amount=27.0)
```

### You can perform the following operations on the Expense Database:
## expense retrieval by id (UUID):
```python
expense = expense_db.get_expense_by_id('607bd6a6-7838-414f-846b-0eb76d4504f9')
```

## expense retrieval by title:
```python
expense = expense_db.get_expense_by_title('Altschool Tuition (Monthly)')
```

## expense removal (by id):
```python
expense_db.remove_expense('607bd6a6-7838-414f-846b-0eb76d4504f9')
```

## get expenses as a list of dictionaries:
```python
expense_dict = expense_db.to_dict()
```

### Or for convenience, just run the following in the terminal ⚡:
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