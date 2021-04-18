# Ebay Scraper
Scrape Ebay product information. Ebay lists its products under specific categories. For example, https://www.ebay.com/b/Mens-Shoes/93427/bn_61999 lists all the products under "Mens-Shoes". This is a paginated list with 48 products per page.

# Running the Scraper
The scraper takes 3 arguments as mentioned below:
```shell
$ python3 ebay_scraper.py <url> <pagecount> <outfile>
```
* url - Base URL (similar to the one given above)
* pagecount - Number of pages you want to scrape
* outfile - Output json file without extension

# Using Oxylabs residential proxies
I am using residential proxies from [Oxylabs](https://oxylabs.io/) which will return the HTML for the URL. Their proxies are efficient when compared to free proxies. You can check the code in [utils.py](https://github.com/saisyam/ebay-scraper/blob/main/utils.py)

# Using free proxies
TBD
