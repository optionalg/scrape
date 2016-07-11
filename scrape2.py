import webbrowser
import sys
import requests

# opens webbrowser
#webbrowser.open('https://google.com')

if len(sys.argv) > 1:
    address = ''.join(sys.argv[1:])
    #print(address)

r = requests.get("https://google.com")

# raises an exception if there is an error downloading the file
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

print(r.status_code)
