import server as s 
s.create("vamsi",25)
s.create("reddy",70,3600) 
s.read("vamsi")
s.read("reddy")
s.create("vamsi",50)
s.modify("vamsi",55)
s.delete("vamsi")
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
t2.sleep()
