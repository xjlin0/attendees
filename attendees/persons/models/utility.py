from datetime import datetime, timedelta, timezone


class Utility:

    # @property
    # def iso_updated_at(self):
    #     return self.updated.isoformat()

    @property
    def all_notes(self):
        return self.notes.all()

    @staticmethod
    def forever():  # 1923 years from now
        return datetime.now(timezone.utc)+timedelta(weeks=99999)

    # @property
    # def notes(self):
    #     return Note.objects.filter(
    # #       status=self.status,
    #         link_table=self._meta.db_table,
    #         link_id=self.id
    #     )
