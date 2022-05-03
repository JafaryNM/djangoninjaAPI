from ninja import NinjaAPI
from tracks.models import Track
from tracks.schema import TrackSchema, NotFoundSchema
from typing import List
api = NinjaAPI()

@api.get("/tracks", response=List[TrackSchema])
def tracks(request):
    return Track.objects.all()
