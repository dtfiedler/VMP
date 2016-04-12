import MySQLdb

class MYSQLDAO(object):

	db = None
	table = None
	cursor = None

	# def __init__(self, db, user, password, table):
 #       #INTIALIZER FUNCTION
 #    return

	def openConnection():
    	# Open database connection
		db = MySQLdb.connect("localhost","root","mysql","vmpTest" )
		# prepare a cursor object using cursor() method
		cursor = db.cursor()
	

	def closeConnection():
		db.close()
	

	def executeQuery(sku):
		# execute SQL query using execute() method.
		cursor.execute("select *  FROM reports where UPC = 0000123")
		print [description[0] for description in cursor.description]
		rows = cursor.fetchall()
		for row in rows:
		    for col in row:
		        print "%s\t" % col
		    print "\n"
	

	def testInsert():
		sku = 'sku-0000'
		artist = 'artist-0000'
		album = 'album-0000'
		UPC = '0000000'

		for num in range(0,10):
			sku += str(num)
			artist += str(num)
			album += str(num)
			UPC += str(num)
			cursor.execute("INSERT INTO reports VALUES (%s, %s, %s, %s)", (sku, UPC, artist, album))
	



