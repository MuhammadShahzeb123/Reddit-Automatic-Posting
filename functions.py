import praw

def post_to_reddit(subreddit_name: str, title: str, text: str, client_id: str, client_secret: str, username: str, password: str):
    """
    Posts a text submission to a given subreddit using Reddit API.

    Parameters:
    - subreddit_name (str): The name of the subreddit to post to.
    - title (str): The title of the Reddit post.
    - text (str): The text content of the Reddit post.
    - client_id (str): The Reddit app client ID.
    - client_secret (str): The Reddit app client secret.
    - username (str): The Reddit username.
    - password (str): The Reddit password.

    Returns:
    - submission (praw.models.Submission): The submission object if the post was successful.
    """
    try:
        # Initialize the Reddit client
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            username=username,
            password=password,
            user_agent="RedditPostBot by /u/{}".format(username)
        )

        # Post to the specified subreddit
        subreddit = reddit.subreddit(subreddit_name)
        submission = subreddit.submit(title, selftext=text)
        
        print(f"Post created: https://www.reddit.com{submission.permalink}")
        return submission

    except Exception as e:
        print(f"An error occurred: {e}")
        return None