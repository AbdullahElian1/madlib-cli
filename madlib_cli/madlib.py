import re
def read_template(file_path:str)->str:
    try:
     with open (file_path) as file:
        content=file.read()
        return content.strip()
    except:
         print(file_path)
         raise FileNotFoundError

def parse_template(word:str)->str:
 actual_part=tuple(re.findall(r'{(.*?)}',word))
 actual_stripped=re.sub('{.*?}','{}',word)
 return actual_stripped,actual_part

