import pandas as pd
import numpy as np
from graphics import *
from random import seed, randint
import datetime
from datetime import timedelta
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from PIL import Image as IMG
import csv
import glob 
import math
import time 

filepath = '/Users/lekshmigopal/CR350Series_Table1.dat'

np.set_printoptions(legacy='1.21')
df=pd.read_csv(filepath, skiprows=3)
# print(df)
#df = df.iloc[:,[0,3,4,5,8,9,10,11,12,13]]
pd.set_option('display.max_columns', 22)
#print(df.iloc[0,:])
# df=df.iloc[:,[0,3,4,5,6,7,8,9]]
# print(df)
df=df.iloc[:,[0,11,8,14,4,13]]
#print(df)
time=np.array(df.iloc[:,0])
         
targetindex=[] 
day=[]       
for i in range(len(time)):
    if (time[i])[3]=='5' and (time[i])[9]=='7':
        targetindex.append(i)
        day.append(time[i])
daydata=(day[0])[0:10]

df=df.iloc[targetindex[0]:targetindex[-1],:]


# print(df)
time=np.array(df.iloc[:,0])

####### averaging by hour #########
#####identify the unique rows 

previous=''
uniquevals=[]
for hr in range(len(time)):
    day1=(time[hr])[8]
    day2=(time[hr])[9]
    hour1=(time[hr])[11]
    hour2=(time[hr])[12]
    if [day1,day2,hour1,hour2]!= previous:
        uniquevals.append(hr)
        previous=[day1,day2,hour1,hour2]
# print("uniquevals are",uniquevals)
#####avgtemp, avgwvc
#   SKIPPING LAST UNIQUE VALUE, LENGTH -1 EXCLUDES LAST ELEMENT 
masterdf=[]
for un in range(len(uniquevals)-1):
    df2=df.iloc[uniquevals[un]:uniquevals[un+1],:]
    df2temp=df2.iloc[:,1]
    df2temp=pd.to_numeric(df2temp,errors='coerce')
    df2temp.replace('NAN',0)
    df2wvc=df2.iloc[:,2]
    df2wvc=pd.to_numeric(df2wvc,errors='coerce')
    df2wvc.replace('NAN',0)
    df2vapor=df2.iloc[:,3]
    df2vapor=pd.to_numeric(df2vapor,errors='coerce')
    df2vapor.replace('NAN',0)
    df2rad=df2.iloc[:,4]
    df2rad=pd.to_numeric(df2rad,errors='coerce')
    df2rad.replace('NAN',0)
    df2air=df2.iloc[:,5]
    df2air=pd.to_numeric(df2air,errors='coerce')
    df2air.replace('NAN',0)
    
    

    
    
    hourlyavgtemp=df2temp.mean(axis=0)
    hourlyavgwvc=df2wvc.mean(axis=0)
    hourlyavgvapor=df2vapor.mean(axis=0)
    hourlyavgrad=df2rad.mean(axis=0)
    hourlyavgair=df2air.mean(axis=0)
    
    
    data = {'Time': [(df2.iloc[0,0])[11:13]],
          'AvgTemp': [hourlyavgtemp],
          'WVc':[hourlyavgwvc*1.94384],
          'Vapor':[hourlyavgvapor],
          'Radiation':[hourlyavgrad],
          'Air Pressure':[hourlyavgair]}
    
    df3 = pd.DataFrame(data)
    masterdf.append(df3)


masterdf=pd.concat(masterdf)

#print(masterdf)

########## INCLUDE LAST UNIQUE VALUE AND TAKE HOURLY AVERAGE OF LAST HOUR #########

dflast=df.iloc[uniquevals[-1]:,:]

dflasttemp=dflast.iloc[:,1]
dflasttemp=pd.to_numeric(df2temp,errors='coerce')
dflasttemp.replace('NAN',0)
avglasttemp=dflasttemp.mean(axis=0)

dflastwvc=dflast.iloc[:,2]
dflastwvc=pd.to_numeric(dflastwvc,errors='coerce')
dflastwvc.replace('NAN',0)
avglastwvc=dflastwvc.mean(axis=0)

dflastvapor=dflast.iloc[:,3]
dflastvapor=pd.to_numeric(dflastvapor,errors='coerce')
dflastvapor.replace('NAN',0)
avglastvapor=dflastvapor.mean(axis=0)

dflastrad=dflast.iloc[:,4]
dflastrad=pd.to_numeric(dflastrad,errors='coerce')
dflastrad.replace('NAN',0)
avglastrad=dflastrad.mean(axis=0)

dflastair=dflast.iloc[:,5]
dflastair=pd.to_numeric(dflastair,errors='coerce')
dflastair.replace('NAN',0)
avglastair=dflastair.mean(axis=0)

datalast={"Time":[(dflast.iloc[0,0])[11:13]],
          'AvgTemp': [avglasttemp],
          'WVc':[avglastwvc*1.94384],
          'Vapor':[avglastvapor],
          'Radiation':[avglastrad],
          'Air Pressure':[avglastair]
          }

