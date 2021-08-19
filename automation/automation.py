import re

path = "assets/potential-contacts.txt"
with open( path, 'r') as file:
    content = file.read()

# print(file_content)

#########################################################################

def get_email_from_text( content ):
    
    find_email = re.findall( r"[\w.+-]+@[\w-]+\.[\w.-]+", content )
    
    all_email = []
    
    for email in find_email:
        if not email in all_email:
            all_email.append( email ) 

    all_email = sorted( all_email )

    with open( 'assets/emails.txt', 'w' ) as result:
        for email in all_email:
            result.write( f"{email}\n" )

    # return all_email

#########################################################################

def get_phone_from_text( content ):
    
    find_phone_number = re.findall( r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', content )
    
    all_phone_number = []
    
    for phone in find_phone_number:

        if "(" in phone:
            phone = phone.replace( "(", "" )

        if ")" in phone or "." in phone:
            phone = phone.replace( ")", "-" )
            phone = phone.replace( ".", "-" )

        if len( phone ) == 10:
            phone = f"{phone[:3]}-{phone[3:6]}-{phone[6:]}"

        if not phone in all_phone_number:
            all_phone_number.append( phone ) 

    all_phone_number = sorted( all_phone_number )
    
    with open( 'assets/phone_numbers.txt', 'w' ) as result:
        for phone in all_phone_number:
            result.write( f"{phone}\n" )

    # return all_phone_number

#########################################################################
#########################################################################

if __name__ == "__main__":
    email = get_email_from_text(content)
    # print(email)
    phone_number = get_phone_from_text(content)
    # print(phone_number)

#########################################################################
#########################################################################
