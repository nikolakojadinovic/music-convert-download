import re
yt_regex = re.compile("http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?")
links = []

with open('chat.txt', 'r') as file:
    chat = file.readlines()


for line in chat:
    
    afterSemicolon = list(filter(lambda x: x[1] == ':', enumerate(line)))
    
    if len(afterSemicolon) < 3:
        continue

    startsMsg, _ = afterSemicolon[1]
    rawMsg = line[startsMsg +1:]
    link = yt_regex.search(rawMsg)
    try:
        with open('links.txt', 'a') as out:
            out.write(link.group(0) + '\n')
    except:
        pass 


    

    


        

    

