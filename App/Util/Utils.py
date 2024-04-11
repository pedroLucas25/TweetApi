from requests_oauthlib import OAuth1Session

from config import Config

class Utils:

    def tweet_post(payload):

        consumer_key = Config.CONSUMER_KEY
        consumer_secret = Config.CONSUMER_SECRET

        request_token_url = Config.REQUEST_TOKEN_URL
        oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

        try:
            fetch_response = oauth.fetch_request_token(request_token_url)
        except ValueError:
            raise Exception("There may have been an issue with the consumer_key or consumer_secret you entered.")
        
        resource_owner_key = fetch_response.get("oauth_token")
        resource_owner_secret = fetch_response.get("oauth_token_secret")

        base_authorization_url = Config.BASE_AUTHORIZATION_URL
        authorization_url = oauth.authorization_url(base_authorization_url)
        print("Please go here and authorize: %s" % authorization_url)
        verifier = input("Paste the PIN here: ")

        access_token_url = Config.ACCESS_TOKEN_URL
        oauth = OAuth1Session(
            consumer_key,
            client_secret=consumer_secret,
            resource_owner_key=resource_owner_key,
            resource_owner_secret=resource_owner_secret,
            verifier=verifier,
        )
        oauth_tokens = oauth.fetch_access_token(access_token_url)

        access_token = oauth_tokens["oauth_token"]
        access_token_secret = oauth_tokens["oauth_token_secret"]

        oauth = OAuth1Session(
            consumer_key,
            client_secret=consumer_secret,
            resource_owner_key=access_token,
            resource_owner_secret=access_token_secret,
        )

        response = oauth.post(
            'https://api.twitter.com/2/tweets',
            json=payload,
        )

        return response

