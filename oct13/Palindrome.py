#user_input = input("Enter the input strings\n")
#Reverse the strings and match with old  strings it should be same
#1 By using Tradintional method
#B built in funcations

def reverse_string(input_string):
    reverse_str =""
    for Char in input_string:
        reverse_str = Char + reverse_str
    return reverse_str#DCBA
original_str ="madam"
rev_str = reverse_string(original_str)
print(rev_str)
if original_str == rev_str:
    print("Plindrome")
else:
    print("It is not Plindrome")