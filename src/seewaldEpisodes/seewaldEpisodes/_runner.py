from scrapy.crawler import CrawlerRunner
from scrapy.settings import Settings

from . import settings as my_settings
from seewaldEpisodes.seewaldEpisodes.spiders.seewald import SeewaldEpisodes
from twisted.internet import reactor
from twisted.internet.defer import Deferred


def get_episode():
    settings: Settings = Settings()
    settings.setmodule(my_settings)
    runner: CrawlerRunner = CrawlerRunner(settings=settings)
    d: Deferred = runner.crawl(crawler_or_spidercls=SeewaldEpisodes)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()


if __name__ == "__main__":
    get_episode()
