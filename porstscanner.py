import nmap

nm = nmap.PortScanner()

target = input("Enter the target IP: ")
options = input("Enter the scan options: ")

nm.scan(target, arguments=options)

for host in nm.all_hosts():
    print("Host: %s (%s)" % (host, nm[host].hostname()))
    print("State: %s" % nm[host].state())

    for proto in nm[host].all_protocols():
        print("Protocol: %s" % proto)

        lport = nm[host][proto].keys()
        for port in lport:
            print("port: %s\tstate: %s" % (port, nm[host][proto][port]['state']))
