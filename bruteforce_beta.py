import zipfile
import os
#import rarfile

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#location
zippath = 'telegram.zip'
passlistpath = 'passlist.txt'

#log
def log(log):
    f = open(f'log({zippath}).txt', 'a')
    f.write(log)

#output
def output(message, message2):
    clear()
    print('- - - - - - - - - - - - - - - - - - - ')
    print('\tZip Password Cracker')
    print('- - - - - - - - - - - - - - - - - - - ')
    print(message)
    print(message2)
    log(f'{message2}\n')

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
                    output(f'Password checking {count}/{len(line)}', f'Password found: {password}')
                    passwordfound = True
                    break
                except RuntimeError as e:
                    output(f'Password checking {count}/{len(line)}', f'Password: {password}, failed: {e}')
                    continue
                except zipfile.BadZipFile as e:
                    output(f'Password checking {count}/{len(line)}', f'Error: {e}')
                    continue
                except Exception as e:
                    output(f'Password checking {count}/{len(line)}', f'Error: {e}')
                    continue
            if count == len(line) and not passwordfound:
                print('Password not in the list')
    except FileNotFoundError:
        print('Zip or Passlist location doesnt exist!')

# def crackRar(passwordlistpath, rarpath):
   
#     try:
#         with rarfile.RarFile(rarpath, 'r') as rar_check:
#             passread = open(passwordlistpath, 'r')
#             line = passread.readlines()
#             count = 1
#             for password in line:
#                 password = password.strip()
#                 try:
#                     rar_check.extractall(pwd=password.encode())
#                     output(f'Password checking {count}/{len(line)}', f'Password found: {password}')
#                     count+=1
#                     break
#                 except RuntimeError as e:
#                     count+=1
#                     output(f'Password checking {count}/{len(line)}', f'Password: {password}, failed: {e}')
#                     continue
#                 except rarfile.BadZipFile as e:
#                     output(f'Password checking {count}/{len(line)}', f'Error: {e}')
#                     break
#                 except Exception as e:
#                     output(f'Password checking {count}/{len(line)}', f'Error: {e}')
#                     # x = input('Try again (y)? :').lower()
#                     # if x == 'y':
#                     #     continue
#                     # else: break
                    
#     except FileNotFoundError:
#         print('Rar or Passlist location doesnt exist!')
#     except Exception as e:
#         print(e)


    
#main
crack(passlistpath, zippath)

    
        
