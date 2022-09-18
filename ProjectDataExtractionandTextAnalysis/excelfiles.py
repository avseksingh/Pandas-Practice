def getFileName(url):
    x = url
    x = x.replace("/", "")
    x = x.replace("http:", "")
    x = x.replace("https:", "")
    x = x + ".txt"
    return x