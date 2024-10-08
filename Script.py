import requests
import json
import csv
import pandas as pd

# Function to get toxic probability from Hatescan API
def get_toxic_probability(text, language='en', flag_detect_lang='False'):
    # Prepare the payload
    text = text.replace('"', '\\"')
    payload = '{"text": "' + text + '", "language": "' + language + '" , "flag_detect_lang": "' + flag_detect_lang + '"}'
    json_payload = json.loads(payload, strict=False)

    # Headers for the API request
    headers = {"Content-Type": "application/json; charset=utf-8"}

    # Hatescan API URL (updated URL)
    api_hatescan_url = 'https://api.hatescan.com/predict/toxic'

    # Send a POST request to the Hatescan API
    hatescan_response = requests.post(api_hatescan_url, headers=headers, json=json_payload)

    # Return the API response as JSON
    return hatescan_response.json()

# Function to read comments from an Excel file
def read_comments_from_excel(filename):
    # Load the comments from an Excel file (assuming the column name is 'comment')
    df = pd.read_excel(filename)
    comments = df['comment'].astype(str).tolist()  # Convert comments to a list of strings
    return comments

# Main function to process the comments
def process_comments(input_file, output_file, language='en', flag_detect_lang='False'):
    # Read comments from the Excel file
    comments = read_comments_from_excel(input_file)
    num_comments = len(comments)

    # Prepare the result list
    results = []

    # Loop through each comment and get toxicity scores
    for idx, comment in enumerate(comments, 1):
        print(f"Processing comment {idx}/{num_comments}: {comment[:100]}")
        try:
            toxic_score = get_toxic_probability(comment, language, flag_detect_lang)
            
            # Correct key to access predictions
            toxic_predictions = toxic_score.get('predictions', 'N/A')

            # Output the results to the terminal
            print(f"Toxic probability score: {toxic_predictions}%\n")

            # Append the comment and toxic probabilities to the result list
            results.append({
                'comment': comment,
                'toxic_predictions': toxic_predictions
            })
        except Exception as e:
            print(f"Error processing comment: {comment}, Error: {e}")

    # Save the results to a CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['comment', 'toxic_predictions']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(results)

    print(f"Results saved to {output_file}")

# Usage
if __name__ == '__main__':
    # Path to the input Excel file with comments
    input_file = 'incels-5000.xlsx'
    
    # Path to the output CSV file where results will be saved
    output_file = 'hatescan_results.csv'

    # Set language and flag for automatic language detection
    language = 'en'  # 'en' for English, 'sv' for Swedish
    flag_detect_language = 'False'  # Set to 'True' to auto-detect language

    # Process the comments and save results to a CSV file
    process_comments(input_file, output_file, language, flag_detect_language)
