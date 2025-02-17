import asyncio
import sys

import cmd_arg
import config
import db
from base.base_crawler import AbstractCrawler
from media_platform.bilibili import BilibiliCrawler
from media_platform.douyin import DouYinCrawler
from media_platform.kuaishou import KuaishouCrawler
from media_platform.tieba import TieBaCrawler
from media_platform.weibo import WeiboCrawler
from media_platform.xhs import XiaoHongShuCrawler
from media_platform.zhihu import ZhihuCrawler


async def main():
    # parse cmd
    await cmd_arg.parse_cmd()
    config.PLATFORM = 'xhs'
    config.LOGIN_TYPE = 'qrcode'
    config.CRAWLER_TYPE = 'mention'

    # init db
    if config.SAVE_DATA_OPTION == "db":
        await db.init_db()

    crawler = XiaoHongShuCrawler()
    await crawler.start()

    if config.SAVE_DATA_OPTION == "db":
        await db.close()

if __name__ == '__main__':
    try:
        # asyncio.run(main())
        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        sys.exit()