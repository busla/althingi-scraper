# althingi-scraper
Sköfur fyrir opin gögn Alþingis. Það er sér skafa fyrir hvert módel sem hægt er að kalla í.


# Uppsetning
pip install -r requirements.txt


# Kalla í sköfurnar úr eigin kóða með HTTP
Sköfurnar koma með vefþjónustu sem hægt er að ræsa svo hægt sé að kalla í sköfurnar með HTTP kalli beint úr kóða og fá json.

## Ræsa vefþjónustuna á porti 9080
```sh
$ scrapyrt
```

## Dæmi
Núverandi löggjafarþing er númer 145.

```sh
$ curl "http://localhost:9080/crawl.json?spider_name=session&url=http://www.althingi.is/altext/xml/loggjafarthing/"
$ curl "http://localhost:9080/crawl.json?spider_name=party&url=http://www.althingi.is/altext/xml/thingflokkar/"
$ curl "http://localhost:9080/crawl.json?spider_name=committee&url=http://www.althingi.is/altext/xml/nefndir/?lthing=145"
$ curl "http://localhost:9080/crawl.json?spider_name=committee_meeting&url=http://www.althingi.is/altext/xml/nefndarfundir/?lthing=145"
$ curl "http://localhost:9080/crawl.json?spider_name=member&url=http://www.althingi.is/altext/xml/thingmenn/?lthing=145"
$ curl "http://localhost:9080/crawl.json?spider_name=issue&url=http://www.althingi.is/altext/xml/thingmalalisti/?lthing=145"
$ curl "http://localhost:9080/crawl.json?spider_name=petition&url=http://www.althingi.is/altext/xml/atkvaedagreidslur/?lthing=145"
```
