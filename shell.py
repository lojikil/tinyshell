import sys
import urllib.parse, urllib.request

endpoint = sys.argv[1]

while True:
    line = input("$ ")
    line = line.strip()
    if line == "quit" or line == "exit":
        sys.exit(0)
    encline = urllib.parse.quote(line, safe='')
    response = urllib.request.urlopen(endpoint + "?c=" + encline)
    data = response.read()
    print(data.decode('ascii'))
