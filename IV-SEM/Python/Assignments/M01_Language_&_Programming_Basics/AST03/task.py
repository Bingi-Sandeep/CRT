def Student_Grade_System(name:str,n1: int,n2: int,n3: int) -> str:
   avg = (n1 + n2 + n3) / 3

   avg = int(avg * 100) / 100

   if avg >= 35:
    return f"Average grade: {avg}, Status: Pass"
   else:

    return f"Average grade: {avg}, Status: fail"    
    
if __name__ == '__main__':
    name = input()
    n1,n2,n3 = list(map(int,input().split()))
    print(Student_Grade_System(name,n1,n2,n3))