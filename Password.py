# password = input('Enter new password')
#
# result = []
#
# if len(password) >=8:
#     result.append(True)
# else:
#     result.append(False)
#
# digit = False
# for i in password:
#     if i.isdigit():
#         digit = True
#
# result.append(digit)
#
# uppercase = False
# for i in password:
#     if i.isupper():
#         uppercase = True
#
# result.append(uppercase)
#
# print(result)
#
# if all(result):#all assumes every parameter should be true
#     print("Strong Password")
# else:
#     print('Weak Password')

# #Lesson Optimize using dictionary
# password = input('Enter new password')
#
# result = {}
#
# if len(password) >=8:
#     result["length"] = True
# else:
#     result["length"] = False
#
# digit = False
# for i in password:
#     if i.isdigit():
#         digit = True
#
# result['digits'] = digit
#
# uppercase = False
# for i in password:
#     if i.isupper():
#         uppercase = True
#
# result['upper-case'] = uppercase
#
# print(result)
#
# if all(result.values()):#all assumes every parameter should be true
#     print("Strong Password")
# else:
#     print('Weak Password')
#
# # Example
# password = input('Enter password')
#
# result = []
#
# if len(password) >= 8:
#     print('Great password there!')
# else:
#     print('Your password is weak')

# # Custom function
#
# password = input('Enter password')
#
# def strength(password):
#     result = {}
#
#     if len(password) >= 8:
#         result['length'] = True
#     else:
#         result['length'] = False
#
#     digit = False
#     uppercase = False
#
#     for i in password:
#         if i.isdigit():
#             digit = True
#
#         if i.isupper():
#             uppercase = True
#
#         if all(result.values()):
#
#             return 'Strong Password'
#         else:
#             return 'Weak Password'
#
# password_strength = strength(password)
# print(strength(password))




