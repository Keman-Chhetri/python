name =input("Enter your name: ")
nep =int(input("Enter nep mark: "))
eng =int(input("Enter eng mark: "))
mat =int(input("Enter mat mark: "))
sci =int(input("Enter sci mark: "))
com =int(input("Enter com mark: "))
total = nep+eng+mat+sci+com
per =total/5
grade=""
if per>35 and per<45:
    grade="C"
elif per>45 and per<60:
    grade="B"
elif per>60 and per<80:
    grade="A"
elif per>80 and per<=100:
    grade="A+"
else:
    grade ="fail"

handle =open("work.txt","a")
handle.write(f"Name:{name} nep:{nep} eng:{eng} mat:{mat} sic:{sci} com:{com} total:{total} percentage:{per} grade: {grade} \n")

handle.close()