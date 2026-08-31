from solutions.heap_priority_queue.medium._0355_design_twitter import Twitter

def test_design_twitter():
    twitter = Twitter()

    twitter.postTweet(1, 5)
    assert twitter.getNewsFeed(1) == [5]

    twitter.follow(1, 2)
    twitter.postTweet(2, 6)

    assert twitter.getNewsFeed(1) == [6, 5]

    twitter.unfollow(1, 2)
    assert twitter.getNewsFeed(1) == [5]
