# -*- coding: utf-8 -*-
"""Reddit_scrapping.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Kw3uKjekPoCnbdSSqo0QCQd2DngDbG7o
"""

# Initialize Reddit API
reddit = praw.Reddit(
    client_id=script,
    client_secret=secret,
    user_agent=user
)

def get_reddit_stock_titles(
    keywords: List[str],
    subreddits: Optional[List[str]] = None,
    start_date: datetime = datetime(2022, 1, 1),
    end_date: datetime = datetime(2024, 11, 30)
) -> pd.DataFrame:
    """
    Collect Reddit posts with specified keywords in their titles from selected subreddits.

    :param keywords: List of keywords to search for.
    :param subreddits: List of subreddit names to search within. Defaults to a predefined list.
    :param start_date: Start of the date range for posts.
    :param end_date: End of the date range for posts.
    :return: DataFrame containing collected posts.
    """
    if subreddits is None:
        subreddits = [
            'stocks', 'investing', 'wallstreetbets', 'unusual_whales', 'Trading',
            'ValueInvesting', 'TradingEdge', 'WallStreetbetsELITE', 'Wallstreetsilver',
            'stockstobuytoday', 'StocksAndTrading', 'stockmarket', 'finance', 'options',
            'pennystocks', 'Bogleheads', 'thetagang', 'Daytrading', 'TheRaceTo10Million',
            'Economics', 'swingtrading'
        ]

    start_timestamp = start_date.timestamp()
    end_timestamp = end_date.timestamp()

    all_titles = []

    for subreddit_name in subreddits:
        subreddit = reddit.subreddit(subreddit_name)
        for keyword in keywords:
            for post in subreddit.search(f'title:{keyword}', sort='new', limit=None):
                if start_timestamp <= post.created_utc <= end_timestamp:
                    all_titles.append({
                        'title': post.title,
                        'score': post.score,
                        'num_comments': post.num_comments,
                        'created_at': datetime.fromtimestamp(post.created_utc),
                        'subreddit': subreddit_name
                    })

    # Convert collected data to a DataFrame
    return pd.DataFrame(all_titles)

keywords = ['AAPL', 'Apple']
popular_subreddits = [
    'stocks', 'investing', 'wallstreetbets', 'unusual_whales', 'ValueInvesting',
    'TradingEdge', 'WallStreetbetsELITE', 'Wallstreetsilver', 'stockstobuytoday',
    'StocksAndTrading', 'stockmarket', 'finance', 'options', 'pennystocks',
    'Bogleheads', 'thetagang', 'Daytrading', 'TheRaceTo10Million', 'Economics', 'swingtrading'
]
reddit_titles = get_reddit_stock_titles(keywords, subreddits=popular_subreddits)

# Save to CSV
reddit_titles.to_csv('reddit_subreddits.csv', index=False)

# Summary
total_posts = len(reddit_titles)
average_score = reddit_titles['score'].mean() if total_posts > 0 else 'N/A'
print(f"Total posts collected: {total_posts}")
print(f"Average post score: {average_score}")