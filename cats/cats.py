#from catlib import *

download_frontpage_to_file()
frontpage_contents = read_file_to_string(cats_dirname, cats_frontpage_basename)
ads = split_into_ads(frontpage_contents)
all_data = data_from_file(cats_dirname, cats_frontpage_basename)
