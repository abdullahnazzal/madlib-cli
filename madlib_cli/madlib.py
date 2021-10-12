import re

def read_file(path):
    with open(path) as file:
        text=file.read()
        stripped_text=text.strip()
    return stripped_text

def parse_file(string):
    spilt_file_list=re.findall(r"\{(.*?)\}",string)
    # print(spilt_file_list)
    spilt_string=re.sub(r"\{(.*?)\}","{}",string)
    # print(spilt_string)
    return spilt_file_list,spilt_string

def merge_file(bare_string,reg):
    return str(bare_string).format(*reg)


if __name__=="__main__":
    print("Welcome To My Madlib Game")
    print("In this Game you will insert some word.")
    string=read_file('assets/dark_and_stormy_night_template.txt')
    user_input=[]
    bare_string,word_list=parse_file(string)
    # print(word_list)
    # print(word_list)
    for word in bare_string:
        u_input=input(f"Give me a {word} >")
        user_input.append(u_input)

    print(user_input)
    print(merge_file(bare_string,user_input))
    merge_file(bare_string,user_input)






