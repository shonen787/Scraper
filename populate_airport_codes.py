# -*- coding: utf-8 -*-
# import libraries
import MySQLdb
import urllib2
from mysql.connector import MySQLConnection, Error
#from deps import python_mysql_dbconfig
from python_mysql_dbconfig import read_db_config
from bs4 import BeautifulSoup

def insert_airport(name, iata, icao):
    query = "INSERT INTO airport(airport_long,airport_short,airport_short_icao) " \
            "VALUES(%s,%s,%s)"
    args = (name, iata, icao)
    try:
    	db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')
	conn.commit()
        cursor.close()
	conn.close()
    except Error as error:
        print(error)
def main():
	lists_of_sites = [ 'http://www.azworldairports.com/indexes/p-apnma.cfm', 'http://www.azworldairports.com/indexes/p-apnmb.cfm', 'http://www.azworldairports.com/indexes/p-apnmc.cfm', 'http://www.azworldairports.com/indexes/p-apnmd.cfm', 'http://www.azworldairports.com/indexes/p-apnme.cfm', 'http://www.azworldairports.com/indexes/p-apnmf.cfm', 'http://www.azworldairports.com/indexes/p-apnmg.cfm', 'http://www.azworldairports.com/indexes/p-apnmh.cfm', 'http://www.azworldairports.com/indexes/p-apnmi.cfm', 'http://www.azworldairports.com/indexes/p-apnmj.cfm', 'http://www.azworldairports.com/indexes/p-apnmk.cfm', 'http://www.azworldairports.com/indexes/p-apnml.cfm', 'http://www.azworldairports.com/indexes/p-apnmm.cfm', 'http://www.azworldairports.com/indexes/p-apnmn.cfm', 'http://www.azworldairports.com/indexes/p-apnmo.cfm', 'http://www.azworldairports.com/indexes/p-apnmp.cfm', 'http://www.azworldairports.com/indexes/p-apnmq.cfm', 'http://www.azworldairports.com/indexes/p-apnmr.cfm', 'http://www.azworldairports.com/indexes/p-apnms.cfm', 'http://www.azworldairports.com/indexes/p-apnmt.cfm', 'http://www.azworldairports.com/indexes/p-apnmu.cfm', 'http://www.azworldairports.com/indexes/p-apnmv.cfm', 'http://www.azworldairports.com/indexes/p-apnmw.cfm', 'http://www.azworldairports.com/indexes/p-apnmx.cfm', 'http://www.azworldairports.com/indexes/p-apnmy.cfm', 'http://www.azworldairports.com/indexes/p-apnmz.cfm' ]
	for lists in lists_of_sites:
		airportcodes = lists
		page = urllib2.urlopen(airportcodes).read()
		soup = BeautifulSoup(page)
		for tr in soup.find_all('tr')[2:]:
			tds = tr.find_all('td')
			insert_airport(tds[0].text, tds[1].text, tds[2].text)

if __name__ == '__main__':
	main()
