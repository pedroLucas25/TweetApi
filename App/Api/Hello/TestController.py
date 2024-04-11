from fastapi import HTTPException, status

from app import app
from app.Bll.TweetPost import TweetPost

@app.get('/test')
def city_get(city: str = ''):

    try:

        tweetPost = TweetPost()
        response = tweetPost.teste(city)

        return response

    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get('/test/tweet', status_code=status.HTTP_201_CREATED)
def tweet_test():

    try:

        tweetPost = TweetPost()
        response = tweetPost.post_tweet()

        return response

    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=500, detail=str(e))