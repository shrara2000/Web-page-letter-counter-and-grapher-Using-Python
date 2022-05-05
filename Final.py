from urllib.request import urlopen as url
import matplotlib.pyplot as plt
import re

def countChars(data):
    count=0;
    for i in data:
        count+=1
    print(count)
def countLC(data):
    lclib=dict()
    for i in data:
        if i.isalpha() and i.islower() and i not in lclib.keys():
            lclib[i]=1
        elif i.isalpha() and i.islower() and i in lclib.keys():
            lclib[i]+=1
            S=sum(lclib.values())
    return S
def countUC(data):
    UClib=dict()
    for i in data:
        if i.isalpha() and i.isupper() and i not in UClib.keys():
            UClib[i]=1
        elif i.isalpha() and i.isupper() and i in UClib.keys():
            UClib[i]+=1
            S=sum(UClib.values())
    return S
def countD(data):
    Dlib ={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    for i in data:
        if i.isdigit():
            Dlib[i]+=1
            S=sum(Dlib.values())
    return S
def countHref(Data):
    print (Data.count('href='))
urllink = input("Enter the URL:")
data=url(urllink).read()
D2=str(url(urllink).read())
while(True):
    choice=input(' 0-exit\n 1- Print Lower case upper case and href and digit counts \n 2- pie chart that shows the occurrences of lower letters, upper letters, and digits \n 3- dentify all of the links(i.e. URLs) and emails that may be available in the source \n 4- draw a column chart with the frequency of all letters in that webpage (A-Z and a-z) \n 5- draw a column chart with the frequency of all characters on that webpage \n 6- draw a pie chart with the frequency of digits\n')
    if(choice=='0'):
        break;

    if(choice=='1'):
                 print('Number of lower Case: ')
                 print(countLC(D2))
                 print('Number of Upper Case: ')
                 print(countUC(D2))
                 print('Number of Digits: ')
                 print(countD(D2))
                 print('Number of href: ')
                 countHref(D2)
    elif(choice=='2'):
        my_labels = 'Lower Case','Upper Case','Digits'
        Tasks=[countLC(D2),countUC(D2),countD(D2)]
        plt.pie(Tasks,labels=my_labels,autopct='%1.1f%%')
        plt.title('Q2')
        plt.axis('equal')
        plt.show()
    elif(choice=='3'):
        
        
        emails =  re.findall(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', D2)
        links  = re.findall(r'(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?', D2)
       
        print("The emails in the reference url : ", emails)
        
        print("The Links in the reference url : ", links)
      

    elif (choice=='4') :
           UClib=dict()
           for i in D2:
               if i.isalpha() and i.upper() not in UClib.keys():
                   UClib[i.upper()]=1
               elif i.isalpha() and i.upper() in UClib.keys():
                   UClib[i.upper()]+=1
           plt.bar(UClib.keys(), UClib.values())
           plt.show()
    elif (choice=='5'):
         Clib=dict()
         for i in D2:
             if i not in Clib.keys():
                 Clib[i]=1
             if i in Clib.keys():
                 Clib[i]+=1
         plt.bar(Clib.keys(), Clib.values())
         plt.show()
    elif (choice=='6'):
        Dlib ={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
        for i in D2:
            if i.isdigit():
                Dlib[i]+=1
        my_labels = Dlib.keys()
        Tasks=Dlib.values()
        plt.pie(Tasks,labels=my_labels,autopct='%1.1f%%')
        plt.title('Q6')
        plt.axis('equal')
        plt.show()
        
            
        

        

        
       
     
                 
                 
                 
                 
                 
             

