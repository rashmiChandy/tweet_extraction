import re

def cleanText(text):

    cleanedText = re.findall("([0-9A-Za-z\s])", text)
    cleanedText = ''.join(cleanedText)
    cleanedText = re.sub("([\n])", "", cleanedText)
    cleanedText = re.sub('http\S+', "", cleanedText)
    cleanedText = re.sub("([\s]{2,})", " ", cleanedText)
    return cleanedText
