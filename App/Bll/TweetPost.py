from PiWeatherMap import return_data


class TweetPost:

    def teste(self, city):

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
            print(e)