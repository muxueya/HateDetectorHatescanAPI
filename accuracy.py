import pandas as pd
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_excel('Sample_toxic_comments.xlsx') 

ml_accuracy = accuracy_score(df['label2'], df['label1'])

# Print ML Method Accuracy
print(f"ML Method Accuracy: {ml_accuracy:.3f}")
