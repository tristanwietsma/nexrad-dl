import os, urllib, re
from BeautifulSoup import BeautifulSoup

CACHE_PATH = os.getenv('NEXRAD_CACHE')
BASE_URL = "http://water.weather.gov/precip/p_download_new/"

def GetLinks(root, patterns, isnum = True):
    u = urllib.urlopen(root)
    soup = BeautifulSoup(u.read())
    refs = []
    for p in patterns:
        refs += soup.fetch('a', {'href': re.compile(p)})
    links = []
    numbers = []
    for ref in refs:
        if isnum:
            if ref.text[:-1].isdigit():
                links.append(root + str(ref.text))
                numbers.append(int(str(ref.text)[:-1]))
        else: links.append(root + str(ref.text))
    if isnum: return zip(links, numbers)
    return links

def Download(url):
    existing_files = os.listdir(CACHE_PATH)
    targets = GetLinks(url, ['nc.tar.gz','1day'], isnum = False)
    for t in targets:
        file_name = t.split('/')[-1]
        if file_name in existing_files:
            print 'Skipping %s'%file_name
            continue
        print 'Downloading %s'%file_name
        urllib.urlretrieve(t, '%s/%s'%(CACHE_PATH, file_name))

def BuildDatabase(last_year=0, last_month=0, last_day=0):
    for (year_url, year) in GetLinks(BASE_URL, ['[0-9]{4}']):
        if year < last_year: continue
        for (month_url, month) in GetLinks(year_url, ['[0-9]{2}']):
            if year == last_year and month < last_month: continue
            for (day_url, day) in GetLinks(month_url, ['[0-9]']):
                if (year == last_year and month == last_month and
                    day <= last_day): continue
                Download(day_url)

def UpdateDatabase():
    existing_files = os.listdir(CACHE_PATH)
    shape_files = [f for f in existing_files if len(f.split('shape'))==2]
    dates = [re.search('[0-9]{8}', f).group(0) for f in shape_files]
    dates.sort()
    if len(dates) > 0:
        last = dates[-1]
        year = int(last[:4]); month = int(last[4:6]); day = int(last[6:])
        BuildDatabase(last_year=year, last_month=month, last_day=day)
    else: BuildDatabase()

if __name__ == '__main__':

    UpdateDatabase()
