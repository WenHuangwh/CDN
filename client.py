# import socket
# from dnslib import DNSRecord, QTYPE, DNSQuestion

# def main():
#     dns_server_ip = "127.0.0.1"  # Change this to your DNS server's IP address
#     dns_server_port = 20020  # Change this to the port your DNS server is running on
#     buffer_size = 1024

#     dns_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     http_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#     req_domain = input("Enter domain name for which you need IP address and content: ")

#     # Resolve the domain using the DNS server
#     question = DNSQuestion(req_domain, qtype=QTYPE.A)
#     request = DNSRecord(q=question)
#     dns_sock.sendto(request.pack(), (dns_server_ip, dns_server_port))
#     data, _ = dns_sock.recvfrom(buffer_size)
#     response = DNSRecord.parse(data)
#     print(response)

#     if response.rr:
#         http_server_ip = str(response.rr[0].rdata)
#         http_server_port = 20020  # Change this to the port your HTTP server is running on
#         print(f"The IP for the domain name {req_domain} is: {http_server_ip}")

#         # Fetch the content from the HTTP server
#         http_sock.connect((http_server_ip, http_server_port))
#         http_request = f"GET /{req_domain} HTTP/1.1\r\nHost: {http_server_ip}\r\n\r\n"
#         http_sock.sendall(http_request.encode())
#         data = http_sock.recv(buffer_size)
#         print(f"Content received from HTTP server at {http_server_ip}:\n{data.decode()}")
#     else:
#         print(f"No IP found for the domain name {req_domain}")

#     dns_sock.close()
#     http_sock.close()

# if __name__ == "__main__":
#     main()


import socket
from dnslib import DNSRecord, QTYPE, DNSQuestion

def main():
    dns_server_ip = "127.0.0.1"  # Change this to your DNS server's IP address
    dns_server_port = 20020  # Change this to the port your DNS server is running on
    buffer_size = 1024

    dns_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    http_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    req_domain = input("Enter domain name for which you need IP address and content: ")

    # Resolve the domain using the DNS server
    question = DNSQuestion(req_domain, qtype=QTYPE.A)
    request = DNSRecord(q=question)
    dns_sock.sendto(request.pack(), (dns_server_ip, dns_server_port))
    data, _ = dns_sock.recvfrom(buffer_size)
    response = DNSRecord.parse(data)
    print(response)

    if response.rr:
        http_server_ip = str(response.rr[0].rdata)
        http_server_port = 20020  # Change this to the port your HTTP server is running on
        print(f"The IP for the domain name {req_domain} is: {http_server_ip}")

        # Fetch the content from the HTTP server
        http_sock.connect((http_server_ip, http_server_port))
        http_request = f"GET /{req_domain} HTTP/1.1\r\nHost: {http_server_ip}\r\n\r\n"
        http_sock.sendall(http_request.encode())
        data = http_sock.recv(buffer_size)
        print(f"Content received from HTTP server at {http_server_ip}:\n{data.decode()}")
    else:
        print(f"No IP found for the domain name {req_domain}")

    dns_sock.close()
    http_sock.close()

if __name__ == "__main__":
    main()
