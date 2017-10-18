from catlib import *

frontpage_contents = read_file_to_string(cat_dirname, frontpage_filename)
ads = split_into_ads(frontpage_contents)
