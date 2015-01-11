# -*- coding: utf-8 -*-

from module.plugins.internal.SimpleHoster import SimpleHoster

class FshareVnVer2(SimpleHoster):
    __name__ = "FshareVnVer2"
    __type__ = "hoster"
    __pattern__ = r"http(s)?://(www\.)?fshare.vn/file/.*"
    __version__ = "0.1"
    __description__ = """FshareVn Download"""
    __authors__ = [("Nam Pham", "thanhnam2k@yahoo.com")]

    DOWNLOAD_URL_GET = "https://www.fshare.vn/download/index"

    def process(self, pyfile):
        self.load(pyfile.url, decode = True)
        url = self.load(self.DOWNLOAD_URL_GET)

        if not url.startswith("http"):
            self.retry(300, 20, "Try again later...")

        _, _, pyfile.name = url.rpartition("/")

        self.setWait(32)
        self.wait()

        self.download(url)
        self.checkDownloadedFile()
