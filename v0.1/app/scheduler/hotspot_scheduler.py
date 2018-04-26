# coding: utf-8
from app.database import redis_client
from app.model import note_manager, catalog_manager


class Scheduler(object):
    """Redis-based scheduler"""

    def __init__(self,):
        """
        client : redis对象
        :param key:
        """
        pass

    def run(self):
        """

        :return:
        """
        notes = note_manager.all_notes()
        r = redis_client
        for note in notes:
            note_id = note.get('id', 0)
            key = 'visit:{}:totals'.format(str(note_id))
            views = r.get(key)
            data = {
                'views': views,
            }
            note_manager.update_note(note_id, data)

    def test_run(self, note_id):
        """

        :param note_id:
        :return:
        """
        r = redis_client
        key = 'visit:{}:totals'.format(str(note_id))
        views = r.get(key)
        data = {
            'views': views,
        }
        note_manager.update_note(note_id, data)
