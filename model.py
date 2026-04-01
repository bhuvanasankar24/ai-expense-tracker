from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

#training data
texts = [
    "bus ticket", "uber ride", "petrol",
    "pizza", "burger", "coffee",
    "movie ticket", "netflix",
    "electric bill", "water bill"
]
labels = [
    "transportation", "transportation", "transportation",
    "groceries", "groceries", "groceries",
    "entertainment", "entertainment",
    "utilities", "utilities"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

def predict_category(description):
    X_test = vectorizer.transform([description])
    return model.predict(X_test)[0]

    