import urllib.request
def gen1_main():
    fp = urllib.request.urlopen("http://localhost:1234/out.txt")
    sine_encodedContent = fp.read()
    sine_decodedContent = sine_encodedContent.decode("utf8")
    return float(sine_decodedContent)
    fp.close()
