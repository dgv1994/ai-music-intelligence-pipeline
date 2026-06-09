import pytest

from unittest.mock import (
    Mock
)

from application.track_service import (
    TrackService
)

from domain.errors import (
    DuplicateTrackError
)

from domain.models import (
    Track
)
'''Приоритетные cases для тестирования взаимодействия между validater, 
mapper и service:'''
# Модульный тест на взаимодействие validater, mapper и service

# синхронизация одного/нескольких нового трека
def test_should_sync_new_track():
    # Arrange
    repository = Mock()

    repository.exists.return_value = (
        False
    )

    lastfm_client = Mock()

    lastfm_client.get_recent_tracks.return_value = {

        "recenttracks": {
            "track": [
                {
                    "name": "Track 1",
                    "artist": {
                        "#text": "Artist 1"
                    },
                    "track_key": ("track 1-artist 1"
                    )
                }
            ]
        }     
    }

    service = TrackService(
        repository,
        lastfm_client
    )
    # Act

    result = (
        service.sync_new_track()
    )
    # Assert
    # 1 трек должен быть сохранен в репозитории, 
    # так как он не существует
    assert len(result) == 1
    
    # проверка сохранения трека в репозитории с правильным track_key,
    assert (
        result[0].track_key == "track 1-artist 1"
    )

def test_should_sync_multiple_tracks():

    repository = Mock()

    repository.exists.return_value = (
        False
    )

    lastfm_client = Mock()

    lastfm_client.get_recent_tracks.return_value = {

        "recenttracks": {
            "track": [
                {
                    "name": "Track 1",
                    "artist": {
                        "#text": "Artist 1"
                    }
                },
                {
                    "name": "Track 2",
                    "artist": {
                        "#text": "Artist 2"
                    }
                },
                {
                    "name": "Track 3",
                    "artist": {
                        "#text": "Artist 3"
                    }
                }
            ]
        }     
    }

    service = TrackService(
        repository,
        lastfm_client
    )

    result = (
        service.sync_new_track()
    )

    # Assert
    # 3 трека должны быть сохранены в репозитории,
    # так как они не существуют
    assert len(result) == 3

    # проверка сохранения треков в репозитории с правильными track_key,
    assert [
        track.track_key 
        for track in result
    ] == [
        "track 1-artist 1",
        "track 2-artist 2",
        "track 3-artist 3"
    ]


# синхранизация трека без обложки/альбома
# влияет ли на pipeline отсутствие обложки/альбома? 
# - нет, так как она не обязательна и
# не влияет на остальные этапы синхронизации трека
def test_should_sync_track_without_cover():

    # Arrange
    repository = Mock()

    repository.exists.return_value = (
        False
    )

    lastfm_client = Mock()

    lastfm_client.get_recent_tracks.return_value = {
        "recenttracks": {
            "track": [
                {
                    "name": "Track 1",
                    "artist": {
                        "#text": "Artist 1"
                    },
                    "album": {
                        "#text": "Album 1"
                    },
                    "image": [
                        {
                            "#text": "",
                            "size": "small"
                        },
                        {
                            "#text": "",
                            "size": "medium"
                        },
                        {
                            "#text": "",
                            "size": "large"
                        }
                    ]
                }
            ]
        }     
    }

    service = TrackService(
        repository,
        lastfm_client
    )
    
    # Act

    result = (
        service.sync_new_track()
    )
    # Assert
    # трек должен быть сохранен в репозитории, 
    # так как он не существует, несмотря на отсутствие обложки
    assert len(result) == 1
    
    # проверка сохранения трека в репозитории с правильным track_key,
    assert (
        result[0].track_key == "track 1-artist 1"
    )

def test_sync_track_track_without_album():

    # Arrange
    repository = Mock()

    repository.exists.return_value = (
        False
    )

    lastfm_client = Mock()

    lastfm_client.get_recent_tracks.return_value = {
        "recenttracks": {
            "track": [
                {
                    "name": "Track 1",
                    "artist": {
                        "#text": "Artist 1"
                    },
                    "album": {
                        "#text": ""
                    },
                }
            ]
        }     
    }

    service = TrackService(
        repository,
        lastfm_client
    )
    
    # Act

    result = (
        service.sync_new_track()
    )
    # Assert
    # трек должен быть сохранен в репозитории, 
    # так как он не существует, несмотря на отсутствие названия альбома
    assert len(result) == 1
    
    # проверка сохранения трека в репозитории с правильным track_key,
    assert (
        result[0].track_key == "track 1-artist 1"
    )

