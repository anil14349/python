# 
# Example file for retrieving data from the internet
#
import urllib.request as request

def main():
  # instantiate the parser and feed it some HTML
  webResponse = request.urlopen("http://www.google.com")
  print("result code : " , str(webResponse.getcode()))
  data = webResponse.read()
  print(data)

if __name__ == '__main__':
  main()
