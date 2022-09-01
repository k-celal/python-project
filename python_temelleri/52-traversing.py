with open("newfile.txt","r",encoding="utf-8") as file:
    content = file.read(10)
    print(content)
    file.seek(0)#kursörü istediğimiz konuma gönderir
    print(file.tell())#kursörün nerede olduğunu söyler
    content2 = file.read(10)
    print(content2)