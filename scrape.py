"""
Yahoo Finance saves all their .csv files, which house the historical
prices of a given ticker, under the same url with the exception of
the ticker. This function will scrape this data for all tickers given
as inputs.
"""

def scrape():
    
    import urllib.request
    
    url = 'http://real-chart.finance.yahoo.com/table.csv?s=KO&d=0&e=22&f=2016&g=d&a=0&b=2&c=1962&ignore=.csv'

    urllib.request.urlretrieve(url, 'KO.csv')

    f = open('KO.csv','r')
    read_file = f.read()
    file_rows = read_file.split('\n')
    
    # print(file_rows)
