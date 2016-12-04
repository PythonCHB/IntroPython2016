

# exec1
fruit = {}

fruit['names']= 'Chris'
fruit['city']='Seattle'
fruit['cake']= 'Chocolate'

fruit
fruit.pop('cake')
fruit

fruit['fruit'] = 'Mango'

cake_key= 'cake' in fruit.keys() 
print('cake is in keys => ',cake_key)


mango_value = 'Mango' in fruit.values()
print('Mango is in values => ', mango_value)


## exec2
dic_num_key = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
dic_num_value =[0,1,2,3,4,5,6,7,8,9, 'A', 'B', 'C', 'D', 'E', 'F']
dic_num=dict(zip(dic_num_key, dic_num_value))
print (dic_num)



## exec3
fruit_value_list=[]

for place, item in enumerate(fruit.values()):
    item = 'a'+ item
    fruit_value_list.append(item)

fruit_new =dict(zip( list(fruit.keys()), fruit_value_list))
print(fruit.items())
 

# exec4 Set 
set2= set(i for i in range(19) if i%2==0)
set3= set(i for i in range(19) if i%3==0)
set4= set(i for i in range(19) if i%4==0)

print('set2 i%2==0 ==> ', set2)
print('set3 i%3==0 ==> ', set3)
print('set4 i%3==4 ==> ', set4)


# exec5
set1 = set('Python')
set1.add('i')
set2 = frozenset('marathon' )
set3 = set1.union(set2)
set4 = set1.intersection(set2)

print('set1: ', set1)
print('set2: ', set2)
print('set3: ', set3)
print('set4: ', set4)

print('set3 is subset of set2 ?', set3.issubset(set2) )
print('set4 is subset of set2 ?', set4.issubset(set2) )





