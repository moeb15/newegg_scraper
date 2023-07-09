import sys
from datetime import datetime
from utils.newegg_scraper import NeweggScraper


BASE_URL = 'https://www.newegg.ca/p/pl?d='
search_query = sys.argv[1]

if search_query == None:
    search_query = ''


def extract_data(query):
    scraper = NeweggScraper(BASE_URL, query)
    df = scraper.paginated_scrape(-1)
    cur_date = datetime.now()
    df.to_csv(f'data/{cur_date.day}-{cur_date.month}-{cur_date.year}-{query}.csv',index=False)

if __name__ == '__main__':
    extract_data(search_query)
