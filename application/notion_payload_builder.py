# преобразования трека в поля Notion
def build_notion_payload(
    track
):

    return {
        "Track": (
            track.track
        ),
        "Artist": (
            track.artist
        ),
        "Track Key": (
            track.track_key
        )
    }