lastdf=pd.DataFrame(datalast)

toconcat=[masterdf,lastdf]
masterdf=pd.concat(toconcat)


############################################### MATCHING TO CURRENT TIME AND TIME STAMP ON PLOT##########################################

nowhr=(datetime.datetime.now() + timedelta(hours=0)).strftime("%H00")


times=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
for i in range(len(times)):
    if times[i]==nowhr[0:2]:
        breakindex=i
        

times=times[0:breakindex+1]
currenttime=times[-1] ## where wx data should end and model data begins
AverageTemp=[]
indices_in_avgtemp=-1

AverageWVc=[]
indices_in_WVc=-1

AverageVapor=[]
AverageRad=[]
AverageAir=[]

for hour in range(len(times)):
    
    #print(times[hour])
    if times[hour] in np.array(masterdf.iloc[:,0]):
        indices_in_avgtemp=indices_in_avgtemp+1
        indices_in_WVc=indices_in_WVc+1
        AverageTemp.append(masterdf.iloc[indices_in_avgtemp,1])
        AverageWVc.append(masterdf.iloc[indices_in_WVc,2])
        AverageVapor.append(masterdf.iloc[indices_in_WVc,3])
        AverageRad.append(masterdf.iloc[indices_in_WVc,4])
        AverageAir.append(masterdf.iloc[indices_in_WVc,5])
    else:
        AverageTemp.append(0)
        AverageWVc.append(0)
        AverageRad.append(0)
        AverageVapor.append(0)
        AverageAir.append(0)



        
data = {'Time': times,
          'AvgTemp': AverageTemp,
          'WVc': AverageWVc,
          "Vapour":AverageVapor,
          "Radiation": AverageRad,
          'Air Pressure': AverageAir}
masterdf=pd.DataFrame(data) 
#print(masterdf)
#######-----------------> DF with current day stats, displaying relevant parameter columns ########3
# #print(df3)


#--------------------------------------------> load and manipulate model data to trim till one hour after current time 

df1=pd.read_excel('/Users/lekshmigopal/eddysampledata.xlsx','KYT.d01y',skiprows=3)
df1=df1.iloc[:,[1,5,6,7,8,10,18,9]]
#print(df)

nowhr2=(datetime.datetime.now() + timedelta(hours=1)).strftime("%H")
nowhr2=int(nowhr2)
obsvstart=10

# times2=np.arange(nowhr,24,step=1)

ts_h=np.array(df1.iloc[:,0])
allhrs=np.arange(1,24,step=1)
previous2=''
hourvals=[]
for hr2 in range(len(ts_h)):
    if ts_h[hr2] in allhrs:
        hourvals.append(hr2)
#print(hourvals)

# num_columns=len(df1.columns)
# lastindex=len(hourvals)
zero=0
masterdfmodel=[]
for inthour in range(len(hourvals)):
    # print("zero is",zero)
    # print("int vals are in",hourvals[inthour])
    dfbreak=df1.iloc[zero:(hourvals[inthour]+1),:]
    dft=dfbreak.iloc[:,1]
    avgt=dft.mean(axis=0)
    dfq=dfbreak.iloc[:,2]
    avgq=dfq.mean(axis=0)
    dfu=dfbreak.iloc[:,3]
    avgu=dfu.mean(axis=0)
    dfv=dfbreak.iloc[:,4]
    avgv=dfv.mean(axis=0)
    dfglw=dfbreak.iloc[:,5]
    avgglw=dfglw.mean(axis=0)
    dfclw=dfbreak.iloc[:,6]
    avgclw=dfclw.mean(axis=0)
    dfpsfc=dfbreak.iloc[:,7]
    avgpsfc=dfpsfc.mean(axis=0)
    windmag=math.sqrt(((avgu)**2)+((avgv)**2))
    e= (avgq*avgpsfc/0.622)
    SVP=1000*(0.61078*(math.exp((17.2694*(avgt-273.15))/(avgt-35.85))))
    RelHum=(e/(SVP))*100
    #print(" this index is working")
    
    data2={ 'Time':[obsvstart],
            'Temp': [avgt-273.15],
            'q':[avgq],
            'Wind Speed':[windmag*1.94384],
            'u':[avgu],
            'v':[avgv],
            'glw':[avgglw],
            'clw':[avgclw],
            'PSFC':[avgpsfc/100],
            'Vapor pressure (e)':e,
            'SVP': SVP,
            'Rel.Humidity' : RelHum}
    
    dfnew=pd.DataFrame(data2)
    masterdfmodel.append(dfnew)
    zero=hourvals[inthour]+1
    obsvstart=(obsvstart + 1)%24
    
    
    
masterdfmodel=pd.concat(masterdfmodel)
    
#print(masterdfmodel)

## start model data from current time 

for indexj in range(len(masterdfmodel.iloc[:,0])):
    if masterdfmodel.iloc[indexj,0]==nowhr2:
        masterdfmodel=masterdfmodel.iloc[indexj:-1,:]
        break
#print(masterdfmodel) -------------------------------> This is final masterdfmodel

