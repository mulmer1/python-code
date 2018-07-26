##downloaded from github
## second push
## third push 
#4 push
def Input(Message):
	  Value = None
	  while Value == None or Value.isdigit()== False:
	  	  try:
	  	  	 Value = str(input(Message)).strip()
	  	  except ValueError:
	  	  	 Value = None
	  return(Value)
	  

def magic(num_list):## return 2 digit interger##
	  return int("".join(num_list))
	  
	  
def switch(argument):
    switcher = {
        4: "Visa",
        34: "Amex",
        37: "Amex",
        16: "Visa",
        51: "MasterCard",
        52: "MasterCard",
        53: "MasterCard",
        54: "MasterCard",
        55: "MasterCard"
        } 
    return (switcher.get(argument, "Invalid"))
def breakapart(numb): ## break apart number * 2
    value = 0

    ##test = input('enter numb')
    value = int(numb) *2
    print(value)
    if (value >9):
        most = 1
        least = value-10
    else:
        most =0
        least = value
    return (most,least)

def evenrotate(plist):
   oddrfinal =""
   for i in range(-2,(-len(plist)-1),-2): 
      oddrfinal = oddrfinal + plist[i]  
   return list(oddrfinal)
  
def oddrotate(plist):
   rfinal =""
   for i in range(-1,(-len(plist)-1),-2): 
      rfinal = rfinal + plist[i]  
   return list(rfinal)
 
def select_choice(test):
    value = 0
    value = int(test) *2
    if (value >9):
        most = 1
        least = value-10
    else:
        most =0
        least = value
    return [most,least]

card1= Input("Input a Card number")
##card1="5105105105105100"
##card1 ="4111111111111111"	    
##card1 ="378282246310005"	        
##card1 ="4400661414839610"
##card1="378282246310005"
cardlist = list(card1)
cardlist1 =cardlist
cardlist2 = cardlist


length = len(cardlist2)
for i in range(length -2):
	   cardlist2.pop()


cardnum = magic(cardlist2)
##print(cardnum)
print(switch(cardnum)) ## print card mfg 

############%
     

cardlist1= list(card1)
oddnumb=(oddrotate(cardlist1)) ##multply *1
evenumb=(evenrotate(cardlist1)) ## multipy *2
oddvalue = 0
evenvalue=0
resultvalue =0
for i in range(len(oddnumb)):
	  oddvalue = oddvalue+ int(oddnumb[i])
for i in range(len(evenumb)):
	  most,least=select_choice(evenumb[i])
	  evenvalue = evenvalue+ most + least
total = oddvalue+evenvalue 
print(total)
if total %10 ==0 :
    print("Valid")
else :
	  print("Invalid")
##print (total)
