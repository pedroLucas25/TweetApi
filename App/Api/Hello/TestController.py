from fastapi import HTTPException

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