import json
import os


class ScrapeUtils:
    def __init__(self):
        pass

    @staticmethod
    def xpath_scrape(response, xpath):
        if not xpath or not isinstance(xpath, str):
            raise ValueError("! Invalid xpath inserted. !")

        try:
            selection = response.xpath(xpath).extract()

        except Exception as exc:
            print(f"! Exception encountered while scraping xpath: {xpath} !\n", exc)
            return None

        else:
            print("xpath navigation successful.")

        return selection if selection else None


if __name__ == "__main__":
    main = ScrapeUtils()
