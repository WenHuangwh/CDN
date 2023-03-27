import socket
from dnslib import DNSRecord, QTYPE, DNSQuestion

def main():

    hostname = socket.gethostname()
    ipaddr = "127.0.0.1"
    dns_server_port = 20020  # Change this to the port your DNS server is running on

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = (ipaddr, dns_server_port)

    c = "y"
    while c.upper() == "Y":
        req_domain = input("Enter domain name for which you need IP address: ")
        question = DNSQuestion(req_domain, qtype=QTYPE.A)
        request = DNSRecord(q=question)
        s.sendto(request.pack(), addr)
        data, address = s.recvfrom(1024)
        response = DNSRecord.parse(data)
        print(response)

        if response.rr:
            print(f"The IP for the domain name {req_domain} is: {response.rr[0].rdata}")
        else:
            print(f"No IP found for the domain name {req_domain}")

        c = input("Continue? (y/n) ")

    s.close()



if __name__ == "__main__":
    main()
