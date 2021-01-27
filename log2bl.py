from subprocess import Popen, PIPE

class  Log2BL:
    """This object holds the methods responsible for a more restrict, maybe
    paranoid secutiry policy

    As everyone knows, thousands of bots are trying to get access to servers by
    using default or common credentials.
    This script is meant to block every access trial from every host who previously
    tried to access the server with an invalid username.

    Changes can be made to check if the host tried to log in more than one time
    with the wrong username. This will remain unimplemented, as the script fits
    my needs as is

    """

    def __init__(self, hosts_path='/etc/hosts.deny', auth_path='/var/log/auth.log'):
        self.hosts_path = hosts_path #/etc/hosts.deny
        self.auth_path = auth_path

    def hosts(self):
        '''Extracts the IPs from the log'''
        ips = list()
        cmd = Popen(f'cat {self.auth_path} | grep "Invalid user"',shell=True,stdout=PIPE).communicate()[0].splitlines()
        for i in cmd:
            ips.append(i.split('from ')[1].split(' port')[0])
        return ips

    def apply(self):
        newhosts = self.hosts()
        newhosts_list = list()
        with open(self.hosts.path) as h:
            h = h.read().splitlines()
            for i in range(len(h)):
                h[i] = h[i].split('sshd: ')[1] #Hosts only
            newhosts_list.append([x for x in newhosts if x not in h])
            final_list = h + newhosts_list
        with open(self.hosts.path,'w') as h:
            for i in newhosts_list:
                h.write(f'sshd: {i}')
                
if __name__ == '__main__':
    l = Log2BL()
    l.apply()