print(masterdfmodel)


#----------------------------------------------------> Finding angle of winddir : physics - beta, met - theta 
thetadir=[]
betadir=[]

for uv in range(len(masterdfmodel)):
    ## SW wind (emerging into 1st quadrant)
    if masterdfmodel.iloc[uv,4]>0 and masterdfmodel.iloc[uv,5]>0:
        beta=math.atan((masterdfmodel.iloc[uv,5])/(masterdfmodel.iloc[uv,4]))
        theta=1.5*math.pi - beta
    ## SE wind (emerging into 2nd quadrant)
    if masterdfmodel.iloc[uv,4]<0 and masterdfmodel.iloc[uv,5]>0:
        beta=math.atan((masterdfmodel.iloc[uv,5])/(masterdfmodel.iloc[uv,4]))
        theta=0.5*math.pi +beta
    ## NE wind(emerging into 3rd quadrant )
    if masterdfmodel.iloc[uv,4]<0 and masterdfmodel.iloc[uv,5]<0:
        beta=math.atan((masterdfmodel.iloc[uv,5])/(masterdfmodel.iloc[uv,4]))
        theta=0.5*math.pi -beta
    ## NW wind (emerging into 4th quadrant)
    if masterdfmodel.iloc[uv,4]>0 and masterdfmodel.iloc[uv,5]<0:
        beta=math.atan((masterdfmodel.iloc[uv,5])/(masterdfmodel.iloc[uv,4]))
        theta=1.5*math.pi +beta
    thetadir.append(theta)
    betadir.append(beta)


betadir[1]=0.3*math.pi
thetadir[1]=1.2*math.pi

betadir[4]=0.3*math.pi
thetadir[4]=0.8*math.pi

betadir[7]=0.3*math.pi
thetadir[7]=0.2*math.pi

betadir[9]=0.3*math.pi
thetadir[9]=1.8*math.pi
print(betadir)
# pltxlabels=[]
# for pltindex in range(len(masterdfmodel.iloc[:,0])):
#     pltxlabels.append(pltindex)
# print(pltxlabels)
# clwcolumn=np.array(masterdfmodel.iloc[:,4])
# plt.scatter(pltxlabels,clwcolumn,color='red')
# plt.xlabel('Time')
# xticks=np.array(masterdfmodel.iloc[:,0])
# plt.xticks([0,5,10,15,20])

columns=len(times) 
columns2=len(masterdfmodel.iloc[:,0])

times2=masterdfmodel.iloc[:,0]
#print(times2)
#print(df3.iloc[:,1])
#------------------------------------------------------------> COLORS FOR WX DATA
######            AVGTEMP colourassign
# for p in df3.iloc[:,1]:
#     print(p)

tempcolors=[]
for p in masterdf.iloc[:,1]:
    if 0<p<=10:
        tempcolors.append("dodgerblue")
    if 10<p<=15:
        tempcolors.append("lightskyblue")
    if 15<p<=20:
        tempcolors.append("white")
    if 20<p<=25:
        tempcolors.append("moccasin")
    if 25<p<=30:
        tempcolors.append("gold")
    if 30<p<=35:
        tempcolors.append("orange")
    if 35<p<=40:
        tempcolors.append("orangered")
    if p==0:
        tempcolors.append('thistle')
        
#######         WVc wind speed colourassign

wvcolors=[]
for q in masterdf.iloc[:,2]:
    if 0.001<q<=18:
        wvcolors.append("blue")
    if 18<q<=20:
        wvcolors.append("cornflowerblue")
    if 20<q<=22:
        wvcolors.append("skyblue")
    if 22<q<=24:
        wvcolors.append("powderblue")
    if 24<q<=26:
        wvcolors.append("lightcyan")
    if 26<q<=28:
        wvcolors.append("mintcream")
    if 28<q<=30:
        wvcolors.append("silver")
    if q==0:
        wvcolors.append("thistle")   
        
#### FOR VAPOUR  ---> humidity

vaporcolors=[]

for v in masterdf.iloc[:,3]:
    if 0<v<=40:
        vaporcolors.append("peru")
    if 40<v<=50:
        vaporcolors.append("sandybrown")
    if 50<v<=60:
        vaporcolors.append("peachpuff")
    if 60<v<=70:
        vaporcolors.append("lightcyan")
    if 70<v<=80:
        vaporcolors.append("skyblue")
    if 80<v<=90:
        vaporcolors.append("blue")
    if v==0:
        vaporcolors.append("thistle")        
        
#### FOR RADIATION
radflux=[]

for f in masterdf.iloc[:,4]:
    if 300<f<=350:
        radflux.append("gold")
    if 350<f<=400:
        radflux.append("orange")
    if 400<f<=450:
        radflux.append("darkorange")
    if 450<f<=500:
        radflux.append("orangered")
    if 500<f<=550:
        radflux.append("red")
    if 550<f<=600:
        radflux.append("firebrick")
    if f==0:
        radflux.append("thistle")         
        
#### Air pressure 

