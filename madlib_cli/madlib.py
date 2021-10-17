import re

def read_template(path):
    with open(path) as file:
        text=file.read()
        # stripped_text=text.strip()
    return text

def parse_template(string):
    spilt_string=re.sub(r"\{(.*?)\}","{}",string)
    # print(spilt_string)
    spilt_file_list=re.findall(r"\{(.*?)\}",string)
    # print(spilt_file_list)
    return (str(spilt_string),tuple(spilt_file_list))

def merge(bare_string,reg):
    return str(bare_string).format(*reg)


if __name__=="__main__":
    print("Welcome To My Madlib Game")
    print("In this Game you will insert some word.")
    # string=read_template('assets/dark_and_stormy_night_template.txt')
    string=read_template('assets/madlib.txt')
    user_input=[]
    bare_string,word_list=parse_template(string)
    # print(word_list)
    # print(word_list)
    for word in word_list:
        u_input=input(f"Give me a {word} >")
        user_input.append(u_input)

    print(user_input)
    print(merge(bare_string,user_input))
    with open("assets/result.txt","w") as result:
        result.write(merge(bare_string,user_input))
    





