import json
import os 

DATA_FILE="expenses.json"

categories = ['groceries', 'transportation', 'entertainment', 'utilities']
expenses = []

def load_data():
    global expenses, categories

    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)

            expenses = data.get("expenses", [])
            categories = data.get("categories", categories)

        except:
            # 🔥 If file is empty or corrupted
            expenses = []
            categories = ['groceries', 'transportation', 'entertainment', 'utilities']
            save_data()
            
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump({"expenses": expenses, "categories": categories}, f, indent=2)

def add_expense(amount, category, description=""):
    load_data()
    next_id = (max([e.get("id", 0)for e in expenses]) + 1) if expenses else 1

    if category not in categories:
        categories.append(category)

    expense = {
        "id" : next_id,
        "amount" : round(amount, 2),
        "category": category,
        "description": description
    }
    expenses.append(expense)
    save_data()
    return expense

def get_expense():
    load_data()
    return expenses

def get_summary():
    load_data()
    total = sum(e["amount"]for e in expenses)

    breakdown = {}
    for e in expenses:
        breakdown[e["category"]] = breakdown.get(e["category"], 0) + e["amount"]
    return {"total": total, "breakdown": breakdown} 