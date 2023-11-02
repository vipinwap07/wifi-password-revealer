import subprocess

a = subprocess.check_output(['netsh', 'wlan', 'show', 'profile']).decode('utf-8').split('\n')
a = [i.split(":")[1][1:-1] for i in a if "All User Profile" in i]

print('╔══════════════════════════════════════╗')
print(' ═════════════ vipinwap07 ═════════════')
print('╚══════════════════════════════════════╝', end='\n\n')

for i in a:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(':')[1][1:-1] for b in results if 'Key Content' in b]
    try:
        print("{:<20} | {:<}".format(i, results[0]))
        print('-'*40)
    except IndexError:
        print("{:<20} | {:<}".format(i, ""))
        print('-'*40)
print()
print()
print('_/﹋\_')
print('(҂`_´)')
print('<,︻╦╤─ ҉ - -')
print('_/﹋\_', end='\n\n')
print('Press Enter to Exit...', end=" ")
input()