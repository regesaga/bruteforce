import os,sys,time,random,requests
from bs4 import BeautifulSoup as bs


url='https://m.facebook.com'
xurl=url+'/login.php'
def banner():
	os.system('clear')
	_="-"*44
	ban=f"""
{_}
 _     ____  _____ _  _     
/ \   /  _ \/  __// \/ \  /|
| |   | / \|| |  _| || |\ ||
| |_/\| \_/|| |_//| || | \||
\____/\____/\____\\\\_/\_/  \|
[Author : Md Josif Khan ]
[Github : github.com/josifkhan ]
{_}
"""
	print(ban)
ua="Mozilla/5.0 (Linux; Android 4.1.2; GT-I8552 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
def login():
	banner()
	user=input('[✦] //Username or Email//: ')
	pswd=input('[✦] //Password//: ')
	try:
		req=requests.Session()

		with req.get(url) as response_body:
			inspect=bs(response_body.text,'html.parser')
			lsd_key=inspect.find('input',{'name':'lsd'})['value']
			jazoest_key=inspect.find('input',{'name':'jazoest'})['value']
			m_ts_key=inspect.find('input',{'name':'m_ts'})['value']
			li_key=inspect.find('input',{'name':'li'})['value']
			try_number_key=inspect.find('input',{'name':'try_number'})['value']
			unrecognized_tries_key=inspect.find('input',{'name':'unrecognized_tries'})['value']
			bi_xrwh_key=inspect.find('input',{'name':'bi_xrwh'})['value']
			data={
			'lsd':lsd_key,'jazoest':jazoest_key,
			'm_ts':m_ts_key,'li':li_key,
			'try_number':try_number_key,
			'unrecognized_tries':unrecognized_tries_key,
			'bi_xrwh':bi_xrwh_key,'email':user,
			'pass':pswd,'login':"submit"}
			response_body2=req.post(xurl,data=data,allow_redirects=True,timeout=300)
			open("resopnse.html",'wb').write(response_body2.content)
			cookie=str(req.cookies.get_dict())
			if 'checkpoint' in cookie:sys.exit("\033[1;31mAccount terminated by Facebook!\033[0m")
			elif 'c_user' in cookie:
				print(f'\n   [\033[38;5;83mSuccessfully Log In!\033[0m] \033[0m\n\n')
				os.system('xdg-open https://facebook.com/josifvai')
				time.sleep(2)
				os.system('xdg-open https://github.com/josifkhan')
				time.sleep(2)
			else:
				sys.exit("\033[38;5;208mIncorrect details\033[0m")
	except requests.exceptions.ConnectionError:sys.exit('No internet')
login()