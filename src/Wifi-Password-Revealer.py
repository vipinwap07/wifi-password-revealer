import os
import subprocess

os.system('title Wi-Fi Password Revealer')
wlanInfo = subprocess.check_output(['netsh', 'wlan', 'show', 'profile']).decode('utf-8').split('\n')
wlanInfo = [i.split(":")[1][1:-1] for i in wlanInfo if "All User Profile" in i]

print("\033[90m{}\033[00m".format('╔══════════════════════════════════════════════════════════╗'))
print("\033[90m{}\033[00m".format('║═══════════════════════'), end='')
print("\033[92m{}\033[00m".format(" vipinwap07 "), end='')
print("\033[90m{}\033[00m".format('═══════════════════════║'))
print("\033[90m{}\033[00m".format('║══'), end='')
print("\033[94m{}\033[00m".format(" https://github.com/vipinwap07/wifi-password-revealer "), end='')
print("\033[90m{}\033[00m".format('══║'))
print("\033[90m{}\033[00m".format('╚══════════════════════════════════════════════════════════╝'), end='\n\n\n')

print("\033[95m━\033[00m"*60)
print("\033[95m{:<30}{}{:<}\033[00m".format("Wi-Fi Name", "\033[97m | \033[00m\033[95m", "Password"))
print("\033[95m━\033[00m"*60)

for i in wlanInfo:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(':')[1][1:-1] for b in results if 'Key Content' in b]
    try:
        print("\033[92m{:<30}{}{:<}\033[00m".format(i, "\033[97m | \033[00m\033[92m", results[0]))
        print("\033[90m-\033[00m"*60)
    except IndexError:
        print("\033[95m{:<30} | {:<}\033[00m".format(i, ""))
        print("\033[90m-\033[00m"*60)

print('', end='\n\n')

print("\033[91m{}\033[00m".format('_/﹋\_'))
print("\033[91m{}\033[00m".format('(҂`_´)'))
print("\033[91m{}\033[00m".format('<,︻╦╤─ ҉ - - - -'))
print("\033[91m{}\033[00m".format('_/﹋\_'), end='\n\n')

print('Press Enter to Exit...', end=" ")
input()