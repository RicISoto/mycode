#!/usr/bin/python3

def main():

    hostipdict = {'host01':'10.0.2.3', 'host02':'192.168.3.3', 'host03':'72.4.23.22'}

    print(hostipdict)

    hostipdict['host04'] = '10.23.43.224'

    print(hostipdict)

    hostipdict['host02'] = '192.168.70.55'

    print(hostipdict)
 
    ##comment after done
    print(hostipdict['toast01'])


    print(hostipdict['host02'])


if __name__ == "__main__":
    main()


