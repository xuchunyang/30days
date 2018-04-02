import threading
from urllib.request import urlopen

class AsyncWget(threading.Thread):
    def __init__(self, url, outfile):
        threading.Thread.__init__(self)
        self.url = url
        self.outfile = outfile

    def run(self):
        with urlopen(self.url) as res:
            with open(self.outfile, 'w') as f:
                bytes = res.read()
                # https://stackoverflow.com/a/31060836/2999892
                s = str(bytes, 'utf-8')
                f.write(s)
        print("Finished background fetching of:", self.url)

background = AsyncWget('http://example.com/index.html', 'index.html')
background.start()
print('The main program continues to run in foreground')
