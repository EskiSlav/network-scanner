import nmap
import logging

# Initialize the nmap object
logger = logging.getLogger(__name__)

class Scanner:
    def __init__(self) -> None:
        logger.info("Scanner init...")
        self.nm = nmap.PortScanner()
        
        with open("network_documentation.txt", "w") as _:
            pass

    def ping_scan(self, network_range):        
        logger.info("Started ping scan...")
        # Perform the scan
        result = self.nm.scan(hosts=network_range, arguments='-sn')
        logger.debug(result)
        # Open a file to write the results to
        with open("network_documentation.txt", "a") as f:
            # Write the header for the file
            f.write("Ping Scan\n")
            f.write("----------------------\n\n")

            # Iterate through the hosts found during the scan
            for host in self.nm.all_hosts():
                f.write("Host: " + host + "\n")
                f.write("State: " + self.nm[host].state() + "\n")

                # Iterate through the services running on the host
                for proto in self.nm[host].all_protocols():
                    lport = self.nm[host][proto].keys()
                    for port in lport:
                        f.write("Port: " + str(port) + "\n")
                        f.write("Service: " + self.nm[host][proto][port]['name'] + "\n")
                        f.write("\n")
            f.write("Scan Complete\n\n")

    def ssh_scan(self, network_range):
        logger.info("Started ssh scan...")
        result = self.nm.scan(hosts=network_range, arguments='-p22 --open')
        logger.debug(result)
        # Open a file to write the results to
        with open("network_documentation.txt", "a") as f:
            # Write the header for the file
            f.write("SSH Scan\n")
            f.write("----------------------\n\n")

            # Iterate through the hosts found during the scan
            for host in self.nm.all_hosts():
                # Verify that port 22 is open on the host
                if self.nm[host].has_tcp(22):
                    f.write("Host: " + host + "\n")
                    f.write("State: " + self.nm[host].state() + "\n")
                    f.write("Port 22: Open\n")
                    f.write("\n")
            f.write("Scan Complete\n\n")
    

    # def http_scan(self, network_range):
    #     logger.info("Started ssh scan...")
    #     result = self.nm.scan(hosts=network_range, arguments='-p80 --open')
    #     logger.debug(result)
    #     # Open a file to write the results to
    #     with open("network_documentation.txt", "a") as f:
    #         # Write the header for the file
    #         f.write("SSH Scan\n")
    #         f.write("----------------------\n\n")

    #         # Iterate through the hosts found during the scan
    #         for host in self.nm.all_hosts():
    #             # Verify that port 22 is open on the host
    #             if self.nm[host].has_tcp(22):
    #                 f.write("Host: " + host + "\n")
    #                 f.write("State: " + self.nm[host].state() + "\n")
    #                 f.write("Port 22: Open\n")
    #                 f.write("\n")
    #         f.write("Scan Complete\n\n")