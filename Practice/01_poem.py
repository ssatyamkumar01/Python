'''# Write a program a poem of twinkle twinkle little star.
print("""Twinkle, twinkle, little star,
How I wonder what you are! 
Up above the world so high,
Like a diamond in the sky.""")

# Write table of five.
print("""5*1=5
5*2=10
5*3=15
5*4=20
5*5=25
5*6=30
5*7=35
5*8=40
5*9=45
5*10=50     
      """)'''

# It give me the path of the file.
import os

path = os.getcwd()  # you can change this to any path
files = os.listdir("/download")

print("Files and Directories:")
for f in files:
    print(f)