import os.path

from scrapy import Request, Spider
from scrapy.http import Response

from ...utils import get_logger
from ..items import SeewaldepisodesItem

log = get_logger(os.path.basename(__file__))


class SeewaldEpisodes(Spider):
    name = "SeewaldEpisodes"

    def start_requests(self):
        yield Request(
            url="https://www.egofm.de/musik/entdecken/sendung-seewald-zum-nachhoeren",
            callback=self.parse,
        )

    def parse(self, response: Response, **kwargs):
        try:
            yield SeewaldepisodesItem(
                url=response.xpath("//meta[@itemprop='contentUrl']/@content").get()
            )
        except Exception as anyErr:
            log.error(f"Failed to find the content url: {anyErr}")
