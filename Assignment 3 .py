def triangle (S1,S2,S3):
              if S1**2+S2**2==S3**2 :
                print("It is a right-angled triangle")
              elif S1**2 + S3**2 == S2**2 :
                print("It is a right-angled triangle")
              elif S2**2 + S3**2 == S2**2 :
                print("It is a right-angled triangle") 
              else :
                print("It is not a right-angled triangle")
S1 =  int(input("Enter the length of first side:")) 
S2 =  int(input("Enter the length of second side:"))   
S3  =  int(input("Enter the length of third side:"))       
triangle (S1,S2,S3)       