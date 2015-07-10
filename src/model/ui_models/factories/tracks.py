from model.ui_models.track import Track

class Tracks():
    @classmethod
    def get_tracks(cls, tracks):
        track_objs = []
        for track in tracks:
            subtracks = track['subtracks'] if 'subtracks' in track else None
            track_obj = Track(title=track['title'])
            if subtracks:
                subtracks_objs = cls.get_tracks(tracks=track['subtracks'])
                track_obj.subtracks = subtracks_objs
            track_objs.append(track_obj)
        return track_objs
