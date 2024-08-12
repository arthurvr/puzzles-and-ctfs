import re
import requests

def get_solution(inp_ascii, shift):
	out_ascii = [(x - shift) for x in inp_ascii]
	out_chars = [chr(x) for x in out_ascii]
	return ''.join(out_chars)

url = "https://www.hackthissite.org/missions/prog/11/index.php"
cookies = {"PHPSESSID":"muo8bfbga72gcv54q778r75345"}

r = requests.get(url, cookies=cookies)

m = re.search(r'\<br \/\>Generated String: (.+)\<br \/\><br \/\>Shift\: (.+)<br \/\><br \/\>', r.text)
inp = m.group(1)
inp_separator = re.search('^\d+(\D+)', inp).group(1)
inp_ascii = [int(x) for x in inp.split(inp_separator)[:-1]]
shift = m.group(2)

sol = get_solution(inp_ascii, int(shift))

r = requests.post(url, cookies=cookies, data={'solution': sol}, headers={'referer':url})

if "Congrats" in r.text:
	print("Congrats! Succeeded mission!")
else:
	print(r.text)
