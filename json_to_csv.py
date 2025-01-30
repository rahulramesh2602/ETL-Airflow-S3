import json
import csv
from datetime import datetime

def process_comments(response_items):
    """
    Process raw comment data to extract relevant fields.
    """
    comments = []
    for comment in response_items:
        # Extract top-level comment details
        top_level_comment = comment['snippet']['topLevelComment']['snippet']
        author = top_level_comment.get('authorDisplayName', 'Unknown Author')
        comment_text = top_level_comment.get('textOriginal', '')
        publish_time = top_level_comment.get('publishedAt', '')

        # Append processed comment to the list
        comment_info = {
            'author': author,
            'comment': comment_text,
            'published_at': publish_time
        }
        comments.append(comment_info)

    print(f'Finished processing {len(comments)} comments.')
    return comments

def save_to_csv(data, filename):
    """
    Save processed comments to a CSV file.
    """
    # Define CSV column headers
    fieldnames = ['author', 'comment', 'published_at']

    # Write data to CSV
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"Processed comments saved to {filename}.")

def main():
    # Load raw comments from the JSON file
    input_filename = "comments.json"
    with open(input_filename, 'r', encoding='utf-8') as file:
        raw_comments = json.load(file)

    # Process the raw comments
    processed_comments = process_comments(raw_comments)

    # Save processed comments to a CSV file
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_filename = f"Youtube_data.csv"
    save_to_csv(processed_comments, output_filename)

if __name__ == "__main__":
    main()