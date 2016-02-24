import urllib.request
import os.path

def scrape(tickers):
    
    url1 = 'http://real-chart.finance.yahoo.com/table.csv?s='
    url2 = '&d=0&e=22&f=2016&g=d&a=0&b=2&c=1962&ignore=.csv'
    
    for tick in tickers:
        if os.path.isfile(tick + '.csv') == False: # checks for existing file
            url = url1 + tick + url2
            file_name = tick + '.csv'
            urllib.request.urlretrieve(url, file_name)

    f = open(tick + '.csv','r')
    read_file = f.read()
    file_rows = read_file.split('\n')
    
    print(file_rows[1]) # just a check, should be deleted soon
