import scraperwiki
import lxml.html

html = scraperwiki.scrape("http://crea.bunshun.jp/list/comic-essay-information")
root = lxml.html.fromstring(html)

ancs = root.cssselect("#contents .layout-news .section-date a")
data = []

for a in ancs:
  data.append({"title": a.text_content(), "link": a.get("href")})

scraperwiki.sqlite.save(unique_keys=["name"], data=data)
