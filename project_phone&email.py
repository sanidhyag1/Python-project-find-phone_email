#TODO: Create a regex for phone numbers
import re, pyperclip
#re.verbose allows multi-line strings in regex
#Indian format of phone-numbers are like +91-123-456-7890 or +911234567890 or 1234567890 or 123-456-7890 , 011-23075184
phoneRegex = re.compile(r'''((\+91)?  #+91 which is supposed to be optional
(-)? #the dash is optional 
(\d\d\d) #The first 3 digits of the number
(-)?  #the dash is optional
(\d\d\d) #the next 3 digits of the number
(-)?  #the dash is optional
(\d\d\d\d)) #the next 4 digits of the number''',re.VERBOSE)

#print(phoneRegex.findall("Let's see if this works first 9424803663, second +919424803663 , third 942-480-3663, and the last pattern that should match +91-942-480-3663"))
#creating another regex for telephone numbers india
telephoneRegex = re.compile(r'''((\d\d\d)? #011 is optional 
(-)? #Optional 
(\d\d\d\d\d\d\d\d)) #the main phone number''', re.VERBOSE)

#TODO: Create a regex for email addresses
# the email can be something@something.something
emailRegex= re.compile(r'''[a-z0-9_.+]+ #Name part of the mail
@ #@ symbol 
[a-z0-9_.+]+# the domain part of the mail ''', re.VERBOSE | re.IGNORECASE)

#print(emailRegex.findall('My mail is sanidhyag1@gmail.com'))

#TODO: Fetch the text off the clipboard
text = pyperclip.paste()

#print(text)

#Extract the email and phone from this text
extractedEmail = emailRegex.findall(text)
extractedPhone = phoneRegex.findall(text)
extractedTelephone = telephoneRegex.findall(text)

allPhoneNumbers = []
for phoneNumbers in extractedPhone:
	allPhoneNumbers.append(phoneNumbers[0]) #findall creates a tuple for a match for every group in the regex, we created a group that covers all the conditions, the group is stored on 0 index

allTelephoneNumbers = []
for telephoneNumbers in extractedPhone:
	allTelephoneNumbers.append(telephoneNumbers[0])

#Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)+ '\n' + '\n'.join(allTelephoneNumbers)
pyperclip.copy(results)

#Now all the phone numbers are stored in your clipboard just paste it in any text editor