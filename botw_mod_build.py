import os

# Get the name of the mod
name_input = input("Mod name: ")
name = f"BreathOfTheWild_{name_input}"

# Get the mod description
desc_input = input('Mod description: ')

data_path = f'{name}/content'

# Get the data folder
while True:
    folders = []
    folder_input = input('folders e.g. Actor/Pack: ')
    folders += [folder_input]

    if folder_input == 'stop':
        for folder in folders:
            os.mkdir(os.path.join(data_path, folder))

        break
with open(f'{name}/rules.txt', 'w') as rules:
    rules.write('[Definition]')
    rules.write('titleIds = 00050000101C9300,00050000101C9400,00050000101C9500')
    rules.write(f'name = {name}')
    rules.write(f'path = "The Legend of Zelda: Breath of the Wild/Mods/{name}"')
    rules.write(f'description = {desc_input}')
    rules.write('version = 3')
    rules.write('fsPriority = 100')


