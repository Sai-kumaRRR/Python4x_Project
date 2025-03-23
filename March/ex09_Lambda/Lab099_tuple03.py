cities = (" london", "paris", "los angles", "tokyo")
print("paris" in cities )
print("new delhi" in cities)

t = (12 , 14 , 16 )
# t . append(12) # attribute error: 'tuple' object has no attribute "append"
my_list = list(t)
my_list.append(4)
t = tuple(my_list)
print(t)

ENV_API_URLS = tuple(["abc.com/get" , "xyz.com/post" ,"qwe.com/put"])
print(ENV_API_URLS)