

list = [
 {
    "name": "Tanjiro",
    "age": 13,
    "sex": "Male"
},
{
    "name": "Nezuko",
    "age": 12,
    "sex": "Female"
},
{
    "name": "Tomioka",
    "age": 19,
    "sex": "Male"
},
{
    "name": "Urokodaki",
    "age": 52,
    "sex": "Male"
},
{
    "name": "Shinobu",
    "age": 18,
    "sex": "Female"
},
{
    "name": "Sanemi",
    "age": 21,
    "sex": "Male"
},
{
    "name": "Obanai",
    "age": 21,
    "sex": "Male"
},
{
    "name": "Tengen",
    "age": 23,
    "sex": "Male"
},]


name = input('your party invite? ')

for x in list:
    if x['name'] == name.capitalize():
        print(f'valid invite , Welcome {name.capitalize()} ')
        break

