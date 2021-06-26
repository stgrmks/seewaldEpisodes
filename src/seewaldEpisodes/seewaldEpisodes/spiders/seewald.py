from scrapy import Request, Spider
from scrapy.http import Response
from seewaldEpisodes.seewaldEpisodes.items import SeewaldepisodesItem


class SeewaldEpisodes(Spider):
    name = "SeeWaldSpider"

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
            print("Failed to find the content url!")
