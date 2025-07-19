import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from utils import calculate_cosine_similarity
 
# Example dataset
data = [
   ("The quick brown fox jumps over the lazy dog.", "The quick brown fox jumps over the lazy dog.", 1),
   ("Data science is interesting.", "I love studying data science.", 1),
   ("Python is cool.", "Java is another language.", 0),
   ("Weather is nice today.", "Apples are tasty.", 0)
]
 
rows = []
for original, submission, label in data:
   sim = calculate_cosine_similarity(original, submission)
   rows.append([sim, label])
 
df = pd.DataFrame(rows, columns=["similarity", "label"])
X = df[["similarity"]]
y = df["label"]
 
model = LogisticRegression()
model.fit(X, y)
joblib.dump(model, "plagiarism_model.pkl")
print("Model trained and saved.")