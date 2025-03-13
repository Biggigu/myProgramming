x = "cisco"
y = " Switch"

x + y
#"Cisco Switch"

x * 3
#"CiscoCiscoCisco"

#x = Cisco

"o" in x
#True

"b" in x
#False

"b" not in x
#True

"Cisco model: 2600XM, 2 WAN slots, IOS 12.4" 
#"Cisco model: 2600XM, 2 WAN slots, IOS 12.4"

"Cisco model: %s, %d WAN slots, IOS %f" % ("2600XM", 2, 12.4)
#"Cisco model: 2600XM, 2 WAN slots, IOS 12.4"

"Cisco model: %s, %d WAN slots, IOS %f" % ("2691XM", 4, 12.3)
#"Cisco model: 2691XM, 4 WAN slots, IOS 12.3"

"Cisco model: %s, %d WAN slots, IOS %f" % ("7200XR", 8, 15.4)
#"Cisco model: 7200XR, 8 WAN slots, IOS 15.4"

"Cisco model: {0}, {1} WAN slots, IOS {2}" % ("420XS", 3, 16.4)
#"Cisco model: 420XS, 3 WAN slots, IOS 16.4"

"Cisco model: {2}, {1} WAN slots, IOS {0}" % ("420XS", 3, 16.4)
#"Cisco model: 16.4, 3 WAN slots, IOS 420XS"

#f-strings

model = "2600XM"
slots = 4
ios = 12.3

f"Cisco model: {model}, {slots} WAN slots, IOS {ios}"
#"Cisco model: 2600XM, 4 WAN slots, IOS 12.3"

expences = 10000
income = 25000
taxes = 4000

f"July Company Numbers: {income=} {expences=} {taxes= }"
f"PROFIT: {income-expences-taxes=}"

#'July Company Numbers: income=25000 expences=10000 taxes= 4000'
#'PROFIT: income-expences-taxes=11000'