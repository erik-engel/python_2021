#1. Model an organisation of employees, management and board of directors in 3 sets.

#Board of directors: Benny, Hans, Tine, Mille, Torben, Troels, Søren

#Management: Tine, Trunte, Rane

#Employees: Niels, Anna, Tine, Ole, Trunte, Bent, Rane, Allan, Stine, Claus, James, Lars

bod = {"Benny", "Hans", "Tine", "Mille", "Torben", "Troels", "Søren"}
management = {"Tine", "Trunte", "Rane"}
employees = {"Niels", "Anna", "Tine", "Ole", "Trunte", "Bent", "Rane", "Allan", "Stine", "Claus", "James", "Lars"}

#who in the board of directors is not an employee?

a = bod.difference(employees)
print(a)

#who in the board of directors is also an employee?

b = bod.intersection(employees)
print(b)

#how many of the management is also member of the board?

c = management.intersection(bod)
print(len(c))

#All members of the managent also an employee

d = management.intersection(employees)
print(d)

#All members of the management also in the board?

e = management.intersection(bod)
print(e)

#Who is an employee, member of the management, and a member of the board?

f = set.intersection(bod, management, employees)
print(f)

#Who of the employee is neither a memeber or the board or management?

g = employees.difference(bod, management)
print(g)

#-----------------------------------------------------------------------------
#Code



#-----------------------------------------------------------------------------
#2. Using a list comprehension create a list of tuples from the folowing datastructure
#{‘a’: ‘Alpha’, ‘b’ : ‘Beta’, ‘g’: ‘Gamma’}
#-----------------------------------------------------------------------------
#Code
#-----------------------------------------------------------------------------

dict = {'a' : 'Alpha', 'b' : 'Beta', 'g': 'Gamma'}
print(dict)
list = [(k, v) for k, v in dict.items()]
print(list)


#3. From these 2 sets:
#{'a', 'e', 'i', 'o', 'u', 'y'}

#{'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}
#-----------------------------------------------------------------------------
 
#-----------------------------------------------------------------------------

h = {'a', 'e', 'i', 'o', 'u', 'y'}

i = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}


#Of the 2 sets create a:

#Union:
#----

j = h.union(i)
print(j)

#Symmetric difference
#----

k = h.symmetric_difference(i)
print(k)

#or

print(h^i)

#difference
#----

l = i.difference(h)
print(l)
m = h.difference(i)
print(m)

#or

print (i-h)
print (h-i)

#disjoint
#----

n = h.isdisjoint(i)
print(n)


# 4. Date Decoder

#A date of the form 8-MAR-85 includes the name of the month, which must be translated to a number.

#Create a dict suitable for decoding month names to numbers.

month = {'JAN' : 1, 'FEB' : 2, 'MAR' : 3, 'APR' : 4, 'MAY' : 5, 'JUN' : 6, 'JUL' : 7, 'AUG' : 8, 'SEP' : 9, 'OKT' : 10, 'NOV' : 11, 'DEC' : 12}
#Create a function which uses string operations to split the date into 3 items using the "-" character.



def split_function(s) :
    return s.split('-')


#Translate the month, correct the year to include all of the digits.

def trans_month(s) :
    i = month.get(s)
    return i

def year_all_digt(i) :
    if i<=21 and i>=00 :
        i += 2000
    else :
        i += 1900
    return i

#The function will accept a date in the "dd-MMM-yy" format and respond with a tuple of ( y , m , d )

def final_function(s) :
    l = split_function(s)
    a = year_all_digt(int(l[2]))
    b = trans_month(l[1])
    return (str(a) + ', ' + str(b) + ', ' + l[0])

s1 = '8-MAR-85'
s2 = '23-JAN-77'
s3 = '11-DEC-19'
s4 = '1-OKT-01'
print(final_function(s1))
print(final_function(s2))
print(final_function(s3))
print(final_function(s4))

