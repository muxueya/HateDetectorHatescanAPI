import pandas as pd
import krippendorff
import numpy as np

# Load the Excel file
df = pd.read_excel('Sample_toxic_comments.xlsx')

# Extract only the columns for the annotators (a, b, c, d, e)
annotations = df[['a', 'b', 'c', 'd', 'e']].values.T  # Transpose to match the input format for Krippendorff's alpha

# Calculate Krippendorff's alpha for binary data (nominal scale)
alpha = krippendorff.alpha(reliability_data=annotations, level_of_measurement='nominal')

# Print the result
print(f"Krippendorff's Alpha: {alpha:.3f}")
