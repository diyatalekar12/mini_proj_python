import random
alpha=int(input("How many alphabets do you want in your password? : "))
num=int(input("How many numbers do you want in your password? : "))
sym=int(input("How many symbols do you wantin your password? : "))
alphabet_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number_list=[0,1,2,3,4,5,6,7,8,9]
symbol_list=["!","@","#","$","%","^","&","*",":","~"]
password_list=[]

for i in range(alpha):
    password_list.append(random.choice(alphabet_list))

for i in range(num):
    password_list.append(str(random.choice(number_list)))

for i in range(sym):
    password_list.append(random.choice(symbol_list))

print(f"Your Generated password is {password_list}")
