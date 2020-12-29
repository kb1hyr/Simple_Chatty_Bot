start_atoms = int(input())
end_atoms = int(input())
HALF_LIFE_DAYS = int(12)

periods = 0
remainder = start_atoms

while end_atoms < (remainder+1):
    periods = periods + 1
    remainder = int(remainder/2)

days = HALF_LIFE_DAYS * periods
print(days)
