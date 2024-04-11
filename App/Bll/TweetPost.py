from app.Util.Utils import Utils
from PiWeatherMap import return_data

class TweetPost:

    def receive_data_from_sdk(self, city):

        try:

            if not city:
                raise Exception('Invalid city!')
            

            data = return_data(city = city)

            day = [day_data for day_data in data.daily]
            
            response = {
                'day 1 weather': day[0]['weather'][0]['description'],
                'day 1 max temp': format((day[0]['temp']['max'] - 273.15), '.2f'),
                'day 2 weather': day[1]['weather'][0]['description'], 
                'day 2 max temp': format((day[1]['temp']['max'] - 273.15), '.2f'),
                'day 3 weather': day[2]['weather'][0]['description'],
                'day 3 max temp': format((day[2]['temp']['max'] - 273.15), '.2f'),
                'day 4 weather': day[3]['weather'][0]['description'],
                'day 4 max temp': format((day[3]['temp']['max'] - 273.15), '.2f'),
                'day 5 weather': day[4]['weather'][0]['description'],
                'day 5 max temp': format((day[4]['temp']['max'] - 273.15), '.2f')
            }

            return response
        
        except Exception as e:
            raise Exception(e)
        
    def post_tweet(self):

        try:

            payload = {
                'text' : 'test post fastapi'
            }

            api = Utils.tweet_post(payload=payload)

            if api.status_code != 201:
                raise Exception(
                    "Request returned an error: {} {}".format(api.status_code, api.text)
                )
            
            return api.json()

        except Exception as e:
            raise Exception(e)