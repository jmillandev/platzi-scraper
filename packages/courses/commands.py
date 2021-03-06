from cleo import Command
from packages.core.utils.app_loop import AppLoop

from .scraper import CoursesScraper

class AllCommands:


    class Scraper(Command):
        """
        Update course and create lessons

        courses:update
        """

        def handle(self):
            AppLoop().get_loop().run_until_complete(
                CoursesScraper().run()
            )
