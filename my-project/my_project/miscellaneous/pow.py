from hashlib import sha256

x=5
y=0

while sha256(f'{x*y}'.encode()).hexdigest()[-1]!= "0":
      y+=1

print(f'The solution is y={y}')