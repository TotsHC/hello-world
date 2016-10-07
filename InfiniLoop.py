print "You are currently in an infinate loop"


answer = raw_input("Would you like to quit the loop? (no) for yes: ")
answer2 = str(answer.lower)

if answer2 == str("no"):
    print "You are still in an infinate loop"
elif answer2 == str("yes"):
    print "You have exited the infinate loop"
else:
    print "ERROR"
