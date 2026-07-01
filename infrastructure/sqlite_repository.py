from domain.contracts import ITrackRepository

class SQLiteTrackRepository(ITrackRepository):

    def exists(self, track_key):
        ...

    def save(self, track):
        ...

    def get_all(self):
        ...