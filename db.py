import json
class Mydb:
    def add_data(self,email,name,password):

        with open('db.json','r') as f:
            data = json.load(f)
        if email in data:
            return 0
        else:
            data[email] = [name,password]
            with open('db.json','w') as wf:
                json.dump(data,wf)
            return 1
            
    def check_data(self,email,password):
        with open('db.json','r') as f:
            data = json.load(f)
        
        if email in data:
            if data[email][1] == password:
                return 1
            else:
                return 0
        else:
            return 0

