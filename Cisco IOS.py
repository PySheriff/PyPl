import netmiko
from netmiko import ConnectHandler


def device_count(cisco_device_model):
    print ('Unauthorized Access Prohibited! \n Violators Shall Be Prosecuted!')
    user_n = input('Enter Admin Username: ') #takes username input
    pass_d = input("Enter Password: ")
    #secret = input("Enter Privilege Exec Password: ")
    count = 0
    for n in range(11, 15):  # loop through from number 11 up to but not including 15
        target_ip = "192.168.1.{0}".format(n)
        try:
            node = ConnectHandler(device_type='cisco_ios', ip=target_ip, username=user_n, password=pass_d) #builds SSH connection the target IP
            Model_Search = node.send_command('show version') #basically the output of the 'show version | in Model' command
            if cisco_device_model in Model_Search:
                count += 1
                node.disconnect()

            else:
                print (node + ' is not a ' + ' Cisco ' + cisco_device_model)

        except:
            print(target_ip + ' is unreachable')
            pass

    return count

print (device_count('Cisco IOS'))

