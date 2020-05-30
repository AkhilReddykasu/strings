#01-strings are arrays : gives output for the  index

a ="Akhil reddy"
print("strs are arrays",a[4])

#02-string slicing : gives the output in range

print("string slicing",a[2:5])

#03-negative indexing

print("negative indexing",a[-5:-2])

#04-string length : lendth of a string

print("str length",len(a))

#05-string methods
#strip : method removes any whitespace from the beginning or the end
b = " Akhil Reddy "
print("strip",b.strip())

#06-lower : converts all to lower case lettes
print("lower",b.lower())

#07-upper : converts all to upper case lettes
print("upper",b.upper())

#08-replacing : replace the existing string
c = b.replace("Akhil Reddy","asha nikhil")
print("replacing",c)

print("replacing",c.replace('a','A'))

#09-splitting : divide the strings

d = "kasu Bala Akhil Reddy"
print("splitting",d.split())

#10-checking string : check whether the searched str in existing string
e = 'kasu' in d
print("checking string",e)

f = 'kasu' not in d
print("checking string",f)

#11-string concartination : combines two different strings
print("string contn",a + b)

#12-using format : pass the argmnts and palce it in a string
mangoes = 3
rupees = 45
txt = "i need {0} kilo grams of mangoes for {1} per kg"
print("using format",txt.format(mangoes, rupees))

#13-captalize: returns the 1st letter capital
text = 'hello ! Welcome To The World'
g = text.capitalize()
print("text cap",g)

#14-casefold: returns all letters into small letters
h = text.casefold()
print("casefld",h)

#15-center : moves the str from left to center
print("center",a.center(50))

#16-count: counts the repeatation of a str
i = "hello world ! welcome to this iconic world"
print("cunt",i.count('world'))

#17-encode : encode the give text
ee = "my name is akhil"
print("encode",ee.encode(encoding="ascii",errors="backslashreplace"))

#18-endswith : reture true or false if the letter ends with the specified str
j = text.endswith("d")
print("endswith",j)

#19-expandtabs: it expand the tab spaces
k = "Pentareddy\tAshrith\tReddy"
l = k.expandtabs(5)
print("expand tabs",k)

#20-find : returns index values when it finds the searched str if not -1
m = i.find('w')
print("find",m)

#21-index: returns index values when it finds the searched str if not an error
print("index",i.index('w',7))

#22-alpha.numeric : retures true if it is aplha and numeric else false
n = "akhil99128"
o = "akhil"
print("alnum",n.isalnum())
print("alnum",o.isalnum())

#23-alpha : retures true if it is aplha else false
print("isalpha",n.isalpha())
print("isalpha",o.isalpha())

#24-decimal : retures true if it is numeric(0-9) else false
p = '545'
q = p.isdecimal()
print("isdecimal",q)

#25-digit : retures true if it is digit else false
p = '545nj'
q = p.isdigit()
print('digit',q)

#26-identifierretures true if it is aplha(a-z) and numeric(0-9) else false
p = 'skdnscs54'
q = p.isidentifier()
print("identifier",q)

#27-lower : retures true if it contains lower letters else false
p = 'Hello'
q = p.islower()
print("islower",q)

#28-numeric : retures true if it contains numreic letters else false
p = '545'
q = p.isnumeric()
print("isnumeric",q)

#29-printable : retures true if it is printable else false
p = '545\tiufdg\n'
q = p.isprintable()
print("isprintable",q)

#30-isspace : retures true if it contains whitespaces else false
p = ' '
q = p.isspace()
print("isspace",q)

#31-istitle : retures true if and only used as title else false
p = '545'
r ="A"
q = p.istitle()
print('istitle',q)
print("istitle",r.istitle())

#32-isupper : retures true if it contains upper letters else false
p = 'AKHIL'
q = p.isupper()
print('isupper',q)

#33-join : joins two strings withs spl symbol
p = "akhil" , "reddy"
q = "@".join(p)
print('join',q)

#34-ijust : Returns a left justified version of the string
ff ="akhil reddy"
q = ff.ljust(20)
print("ljust",q,"kasu bala akhil")

#35-lstrip : Returns a left trim version of the string
s = "     AshaNikhil       "
t = s.lstrip()
print("lstrip","hello",s,"how are you")

#36-patition : Returns a tuple where the string is parted into three parts
u = "asha & nihkil stays in bangalore"
v = u.partition('stays')
print('partitin',v)

#37-replace : Returns a string where a specified value is replaced with a specified value
w = "kasu bala akhil reddy"
x = w.replace("reddy",'bala')
print("replace",x)

#38-rfind : Searches the string for a specified value and returns the last position of where it was found
y = u.rfind("stays")
print("rfind",y)

#39-rindex: Searches the string for a specified value and returns the last position of where it was found
print("rindex",u.rindex("bangalore"))

#40-rjust: Returns a right justified version of the string
z = w.rjust(20)
print("rjust",z,"stays in warangal")

#41-split : 	Splits the string at the specified separator, and returns a list
print("split",w.split())

#42-splitlines: Splits the string at line breaks and returns a list
aa = "if you are bad\n i'm your dad"
print("splitlines",aa.splitlines())

#43-stratswith:
print("startswith",u.startswith("kasu"))

#44-strip: 	Returns true if the string starts with the specified value
bb = "      akhil    "
print("strip",bb.strip(),"reddy kasu")

#45-swapcase: Swaps cases, lower case becomes upper case and vice versa
cc = "Hey Buddy! whats Up"
print("swapcase",cc.swapcase())

#46-title: Converts the first character of each word to upper case
print("title",w.title())

#47-zfill: Converts a string into upper case
dd = "45"
print("zfill",dd.zfill(20))