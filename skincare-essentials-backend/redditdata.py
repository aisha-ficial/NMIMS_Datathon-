import praw

# Initialize Reddit API credentials
reddit = praw.Reddit(client_id='your_client_id',
                     client_secret='your_client_secret',
                     user_agent='your_user_agent')

# Define skincare-related subreddits
skincare_subreddits = ['skincareaddiction', 'AsianBeauty', 'acne', 'MakeupAddiction']

# Define the number of posts to scrape from each subreddit
num_posts = 10

# Function to scrape data from Reddit
def scrape_reddit_skincare_data(subreddits, num_posts):
    skincare_data = []
    for subreddit_name in subreddits:
        subreddit = reddit.subreddit(subreddit_name)
        print(f"Scraping data from r/{subreddit_name}...")
        for submission in subreddit.hot(limit=num_posts):
            skincare_data.append({
                'title': submission.title,
                'score': submission.score,
                'url': submission.url
            })
    return skincare_data

# Main function
def main():
    skincare_data = scrape_reddit_skincare_data(skincare_subreddits, num_posts)

    # Print scraped data
    for data in skincare_data:
        print(f"Title: {data['title']}")
        print(f"Score: {data['score']}")
        print(f"URL: {data['url']}")
        print()

if __name__ == "__main__":
    main()
