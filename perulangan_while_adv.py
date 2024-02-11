print('Mom said,"Read your Books"')
book = 10
read_count =0
read_understood=0
print(f'Number read and understood {read_understood}')

while read_count < book * 2:
    read_count = read_count +1
    if read_understood ==9:
        print (f'Book Number {read_understood +1} has not been undserstood')
    else:
        read_understood = read_understood +1
        print(f'{read_understood} Book Has Read and Understood')

print(f'Number of Read and Understood Book {read_understood}')
if read_understood == book:
    print('Mom, all books have read and understood')

else :
    print(f'MOm, not all books have read and understood. '
          f'I can understaan only {read_understood} book')

