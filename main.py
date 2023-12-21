import uuid
from datetime import datetime, timezone


class Expense:
    """
    Represents an individual financial expense.

    Attributes:
    - id (str): A unique identifier generated as a UUID string.
    - title (str): A string representing the title of the expense.
    - amount (float): A float representing the amount of the expense.
    - created_at (str): A timestamp indicating when the expense was created.
    - updated_at (str): A timestamp indicating the last time the expense was updated.

    Note:
    - 'id' is generated using uuid.uuid4() because it creates a random UUID.
    - On initialization, 'updated_at' timestamp is a copy of 'created_at', 
        this prevents storing a different timestamp for 'updated_at' & 'created_at'
        when initializing the Expense object (which is inaccurate)
    """
    def __init__(self, title: str, amount: float) -> None:
        """Initializes Expense object"""
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = get_utc_timestamp()
        self.updated_at = self.created_at

    def update(self, title: str = None, amount: float = None) -> None:
        """
        Allows updating the title and/or amount, updating the updated_at timestamp
        if a change is made.

        Parameters:
        - title (str): The new title of the Expense.
        - amount (float): The new amount of the Expense.

        Returns:
        None

        If title and amount are both None, no action is taken.
        """
        if title == None and amount == None:
            return
        
        if title != None:
            self.title = title
        if amount != None:
            self.amount = amount

        self.updated_at = get_utc_timestamp()

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the expense.

        Returns:
        dict: A dictionary containing the attributes of the Expense object.
        """
        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


class ExpenseDatabase:
    """
    Manages a collection of Expense objects.

    Attributes:
    - expenses (list): A list storing Expense instances.
    """
    def __init__(self) -> None:
        """Initializes the list"""
        self.expenses = []

    def add_expense(self, expense: Expense) -> None:
        """
        Adds an expense.

        Parameters:
        - expense (Expense): An instance of Expense

        Returns:
        None
        """
        self.expenses.append(expense)

    def remove_expense(self, expense_id: str) -> None:
        """
        Removes an expense.

        Parameters:
        - expense_id (str): A UUID to identity the expense

        Returns:
        None
        """
        for expense in self.expenses:
            if expense.id == expense_id:
                self.expenses.remove(expense)
            return

    def get_expense_by_id(self, expense_id: str) -> Expense | None:
        """
        Retrieves an expense by ID.

        Parameters:
        - expense_id (str): The UUID to identity the expense

        Returns:
        Expense | None: Returns an Expense object if found or None if not.
        """
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense

    def get_expense_by_title(self, expense_title: str) -> Expense | None:
        """
        Retrieves an expense by title.

        Parameters:
        - expense_title (str): The Title to identity the expense

        Returns:
        Expense | None: Returns an Expense object if found or None if not.
        """
        for expense in self.expenses:
            if expense.title == expense_title:
                return expense

    def to_dict(self) -> list[dict]:
        """
        Returns a list of dictionaries representing expenses,
        utilizing the 'to_dict()' method of the Expense object

        Returns:
        list[dict]: A list containing dictionaries
        """
        temp_list = []

        for expense in self.expenses:
            temp_list.append(expense.to_dict())

        return temp_list


def get_utc_timestamp() -> str:
    """
    Returns a string of the current time (UTC) in ISO 8601 format

    Returns:
    str: A string representation of the current time (UTC) in ISO 8601 format
    """
    current_time_in_utc = datetime.now(timezone.utc)
    current_time_iso_8601 = current_time_in_utc.isoformat(' ')
    
    return current_time_iso_8601


if __name__ == '__main__':
    # create new expense database object
    expense_db = ExpenseDatabase()

    # create new expense object
    monthly_expense = Expense('Altschool Tuition (Monthly)', 30.0)
    quarterly_expense = Expense('Altschool Tuition (Quarterly)', 80.0)
    annual_expense = Expense('Altschool Tuition (Annual)', 290.0)

    # add expenses to expense_db
    expense_db.add_expense(monthly_expense)
    expense_db.add_expense(quarterly_expense)
    expense_db.add_expense(annual_expense)

    print('Initial expenses:')
    all_expenses_dict = expense_db.to_dict()
    for expense_dict in all_expenses_dict:
        print(expense_dict, end='\n\n')

    # apply update
    for expense_dict in all_expenses_dict:
        expense = expense_db.get_expense_by_id(expense_dict['id'])
        curr_expense_amount = expense.amount
        discount_in_percentage = 0.1  # -10%
        new_expense_amount = curr_expense_amount - (curr_expense_amount * discount_in_percentage)
        expense.update(amount=new_expense_amount)

    print('After update:')
    all_expenses_dict = expense_db.to_dict()
    for expense_dict in all_expenses_dict:
        print(expense_dict, end='\n\n')
