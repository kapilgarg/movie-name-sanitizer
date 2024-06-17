import re
import csv

def generate_test_train_data(): 
    output=[]
    with open("data.csv") as f:
        data = csv.reader(f, delimiter=',')
        for line in data:            
            filename, moviename = line[0],line[1]
            filename = filename.lower().replace("."," ")
            moviename = moviename.lower().replace("."," ").replace("\n","")
            try:
                idx = filename.index(moviename)        
                start, end = idx, idx+len(moviename)
                match = re.search(" \d{4} |\(\d{4}\)", filename)
                if match:
                    span = match.span()[0]+1, match.span()[1]-1    
                entities = [(start,end,'movie')]
                if match:
                    entities.append((span[0],span[1],'year'))
                output.append((filename,dict(entities=entities)))       
            except:
                print("Error",moviename)
    l = len(output)
    return output[:l//2], output[l//2:]