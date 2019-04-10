import twitter
import re
from stop_words import get_stop_words
from twitter import *

#consumer_key='55suUJm6onAAI4XAECubk4qSI'
#consumer_secret='Zg1IStJmFkTYUfSfmwOSqTklAVqC0lsxTo1KKlBwZ6cqBfOsTs'
#access_token_key='705776698785189888-hqG3Utf5JyoJcjcSkaQgfJX1eAUG4xg'
#access_token_secret='JHcfpoCEMvPlNlIOU8pRPuEMK2SOli2jRzNKAImH8SPEr'


def word_counter(array):
    acceptable_languages = ['arabic', 'bulgarian', 'catalan', 'czech', 'danish', 'dutch', 'english', 'finnish',
                            'french', 'german', 'hungarian', 'indonesian', 'italian',
                            'norwegian', 'polish', 'portuguese', 'romanian', 'russian', 'spanish', 'swedish', 'turkish',
                            'ukrainian']

    if not isinstance(array, str):
        raise TypeError

    string_list_lowercase = []
    final_list = []
    list_aux = []
    forbidden_words = []

    for language in acceptable_languages:
        forbidden_words.append(get_stop_words(language))

    word_list = (array.lower()).split()

    for word in word_list:
        is_stopword = 0
        for forbidden in forbidden_words:

            if word in forbidden and is_stopword == 0:
                is_stopword = 1

        if is_stopword == 0:
            list_aux.append(word)

    for x in list_aux:
        reemplazo = re.sub("[^\w]", "", x)
        if reemplazo != '':
            string_list_lowercase.append(re.sub("[^\w]", "", x))

    while len(string_list_lowercase) > 0:
        current_word = string_list_lowercase[0]
        counter = string_list_lowercase.count(current_word)
        while current_word in string_list_lowercase:
            string_list_lowercase.remove(current_word)

        final_list.append([current_word, counter])

    return sorted(final_list, key=lambda x: x[1], reverse=True)


#def mierdas_twitter():
#    array = []
#
#    # Get the public timeline
#
#    t = Twitter(
#        auth=OAuth(access_token_key, access_token_secret, consumer_key, consumer_secret))
#    print(t.statuses.home_timeline(user_id='@realdonaldtrump',count=50 ))
#


def mierdas_twitter():
    api = twitter.Api(consumer_key='xJBNVbtmRJrd44fslR38GiJNr', consumer_secret='w22znbElOOjVs2oYORs2hqxmUF1K6MfJ3YUEoefttZVDG5SbwW',access_token_key='831510109629071361-OFLx61XL1iiFQNDvH1OeBYgBWZn5dQR', access_token_secret='l3NObDqc4psYpok3YSv7HFKwuVEAdijABoE0WSE3CEfDT' )
    array = ''
    twits = api.GetUserTimeline(screen_name='@realdonaldtrump', count=50)

    for twit in twits:
        array= array + twit.text
    print(array)
    print(word_counter(array))


    # tweets = api.GetUserTimeline(screen_name='@realdonaldtrump',count=50)
    # for tweet in tweets:
    #    array.append(tweets.text)
    # print(word_counter(array))


mierdas_twitter()
