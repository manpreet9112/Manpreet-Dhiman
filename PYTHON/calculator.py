choice=0
print("1) Addition")
print "2) Subtraction"
print("3) Multiply")
print("4) Divide")
print(" ")
print(" enter your choice") 
choice = input(" choose any operation")
if choice == 1:
   n1=input("enter number1")
   n2=input("enter number2")
   add=n1+n2
   print "addition is=", add
  
elif choice == 2:
   s1=input("enter number1")
   s2=input("enter number 2")
   sub=s1-s2
   print(" Subtraction is=", sub)
   
elif choice == 3:
   m1=input("enter number 1")
   m2=input(" enter number 2")
   mul= m1-m2
   print(" multiplication =", mul)
elif choice == 4:
  d1=input("enter number1" )
  d2=input("ente number 2")
  divide=d1-d2
  print(" divison is=" ,divide)

