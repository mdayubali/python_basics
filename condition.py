# in condition you have to focus on line indentation

password = "mypassword"
cpassword = "mypassword1"
admin = True

if cpassword==password:
    print("password matched")
elif admin:
    print("Admin match, but password don't match")
else:
    print ("Nothing is match")