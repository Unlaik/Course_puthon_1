first_number=int(input())
second_number=int(input())
start_mass=int(input())
end_mass=int(input())
for gorizontal in range(start_mass,end_mass+1):
    print('  ', gorizontal, end=' ')
print()
for vertical in range(first_number,second_number+1):
    print(vertical,end='  ')
    for gorizontal in range(start_mass,end_mass+1):
        print(vertical*gorizontal,end='    ')
    print('\t')



