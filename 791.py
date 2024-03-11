
def customSortString( order: str, s: str) -> str:
    p1 ,p2 = 0,0
    result=[]
    final_result =""
    order_list = list(order)
    s_list = list(s)
    while p1 < len(order_list) and p2 < len(s_list):
        if order_list[p1] in s_list :
            result.append(order_list[p1])
            s_list.pop(s_list.index(order_list[p1]))
            s_list.append("")
            p1= p1+1
            p2=p2+1
    for i in result:
        final_result = final_result+i
    for i in s_list:
        if i !="":
            final_result = final_result+i
    return result
    
print(customSortString("cba","abcd" ))
            