import difflib

text1 = "ACTGTGGTCTCACATTT"
text2 = "ACTGGTCACATTT"

sequence = difflib.SequenceMatcher(isjunk = None, a = text1, b = text2)

difference = sequence.ratio()*100
difference = round(difference, 1)

print str(difference) + "% match"