import random
base_pass=["a","b","c","d","e","f","g","h","i","j","k"
       ,"l","m","n","o","p","q","r","s","U","V","W","X","Y","Z"
       ,"1","2","3","4","5","6","7","8","9","0","!","@","#","$","^","&","*","(",")"]
password = ""
for x in range(int(input("Enter your password range: "))):
    password = password + random.choices(base_pass)[0]

print("Your password is:\n",password)