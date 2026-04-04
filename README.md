📝 AI Expense Tracker (Flask + Streamlit)

Overview
This project is an AI-powered expense tracker that allows users to:
- Add and manage expenses
- Analyze spending patterns
- Predict expense categories using Machine Learning

---

🚀 Features

- REST API using Flask
- Interactive UI using Streamlit
- Category prediction using ML (Naive Bayes)
- JSON-based data storage

---

👩‍💻 Tech Stack

- Python
- Flask
- Streamlit
- Scikit-learn

---


🗃️ Project Structure

ai-expense-tracker/
```
│
├── expenses.json/    # stores the data in json format
│
├── app.py            # API integration using Flask and Requests
├── logic.py          # Core logic for accessing the tracker
├── model.py          # AI model using NB algorithm and CounterVectorizer to predict category 
|── ui.py             # User Interface (basic) using streamlit
├── requirements.txt  # Pre-requisites to be downloaded
└── README.md         # Project documentation (you're here!)
```
---

⚙️ How to Run

1. **Install Dependencies**
    ```Bash
    pip install -r requirements.txt

2. **Run backend**
    python app.py

3. **Run UI**
    streamlit run ui.py

---

**Author**

Bhuvaneshwari S 

LinkedIn - www.linkedin.com/in/bhuvana-sankar, 

Mail - bhuvanaasankar241@gmail.com  

---

This project is for educational purposes. You can use and modify it freely.