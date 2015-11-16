import os
s='';
r=''
i=0
for file in os.listdir("."):
    if file.endswith(".json"):
    	i+=1
    	with open(file,'r') as f:
		s=f.read()
		if i!=1:
			s=s[1:]
		s=s[0:-1]
		s+=','
		r+=s
r=r+']'
with open('iitd.json','w') as f:
	f.write(r)		
