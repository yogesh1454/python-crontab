import pexpect

import sys
import pyte



if __name__ == "__main__":
    #run("opc", "device1", "%", "pwd", "logout")
    child = pexpect.spawn("ssh YBard1@AP3BMD6M166EC4.local")
    child.logfile = sys.stdout.buffer
    child.expect('Password:')
    child.sendline("Cisco@123456789")
    child.expect("%")
    child.sendline("cat menu.txt")
    child.expect('[%\$]')

    # We expect any of these three patterns...
    print("before command: ")

    i = child.expect(['Permission denied', 'Terminal type', '[%\$]'])

    print(" Switch Condition: ")
    if i == 0:
        print('Permission denied on host. Cant login')
        child.kill(0)
    elif i == 2:
        print('Login OK... need to send terminal type.')

        before_command = child.before
        print(before_command.splitlines())
        screen = pyte.Screen(80, 24)
        stream = pyte.ByteStream(screen)

        print("Output: #########")
        output = before_command.splitlines()
        stream.feed(before_command)
        print("Screen Output: #########")
        #print(*screen.display, sep="\n")
        for line in screen.display:
            print(line)


        #child.sendline('ls')
        #child.expect('[%\$] ')
    elif i == 3:
        print('Login OK.')
        print('Shell command prompt', child.after)
