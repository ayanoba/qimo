import urllib3

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        response = urllib3.urlopen(url)

        if response.getcode() !=200:
            return None
        return response.read()