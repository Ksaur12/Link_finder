import urllib.request, urllib.parse, urllib.error
import re
import ssl

#Made by Ksaur12

print('''You can use this program to find links in a webpage, the links can be used for downloading
For example:''')
print('		If you want to download something but')
print('		the website keep your see ads, ')
print('		then can use this for retrieving the downloadable link\n\nEnter the full URL link like ---> https://www.google.com')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#empty list for storing the url, one by one
lst = []

#Prompt for the url
url = input('Enter the url- ')
print(url)

print('\n\nFinding the url.....')
try:
	#Open the url in it's source code
	html = urllib.request.urlopen(url, context=ctx).read()
except:
	print('\nError in network or in URL\nTry again')
	exit()

print('\n\nFinding the links in the url entered......')

links = re.findall(b'href="(http[s]?://.*?)"', html)
for link in links:
	link = link.decode() + '\n'
	lst.append(link)
file = open('links_retrieved.txt', 'w')
for i in lst:
	#Append every link into the links_retrieved.txt 
	file.write(i + '\n')

print("\nAll the links are saved in the links_retrieved.txt file\nPlease check your current folder")