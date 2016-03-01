import scraperwiki
import lxml.html

data = []
html = scraperwiki.scrape("http://crea.bunshun.jp/list/comic-essay-information")
root = lxml.html.fromstring(html)

divs = root.cssselect("#contents .layout-news .section-date")

for div in divs:
  a = div.cssselect("a")[0]
  data.append({
    "link"    : "http://crea.bunshun.jp" + a.get("href"),
    "title"   : a.text_content(),
    "content" : div.cssselect("p")[0].text_content(),
    "date"    : div.cssselect(".date")[0].text_content().replace(".", "-") + \
                "T00:00:00Z",
  })

scraperwiki.sqlite.save(unique_keys=["link"], data=data)
