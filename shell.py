import sys
import urllib.parse, urllib.request

def run_command(endpoint, command):
    encline = urllib.parse.quote(command, safe='')
    response = urllib.request.urlopen(endpoint + "?c=" + encline)
    return response.read().decode('utf-8')

if __name__ == "__main__":
    endpoint = sys.argv[1]
    while True:
        line = input("$ ")
        line = line.strip()
        if line == "quit" or line == "exit":
            sys.exit(0)
        print(run_command(endpoint, line))
