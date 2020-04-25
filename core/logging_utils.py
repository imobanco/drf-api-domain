from logging import Filter


class NotInTestFilter(Filter):
    def filter(self, record):
        # Although I normally just put this class in the settings.py
        # file, I have my reasons to load settings here. In many
        # cases, you could skip the import and just read the setting
        # from the local symbol space.
        from django.conf import settings

        # TEST is some settings variable that tells my code
        # whether the code is running in a testing environment or
        # not. Any test runner I use will load the Django code in a
        # way that makes it True.
        try:
            return not settings.TEST
        except AttributeError:
            return True
