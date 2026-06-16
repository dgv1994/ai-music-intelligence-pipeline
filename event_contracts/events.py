from pydantic import BaseModel


class TrackCreatedEvent(BaseModel):
    track_key: str
    track: str
    artist: str