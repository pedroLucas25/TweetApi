from fastapi import HTTPException, status

from app import app
from app.Bll.TweetPost import TweetPost

from app.Models.CityReceiveModel import CityReceiveModel

@app.get('/test')
def city_get(city: str = None):

    try:

        tweetPost = TweetPost()
        response = tweetPost.receive_data_from_sdk(city)

        return response

    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post('/tweet', status_code=status.HTTP_201_CREATED)
def post_tweet(cityReceive: CityReceiveModel):

    try:

        tweetPost = TweetPost()
        response = tweetPost.post_tweet(city=cityReceive.city)

        return response

    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=500, detail=str(e))