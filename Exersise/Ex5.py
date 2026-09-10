import time

a = time.strftime('%H:%M:%S')
print("Current Time:", a)

a = int(time.strftime('%H'))

if a >= 5 and a < 12:
    print("Good Morning 🌅")

elif a >= 12 and a < 17:
    print("Good Afternoon ☀️")

elif a >= 17 and a < 21:
    print("Good Evening 🌇")

else:
    print("Good Night 🌙")
