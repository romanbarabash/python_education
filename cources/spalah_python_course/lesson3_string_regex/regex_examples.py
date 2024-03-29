import re

phrase = 'we are the dreamer who dreams and lives inside the dream'

result = re.findall(r'\w+', phrase)
print(result)  # ['we', 'are', 'the', 'dreamer', 'who', 'dreams', 'and', 'lives', 'inside', 'the', 'dream']

result = re.findall(r'^\w+', phrase)
print(result)  # ['we']

result = re.findall(r'\w+$', phrase)
print(result)  # ['dream']

result = re.findall(r'\b\w.', phrase)
print(result)  # ['we', 'ar', 'th', 'dr', 'wh', 'dr', 'an', 'li', 'in', 'th', 'dr']

result = re.findall(r'\b[aeiouAEIOU]\w+', phrase)
print(result)  # ['are', 'and', 'inside'] ,print words which starts vowel

result = re.findall(r'\b[^aeiouAEIOU ]\w+', phrase)
print(result)

emails = 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz'

result = re.findall(r'@\w+.\w+', emails)
print(result)  # ['@gmail.com', '@test.in', '@analyticsvidhya.com', '@rest.biz']

result = re.findall(r'@\w+.(\w+)', emails)
print(result)  # ['com', 'in', 'com', 'biz']

date = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'

result = re.findall(r'\d{2}-\d{2}-\d{4}', date)
print(result)  # ['12-05-2007', '11-11-2011', '12-01-2009']

result = re.findall(r'\d{2}-\d{2}-(\d{4})', date)
print(result)  # ['2007', '2011', '2009']

phone = ['9999999999', '999999-999', '99999x9999']
valid_phone = []

for val in phone:
    if re.match(r'[8-9]{1}[0-9]{9}', val) and len(val) == 10:
        valid_phone.append(val)

print(valid_phone)  # ['9999999999']

char_set = 'asdf fjdk;afed,fjek,asdf,foo'  # String has multiple delimiters (";",","," ").
result = re.split(r'[;,\s]', char_set)
print(result)  # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

html = "1NoahEmma2LiamOlivia3MasonSophia4JacobIsabella5WilliamAva6EthanMia7MichaelEmily"
result = re.findall(r'\d([A-Z][A-Za-z]+)([A-Z][A-Za-z]+)', html)
print(result)
# [('Noah', 'Emma'), ('Liam', 'Olivia'), ('Mason', 'Sophia'), ('Jacob', 'Isabella'), ('William', 'Ava'),
# ('Ethan', 'Mia'), ('Michael', 'Emily')]


raw = """
a
(L 0E  !a_ART_POS_Store
10000000000
_ART_POS_Address0
_ART_POS_City0 NY 16270
                     _ART_POS_TERMINAL TSR
employee: Raul Gonzalez Raul Gonzalez
a06/30/2020 05:09 PM
aOrder # 6660000002
a ITEM                        QTY      PRICE
a ------------------------------------------
_ART_POS_Burger              1      $11.00
!------------------------------------------

                     Subtotal       $11.00
Tax                                  $0.55
------------------------------------------
!                     Total          $11.55!

                     CASH            $5.50
                     CREDIT          $6.05

!


Signature ________________________________


a!Suggested Tip Amounts
!------------------------------------------
    15%             18%             20%
   $1.70           $2.10           $2.30

!Account #:           xxxxxxxxxxxx4111
Authorization:       051389
Terminal ID:         666
Trace No:            361
Balance:             $15.00
Amount:              $6.05

a!!0Table 58
!
aMerchant Copy
axenial.pos+across_safe@dev-pro.neta !dV0
"""



CARD_INFO_REGEX = r"Account #:\s*(?P<accountNumber>.*?)\s*" \
                      r"(Authorization:\s*(?P<authorizationNumber>.*?)\s*)?" \
                      r"(Terminal ID:\s*(?P<terminalID>\w*(\s\w*)*?)\s*)?" \
                      r"(Trace No:\s*(?P<traceNumber>\w*(\s\w*)*?)\s*)?" \
                      r"(Balance:\s*(?P<balance>.*?)\s*)?" \
                      r"Amount:\s*(?P<amount>.*?)\s"

credit_payment_section = re.split(r"-{3,}", raw)[3]
details = [regex_item.groupdict() for regex_item in re.finditer(CARD_INFO_REGEX, credit_payment_section)]
print(details)


actual_text = """Patient: Tammyuaq2xy7weight Gonzalezsnizie9bad
Date of birth: 08/02/2020
Specimen 1: Blood
Date collected: 01/26/2022
Date received: 01/27/2022

Specimen 2: Cells
Date collected: 01/27/2022               Order #: COI7896016
Date received: 01/28/2022                Lab ID: 22180223
Ref diagnosis: Metabolic Abnormality, 194.0-Malignant neoplasm of adrenal gland 
Report Date: 01/28/2022 03:57 AM
Test: Expanded Carrier Screen (283 genes)
Method: NA
Positive by Progressive Familial Intrahepatic Cholestasis, Type 2
Associated gene(s): ABCB11
Variants detected: c.37C>G, p.R13G, Pathogenic, Heterozygous (one copy)

Negative for all other genes tested

Recommendations
CGG repeat analysis of FMR1 for fragile X syndrome is not performed on males as repeat expansion of premutation alleles is not expected in the male germline.
Individuals of Asian, African, Hispanic and Mediterranean ancestry should also be screened for hemoglobinopathies by CBC and hemoglobin electrophoresis.
Consideration of residual risk by ethnicity after a negative carrier screen is recommended for the other diseases on the panel, especially in the case of a positive family history for a specific disorder.

Final report signed by Roman Barabash, Dummy, Qualification
Test performed at Sema4 Opco, Inc
Referred by: Provider Integration"""
result = str(re.findall(r'Report Date:\s(\d{2}/\d{2}/\d{4} \d{2}:\d{2} \w{2})', actual_text))
print(result)
