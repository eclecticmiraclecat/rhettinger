'Simple message publisher/subscriber service'

from typing import NamedTuple, DefaultDict, Deque, Dict, Set, Optional, List
from collections import namedtuple, deque, defaultdict
import time
from itertools import islice
from heapq import merge
from sys import intern

User = str
Post = NamedTuple('Post', [('timestamp', float), ('user', str) , ('text', str)])

posts = deque()                     # type: Deque[Post]     # Posts from newest to oldest
user_posts = defaultdict(deque)     # type: DefaultDict[User, deque]
following = defaultdict(set)        # type: DefaultDict[User, Set[User]]
followers = defaultdict(set)        # type: DefaultDict[User, Set[User]]

def post_message(user: User, text: str, timestamp: float=None) -> None:
    user = intern(user)
    timestamp = timestamp or time.time()
    post = Post(timestamp, user, text)
    posts.appendleft(post)
    user_posts[user].appendleft(post)

def follow(user: User, followed_user: User) -> None:
    user, followed_user = intern(user), intern(followed_user)
    following[user].add(followed_user)
    followers[followed_user].add(user)

def posts_by_user(user: User, limit: Optional[int] = None) -> List[Post]:
    return list(islice(user_posts[user], limit))

def posts_for_user(user: User, limit: Optional[int] = None) -> List[Post]:
    relevant = merge(*[user_posts[followed_user] 
                      for followed_user in following[user]], reverse=True)
    return list(islice(relevant, limit))

def search(phrase:str, limit: Optional[int] = None) -> List[Post]:
    # Todo: Add pre-indexing to speed-up searches
    # Todo: Add time sensetive caching for search queries
    return list(islice((post for post in posts if phrase in post.text), limit))
