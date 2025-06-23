import pandas as pd # type: ignore
from sklearn.ensemble import RandomForestClassifier # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
import pickle

# Load the dataset
data = pd.read_csv("C:/Users/Triveni/Downloads/archive (2)/phishing.csv")

# Drop 'Index' if it exists
if 'Index' in data.columns:
    data.drop('Index', axis=1, inplace=True)

# Select features and target
features = ['PrefixSuffix-', 'SubDomains', 'HTTPS', 'AnchorURL', 'WebsiteTraffic']
X = data[features]
y = data['class']  # 1 = legitimate, -1 = phishing

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate model
from sklearn.metrics import accuracy_score # type: ignore
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save model
with open('phishing_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model saved as phishing_model.pkl")
