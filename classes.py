def eachcontact(name, number,DOB, email, address):
    list_a = []
    list_a.append(number)
    for i in range(len(list_a)):
        list_a[i] = {list_a[i]:{"name":name,
                                "number":number,
                                "DOB":DOB,
                                "email":email,
                                "address":address}}
    return list_a

