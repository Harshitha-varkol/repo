# n=int(input("enter the number:"))
# sum=0
# count=0
# for i in range(1,n+1):
#     sum+=i
#     count+=1
#     total=sum//count
# print(total)    

# arr=[2,3,4,4,5,5,87,99,65,43,90,99,87,76,78,9878,90,3,2,4,3,2]
# count=0
# for i in arr:
#     if i<50:
#         count+=1
# print(count)        


# def sum(arr):
#     count=0
#     for i in arr:
#         if i<50:
#             count+=1
#     return count

# arr=[6,90,87,99,4,6,3]
# result=sum(arr)
# print(result)



# def count(num):
#     count=0
#     while num>0:
#         rem=num%10
#         count+=1
#         num=num//10
#     return count

# num=int(input("enter the number:"))
# result=count(num)
# print(result)    


# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display_info(self):
#         print('the name of the student is',self.name)    
#         print('the agee of the student is',self.age)    
# obj=Student("harsh",22)
# print(obj.display_info())


# class Car:
#     def __init__(self,name,age):
#         self.name=name
#         self.color=age
#     def display_info(self):
#         print('the name of the student is',self.name)    
#         print('the agee of the student is',self.age)    
# obj=Student("toyato","red")
# obj.display_info()


lst=[1,2,4,4,5,5,3,4,3,9,8,7,4,3,2,2]
lst2=[]
lst3=[]
for i in lst:
    if i in lst2 and i not in lst3:
        lst3.append(i)
    else:
        lst2.append(i)    
print(lst3)   



# lst=[5,4,3,5,6,4,2,4,9,0]
# print(set(list(lst)))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
# lst=[5,4,3,5,6,4,2,4,9,0]
# print(list(set(lst)))