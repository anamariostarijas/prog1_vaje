import os
import re
import string
import requests
import csv
cats_frontpage_basename = 'macke.html'
cats_frontpage_url = 'http://www.bolha.com/zivali/male-zivali/macke/'
base_url = 'http://www.bolha.com'
cats_dirname ='C:\prog1_vaje'
cats_frontpage_fn = os.path.join(cats_dirname, cats_frontpage_basename)
csv_filename = 'cats.csv'


def download_url_to_string(url):
    try:
        r = requests.get(url)

    except requests.exceptions.ConnectionError:
        print("failed to connect to url " + url)
        return
    
    return r.text
#r.text, r.status_code
    
    
def save_string_to_file(text, directory, filename):
    '''Write "text" to the file "filename" located in directory "directory",
    creating "directory" if necessary. If "directory" is the empty string, use
    the current directory.'''
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding = 'utf8') as file_out:
        file_out.write(text)
    return 

def download_frontpage_to_file():
    url_text = download_url_to_string(cats_frontpage_url)
    file = save_string_to_file(url_text, cats_dirname, cats_frontpage_basename)

    
def read_file_to_string(directory, filename):
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf8') as file_in:
        return file_in.read()
#add open(path, 'r', encoding = 'utf8') if encoding doesn't work with your document

#? makes the star to take just as much as necessery to match
def split_into_ads(page_contents):
    '''splits page into segments, list of strings'''
    #rx = re.compile(r'<div class="ad">(.*?)<div class="clear">', re.DOTALL)
    ads = re.findall(r'<div class="ad">(.*?)<div class="clear">' , page_contents, re.DOTALL)
    #split_file = page_contents.split(rx)
    return ads

def data_from_one_ad(block):
    '''takes a string and extracts name, price, description of one ad'''

    rx = re.compile(r'title="(?P<title>.*?)"'
                    r'.*?</h3>\s*(?P<description>.*?)\s*</?div'
                    r'.*?class="price">(?P<price>.*?)</div',
                    re.DOTALL)

    data=re.search(rx, block)
    ad_dict = data.groupdict()
    return ad_dict


def data_from_file(directory, filename):
    '''reads a page from a file and returns the list of dictionaries containing the information for each ad on that page'''
    page_contents = read_file_to_string(directory, filename)
    all_ads = split_into_ads(page_contents)
    all_data = []
    for ad in all_ads:
        all_data.append(data_from_one_ad(ad))
        print (all_data)
    


########################################################################
# We processed the data, now let's save it for later.
########################################################################

def write_csv(fieldnames, rows, directory, filename):
    '''Write a CSV file to directory/filename. The fieldnames must be a list of
    strings, the rows a list of dictionaries each mapping a fieldname to a
    cell-value.
    '''
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return None


