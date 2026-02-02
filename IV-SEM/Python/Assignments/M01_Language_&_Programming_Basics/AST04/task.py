def Reverse_String(s: str) -> str:
   result = ""
   for i in range(len(s)-1, -1, -1):
       result += s[i]
   return result

if __name__ == '__main__':
    s = input()
    print(Reverse_String(s))