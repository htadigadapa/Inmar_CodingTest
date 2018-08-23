import re
#given_string="123-45-5678"
given_number=input("enter ssn number:")

if (len(given_number) != 9) or (str(given_number)=="078051120") or (str(given_number)=="219099999"):
    print("Invalid SSN(length not euqal to 9 or given #is already a known fake number)")

else:
    number_list=list(given_number)
    number_list.insert(3,"-")
    number_list.insert(6,"-")
    if (str(''.join(number_list[:3]))=="000") or (str(''.join(number_list[4:6]))=="00") or (str(''.join(number_list[7:]))=="0000"):
        print("Invalid SSN(None of the group should have only zeros)")
    elif str(''.join(number_list[:3]))=="666":
        print("Invalid SSN(Cannot start with 666)")

    else:
        ssn_string=''.join(number_list)
        SSN_Pattern=re.compile('^\d{3}-\d{2}-\d{4}$')
        if re.match(SSN_Pattern,ssn_string):
            print("Valid SSN")
        else:
            print("Invalid SSN(Does not match with required pattern xxx-xx-xxxx)")
