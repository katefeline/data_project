import csv

filename = '102-indeksi-realnoyi-zarobitnoyi-plati-za-regionami-do-poperednogo-roku.csv'
with open(filename) as f:
    reader = csv.reader(f)


    # for i in reader: #printing all the tables as list
    #     print(i)

    # for i in reader:  #printing first index of list
    #     index = []
    #     new = i[0]
    #     index.append(new)
    #     print(index)

    # for i in reader: #printing all the tables in readable format
    #     print(', '.join(i))

    # for i in reader: #printing all the tables as list
    #     try:
    #         print(next(reader))
    #     except StopIteration:
    #         continue

