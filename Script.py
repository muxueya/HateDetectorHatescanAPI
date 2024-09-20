import requests
import json
import csv

# Function to get toxic and threat probability from Hatescan API
def get_toxic_threat_probability(text, language='en', flag_detect_lang='False'):
    # Prepare the payload
    text = text.replace('"', '\\"')
    payload = '{"text": "' + text + '", "language": "' + language + '" , "flag_detect_lang": "' + flag_detect_lang + '"}'
    json_payload = json.loads(payload, strict=False)

    # Headers for the API request
    headers = {"Content-Type": "application/json; charset=utf-8"}

    # Hatescan API URL
    api_hatescan_url = 'https://detect.hatescan.com/predict/toxic'

    # Send a POST request to the Hatescan API
    hatescan_response = requests.post(api_hatescan_url, headers=headers, json=json_payload)

    # Return the API response as JSON
    return hatescan_response.json()

# Function to read comments from a text file
def read_comments_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        comments = [line.strip() for line in file.readlines()]
    return comments

# Main function to process the comments
def process_comments(input_file, output_file):
    # Read comments from the input file
    comments = read_comments_from_file(input_file)
    num_comments = len(comments)

    # Prepare the result list
    results = []

    # Loop through each comment and get toxicity/threat scores
    for idx, comment in enumerate(comments, 1):
        
        print(f"Processing comment {idx}/{num_comments}: {comment[:100]}")
        try:
            toxic_threat_score = get_toxic_threat_probability(comment)
            # Output the results to the terminal
            print(f"Toxic probability score: {toxic_threat_score['toxic_predictions']}%, Threat probability score: {toxic_threat_score['threat_predictions']}%\n")

            # Append the comment, toxic, and threat probabilities to the result list
            results.append({
                'comment': comment,
                'toxic_predictions': toxic_threat_score['toxic_predictions'],
                'threat_predictions': toxic_threat_score['threat_predictions']
            })
        except Exception as e:
            print(f"Error processing comment: {comment}, Error: {e}")


    # Save the results to a CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['comment', 'toxic_predictions', 'threat_predictions']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(results)

    print(f"Results saved to {output_file}")

# Usage
if __name__ == '__main__':
    # Path to the input text file with comments (one comment per line)
    input_file = 'comments.txt'
    
    # Path to the output CSV file where results will be saved
    output_file = 'hatescan_results.csv'

    # Process the comments and save results to a CSV file
    process_comments(input_file, output_file)
