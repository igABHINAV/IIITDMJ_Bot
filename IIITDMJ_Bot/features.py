import requests
x=requests.get('http://127.0.0.1:8000/getp/')


places=[]
lat=[]
lon=[]
ab=[]
for d in x.json() :
    for i,j in d.items() :
        if i=='name':
            places.append(j)
        elif i=='about' :
            ab.append(j)
        elif i=='latitude' :
            lat.append(j)
        else : lon.append(j)



def details(s) :
    for i in range(len(places)) :
        if places[i]==s :
            l=[]
            l.append(places[i])
            l.append("longitude is :" +lon[i])
            l.append("latitude is :"+lat[i])
            l.append(ab[i])
            l.append("google maps link : "+"https://www.google.com/maps/search/?api=1&query="+lon[i]+","+lat[i])
            return l
    return "not found"

