from scrapy.crawler import CrawlerRunner
from scrapy.settings import Settings
from twisted.internet import reactor
from twisted.internet.defer import Deferred

from seewaldEpisodes.seewaldEpisodes.spiders.seewald import SeewaldEpisodes

from . import settings as my_settings


def get_episode(**custom_settings):
    settings: Settings = Settings()
    settings.setmodule(my_settings)
    settings.update(custom_settings)
    runner: CrawlerRunner = CrawlerRunner(settings=settings)
    d: Deferred = runner.crawl(crawler_or_spidercls=SeewaldEpisodes)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
