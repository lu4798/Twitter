# Twitter Word Counter
App based on **Twitter's API** that counts how many times a word is tweeted by an account on its last tweets. 

Some considerations to have in mind:

- The app does not tweet, like nor retweet any content
- The app does not consider retweets nor replies in the count of the words.
- The app does not consider links as words
- The app considers hashtags as words
- The app does not consider stopwords

## twitter_word_counter has one source file and two test files:

**twitter_api.py** 

- *twitter_tweets()* : Conects to twitter api using consumer_key, consumer_secret, access_token_key, access_token_secret. In order to get them, you need to have a twitter developer account. (To find how to get yours verified go to https://developer.twitter.com/). Then gets among the last 200 tweets, retweets and replies, the latest 50 tweets (does not consider the retweets or the replies)

- *twitter_word_count()* : 

- *iterate()* : Removes the urls and media urls from the tweet text and sends the tweets to *word_counter()*

- *word_counter()*: Counts how many times a word appears on a given array. It does not considerate stopwords. 

**counter_test.py** tests word_counter() functionality

<<<<<<< HEAD
* pytest test_function.py -v

**twitter_test.py** tests the twitter's api integration and functionality

=======
**twitter_test.py** tests the twitter's api integration and functionality
>>>>>>> origin/master
