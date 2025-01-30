from googleapiclient.discovery import build
import os
import json

def fetch_all_comments(youtube, video_id):
    """
    Fetch all comments for a video using pagination.
    """
    comments = []
    next_page_token = None

    while True:
        # Make API request to fetch comments
        request = youtube.commentThreads().list(
            part="snippet,replies",
            videoId=video_id,
            pageToken=next_page_token
        )
        response = request.execute()

        # Add comments to the list
        comments.extend(response['items'])

        # Check if there are more pages
        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    return comments

def main():
    # Set up the YouTube API client
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyC2CQ0uLsjqcU8HHsuAo4lD9wdTTikc_gM"  # Use environment variable for API key

    if not DEVELOPER_KEY:
        raise ValueError("Please set the YOUTUBE_API_KEY environment variable.")

    youtube = build(api_service_name, api_version, developerKey=DEVELOPER_KEY)

    # Fetch all comments for a specific video
    video_id = "q8q3OFFfY6c"  # Replace with your video ID
    comments = fetch_all_comments(youtube, video_id)

    # Save comments to a JSON file
    with open("comments.json", "w") as f:
        json.dump(comments, f, indent=4)

    print(f"Fetched {len(comments)} comments. Saved to comments.json.")

if __name__ == "__main__":
    main()