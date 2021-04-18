from packages.core.scraper.page_objects import BasicPage


class CareersPage(BasicPage):
    type_page = 'careers'

    @property
    def names(self):
        return self._get_property('names')

    @property
    def paths(self):
        return self._get_property('paths')