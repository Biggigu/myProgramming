my_string = "This is my first string"

print(my_string)

my_string = """This\
is\
my\
first\
string"""

print(my_string)

string1 = "Cisco Router"

print(string1)

print(string1[0] + string1[1] + string1[2] + string1[3] + string1[4] + string1[5] + string1[-1] + string1[-2] + string1[-3] + string1[-4] + string1[-5] + string1[-6])

string1[0] 
string1[1] 
string1[2] 
string1[3] 
string1[4] 

string1[-1] 
string1[-2] 
string1[-3] 
string1[-4] 
string1[-5] 
string1[-6] 
 

#now we start talking about methods
a = "cisco switch"

a.index("i")
#1
a.index("t")
#9
a.count("i")
#2
a.find("sco")
#2
a.find("tch")
#9
a.lower()
#'cisco switch'
a.upper()
#'CISCO SWITCH'
a.startswith("B")
#False
a.startswith("c")
#True
a.endswith("h")
#True


b = "      cisco switch      "

b.strip()
#
'cisco switch'

c = "$$$$cisco switch$$$$"
c.strip("$")
#'cisco switch'
b.replace ("switch", "Router")
#'      cisco Router      '

d = "cisco, juniper, hp, avaya, nortel"
d.split(",")
#['cisco', ' juniper', ' hp', ' avaya', ' nortel']
"_".join(a)
#'c_i_s_c_o_ _s_w_i_t_c_h'
