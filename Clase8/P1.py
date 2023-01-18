file = open('hello_world.txt', 'w')
file.write('First Line write with file on python \n')
file.write('Hello World \n')
file.close()

file = open('hello_world.txt', 'r+')
file.readline()
file.write('Line after Hello World \n')

file.seek(0)
print(file.read())
file.close()