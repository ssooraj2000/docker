import urllib.request
def gen2_main():
    fp = urllib.request.urlopen("http://localhost:1235/out.txt")
    sine_encodedContent = fp.read()
    sine_decodedContent = sine_encodedContent.decode("utf8")
    return float(sine_decodedContent)
    fp.close()
