import sys
import urllib.parse, urllib.request

def run_command(endpoint, command, paramname=None, extraparams=None):
    encline = urllib.parse.quote(command, safe='')
    pname = "c"

    if paramname is not None:
        pname = paramname

    # smoosh everything together here into a single URL
    # including any extra parameters the user may have
    # requested we include
    query = endpoint + "?{0}={1}".format(pname, encline)

    if extraparams is not None:
        query = "{0}&{1}".format(query, extraparams)

    response = urllib.request.urlopen(query)
    return response.read().decode('utf-8')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: shell endpoint [parameter name] [extraparams]")
        sys.exit(0)

    endpoint = sys.argv[1]

    paramname = None
    extraparams = None

    # intentionally done as two `if` forms
    # the first pulls out a custom parameter name
    # the second, any extra data we wish to include
    if len(sys.argv) > 2:
        paramname = sys.argv[2]

    if len(sys.argv) > 3:
        extraparams = sys.argv[3]

    while True:
        line = input("$ ")
        line = line.strip()
        if line == "quit" or line == "exit":
            sys.exit(0)
        print(run_command(endpoint, line, paramname=paramname, extraparams=extraparams))
