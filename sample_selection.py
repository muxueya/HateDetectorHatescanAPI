import pandas as pd

# Function to randomly select X and Y comments based on toxicity predictions and save to separate files
def select_comments(input_file, high_output_file, low_output_file, X, Y):
    # Load the hatescan_results.csv file into a DataFrame
    df = pd.read_csv(input_file)
    
    # Convert the 'toxic_predictions' column to numeric (in case it's a string)
    df['toxic_predictions'] = pd.to_numeric(df['toxic_predictions'], errors='coerce')

    # Filter the comments into two categories:
    # 1. Comments where toxic_predictions >= 50%
    high_toxic = df[df['toxic_predictions'] >= 50]

    # 2. Comments where toxic_predictions < 50%
    low_toxic = df[df['toxic_predictions'] < 50]

    # Randomly sample X comments from high_toxic
    selected_high_toxic = high_toxic.sample(n=X, random_state=42)

    # Randomly sample Y comments from low_toxic
    selected_low_toxic = low_toxic.sample(n=Y, random_state=42)

    # Save the high-toxicity comments to a CSV file
    selected_high_toxic.to_csv(high_output_file, index=False, encoding='utf-8')

    # Save the low-toxicity comments to a separate CSV file
    selected_low_toxic.to_csv(low_output_file, index=False, encoding='utf-8')

    print(f"Randomly selected {X} high-toxicity comments saved to {high_output_file}")
    print(f"Randomly selected {Y} low-toxicity comments saved to {low_output_file}")

# Usage
if __name__ == '__main__':
    # Path to the hatescan_results.csv file
    input_file = 'hatescan_results.csv'

    # Output file for the high-toxicity comments
    high_output_file = 'high_toxic_comments.csv'

    # Output file for the low-toxicity comments
    low_output_file = 'low_toxic_comments.csv'

    # Number of comments to select
    X = 213  # Number of comments with toxic_predictions >= 50%
    Y = 342  # Number of comments with toxic_predictions < 50%

    # Select comments and save the results
    select_comments(input_file, high_output_file, low_output_file, X, Y)
