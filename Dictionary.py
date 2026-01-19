country = {
"China":"Beijing", "Japan":"Tokyo",
"Netherlands":"Amsterdam",
"Brazil":"Brazilia"

}

print(country)

#Add/Edit Item
country["Brazil"]="Spain"
country["Russia"]="Moscow"
print(country)

del country["Netherlands"]
print(country)

if "China" in country.items():
    print("Item is Present")
else:
    print(" Item not Found")

for key,value in country.items():
    print(key,value)


textbook = {
    "Math Book":15, "Science":15,
    "History":10,
    "Geography":7,
    "English":12,
    "Politics":12
}

print(textbook)

#Add/Edit Item
textbook["Geography"]=10
textbook["Arts"]=7

print(textbook)