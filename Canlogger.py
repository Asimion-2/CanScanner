import csv
import subprocess
import os 
import pandas as pd
import glob
import datetime



try:
	subprocess = subprocess.Popen("candump -l -n 1000 vcan0", shell=True, stdout=subprocess.PIPE)
	subprocess_return = subprocess.stdout.read()
	release = str(subprocess_return,'utf-8')
	thislist = [release]

	txtfiles = []
	for file in glob.glob("*.log"):
	    txtfiles.append(file)
	x = str(datetime.datetime.now())
	df = pd.read_csv(txtfiles[-1],delimiter=',')
	df.to_csv(x + '.csv')
	os.system('rm *.log')
	print('Done')
except:
	print('You need to download Can-ulis')


