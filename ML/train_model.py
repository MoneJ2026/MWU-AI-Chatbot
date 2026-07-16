from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# Convert text to numbers
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(X)


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create model
model = LogisticRegression()


# Train model
model.fit(X_train, y_train)


# Test model
prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)

print("Accuracy:", accuracy)