aircolors=[]

for ap in masterdf.iloc[:,5]:
    if 0<ap<=300:
        aircolors.append("blue")
    if 300<ap<=400:
        aircolors.append("cornflowerblue")
    if 400<ap<=500:
        aircolors.append("skyblue")
    if 500<ap<=600:
        aircolors.append("powderblue")
    if 600<ap<=700:
        aircolors.append("lightcyan")
    if 700<ap<=800:
        aircolors.append("mintcream")
    if ap==0:
        aircolors.append("thistle")        




######     Darkness colourassign

hrs= 24

time=[]   
for c in times:
    if (c[0]=='0' and (c[1]=='0' or c[1]=='1' or c[1]=='2' or c[1]=='3' or c[1]=='4' or c[1]=='5')) or c[0]=='2' or (c[0]=='1' and c[1]=='9'):
        time.append('navy')
    if (c[0]=='1' and c[1]=='6') or c[1]=='7' or (c[0]=='0' and c[1]=='8') or (c[0]=='0' and c[1]=='9') or (c[0]=='1' and (c[1]=='0' or c[1] =='1' or c[1]=='2' or c[1]=='3' or c[1]=='4' or c[1]=='5')):
        time.append("gold")
    if (c[0] =='0' and c[1] =='6') or (c[0] =='1' and c[1]=='8'):
        time.append('orange')


#------------------------------------------------------------colors for model 

###Temperature

tempcolors2=[]
for p in masterdfmodel.iloc[:,1]:
    if 0<p<=10:
        tempcolors2.append("dodgerblue")
    if 10<p<=15:
        tempcolors2.append("lightskyblue")
    if 15<p<=20:
        tempcolors2.append("white")
    if 20<p<=25:
        tempcolors2.append("moccasin")
    if 25<p<=30:
        tempcolors.append("gold")
    if 30<p<=35:
        tempcolors2.append("orange")
    if 35<p<=40:
        tempcolors2.append("orangered")
    if p==0:
        tempcolors2.append('thistle')
#print("tempcolors2 is",tempcolors2)


### Wind Speed
wvcolors2=[]
for q in masterdfmodel.iloc[:,3]:
    if 0.001<q<=18:
        wvcolors2.append("blue")
    if 18<q<=20:
        wvcolors2.append("cornflowerblue")
    if 20<q<=22:
        wvcolors2.append("skyblue")
    if 22<q<=24:
        wvcolors2.append("powderblue")
    if 24<q<=26:
        wvcolors2.append("lightcyan")
    if 26<q<=28:
        wvcolors2.append("mintcream")
    if 28<q<=30:
        wvcolors2.append("silver")
    if q==0:
        wvcolors2.append("thistle")    
        
## Vapour Ratio

vaporcolors2=[]
#print("vapor max ",(masterdfmodel.iloc[:,2]).max(axis=0))
#print("vapor min ",(masterdfmodel.iloc[:,2]).min(axis=0))


for v in masterdfmodel.iloc[:,11]:
    if 0<v<=20:
        vaporcolors2.append("peru")
    if 20<v<=40:
        vaporcolors2.append("sandybrown")
    if 40<v<=60:
        vaporcolors2.append("peachpuff")
    if 60<v<=80:
        vaporcolors2.append("lightcyan")
    if 80<v<=90:
        vaporcolors2.append("skyblue")
    if 90<v<=100:
        vaporcolors2.append("blue")
    if v==0:
        vaporcolors2.append("thistle")        
#print(vaporcolors2)
        
### Darkness 

timecolors2=[]   
for c in times2:
    if c==6 or c==18:
        timecolors2.append("orange")
    if 18<c<=24:
        timecolors2.append("navy")
    if 0<=c<6:
        timecolors2.append("navy")
    if 6<c<18:
        timecolors2.append("gold")
        
## RADIATION AT GROUND (GLW)

radflux2=[]

for f in masterdfmodel.iloc[:,6]:
    if 310<f<=330:
        radflux2.append("gold")
    if 330<f<=340:
        radflux2.append("orange")
    if 340<f<=350:
        radflux2.append("darkorange")
    if 350<f<=360:
        radflux2.append("orangered")
    if 360<f<=370:
        radflux2.append("red")
    if 370<f<=380:
        radflux2.append("firebrick")
    if f==0:
        radflux2.append("thistle")         
        
## CLOUD CLW 

cloud2=[]

for c in masterdfmodel.iloc[:,7]:
    if 1e-6<c<=0.0001:
        cloud2.append("white")
    if 0.0001<c<=0.1:
        cloud2.append("whitesmoke")
    if 0.1<c<=0.5:
        cloud2.append("gainsboro")
    if 0.5<c<=1:
        cloud2.append("lightgrey")
    if 1<c<=1.5:
        cloud2.append("silver")
    if 1.5<c<=2:
        cloud2.append("darkgrey")
    if 2<c<=2.5:
        cloud2.append("grey")
    if 2.5<c<=3:
        cloud2.append("dimgrey")
    if c==0:
        cloud2.append("thistle")        

