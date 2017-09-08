import json
import requests

from photos.models import Photo
from photos import settings as photo_settings


def get_latest_flickr_image():
    url = photo_settings.FLICKR_JSON_FEED_URL
    r = requests.get(url)
    page_content = r.text

    probably_json = page_content.replace("\\'", "'")

    feed = json.loads(probably_json)
    images = feed['items']
    return images[0]


def save_latest_flick_image():
    flickr_image = get_latest_flickr_image()

    if not Photo.objects.filter(link=flickr_image['link']).exists():
        photo = Photo(
            title       = flickr_image['title'],
            link        = flickr_image['link'],
            image_url   = flickr_image['media']['m'],
            description = flickr_image['description']
        )
        photo.save()
