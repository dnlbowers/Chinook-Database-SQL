import psycopg2

# connect to "chinook" database
connection = psycopg2.connect(database="chinook")


# build a cursor object of the database
cursor = connection.cursor()

# Query 1 -selct all records from the "Artist table"
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "Name" column form the "Artist" table"
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Queen" form the "Artist" table - the %s is a python
# string holder
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only "Queen" by artist !d (51) form the "Artist" table -
# the %s is a python string holder
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', ["51"])

# Query 5 - select only the albums with the "ArtistId" #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', ["51"])

# Query 6 = Select all tracks where the composer is "Queen" from "track" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Query 7 = What hapens when item doesn't exits
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Test"])

# Query 8 = Another composer
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Van Halen"])

# fetch the results (multiple) - returns tuple of results
results = cursor.fetchall()

# fetch the result(single) - prints each column individually
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)
