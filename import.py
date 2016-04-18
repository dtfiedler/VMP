import csv
import sys
#open connection and import into DB
import MySQLdb

#buffer to hold file input
data = []

import glob

	# Open database connection
db = MySQLdb.connect("localhost","root","mysql","vmpTest")
	# prepare a cursor object using cursor() method
cursor = db.cursor()

#iterate through all files provided in command line
with open(sys.argv[1], "rbU") as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		#print 'Sku:' + row['Sku'] + '\tUPC: '  + row['UPC']  + "\tArtist: "  + row['Artist'] + "\tAlbum: "  + row['Album']
		data.append(row)

for row in data:
	cursor.execute("INSERT IGNORE INTO reports VALUES (%s, %s, %s, %s)", (row['Sku'], row['UPC'], row['Artist'], row['Album']))

db.commit();	
db.close();