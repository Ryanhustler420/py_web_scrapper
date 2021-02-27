from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--profile-directory=Default') 

def get_Players(url):
	try:
		driver = webdriver.Chrome(options = options, executable_path= r'C:\chromedriver.exe') # This fires a browser
		driver.get(url)

		players = {}

		html_doc = driver.page_source
		soup = BeautifulSoup(html_doc, 'html.parser')
		table = soup.find('table').find('tbody').findChildren()

		for tr in table:
			data = tr.find('a', class_ = 'player-name ng-isolate-scope')
			if(data != None):
				fn = ""
				for fl in data.findAll('span'):
					fn = fn + " " + fl.text
				players[fn.strip()] = 'https://in.global.nba.com' + data['href']

		driver.quit()
		return players

	except Exception as err:
		print(err)
		driver.quit()
		return players

def get_single_player_detail(url):
	try:
		driver = webdriver.Chrome(options = options, executable_path= r'C:\chromedriver.exe') # This fires a browser
		driver.get(url)

		detail = '';
		htmlDoc = driver.page_source
		soup = BeautifulSoup(htmlDoc, 'html.parser')

		p_childrens = soup.find('div', class_ = "player-info-right hidden-sm").find('p').findChildren()
		for span in p_childrens:
			if span.has_attr("class"):
				if "player-info-right--bio" in span.get('class'):
					detail = detail + span.text
		driver.quit()
		return detail.strip()
	except Exception as err:
		print(err)
		driver.quit()
		return detail.strip()

def digData():
	try:
		final = []
		all_players = get_Players('https://in.global.nba.com/playerindex/')
		for pl in all_players:
			val = get_single_player_detail(all_players[pl])			
			final.append(val)

		for c in final:
			print(c)
			print('------')

	except Exception as e:
		print(e)

digData()

# get_Players('')

# Electronic -> Mobile -> Brand -> All Fetch

# note pagination, because if gets croupt then we can note the 
# last saved line / 20 each % 20 == 0, it will also get the page number

# 6-8 / 225 lbs
# Born: 1999-09-19Drafted: 2020Experience: 0 yearsPrior to NBA: Memphis/Nigeria
# ------
# 6-0 / 225 lbs
# Born: 1996-05-04Drafted: 2018Experience: 2 yearsPrior to NBA: St. Bonaventure/United States
# ------
# 6-11 / 265 lbs
# Born: 1993-07-20Drafted: 2013Experience: 7 yearsPrior to NBA: Pittsburgh/New Zealand
# ------
# 6-9 / 255 lbs
# Born: 1997-07-18Drafted: 2017Experience: 3 yearsPrior to NBA: Kentucky/United States
# ------
# 6-11 / 250 lbs
# Born: 1985-07-19Drafted: 2006Experience: 14 yearsPrior to NBA: Texas/United States
# ------
# 6-3 / 195 lbs
# Born: 1998-07-16Drafted: 2020Experience: 0 yearsPrior to NBA: Creighton/United States
# ------
# 6-6 / 205 lbs
# Born: 1998-09-02Drafted: 2019Experience: 1 yearsPrior to NBA: Virginia Tech/Canada
# ------
# 6-4 / 198 lbs
# Born: 1995-10-08Drafted: 2018Experience: 2 yearsPrior to NBA: Duke/United States
# ------
# 6-11 / 243 lbs
# Born: 1998-04-21Drafted: 2017Experience: 3 yearsPrior to NBA: Texas/United States
# ------
# 6-8 / 220 lbs
# Born: 1990-09-21Drafted: 2010Experience: 10 yearsPrior to NBA: Wake Forest/United States
# ------
# 6-9 / 230 lbs
# Born: 1993-09-20Drafted: 2014Experience: 6 yearsPrior to NBA: UCLA/United States
# ------
# 6-11 / 242 lbs
# Born: 1994-12-06Drafted: 2013Experience: 7 yearsPrior to NBA: Filathlitikos/Greece
# ------
# 6-10 / 200 lbs
# Born: 1997-11-20Drafted: 2018Experience: 2 yearsPrior to NBA: Dayton/Greece
# ------
# 6-6 / 219 lbs
# Born: 1992-07-18Drafted: 2014Experience: 2 yearsPrior to NBA: Panathinaikos/Greece
# ------
# 6-7 / 238 lbs
# Born: 1984-05-29Drafted: 2003Experience: 17 yearsPrior to NBA: Syracuse/United States
# ------
# 6-2 / 185 lbs
# Born: 2000-05-15Drafted: 2020Experience: 0 yearsPrior to NBA: North Carolina/United States
# ------
# 6-7 / 232 lbs
# Born: 1997-07-17Drafted: 2017Experience: 3 yearsPrior to NBA: Indiana/United Kingdom
# ------
# 6-3 / 195 lbs
# Born: 1994-03-26Drafted: 2016Experience: 3 yearsPrior to NBA: Villanova/United States
# ------
# 6-8 / 215 lbs
# Born: 1985-06-30Drafted: 2004Experience: 16 yearsPrior to NBA: UCLA/United States
# ------
# 5-11 / 183 lbs
# Born: 1987-11-10Drafted: 2008Experience: 12 yearsPrior to NBA: Texas/United States
# ------
# 6-9 / 210 lbs
# Born: 2001-01-03Drafted: 2020Experience: 0 yearsPrior to NBA: Maccabi Tel Aviv/Israel
# ------
# 6-11 / 250 lbs
# Born: 1998-07-23Drafted: 2018Experience: 2 yearsPrior to NBA: Arizona/Bahamas
# ------
# 6-10 / 280 lbs
# Born: 1999-09-17Drafted: 2020Experience: 0 yearsPrior to NBA: Kansas/Nigeria
# ------
