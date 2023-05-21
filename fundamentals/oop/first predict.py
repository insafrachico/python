def countdown(n, list=[]):
    list = list.copy()
    if n >=0 :
         list.append(n)
         return countdown(n-1, list)
     else:
        return list
 result = countdown(5)