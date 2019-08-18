# smtplib module send mail

import smtplib
import os
import platform
import ctypes


TO = 'YOUR_EMAIL'
SUBJECT = 'YOUR RNODE IS DEAD'
TEXT = 'FCK.'

# Gmail Sign In
gmail_sender = 'YOUR_EMAIL'
gmail_passwd = 'YOUR_PASSWORD'




def get_pid():  
    read_pid=0;
    with open('pid.txt') as f:
        read_pid = f.read()
    f.closed
    return int(read_pid)

def is_pid_running(pid):
    return (_is_pid_running_on_windows(pid) if platform.system() == "Windows"
        else _is_pid_running_on_unix(pid))


def _is_pid_running_on_unix(pid):
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    return True


def _is_pid_running_on_windows(pid):
    import ctypes.wintypes
 
    kernel32 = ctypes.windll.kernel32
    handle = kernel32.OpenProcess(1, 0, pid)
    if handle == 0:
        return False
 
    # If the process exited recently, a pid may still exist for the handle.
    # So, check if we can get the exit code.
    exit_code = ctypes.wintypes.DWORD()
    is_running = (
        kernel32.GetExitCodeProcess(handle, ctypes.byref(exit_code)) == 0)
    kernel32.CloseHandle(handle)
 
    # See if we couldn't get the exit code or the exit code indicates that the
    # process is still running.
    return is_running or exit_code.value == _STILL_ACTIVE

def send_email():
    server = smtplib.SMTP('smtp.googlemail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)

    BODY = '\r\n'.join(['To: %s' % TO,
                      'From: %s' % gmail_sender,
                      'Subject: %s' % SUBJECT,
                      '', TEXT])

    try:
        server.sendmail(gmail_sender, [TO], BODY)
        print ('email sent')
    except:
        print ('error sending mail')

    server.quit()

if __name__=='__main__':
	  pid=get_pid()
	  if is_pid_running(pid) != True:
	      send_email()
