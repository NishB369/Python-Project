print("Login Page")
p1=input("Enter your first password: ")
p2=input("Enter your second password: ")
p3=input("Enter your third password: ")
u_name=input("Enter your username: ")
p=input("Enter new password: ")
print('-'*50)



def length(s):
    if len(s)>=10:
        return 1
    else:
        print(f"The required length is atleast 10 character, add {10-len(s)} or more characters.")
        return 0

def case(s):
    uc=0
    lc=0
    dc=0
    sc=0
    for i in s:
        if i.isalpha():
            if i.isupper():
                uc+=1
            else:
                lc+=1
        elif i.isdigit():
            dc+=1
        else:
            sc+=1
     
    errors = []
    if uc < 2:
        errors.append(f"Add {2 - uc} Upper case character(s)")
    if lc < 2:
        errors.append(f"Add {2 - lc} Lower case character(s)")
    if dc < 2:
        errors.append(f"Add {2 - dc} Digit(s)")
    if sc < 2:
        errors.append(f"Add {2 - sc} Special case character(s)")

    if errors:
        print("\n".join(errors))
        return 0
    else:
        return 1
        

def passwd(s1,s2,s3,s):
    if s in [s1,s2,s3]:
        print(f"Your current password matches one of your earlier passwords: {s}")
        return 0
    else:
        return 1
    
def continuous(s):
    flag=1
    for i in range(len(s) - 3):          
        if s[i:i+4] == s[i]*4:
            flag=0
    if flag==0:
        print("There should not be more than 3 continuous characters")
        return 0
    else:
        return 1

def from_u_name(u, s):
    for i in range(len(u) - 2):
        substring = u[i:i+3]
        if substring in s:
            print("Sequence of 3 or more continuous characters of username is used in password")
            return 0
    return 1

while True:
    f1=length(p)
    f2=case(p)
    f3=passwd(p1,p2,p3,p)
    f4=continuous(p)
    f5=from_u_name(u_name,p)

    if f1+f2+f3+f4+f5!=5:
        p=input("Enter new password: ")
        print('-'*50)
    else:
        print("Strong Password")
        break
    

