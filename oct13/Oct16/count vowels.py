#Count vowels and consonants in a String
str1 = input("enter your string\n")
vowels =0
consonants =0
for i in str1:
    if(i == 'a' or i == 'e' or i == 'i' or i== 'o' or i == "A" or i == 'E' or i == 'E' or i =='O' or i == 'U' ):
        vowels =vowels+1
    else:
        consonants =consonants+1
print("Total numer of vowels:",vowels)
print("Total number of consonants:",consonants)
#Create a function with parameter which can do x^y
def cal(x,y):
        z=x^y
        print(z)
cal(4,8)
# Lamba expression to triple power a number
output = lambda value :value**3
print(output(8))
#Right star triangle
