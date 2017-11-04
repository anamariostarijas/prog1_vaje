import os
import re
import string
import requests
import csv
cats_frontpage_basename = 'macke.html'
cats_frontpage_url = 'http://www.bolha.com/zivali/male-zivali/macke/'
base_url = 'http://www.bolha.com'
cats_dirname ='C:\Anamari\Documents\prog1_vaje'
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
    with open(path, 'w') as file_out:
        file_out.write(text)
    return None

def download_frontpage_to_file():
    url_text = download_url_to_string(cats_frontpage_url)
    file = save_string_to_file(url_text, cats_dirname, cats_frontpage_fn )

    
def read_file_to_string(directory, filename):
    path = os.path.join(directory, filename)
    with open(path, 'r') as file_in:
        return file_in.read()


# Define a function that takes a webpage as a string and splits it into
# segments such that each segment corresponds to one advertisement. This
# function will use a regular expression that delimits the beginning and end of
# each ad. Return the list of strings.
# Hint: To build this reg-ex, you can use your text editor's regex search functionality.
#? makes the star to take just as much as necessery to match
def split_into_ads(page_contents):
    '''splits page into segments'''
    rx = re.compile(r'<div class="ad">(.*?)<div class="clear">', re.DOTALL)
    ads = rx.findall(page_contents)
    split_file = page_contents.split(ads)
    return ads

# Define a function that takes a string corresponding to the block of one
# advertisement and extracts from it the following data: Name, price, and
# the description as displayed on the page.
def undefined( TODO ):
    '''TODO'''
    TODO



# Write a function that reads a page from a file and returns the list of
# dictionaries containing the information for each ad on that page.
def undefined( TODO ):
    '''TODO'''
    TODO



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


