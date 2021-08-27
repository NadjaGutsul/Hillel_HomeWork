names = ['Brad Pitt', 'Kevin Smitt', 'Christoph Waltz', 'Michael Fassbender', 'Eli Roth', 'Diane Kruger', 'Daniel Brühl', 'Til Schweiger', 'Mélanie Laurent', 'August Diehl']
instruction=input()
while instruction != 'stop':
    if instruction == 'add':
        name=input()
        names.append(name)  
    elif instruction == 'name':
        name=input()
        if name in names:
            print('True')
        else:
            print('False')
    elif instruction == 'list':
        print(*names)
    elif instruction == 'delete':
        name=input()
        del names[names.find(name)]
    instruction = input()
