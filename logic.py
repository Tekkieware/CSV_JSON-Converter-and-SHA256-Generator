import csv, json, hashlib, os

#appending the file part to the name provided
input_file_path = 'Input CSV File/'
input_file_name = 'NFT Naming csv - All Teams.csv'
input_file = input_file_path + input_file_name


def logic(input_file):
    #reading the input csv file
    with open(input_file, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
    #looping through each row in the csv file
        for row in reader:
            #name and path to the output json for each row
            json_file_name = row['Filename']
            json_file_path = 'Output JSON Files/'
            #creating a json file for each row in the csv file
            with open((json_file_path + json_file_name + '.json'), 'w', encoding='utf-8') as jsonfile:
                jsonfile.write(json.dumps(row, indent=4))
            #generating the sha256 for each json file
            full_file_path = json_file_path + json_file_name + '.json'
            sha256 = hashlib.sha256(open(full_file_path, 'rb').read()).hexdigest()
            #reading each json file data
            file = open(full_file_path, 'r')
            data = json.load(file)
            hash_data = {'Sha256': sha256}
            data.update(hash_data)
            file.close()
            #appending the sha256 to each file
            file = open(full_file_path, 'w')
            file.write(json.dumps(data, indent=4))
            file.close()

                
            
                
            


logic(input_file)