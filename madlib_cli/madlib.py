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

def merge(string_text:str,word_to_add:tuple):
    final_text=string_text.format(*word_to_add)
    with open('assets/result.txt','w') as output:
        output.write(final_text)
    return final_text
#teeeeeeeeeeeeest


answer=[]

print("wlcome to midlib game")


def start_game():
    read=read_template("assets/text.txt")
    text,value=parse_template(read)
    for item in value:
        input_user=input(f"enter {item}")
        answer.append(input_user)
    return merge(text,answer)

if __name__== "__main__":
 start_game()

