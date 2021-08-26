#import Packages

import json

import string



#---------------functions-------------------

def read_json():

    with open('./recipes.json') as f:  

        data = json.load(f)

    listofindex=[]

    for i in range(len(data)):

        if len(data[i])==0:

            listofindex.append(i)

    for i in listofindex:

        data.pop(i)

    return data

json_data=read_json()



def removalsymbol():

    punctuation_data = string.punctuation

    digit_data=string.digits

    total_removal_char=punctuation_data+digit_data

    return total_removal_char



def removePunctutation(json_data_str):

    unwantedsym=removalsymbol()

    for i in unwantedsym:

        json_data_str=json_data_str.replace(i,' ')

    return json_data_str



def tokenistions(json_data_str):

    token_array=json_data_str.split()

    remove_data=[]

    for i in range(len(token_array)):

        token_array[i]=token_array[i].lower()

        if len(token_array[i]) < 3:

            remove_data.append(token_array[i])

    for i in remove_data:

        token_array.remove(i)

    return token_array



def getDataFromJsonNew(index,typed):

    data=[]

    try:

        a=removePunctutation(str(json_data[index][typed]))  

        data=tokenistions(a)

    except:

        data=[0]

    return data





rating=[]



for i in range(len(json_data)):

    try:

        rating.append(json_data[i]['rating'])

    except:

        rating.append(0)



def search(query, ordering, count):     

    query = str(query).lower()          
    query=removePunctutation(query)
    

    ordering = str(ordering).lower()    

    count = int(count)                  

    q_array=tokenistions(query)

    q_array=list(map(lambda x:x.lower(),q_array))

    matchResult=[]

    for i in range(len(json_data)):

        k=0

        title=getDataFromJsonNew(i,"title")

        categories=getDataFromJsonNew(i,'categories')

        ingredients=getDataFromJsonNew(i,'ingredients')

        directions=getDataFromJsonNew(i,"directions")

        for j in range(len(q_array)):

            if q_array[k] in title:

                k=k+1

            elif q_array[k] in categories:

                k=k+1

            elif q_array[k] in ingredients:

                k=k+1

            elif q_array[k] in directions:

                k=k+1

            if k==len(q_array):

                matchResult.append(i)

                break

    if len(matchResult)==0:

        pass

        

    else:

        if ordering=="normal":

            normalOrdering(query,count,matchResult)

        elif ordering=="simple":

            simpleOrdering(count,matchResult)

        elif ordering=="healthy":

            healthyOrdering(count,matchResult)



def normalOrdering(query,count,matchResult):

    a=removePunctutation(query)

    q_array=tokenistions(a)

    score=0

    scoreList=[]

    matchResult.sort(reverse=False)

    for i in matchResult:

        k=0

        score=0

        title=getDataFromJsonNew(i,"title")

        categories=getDataFromJsonNew(i,'categories')

        ingredients=getDataFromJsonNew(i,'ingredients')

        directions=getDataFromJsonNew(i,"directions")

        for k in range(len(q_array)):

            ct=title.count(q_array[k])

            cc=categories.count(q_array[k])

            ci=ingredients.count(q_array[k])

            cd=directions.count(q_array[k])

            score=score+ 8*ct+ 4*cc+2*ci+cd

              # print(ct,cc,ci,cd,rating[i],q_array[k])

        scoreList.append(float(score)+float(rating[i]))

    topsearch = []
    if len(scoreList)==0:
        print("No Recipes Found")
        
    if len(scoreList) != 0:

        length = min(count, len(scoreList))             

        for i in range(length):                          

            maxx = max(scoreList)

            ind = scoreList.index(maxx)

            topsearch.append(ind)

            scoreList[ind] = 0

        for r in topsearch:

            print(json_data[matchResult[r]]['title'])
    else:
        print("No Recipes Found")



def simpleOrdering(count,matchResult):

    scoreList=[]

    for i in matchResult:

        if len(json_data[i]["ingredients"]) > 1 and len(json_data[i]["directions"]) > 1:    

            score = len(json_data[i]["ingredients"]) * len(json_data[i]["directions"])      

        else:                                                                              

            score = 1000000                                                                 

        scoreList.append(score)

    printResultmin(count,scoreList,matchResult)



def healthyOrdering(count,matchResult):

    emptyindex=[]

    for i in matchResult:

        try:

            (json_data[i]['fat'],json_data[i]['protein'],json_data[i]['calories'])

            if json_data[i]['fat']>0 and json_data[i]['protein']>0 and json_data[i]['calories']>0:

                pass

            else:

                emptyindex.append(i)

        except:

            emptyindex.append(i)



    emptyindex=set(emptyindex)

    emptyindex=list(emptyindex)



    scoreList=[]

    for i in matchResult:

        if i not in emptyindex:

            n=1

            calval=abs((json_data[i]['calories']-510*n)/510)

            proval=2*abs((json_data[i]['protein']-18*n)/18)

            fatval=4*abs((json_data[i]['fat']-150*n)/150)

            score=calval+proval+fatval

            scoreList.append(score)

    for i in emptyindex:

        if i in matchResult:

            matchResult.remove(i)

    printResultmin(count,scoreList,matchResult)



def printResultmin(count,scoreList,matchResult):

    topsearch=[]
    if len(scoreList)==0:
        print("No Recipes Found")
        
    if len(scoreList)!=0:

        length = min(count,len(scoreList))

        for i in range(length):

            minn=min(scoreList)

            ind=scoreList.index(minn)

            topsearch.append(ind)

            scoreList[ind]=1000000

        for r in topsearch:

            print(json_data[matchResult[r]]['title'])

        


def getRecipe(name):
    name = name.strip()+" "
    found = False
    loc = -1
    for i in range(len(json_data)):
        if(json_data[i]['title']==name):
            loc = i;
            found = True
            break;
    if(loc!=-1 and found):
        print("Title : ",json_data[loc]['title'])
        print("\nCATEGORIES : ")
        for i in range(len(json_data[loc]['categories'])):
            print((i+1),". ",json_data[loc]['categories'][i],end = "  ")
        print("\nINGREDIENTS : ")
        for i in range(len(json_data[loc]['ingredients'])):
            print((i+1),". ",json_data[loc]['ingredients'][i])
        print("\nDIRECTIONS : ")
        for i in range(len(json_data[loc]['directions'])):
            print((i+1),". ",json_data[loc]['directions'][i])

    else:
        print("Recipe Not Found")
