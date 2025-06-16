Rjecnik={}

fhand = open ('song.txt')
for line in fhand :
    line = line . rstrip ().replace(',','')
    
    words = line . split ()
    for word in words:
        if Rjecnik.setdefault(word,0)!=None:
            Rjecnik[word]+=1


fhand.close()
counter=0
for key,value in Rjecnik.items():
    if value==1:
        print(key)
        counter+=1
print(counter)