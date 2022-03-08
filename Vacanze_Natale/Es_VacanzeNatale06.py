
f=open("./covid-19_gen1.txt","r")
testo,dict = f.readlines(),{"A" : 0 ,"T": 0 ,"C": 0 ,"G": 0 }
f.close()

for linee in testo:
         for char in linee:
            if char in dict:
                dict[char]+=1

print (dict)


