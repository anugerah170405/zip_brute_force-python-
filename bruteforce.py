import zipfile
import os
import random
#import rarfile

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#location
zippath = 'protected.zip'
passlistpath = 'passlist.txt'

#log
def log(log):
    f = open(f'log({zippath}).txt', 'a')
    f.write(log)

#output
def output(message, message2):
    clear()
    print('------·························------')
    print(f'{'':>9}Zip Password Cracker')
    print('------·························------')
    print(message)
    print(message2)
    #log(f'{message2}\n')
    print('--------------------------------------')
def logpassword(log):
    f = open(f'Log_Password.txt', 'a')
    f.write(log)

#cracker engine
def crack(passwordlistpath, zippath):
   
    try:
        with zipfile.ZipFile(zippath, 'r') as zip_check:
            passread = open(passwordlistpath, 'r')
            line = passread.readlines()
            passwordfound = False
            count = 0
            for password in line:
                password = password.strip()
                count+=1
                try:
                    zip_check.extractall(pwd=password.encode())
                    output(f'Method: Crack in Sequence\nPassword checking: {count}/{len(line)}', f'Password found: {password}')
                    passwordfound = True
                    logpassword(f'Password ({zippath}): {password}\n')
                    x = input('\nPress enter to continue')
                    break
                except RuntimeError as e:
                    output(f'Method: Crack in Sequence\nPassword checking: {count}/{len(line)}', f'Password: {password}, failed: {e}')
                    continue
                except zipfile.BadZipFile as e:
                    output(f'Method: Crack in Sequence\nPassword checking: {count}/{len(line)}', f'Error: {e}')
                    continue
                except Exception as e:
                    output(f'Method: Crack in Sequence\nPassword checking: {count}/{len(line)}', f'Error: {e}')
                    continue
            if count == len(line) and not passwordfound:
                print('Password not in the list')
                x = input('\nPress enter to continue')
    except FileNotFoundError:
        print('Zip or Passlist location doesnt exist!')

#cracker engine randomly

def crackRandom(passwordlistpath, zippath):

    ischecked = []
    try:
        with zipfile.ZipFile(zippath, 'r') as zip_check:
            passread = open(passwordlistpath, 'r')
            line = passread.readlines()
            passwordfound = False
            count = 0
            for _ in range(len(line)):
                i = random.randint(0,len(line)-1)
                line[i] = line[i].strip()

                while i in ischecked:
                    i = random.randint(0,len(line)-1)
                    line[i] = line[i].strip()

                count+=1
                ischecked.append(i+1)
                try:
                    zip_check.extractall(pwd=line[i].encode())
                    output(f'Method: Crack Randomly\nPassword checking: {i+1}/{len(line)}', f'Password found: {line[i]}')
                    passwordfound = True
                    logpassword(f'Password ({zippath}): {line[i]}\n')
                    x = input('\nPress enter to continue')
                    break
                except RuntimeError as e:
                    output(f'Method: Crack Randomly\nPassword checking: {i+1}/{len(line)}', f'Password: {line[i]}, failed: {e}')
                    continue
                except zipfile.BadZipFile as e:
                    output(f'Method: Crack Randomly\nPassword checking: {i+1}/{len(line)}', f'Error: {e}')
                    continue
                except Exception as e:
                    output(f'Method: Crack Randomly\nPassword checking: {i+1}/{len(line)}', f'Error: {e}')
                    continue
            if count == len(line) and not passwordfound:
                print('Password not in the list')
                x = input('\nPress enter to continue')
    except FileNotFoundError:
        print('Zip or Passlist location doesnt exist!')


    
#main


def menu():
    clear()
    print('------·························------')
    print(f'{'':>9}Zip Password Cracker')
    print('------·························------')
    print('Menu :')
    print('1. Crack in Sequence')
    print('2. Crack Randomly')
    print('3. Review all password found')
    print('4. Exit')
    x = int(input('Enter your input: '))
    return x

while True:
    try:
        x = menu()
        if x == 1:
            crack(passlistpath, zippath)
        elif x == 2:
            crackRandom(passlistpath, zippath)
        elif x == 3:
            f = open(f'Log_Password.txt', 'r')
            print()
            print(f.read())
            y = input('\nPress enter to continue')
        elif x == 4:
            break
        else:
            print('\nInvalid input!')
    except ValueError:
        print('\nInput only support number!')


    
        
