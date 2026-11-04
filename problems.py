import random
import time

opertators = ["+","-","*"]
reply = ["wow,correct answer!","Nice,keep it up!","Good!"]
MIN_OPERENDS = 4
MAX_OPERENDS = 15
re= ["Nice try,try again!","don't give up, you can do it.","Try again."]
MAX_PROBLEMS = 10

def generate():
    left  =  random.randint(MIN_OPERENDS,MAX_OPERENDS)
    right=  random.randint(MIN_OPERENDS,MAX_OPERENDS)
    oper = random.choice(opertators)
    
    exp = str(left) +" " + oper + " "+str(right)
    
    answer  = eval(exp)    
    return exp ,answer

def random_reply():
    re = random.choice(reply)
    return re

def random_re():
    rr = random.choice(re)
    return rr
    
    
start_time = time.time()    
    

input("press enter to start!")

print("========================")    
for i in range(MAX_PROBLEMS):
    exp,answer = generate()
    while True:
        guess =  input("problem #"+ str(i+1)+":" +" "+ exp + "=")
        if guess == str(answer):
            print(random_reply())
            break
        else:
            print(random_re())
            wrong_+=1



end_time =  time.time()
total_time  = end_time - start_time
                     
print("========================")  
print(f"GOOD JOB, You finished in {round(total_time,2)} sec.")
