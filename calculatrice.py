def addition (a,b):
    return a+b

def soustraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    if b==0:
        return "Division par zéro impossible!"
    else:
        return a/b
    
a = float(input("Enter the 1st number: "))
b = float(input("Enter the 2nd number: "))
operation = input("Entrez l'opération (+, -, *, /): ")

if operation =="+":
    resulat = addition(a,b)

elif operation =="-":
    resultat = soustraction(a,b)

elif operation =="*":
    resultat = multiplication(a,b)
    
elif operation =="/":
    resultat = division(a,b)

else:
    resultat = "Opération invalide!"

print (f"Le résulat est: {resulat}")