import sys
n,m,k=list(map(int,sys.stdin.readline().split()))
data=[]
for _ in range(m):
    data.append(list(map(int,sys.stdin.readline().split())))

for _ in range(k):
    meteodict = dict()
    meteodictup=dict()
    meteomess={}
    meteovelocity={}
    meteod={}
    namedict={}
    for meteo in data:
        for _ in range(meteo[3]):
            if meteo[4]==0:
                if meteo[0]!=1:
                    meteo[0]-=1
                else:
                    meteo[0]=n
            elif meteo[4]==1:
                if meteo[0]!=1:
                    meteo[0]-=1
                else:
                    meteo[0]=n
                if meteo[1]!=n:
                    meteo[1]+=1
                else:
                    meteo[1]=1
            elif meteo[4]==2:
                if meteo[1]!=n:
                    meteo[1]+=1
                else:
                    meteo[1]=1
            elif meteo[4]==3:
                if meteo[1]!=n:
                    meteo[1]+=1
                else:
                    meteo[1]=1
                if meteo[0]!=n:
                    meteo[0]+=1
                else:
                    meteo[0]=1
            elif meteo[4]==4:
                if meteo[0]!=n:
                    meteo[0]+=1
                else:
                    meteo[0]=1
            elif meteo[4]==5:
                if meteo[0]!=n:
                    meteo[0]+=1
                else:
                    meteo[0]=1
                if meteo[1]!=1:
                    meteo[1]-=1
                else:
                    meteo[1]=n
            elif meteo[4]==6:
                if meteo[1]!=1:
                    meteo[1]-=1
                else:
                    meteo[1]=n
            elif meteo[4]==7:
                if meteo[1]!=1:
                    meteo[1]-=1
                else:
                    meteo[1]=n
                if meteo[0]!=1:
                    meteo[0]-=1
                else:
                    meteo[0]=n
        name = str(meteo[0]) +"/"+str(meteo[1])
        namedict[name]=[meteo[0],meteo[1]]
        if name not in meteodict:
            meteodict[name]=[meteo[2],meteo[3],meteo[4]]
            meteomess[name]=meteo[2]
            meteovelocity[name]=meteo[3]
            meteod[name]=[meteo[4]]
            namedict[name] = [meteo[0], meteo[1]]
        else:
            meteomess[name]+=meteo[2]
            namedict[name] = [meteo[0], meteo[1]]
            meteovelocity[name]+=meteo[3]
            meteod[name].append(meteo[4])
    new_meteo=[]
    for i in meteod.keys():
        a = namedict[i][0]
        b = namedict[i][1]
        c = meteomess[i]
        d=meteovelocity[i]
        e=meteod[i]
        if len(e)>=2:
            check = 1
            for j in range(len(e)):
                if check==4:
                    break
                elif e[j]%2==1 and check==3:
                    check=4
                # 전에 짝수였다가 이번에 홀수 check=4
                elif e[j]%2==0 and check==2:
                    check=4
                # 전에 홀수였다가 이번에 짝수 check=4
                elif e[j]%2==1 and check!=4:
                    check=2
                # 홀수이면서 check가 4가 아니면은 check는 2 유지
                elif e[j]%2==0 and check!=4:
                    check=3
                # 짝수이면서 check가 4가 아니면은 check는 3유지
            a=namedict[i][0]
            b=namedict[i][1]
            c=c//5
            d=d//len(e)
            if check==2 or check==3:
                new_meteo.append([a,b,c,d,0])
                new_meteo.append([a, b, c, d, 2])
                new_meteo.append([a, b, c, d, 4])
                new_meteo.append([a, b, c, d, 6])
            else:
                new_meteo.append([a, b,c, d, 1])
                new_meteo.append([a, b,c, d, 3])
                new_meteo.append([a, b,c, d, 5])
                new_meteo.append([a, b,c, d, 7])
            checkname=[]
            checkname.append([a,b])
        else:
            new_meteo.append([a,b,c,d,e[0]])

    if new_meteo:
        data=new_meteo


sum=0
for i in data:
    sum+=i[2]
print(sum)