import os
# print(os.environ["USERNAME"])
# print(os.environ["HOME"])

cwd = os.getcwd()
# os.chdir('data/')
# with open('smit.txt','r') as file:
#     pass
# print(os.getcwd())

# for file in os.listdir('.'):
#     if file.endswith('.csv'):
#         print(file)

# os.system('mkdir test')

# print(os.listdir('.'))

for path,dir,files in os.walk(cwd):
    print(f"path: {path}")
    print(f"Folders: {dir}")
    print(f"Files: {files}")
    print('*'*20)