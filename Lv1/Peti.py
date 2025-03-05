fhand = open ('SMSSpamCollection.txt')
exclamation_and_spam=0
ham=0
spam=0
spam_words=0
ham_words=0
for line in fhand :
    line = line.rstrip ()

    if line.startswith("spam"):
        spam+=1
        spam_words+=len(line.split())-1
    else:
        ham+=1
        ham_words+=len(line.split())-1

if line.startswith("spam") and line.endswith("!"):
    exclamation_and_spam+=1

fhand . close ()



print('spam words avg:',spam_words/spam)
print('ham words avg',ham_words/ham)
print('spam sa usklićnikom',exclamation_and_spam)