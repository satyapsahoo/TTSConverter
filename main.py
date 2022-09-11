import requests

url = "https://voicerss-text-to-speech.p.rapidapi.com/"

querystring = {
	"key": "d9196f5465msh2266fdd32ed2583p148b6djsn84eed7aa4a3e",
	"src": "Hello, world!",
	"hl": "en-us",
	"r": "0",
	"c": "mp3",
	"f": "8khz_8bit_mono"
}

headers = {
	"X-RapidAPI-Key": "d9196f5465msh2266fdd32ed2583p148b6djsn84eed7aa4a3e",
	"X-RapidAPI-Host": "voicerss-text-to-speech.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.text)
