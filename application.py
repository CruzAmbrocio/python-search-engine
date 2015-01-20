import urllib2
import re

print ""
while True:
    try:
        tofind = raw_input("Enter a valid URL: ")
        complet = "http://" + str(tofind)
        urlrequest = urllib2.urlopen(str(complet))
        reading = urlrequest.read()
        urlrequest.close()
        print "      *Done!"
        break
    except:
        print "   >*Page not found!"


while True:
    try:
        tofindtwo = raw_input("Enter a valid URL: ")
        complettwo = "http://" + str(tofindtwo)
        urlrequesttwo = urllib2.urlopen(str(complettwo))
        readingto = urlrequesttwo.read()
        urlrequesttwo.close()
        print "      *Done!"
        break
    except:
        print "   >*Page not found!"


while True:
    print ""
    word = raw_input("What word you want to find? ")
    empty = str(word).isspace()
    emptynumb = len(word)
    if empty == False and emptynumb > 0:
        de = re.findall(word,reading)
        searcher = re.findall(word, readingto)
        coincidence = len(de)
        coincidencetwo = len(searcher)
        if coincidence > coincidencetwo:
            print ""
            print "Words found on", str(tofind), ":", str(coincidence)
            print "Words found on", str(tofindtwo), ":", str(coincidencetwo)
            print ""
            print "  >>*We recommend", str(tofind), "because it has more matches."
            break
        elif coincidencetwo > coincidence:
            print ""
            print "Words found on", str(tofind), ":", str(coincidence)
            print "Words found on", str(tofindtwo), ":", str(coincidencetwo)
            print ""
            print "We recommend", str(tofindtwo), "because it has more matches."
            break
        elif coincidence == coincidencetwo:
            print ""
            print "Words found on", str(tofind), ":", str(coincidence)
            print "Words found on", str(tofindtwo), ":", str(coincidencetwo)
            print ""
            print "You can visit any website, because the results are the same."
            break
        else:
            print ""
            print "No matches found."
            break
    else:
        print "Enter some data"

