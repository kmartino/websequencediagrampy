import urllib
import re

"""Sends a request to websequencediagrams.com to render a sequence diagram and 
captures the result.

Please see http://www.websequencediagrams.com/embedding.html for the original 
inspiration for this script.
"""

def getSequenceDiagram(style, text, outputFile):
    """Issues a call to websequencediagrams.com and creates the output file."""

    request = {}
    request["message"] = text
    request["style"] = style

    url = urllib.urlencode(request)

    f = urllib.urlopen("http://www.websequencediagrams.com/", url)
    line = f.readline()
    f.close()

    expr = re.compile("(\?img=[a-zA-Z0-9]+)")
    m = expr.search(line)

    if m == None:
        print "Invalid response from server."
        return False

    urllib.urlretrieve("http://www.websequencediagrams.com/" + m.group(0),
            outputFile )
    return True

def main():
    """Queries the user what style, input file to render, and output file to save before issuing 
    a call to websequencediagrams.com"""

    styles = ['default', 'earth', 'modern-blue', 'mscgen', 'omegapple', 'qsd', 
              'rose', 'roundgreen', 'napkin']

    print ", ".join(str(index+1) + ") " + str(value) for index, value in enumerate(styles))

    style = styles[int(raw_input("Choose style: "))-1]
    inFile = raw_input("Source file to render (example filename.txt): ")
    pngFile = raw_input("File to output (example filename.png): ")

    f = open(inFile, 'r')
    text = '\n'.join(f.readlines())
  
    getSequenceDiagram(style, text, pngFile) 

if __name__ == '__main__': 
    main()