airpressure2=[]

for ap in masterdfmodel.iloc[:,8]:
    if 0<ap<=300:
        airpressure2.append("blue")
    if 300<ap<=500:
        airpressure2.append("cornflowerblue")
    if 500<ap<=700:
        airpressure2.append("skyblue")
    if 700<ap<=900:
        airpressure2.append("powderblue")
    if 900<ap<=1000:
        airpressure2.append("lightcyan")
    if 1000<ap<=1200:
        airpressure2.append("mintcream")
    if ap==0:
        airpressure2.append("thistle")        

        

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~graphics window~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():

    top_left_x = 100
    top_left_y = 200
    width = 16
    height = 16
    num_rows = 1 
    num_columns = columns 
    num_columns2=columns2
    window = GraphWin('Lab 4B', 800, 1000)
        ## Title 
    title = Text(Point(400,10),"Mt. Kenya - Sample")
    title.setSize(20)
    title.draw(window)
    #window.setBackground("black")
    
    # daytext=Text(Point(325,40),daydata)
    # daytext.draw(window)
    
    # @@@@@@@@@@@@@@@@@@@@@@ PICK CURRENT DAY TEXT IF LIVE
    
    today = datetime.date.today().strftime('%d-%m-%Y')
    todaypl1 = (datetime.date.today()+ timedelta(days=1)).strftime('%d-%m-%Y')
    
    date1= Text(Point(360,40),today)
    hyph = Text(Point(400,40),"-")
    date2 = Text(Point(440,40),todaypl1)
    date1.draw(window)
    hyph.draw(window)
    date2.draw(window)
    
    ##-------> text for cmap title 
    
    colormap=Text(Point(top_left_x/2,620),"Colourmaps:")
    colormap.setSize(10)
    colormap.setStyle("bold")
    colormap.draw(window)
    
    ##-----------------------------> LEGEND FOR TEMPERATURE
    
    tempcmap = IMG.open('/Users/lekshmigopal/Tempcmap.gif')
    tempcmap = tempcmap.crop((11, 7.3, 363, 29.5))
    tempcmap = tempcmap.resize((271, 16))
    # wid, hgt = tempcmap.size 
    # print(str(wid) + "x" + str(hgt))
    tempcmap.save('Tempcmapresize.gif')
    tempcmap=Image(Point(top_left_x/2 +200,650), "Tempcmapresize.gif")
    tempcmap.draw(window)    
    
    cmaptemp = Text(Point(top_left_x/2,650),"Temperature")
    cmaptemp.setSize(10)
    cmaptemp.draw(window)  
    
    temprange1=Text(Point(top_left_x/2 +75,650),"0C")
    temprange2=Text(Point(top_left_x/2 +322,650),"40C")
    temprange1.setSize(10)
    temprange2.setSize(10)
    temprange1.draw(window)
    temprange2.draw(window)
    ##-----------------------------------> LEGEND FOR REL HUMIDITY (VAPOUR)
    
    humcmap = IMG.open('/Users/lekshmigopal/humiditycmap.png')
    humcmap = humcmap.crop((11, 7.3, 363, 29.5))
    humcmap = humcmap.resize((271, 16))
    # wid, hgt = tempcmap.size 
    # print(str(wid) + "x" + str(hgt))
    humcmap.save('humcmapresize.png')
    humcmap=Image(Point(top_left_x/2 +200,680), "humcmapresize.png")
    humcmap.draw(window)       
    
    cmaphum = Text(Point(top_left_x/2,680),"Rel.Humidity")
    cmaphum.setSize(10)
    cmaphum.draw(window)    
    
    humrange1=Text(Point(top_left_x/2 +78,680),"0%")
    humrange2=Text(Point(top_left_x/2 +321,680),"100%")
    humrange1.setSize(10)
    humrange2.setSize(10)
    humrange2.setFill("mintcream")
    humrange1.draw(window)
    humrange2.draw(window)        
    ##-----------------------------------> LEGEND FOR GLW
    glwcmap = IMG.open('/Users/lekshmigopal/glwcmap.png')
    glwcmap = glwcmap.crop((11, 7.3, 363, 29.5))
    glwcmap = glwcmap.resize((271, 16))
    # wid, hgt = tempcmap.size 
    # print(str(wid) + "x" + str(hgt))
    glwcmap.save('glwcmapresize.gif')
    
    glwcmap=Image(Point(top_left_x/2 +200,710), "glwcmapresize.gif")
    glwcmap.draw(window)       
    
    cmapglw = Text(Point(top_left_x/2,710),"GLW")
    cmapglw.setSize(10)
    cmapglw.draw(window)    
    
    glwrange1=Text(Point(top_left_x/2 +94,710),"310W/m^2")
    glwrange2=Text(Point(top_left_x/2 +310,710),"380W/m^2")
    glwrange1.setSize(10)
    glwrange2.setSize(10)
    glwrange2.setFill("mintcream")
    glwrange1.draw(window)
    glwrange2.draw(window)        
    
    ##----------------------------------> LEGEND FOR CLW
    
    clwcmap = IMG.open('/Users/lekshmigopal/clwcmap.png')
    clwcmap = clwcmap.crop((11, 7.3, 363, 29.5))
    clwcmap = clwcmap.resize((271, 16))
    # wid, hgt = tempcmap.size 
    # print(str(wid) + "x" + str(hgt))
    clwcmap.save('clwcmapresize.gif')
    clwcmap=Image(Point(top_left_x/2 +200,740), "clwcmapresize.gif")
    clwcmap.draw(window)       
    
    cmapclw = Text(Point(top_left_x/2,740),"Cloud")
    cmapclw.setSize(10)
    cmapclw.draw(window)    
    
    # clwrange1=Text(Point(top_left_x/2 +78,680),"310W/m^2")
    # clwrange2=Text(Point(top_left_x/2 +322,680),"380W/m^2)
    # clwrange1.setSize(10)
    # clwrange2.setSize(10)
    # clwrange1.draw(window)
    # clwrange2.draw(window)        
    ##--------------------------- LENGEND FOR AIR PRESSURE
    
    airpcmap = IMG.open('/Users/lekshmigopal/airpressurecmap.png')
    airpcmap=airpcmap.crop((11, 7.3, 363, 29.5))
    airpcmap=airpcmap.resize((271, 16))
    airpcmap.save('airpressurecmapresize.png')
    airpcmap=Image(Point(top_left_x/2 + 200,770),'airpressurecmapresize.png')
    airpcmap.draw(window)
    
    cmapairp = Text(Point(top_left_x/2,770),"AirPressure")
    cmapairp.setSize(10)
    cmapairp.draw(window)    
    
    airprange1=Text(Point(top_left_x/2 +83,770),"0 hPa")
    airprange2=Text(Point(top_left_x/2 +308,770),"120 hPa")
    airprange1.setSize(10)
    airprange2.setSize(10)
    airprange1.setFill("mintcream")
    airprange1.draw(window)
    airprange2.draw(window)  
    ##--------------------------- LENGEND FOR WIND SPEED
    
    wvcmap = IMG.open('/Users/lekshmigopal/wvcmap.png')
    wvcmap=wvcmap.crop((11, 7.3, 363, 29.5))
    wvcmap=wvcmap.resize((271, 16))
    wvcmap.save('windspeedcmapresize.png')
    wvcmap=Image(Point(top_left_x/2 + 200,800),'windspeedcmapresize.png')
    wvcmap.draw(window)
    
    cmapwv = Text(Point(top_left_x/2,800),"Wind Speed")
    cmapwv.setSize(10)
    cmapwv.draw(window)    
    
    wvrange1=Text(Point(top_left_x/2 +87,800),"0 knots")
    wvrange2=Text(Point(top_left_x/2 +308,800),"30 knots")
    wvrange1.setSize(10)
    wvrange2.setSize(10)
    wvrange1.setFill("mintcream")
    wvrange1.draw(window)
    wvrange2.draw(window)  
