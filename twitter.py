import tweepy
import tweepy.models

class Twitter:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.client = tweepy.Client(
            consumer_key=consumer_key, consumer_secret=consumer_secret,
            access_token=access_token, access_token_secret=access_token_secret
        )

    def tweet(self, text, images):
        media_ids = []
        if images:
            for image in images:
                media = tweepy.API.media_upload(file=image)
                media_ids.append(media.media_id_string)
        response = self.client.create_tweet(
            text=text, media_ids=media_ids
        )
        return response.id
