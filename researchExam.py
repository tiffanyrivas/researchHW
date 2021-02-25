# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
cities_list = ["Atlanta", "Baltimore", "Boston", "Charlotte", "Dallas", "Denver", "Jacksonville", "Minneapolis", "Orlando", "Sacramento", "Tampa", "Washington"]


print("The name of all cities which are available ---> \n")
for city in cities_list:
    print(f"{city}")


start_city = input("\nEnter the city name from where to want to start trip: ").capitalize()
target_city = input("Enter the city name where you want to reach at: ").capitalize()


while (start_city not in cities_list or start_city not in cities_list):
    print ("\nEnter another approcriate cities which are available\n")
    start_city = input("Enter the city name from where to want to start trip: ")
    target_city = input("Enter the city name where you want to reach at: ")


print("Thank you! For using our services")


#%%

# quadratic equation problem
import cmath

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))
# %%


#%%
import numpy as np

Mary = np.array([1.204, 6.6, 0.32])

print(Mary)

print(type(Mary))

# %%
