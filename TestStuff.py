things = raw_input("Input a number of things: ")
print "You input %s Things" % (things)
things = int(things)
if things < 10:
    print "There are less than 10 things"
elif things > 10:
    print "There are more than 10 things"
else:
    print "There are 10 things"
