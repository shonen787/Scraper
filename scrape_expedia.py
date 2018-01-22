# -*- coding: utf-8 -*-
# import libraries
import MySQLdb
import urllib2
from mysql.connector import MySQLConnection, Error
#from deps import python_mysql_dbconfig
from python_mysql_dbconfig import read_db_config
from bs4 import BeautifulSoup


lists_of_sites = ['https://www.expedia.com/Flights-Search?trip=roundtrip&leg1=from%3AMiami%20(MIA)%2Cto%3ANew%20York%2C%20NY%2C%20United%20States%20(LGA)%2Cdeparture%3A04%2F03%2F2018TANYT&leg2=from%3ANew%20York%2C%20NY%2C%20United%20States%20(LGA)%2Cto%3AMiami%20(MIA)%2Cdeparture%3A04%2F03%2F2018TANYT&passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.com']
#'http://www.azworldairports.com/indexes/p-apnmb.cfm', 'http://www.azworldairports.com/indexes/p-apnmc.cfm', 'http://www.azworldairports.com/indexes/p-apnmd.cfm', 'http://www.azworldairports.com/indexes/p-apnme.cfm', 'http://www.azworldairports.com/indexes/p-apnmf.cfm', 'http://www.azworldairports.com/indexes/p-apnmg.cfm', 'http://www.azworldairports.com/indexes/p-apnmh.cfm', 'http://www.azworldairports.com/indexes/p-apnmi.cfm', 'http://www.azworldairports.com/indexes/p-apnmj.cfm', 'http://www.azworldairports.com/indexes/p-apnmk.cfm', 'http://www.azworldairports.com/indexes/p-apnml.cfm', 'http://www.azworldairports.com/indexes/p-apnmm.cfm', 'http://www.azworldairports.com/indexes/p-apnmn.cfm', 'http://www.azworldairports.com/indexes/p-apnmo.cfm', 'http://www.azworldairports.com/indexes/p-apnmp.cfm', 'http://www.azworldairports.com/indexes/p-apnmq.cfm', 'http://www.azworldairports.com/indexes/p-apnmr.cfm', 'http://www.azworldairports.com/indexes/p-apnms.cfm', 'http://www.azworldairports.com/indexes/p-apnmt.cfm', 'http://www.azworldairports.com/indexes/p-apnmu.cfm', 'http://www.azworldairports.com/indexes/p-apnmv.cfm', 'http://www.azworldairports.com/indexes/p-apnmw.cfm', 'http://www.azworldairports.com/indexes/p-apnmx.cfm', 'http://www.azworldairports.com/indexes/p-apnmy.cfm', 'http://www.azworldairports.com/indexes/p-apnmz.cfm' ]
for lists in lists_of_sites:
	airportcodes = lists
	page = urllib2.urlopen(airportcodes).read()
	soup = BeautifulSoup(page)
#	with open("expedia.html", "w") as file:
#   		file.write(str(soup))
	print soup
#for tr in soup.find_all('tr')[2:]:
#	tds = tr.find_all('td')
#	print ("%s, %s, %s") % (tds[0].text, tds[1].text, tds[2].text)
