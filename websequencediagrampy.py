"""%prog [options] arg

Sends a request to websequencediagrams.com to render a sequence diagram and 
captures the result.

The script, when passed no options, will query you for them.

Please see http://www.websequencediagrams.com/embedding.html for the original 
inspiration for this script."""

def getSequenceDiagram(style, text, outputFile):
    """Issues a call to websequencediagrams.com and creates the output file."""

    import urllib
    import re

    request = {"message":text, "style":style}

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
    """Queries the user what style, input file to render, and output file to 
    save before issuing a call to websequencediagrams.com"""

    styles = ['default', 'earth', 'modern-blue', 'mscgen', 'omegapple', 'qsd', 
              'rose', 'roundgreen', 'napkin']

    import optparse        

    parser = optparse.OptionParser(__doc__)
    parser.add_option("-s", "--style", dest="style",
                      help="style of diagram, valid options: %s" % ", ".join(styles))
    parser.add_option("-i", "--input", dest="inFile", 
                      help="read sequence diagram source from FILENAME")
    parser.add_option("-p", "--png", dest="pngFile",
                      help="the FILENAME png to generate")
    (opts, args) = parser.parse_args()

    if not opts.inFile or not opts.pngFile or not opts.style:
        print ("Welcome to websequencediagrams.py.")
        print ("Please input the following to continue. CTRL+ESC to cancel.")
        print (", ".join(str(index+1) + ") " + str(value) for index, value in enumerate(styles)))
        opts.style = styles[int(raw_input("Choose style: "))-1]
        opts.inFile = raw_input("Source file to render (example filename.txt): ")
        opts.pngFile = raw_input("File to output (example filename.png): ")

    f = open(opts.inFile, 'r')
    text = '\n'.join(f.readlines())
  
    getSequenceDiagram(opts.style, text, opts.pngFile) 

if __name__ == '__main__': 
    main()

