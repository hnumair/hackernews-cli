echo "{\"posts\": " > items.json
scrapy crawl hackernews -o items.json &> log.txt
echo "}" >> items.json
python read.py