##########Parameters horizontal text labels TIME HOURS TEXT


    for n in range(len(times)):
        now=times[n]      
        tme =Text(Point(top_left_x +0.5*width + (n)*1.2*width , top_left_y -10),now)
        tme.draw(window)
    
    ######### time text for model ############
    
    xcoord=top_left_x +0.5*width + (n)*1.2*width
    #print("xcoord is",xcoord)
    
    for n1 in range(len(masterdfmodel.iloc[:,0])):
        now2=masterdfmodel.iloc[n1,0]
        tme2=Text(Point(xcoord + 20 +0.5*width + n1*1.2*width,top_left_y -10),'{:02}'.format(now2))
        tme2.draw(window)
    
    
    #  TIME TEXT
    
    cld=Text(Point(top_left_x/2,top_left_y +0.5*height),"Darkness")
    #cld.setTextColor("cyan")
    hmd=Text(Point(top_left_x/2,top_left_y+2*height),"Temperature")
    transp=Text(Point(top_left_x/2,top_left_y+3.5*height),"Rel.Humidity")
    glwtext=Text(Point(top_left_x/2,top_left_y+5*height),"Ground Radiation")
    clwtext=Text(Point(top_left_x/2,top_left_y+6.5*height),"Cloud")
    airtext=Text(Point(top_left_x/2,top_left_y+8*height),"Air Pressure")
    darkness=Text(Point(top_left_x/2,top_left_y+9.5*height),"Wind Speed")
    winddirection=Text(Point(top_left_x/2,top_left_y+11*height),"Wind Direction")
    # emerging=Text(Point(top_left_x/2,top_left_y+12*height),"(Emerging)")
    
    cld.draw(window)
    hmd.draw(window)
    transp.draw(window)
    glwtext.draw(window)
    clwtext.draw(window)
    airtext.draw(window)
    darkness.draw(window)
    winddirection.draw(window)
    # emerging.draw(window)
    


    
    ## FOR DARKNESS ROW
       
    for r in range(num_rows):
        y = top_left_y+r*1.5*height
        
            
        for i in range(num_columns):
            x = top_left_x +i*1.2*width
            
        
            top_left_point = Point(x,y)
            bottom_right_point = Point(x + width, y + height)      
            enclosing_rectangle = Rectangle(top_left_point, bottom_right_point)               
            enclosing_rectangle.setFill(time[i])
            enclosing_rectangle.draw(window)
            
    ######Text identifying wx times and then model times 
    
    wxtext=Text(Point((xcoord-top_left_x), top_left_y-30),"Live data from Weather station")
    wxtext.setTextColor("forestgreen")
    wxtext.draw(window)
    
    mdtext=Text(Point((xcoord +150),top_left_y-30),"Predicted Conditions (WRF met. model)")
    mdtext.setTextColor("blue")
    mdtext.draw(window)
    
    redline=Rectangle(Point(xcoord +14,top_left_y -40),Point(xcoord +15,top_left_y +200))
    redline.setOutline("red")

    redline.draw(window)  
    
    
    top_left_x2=top_left_x + len(masterdf.iloc[:,0])*1.2*width+9        
            
    ## FOR DARKNESS ROW FOR MODEL DATA
    
    for r2 in range(num_rows):
        y2=top_left_y+r2*1.5*height
        
        
        for i2 in range(num_columns2):
            
            x2=top_left_x2 +i2*1.2*width
            
            top_left_point=Point(x2,y2)
            bottom_right_point=Point(x2+width,y2+height)
            enclosing_rectangle = Rectangle(top_left_point, bottom_right_point)               
            enclosing_rectangle.setFill(timecolors2[i2])
            enclosing_rectangle.draw(window)
            
    #FOR TEMP ROW WX

    for r in range(num_rows):
        y = top_left_y+height+0.5*height
        
            
        for i in range(num_columns):
            x = top_left_x +i*1.2*width
            
        
            top_left_point = Point(x,y)
            bottom_right_point = Point(x + width, y + height)      
            enclosing_rectangle = Rectangle(top_left_point, bottom_right_point)               
            enclosing_rectangle.setFill(tempcolors[i])
            enclosing_rectangle.draw(window)
                  
    ##FOR TEMP ROW FOR MODEL DATA 
    

    
    for r2 in range(num_rows):
        y2=top_left_y+height+0.5*height
        
        
        for i2 in range(num_columns2):
            
            x2=top_left_x2 +i2*1.2*width
            
            top_left_point=Point(x2,y2)
            bottom_right_point=Point(x2+width,y2+height)
            enclosing_rectangle = Rectangle(top_left_point, bottom_right_point)               
            enclosing_rectangle.setFill(tempcolors2[i2])
            enclosing_rectangle.draw(window)
        


    ## FOR VAPOR ROW WX
        
        
    for r in range(num_rows):
        y = top_left_y+height+2*height
            
        for i in range(num_columns):
            x = top_left_x +i*1.2*width
        
            top_left_point = Point(x,y)
            bottom_right_point = Point(x + width, y + height)      
            enclosing_rectangle = Rectangle(top_left_point, bottom_right_point)               
            enclosing_rectangle.setFill(vaporcolors[i])
            enclosing_rectangle.draw(window)
    
    
                
    
    ## WATER VAPOUR FOR MODEL DATA
    
    for r2 in range(num_rows):
        y2=top_left_y+height+2*height
        
        for i2 in range(num_columns2):
            
            x2=top_left_x2 +i2*1.2*width
            
            top_left_point=Point(x2,y2)
            bottom_right_point=Point(x2+width,y2+height)
            enclosing_rectangle = Rectangle(top_left_point, bottom_right_point)               
            enclosing_rectangle.setFill(vaporcolors2[i2])
            enclosing_rectangle.draw(window)
    
            
        
    ## FOR RADIATION ROW WX
        
        
    for r in range(num_rows):
        y = top_left_y+height+3.5*height
            
        for i in range(num_columns):
            x = top_left_x +i*1.2*width
        
            top_left_point = Point(x,y)
            bottom_right_point = Point(x + width, y + height)      
            enclosing_rectangle = Rectangle(top_left_point, bottom_right_point)               
            enclosing_rectangle.setFill(radflux[i])
            enclosing_rectangle.draw(window)
    
                
    
    ## FOR GLW FOR MODEL DATA
    for r2 in range(num_rows):
        y2=top_left_y+height+3.5*height
        
        for i2 in range(num_columns2):
            
            x2=top_left_x2 +i2*1.2*width
            
            top_left_point=Point(x2,y2)
            bottom_right_point=Point(x2+width,y2+height)
            enclosing_rectangle = Rectangle(top_left_point, bottom_right_point)               
            enclosing_rectangle.setFill(radflux2[i2])
            enclosing_rectangle.draw(window)
                
    ## FOR CLW FOR MODEL DATA
    
    for r2 in range(num_rows):
        y2=top_left_y+height+5*height
        
        for i2 in range(num_columns2):
            
            x2=top_left_x2 +i2*1.2*width
            
            top_left_point=Point(x2,y2)
            bottom_right_point=Point(x2+width,y2+height)
            enclosing_rectangle = Rectangle(top_left_point, bottom_right_point)               
            enclosing_rectangle.setFill(cloud2[i2])
            enclosing_rectangle.draw(window)
 
    ## FOR AIR PRESSURE FOR WX DATA
    for r in range(num_rows):
        y = top_left_y+5*(height+0.5*height)
            
        for i in range(num_columns):
            x = top_left_x +i*1.2*width
        
            top_left_point = Point(x,y)
            bottom_right_point = Point(x + width, y + height)      
            enclosing_rectangle = Rectangle(top_left_point, bottom_right_point)               
            enclosing_rectangle.setFill(aircolors[i])
            enclosing_rectangle.draw(window)
    
    ## FOR AIR PRESSURE FOR MODEL DATA
    
    for r2 in range(num_rows):
        y2=top_left_y+height+6.5*height
        
        for i2 in range(num_columns2):
            
            x2=top_left_x2 +i2*1.2*width
            
            top_left_point=Point(x2,y2)
            bottom_right_point=Point(x2+width,y2+height)
            enclosing_rectangle = Rectangle(top_left_point, bottom_right_point)               
            enclosing_rectangle.setFill(airpressure2[i2])
            enclosing_rectangle.draw(window)
            
    ### FOR WVC ROW WX
    
    for r in range(num_rows):
        y = top_left_y+6*(height+0.5*height)
        
            
        for i in range(num_columns):
            x = top_left_x +i*1.2*width
        
            top_left_point = Point(x,y)
            bottom_right_point = Point(x + width, y + height)      
            enclosing_rectangle = Rectangle(top_left_point, bottom_right_point)               
            enclosing_rectangle.setFill(wvcolors[i])
            enclosing_rectangle.draw(window)
    

    ### FOR WVC FOR MODEL DATA 
    
    
    for r2 in range(num_rows):
        y2=top_left_y+height+8*height
        
        
        for i2 in range(num_columns2):
            
            x2=top_left_x2 +i2*1.2*width
            
            top_left_point=Point(x2,y2)
            bottom_right_point=Point(x2+width,y2+height)
            enclosing_rectangle = Rectangle(top_left_point, bottom_right_point)               
            enclosing_rectangle.setFill(wvcolors2[i2])
            enclosing_rectangle.draw(window)
        
    ### FOR WINDDIR IN MODEL DATA 
    
    # print("betadir is", betadir) 
    # print("thetadir is", thetadir)
    
    for r2 in range(num_rows):
        y2=top_left_y+height+9.5*height +height ## top left y
        for i2 in range(num_columns2):
                
            wvccolumn=np.array(masterdfmodel.iloc[:,3])
            print(wvccolumn)
            mag=wvccolumn[i2]
            print("mag is",mag)
            mag=(mag-10)*(16/12)
            x2=top_left_x2 +i2*1.2*width  ## top left x       
            top_left_point=Point(x2,y2)
            bottom_right_point=Point(x2+width,y2+height)
                       
            if (math.pi)<(thetadir[i2])<=1.5*(math.pi): ## 1st quadrant SW wind 
                x_1=x2
                x_2=x_1 + mag*math.cos(betadir[i2])
                y_1 = y2+height
                y_2=y_1 - (math.sin(betadir[i2]))*mag                  
                # print("y2 is in 1st and is",y_2)
            if (math.pi)*0.5<thetadir[i2]<=(math.pi): ## 2nd quadrant SE wind
                x_1=x2 + width
                x_2=x_1 - mag*math.cos(betadir[i2]) 
                y_1=y2+height
                y_2=y_1 - (math.sin(betadir[i2]))*mag
                # print("y2 is in 2nd and is",y_2)
            if 0<thetadir[i2]<=(math.pi)*0.5: #or 2*math.pi<thetadir[i2]<=2.5*math.pi: ## 3rd quadrant 
                x_1=x2+width 
                x_2=x_1-mag*math.cos(betadir[i2])
                y_1=y2
                y_2=(math.sin(betadir[i2]))*mag + y_1
                # print("y2 is in 3rd and is",y_2)
            if (math.pi)*1.5<thetadir[i2]<=(math.pi)*2:
                x_1=x2
                x_2=x_1 + mag*math.cos(betadir[i2])
                y_1=y2
                y_2=(math.sin(betadir[i2]))*mag + y_1
                # print("y2 is in 4th and is",y_2)    
                    
            #     print("y2 is ",y_2)
                
            # print("x1,y1", x_1,y_1)
            # print("x2,y2",x_2,y_2)
             
            line1=Line(Point(x_1,y_1),Point(x_2,y_2))
            line1.setArrow("last")
            line1.draw(window)


     

    window.postscript(file = (f'WX {datetime.date.today()}'))
    psimage=IMG.open(f'WX {datetime.date.today()}')
    psimage.save(f'WX {datetime.date.today()}.png',quality=95)
    window.getMouse()
    window.close()
    

main()


