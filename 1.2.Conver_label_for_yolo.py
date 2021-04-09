print ("start")
save_changes = open('C:/Users/new_train.txt', 'w')
for a in range (101,301,1):
 
 a=str(a)
 f="C:/Users/label/001/"+a+".txt"


 f=open(f)
 
 text=[]
 for a1 in f:
  text.append(a1)
 print (text)
 text=str(text[1])
 text=text.replace(' ', ',')
 text=text[:len(text)-1]
 text = "C:/Users/image/" +a+".jpg" + " "+text+",0\n"
 print (text)
 save_changes.writelines(text)

save_changes.close()

