import json
import os 
dir_path = os.path.dirname(os.path.realpath("data.json"))
loaded_content = json.load(open(dir_path.replace("/code","/data")+"/data.json"))
print(type(loaded_content))
print(loaded_content)