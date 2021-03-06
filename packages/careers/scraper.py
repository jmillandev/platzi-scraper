import asyncio
import logging

from packages.categories.models import Category
from packages.core.scraper.web_clients import PyppetterWebClient
from packages.courses.models import Course

from .models import Career
from .page_objects.careers.page import CareersPage
from .page_objects.courses.page import CareersCoursesPage

logger = logging.getLogger('log_print')


class CareersScraper(PyppetterWebClient):

    async def run(self):
        categories = await Category.all()
        await self.init_client()
        coros = [self.scraper_career(category) for category in categories]
        await asyncio.gather(*coros)
        await self.close_client()

    async def scraper_career(self, category: Category):
        url = self.URL_BASE + category.path
        html = await self.visit_page(url)
        career = CareersPage(html, url)
        logger.info(f"Saving data from {url}")
        for row in zip(career.names, career.paths):
            logger.debug(f"Get or create Career {row[0]}")
            await Career.get_or_create(
                name=row[0],
                path=row[1],
                category=category,
            )

class CoursesScraper(PyppetterWebClient):

    async def run(self):
        await self.init_client()
        careers = await Career.all()
        coros = [self.scraper_courses(career) for career in careers]
        await asyncio.gather(*coros)
        await self.close_client()

    async def scraper_courses(self, career: Career):
        url = self.URL_BASE + career.path
        html, raw_json_data = await self.visit_page(url, js_callback='_ => window.initialProps')

        courses = CareersCoursesPage(html, url, raw_json_data=raw_json_data)
        logger.info(f"Saving data from {url}")
        for properties in courses.resolve():
            course, _ = await Course.update_or_create(**properties)
            logger.info(f"Linked course({course}) to career({career}) ")
            await course.careers.add(career)
