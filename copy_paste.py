import os

source = "test_file.txt"
destination = "test_copy.txt"
os.system(f'copy {source} {destination}')
