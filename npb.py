from bs4 import BeautifulSoup as bs
import requests as re
from datetime import datetime as dt

# dd/mm/YY
today = dt.today()
d = today.strftime("%Y%m%d")
print(d)

url = 'https://npb.jp/bis/eng/2022/games/gm'+d+'.html'
#url = 'https://npb.jp/bis/eng/2022/games/gm20221017.html'
req = re.get(url)
s2 = bs(req.content,'html.parser')


#hruns = "Hanshin Tigers didn't play today"
#oppsruns = ""
teams = s2.findAll(class_="contentsTeam")
#for each in range(0,len(teams)):
	#if teams[each].get_text() == 'Hanshin':
		#hruns = 'Hanshin Tigers Scored '+teams[each].previous_sibling.get_text()
		#if each%2 == 0:
			#oppsruns = teams[each+1].get_text() + ' scored ' + teams[each+1].previous_sibling.get_text()
		#else:
			#oppsruns = teams[each-1].get_text() + ' scored ' + teams[each-1].nextSibling.get_text()
#print(hruns)
#print(oppsruns)

for each in range(0,len(teams)):
	if each%2 == 0:
		firstruns = teams[each].get_text() + ' scored ' + teams[each].nextSibling.get_text()
		secondruns = teams[each+1].get_text() + ' scored ' + teams[each+1].previous_sibling.get_text()
		print(firstruns)
		print(secondruns)

