import re
def read_template(file_path:str)->str:
    try:
     with open (file_path) as file:
        content=file.read()
        return content.strip()
    except:
         print(file_path)
         raise FileNotFoundError

