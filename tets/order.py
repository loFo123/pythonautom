import sys

list1 = sys.argv[1]
list2 = sys.argv[2]

olist1 = list1.split()
olist2 = list2.split()
list=[]
# print(list2)
for element in olist1:
    if(olist2.__contains__(element)):
        # print("present")
        continue
    else:
        # print(element)
        sys.stdout.write(element+" ")
        list.append(element)


# print(list)
