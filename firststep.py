import pymssql  
    conn = pymssql.connect(server='D32DB01', user='c1\PJHA', password='Dumara1~', database='Cicleone')
    cursor = conn.cursor()  
    cursor.execute('SELECT top 10 * from FROM Listings;')
    row = cursor.fetchone()  
    while row:  
        print str(row[0]) + " " + str(row[1]) + " " + str(row[2])     
        row = cursor.fetchone() 