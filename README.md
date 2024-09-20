# Toxic Comment Detection Using Hatescan API

## Project Description
This project utilizes the Hatescan machine learning API to detect and classify hateful and toxic comments from a text file. The API predicts the likelihood that a given comment is perceived as toxic or threatening. Each comment is analyzed for its toxic and threat probabilities, and the results are saved to a CSV file for further review and analysis.

## Key Features
- **Input**: A text file containing comments (one comment per line).
- **Processing**: Each comment is sent to the Hatescan API, which returns toxicity and threat probabilities.
- **Output**: Results are saved in a CSV file, including the original comment, its toxicity score, and its threat score.


## Setup Instructions

### 1. Create and activate a virtual environment:
```bash
python -m venv sifu
```

- On **Windows**:
```bash
sifu\Scripts\activate
```

- On **Linux/Mac**:
```bash
source sifu/bin/activate
```

### 2. Prepare input file:
- **comments.txt**: A text file where each line represents a comment to be analyzed.

## Running the Script
1. To run the script and detect toxic comments, use the following command:
```bash
python script.py
```

2. The script will read the comments from `comments.txt`, send them to the Hatescan API, and generate a CSV file `hatescan_results.csv` containing the toxic and threat probabilities for each comment.

## Example Output (CSV):
```
comment,toxic_predictions,threat_predictions
"This is an example comment",2.5,0.0
"This is a toxic comment",5.0,0.8
...
```

## Notes:
- Make sure your API usage respects rate limits and permissions set by the Hatescan service.
- This project works with English and Swedish text. The language can be auto-detected by setting the `flag_detect_lang` to `True`.


