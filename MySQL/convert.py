import json

#  create person.del
data = json.load(open("/home/cs143/data/nobel-laureates.json", "r"))
file = open('person.del', 'w', encoding = 'utf-8')
for i in range(len(data["laureates"])):
    laureate = data["laureates"][i]
    laureate_keys = list(laureate.keys())
    if laureate_keys[1] == "knownName":
        laureate_id = laureate["id"]
        givenName = laureate["givenName"]["en"]
        if laureate_keys[3] == "familyName":
            familyName = laureate["familyName"]["en"]
        else:
            familyName = '\\N'
        gender = laureate["gender"]
        if "birth" in laureate_keys:
            birth = laureate["birth"]
            birth_keys = list(birth.keys())
            if "date" in birth_keys:
                dob = laureate["birth"]["date"]
            else:
                dob = '\\N'
            birthplace = laureate["birth"]["place"]
            birthplace_keys = list(birthplace.keys())
            if "city" in birthplace_keys:
                city = laureate["birth"]["place"]["city"]["en"]
                country = laureate["birth"]["place"]["country"]["en"]
            else:
                city = '\\N'
                country = '\\N'
        laureate_dict = {'id':laureate_id, 'givenName':givenName, 'familyName':familyName, 'gender':gender, 'dob':dob, 'city':city, 'country':country}
        file.write('"'+laureate_dict['id']+'"' + ',' + '"'+laureate_dict['givenName']+'"' + ','+ '"'+laureate_dict['familyName']+'"' + ',' + '"'+laureate_dict['gender'] +'"'+ ',' + '"'+laureate_dict['dob']+'"' + ',' + '"'+laureate_dict['city'] +'"'+ ',' + '"'+laureate_dict['country'] +'"'+ '\n')
        
# create org.del

data = json.load(open("/home/cs143/data/nobel-laureates.json", "r"))
file = open('org.del', 'w', encoding = 'utf-8')
for i in range(len(data["laureates"])):
    laureate = data["laureates"][i]
    laureate_keys = list(laureate.keys())
    if laureate_keys[1] == "orgName":
        laureate_id = laureate["id"]
        orgName = laureate["orgName"]["en"]
        if "founded" in laureate_keys:
            founded = laureate["founded"]
            founded_keys = list(founded.keys())
            if "date" in founded_keys:
                date = laureate["founded"]["date"]
            else:
                date = '\\N'
            if "place" in founded_keys:
                foundedplace = laureate["founded"]["place"]
                foundedplace_keys = list(foundedplace.keys())
                if "city" in foundedplace_keys:
                    city = laureate["founded"]["place"]["city"]["en"]
                else:
                    city = '\\N';
                if "country" in foundedplace_keys:
                    country = laureate["founded"]["place"]["country"]["en"]
                else:
                    country = '\\N';
        laureate_dict = {'id':laureate_id, 'orgName':orgName, 'date':date, 'city':city, 'country':country}
        file.write('"'+laureate_dict['id']+'"' + ',' +'"'+ laureate_dict['orgName']+'"' + ','+ '"'+laureate_dict['date']+'"' + ',' + '"'+laureate_dict['city'] +'"'+ ',' +'"'+ laureate_dict['country'] +'"'+ '\n')
        
# create award.del
data = json.load(open("/home/cs143/data/nobel-laureates.json", "r"))
file = open('award.del', 'w', encoding = 'utf-8')
for i in range(len(data["laureates"])):
    laureate = data["laureates"][i]
    laureate_id = laureate["id"]
    if len(laureate["nobelPrizes"]) == 1:
        awardYear = laureate["nobelPrizes"][0]["awardYear"]
        category = laureate["nobelPrizes"][0]["category"]["en"]
        sortOrder = laureate["nobelPrizes"][0]["sortOrder"]
        laureate_dict = {'id':laureate_id, 'awardYear':awardYear, 'category':category, 'sortOrder':sortOrder}
        file.write('"'+laureate_dict['id']+'"' + ',' +'"'+ laureate_dict['awardYear'] +'"'+ ','+'"'+ laureate_dict['category']+'"' + ',' +'"'+ laureate_dict['sortOrder'] +'"'+ '\n')
    else:
        for j in range(len(laureate["nobelPrizes"])):
            awardYear = laureate["nobelPrizes"][j]["awardYear"]
            category = laureate["nobelPrizes"][j]["category"]["en"]
            sortOrder = laureate["nobelPrizes"][j]["sortOrder"]
            laureate_dict = {'id':laureate_id, 'awardYear':awardYear, 'category':category, 'sortOrder':sortOrder}
            file.write('"'+laureate_dict['id']+'"' + ',' +'"'+ laureate_dict['awardYear']+'"' + ','+ '"'+laureate_dict['category']+'"' + ',' + '"'+laureate_dict['sortOrder']+'"' + '\n')
            
# # create affiliations.del

data = json.load(open("/home/cs143/data/nobel-laureates.json", "r"))
file = open('affiliations.del', 'w', encoding = 'utf-8')
for i in range(len(data["laureates"])):
        laureate = data["laureates"][i]
        laureate_id = laureate["id"]
        if len(laureate["nobelPrizes"]) == 1:
            if "affiliations" in laureate["nobelPrizes"][0]:
                name = laureate["nobelPrizes"][0]["affiliations"][0]["name"]["en"]
                if "city" in laureate["nobelPrizes"][0]["affiliations"][0]:
                    city = laureate["nobelPrizes"][0]["affiliations"][0]["city"]["en"]
                else:
                    city = '\\N'
                if "country" in laureate["nobelPrizes"][0]["affiliations"][0]:
                    country = laureate["nobelPrizes"][0]["affiliations"][0]["country"]["en"]
                else:
                    country = '\\N'
                laureate_dict = {'id':laureate_id, 'name':name, 'city':city, 'country':country}
                file.write('"'+laureate_dict['id']+'"' + ',' +'"'+ laureate_dict['name']+'"' + ','+ '"'+laureate_dict['city'] +'"'+ ',' + '"'+laureate_dict['country']+'"' + '\n')
        else:
            for j in range(len(laureate["nobelPrizes"])):
                if "affiliations" in laureate["nobelPrizes"][j]:
                    name = laureate["nobelPrizes"][j]["affiliations"][0]["name"]["en"]
                    if "city" in laureate["nobelPrizes"][j]["affiliations"][0]:
                        city = laureate["nobelPrizes"][j]["affiliations"][0]["city"]["en"]
                    else:
                        city = '\\N'
                    if "country" in laureate["nobelPrizes"][j]["affiliations"][0]:
                        country = laureate["nobelPrizes"][j]["affiliations"][0]["country"]["en"]
                    else:
                        country = '\\N'
                    laureate_dict = {'id':laureate_id, 'name':name, 'city':city, 'country':country}
                    file.write('"'+laureate_dict['id']+'"' + ',' +'"'+ laureate_dict['name']+'"' + ','+ '"'+laureate_dict['city'] +'"'+ ',' + '"'+laureate_dict['country']+'"' + '\n')
      
    

