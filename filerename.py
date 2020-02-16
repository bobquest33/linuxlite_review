import os

for f in os.listdir():
    if f.startswith('linuxlite'):
        
        nf = f.replace(" ",'-')
        print(f,nf)
        os.rename(f,nf)