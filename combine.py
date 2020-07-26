import os
import glob
import pandas as pd
os.chdir("csv/")

'''
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
'''

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension)) if not "Bank" in i]
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])

combined_csv.to_csv( "../combined_csv.csv", index=False, encoding='utf-8-sig')
