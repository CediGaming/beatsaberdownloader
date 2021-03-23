import cloudscraper

def scrapeZipFile(url: str, dstFilePath: str):
	print("Downloading...")
	scraper = cloudscraper.create_scraper()
	content = scraper.get(url).content
	scraper.close()
	print("Downloading finished!")

	print("Saving zip...")
	file = open(dstFilePath, 'wb')
	file.write(content)
	file.close()
	print("Zip saved!")