# Deduplication Testing Cases:

# проверка условия возникновения ошибки Дедубликации: 
# при попытке синхронизации трека, который уже существует в репозитории, 
# должен быть вызван DuplicateTrackError
def test_should_raise_duplicate_error():
    # Arrange
    repository = Mock()

    repository.exists.return_value = (
        True
    )

    lastfm_client = Mock()

    lastfm_client.get_recent_tracks.return_value = {
        "recenttracks": {
            "track": [
                {
                    "name": "Track 1",
                    "artist": {
                        "#text": "Artist 1"
                    },
                    "album": {
                        "#text": "Album 1"
                    },
                }
            ]
        }     
    }

    service = TrackService(
        repository,
        lastfm_client
    )
    # Act & Assert
    # при попытке синхронизации трека, который уже 
    # существует в репозитории, должен быть вызван DuplicateTrackError 
    # и не должен быть сохранен новый трек, так как он уже существует
   
    with pytest.raises(DuplicateTrackError):
        service.sync_new_track()
    

# проверка условия успешной синхронизации уникального трека
# /несохранения существующего трека
# (без исспользования контракта с репозиторием Last.fm, 
# так как он не влияет на логику синхронизации трека)
def test_should_accept_unique_track ():
    # Arrange
    repository = Mock()

    repository.exists.return_value = (
        False
    )

    service = TrackService(
        repository,
        None
    )

    track = Track(

        track="Numb",

        artist="Linkin Park",

        album="Meteora",

        track_key=(
            "numb-linkin park"
        ),

        cover_image=None
    )
    
    # Act

    result = (
        service.sync_duplicate(
            track
        )
    )
    # Assert
    # при попытке синхронизации трека, который не существует в репозитории, 
    # должен быть возвращен True, так как трек уникальный и может быть сохранен
    assert result is True

def test_should_not_save_duplicate_track():

    repository = Mock()

    repository.exists.return_value = (
        True
    )

    service = TrackService(
        repository,
        None
    )

    track = Track(

        track="Numb",

        artist="Linkin Park",

        album="Meteora",

        track_key=(
            "numb-linkin park"
        ),

        cover_image=None
    )
    
    # Act & Assert

    with pytest.raises(DuplicateTrackError):
        service.sync_duplicate(
            track
        )
    
    # при попытке синхронизации трека, который уже существует в репозитории, 
    # должен быть вызван DuplicateTrackError и не должен быть сохранен новый трек, 
    # так как он уже существует
    repository.save.assert_not_called()

''' Дополнительные cases для тестирования взаимодействия между models и 
service:'''
# для корректного прохождения cover image через весь pipeline
def test_should_return_cover_image():
    # Arrange
    track = Track(

        track="Numb",

        artist="Linkin Park",

        album="Meteora",

        track_key=(
            "numb-linkin park"
        ),

        cover_image=(
            "https://lastfm.freetls.fastly.net/i/u/300x300/d52df9b1ecc01cd5da0530322198f8d1.jpg"
        )
    )

    service = TrackService(
        None,
        None
    )
    
    # Act

    result = (
        service.sync_cover(
            track
        )
    )
    # Assert
    # если у трека есть обложка, то она должна быть возвращена
    assert result == (
        "https://lastfm.freetls.fastly.net/i/u/300x300/d52df9b1ecc01cd5da0530322198f8d1.jpg"
    )
# возращает None, если у трека нет обложки, и не влияет на остальные 
# этапы синхронизации трека
def test_should_return_none_when_cover_missing():

    # Arrange
    track = Track(

        track="Numb",

        artist="Linkin Park",

        album="Meteora",

        track_key=(
            "numb-linkin park"
        ),

        cover_image=None
    )

    service = TrackService(
        None,
        None
    )
    
    # Act

    result = (
        service.sync_cover(
            track
        )
    )
    # Assert
    # если у трека нет обложки, то должно быть возвращено None
    assert result is None

