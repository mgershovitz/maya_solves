import pandas as pd
import timeit


class Fields:
    LIKES_FIELD = 'nlikes'
    POPULARITY_FIELD = 'tweet_popularity'


def rate_tweet_popularity(num_likes):
    if num_likes <= 50:
        return 'low'
    if 50 < num_likes <= 500:
        return 'medium'
    if num_likes > 500:
        return 'high'


def run_with_iter(df):
    tweet_popularity = []
    for i, row in df.iterrows():
        tweet_popularity.append(rate_tweet_popularity(row[Fields.LIKES_FIELD]))
    df[Fields.POPULARITY_FIELD] = tweet_popularity


def run_with_apply(df):
    df[Fields.POPULARITY_FIELD] = df.apply(lambda row: rate_tweet_popularity(row[Fields.LIKES_FIELD]), axis=1)


def run_with_vectors(df):
    df[Fields.POPULARITY_FIELD] = 0
    df.loc[(df[Fields.LIKES_FIELD] <= 50), Fields.POPULARITY_FIELD] = 'low'
    df.loc[(50 <= df[Fields.LIKES_FIELD]) & (df[Fields.LIKES_FIELD] < 500), Fields.POPULARITY_FIELD] = 'medium'
    df.loc[(500 < df[Fields.LIKES_FIELD]), Fields.POPULARITY_FIELD] = 'high'


if __name__ == '__main__':
    data_set = pd.read_csv('~/Downloads/elon-musk/2020.csv')
    print("Method run_with_vectors finished in", timeit.timeit(
        "run_with_vectors(data_set)", globals=globals(), number=1
    ), "ms")
    print("Popularity results: \n", data_set[Fields.POPULARITY_FIELD].value_counts())
