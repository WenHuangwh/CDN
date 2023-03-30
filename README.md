# CDN
Hight-level approach:
1. DNS Server: The DNS server is responsible for resolving domain names to their respective IP addresses. It is implemented using Python's socket module and the dnslib library. The server listens for incoming requests, processes the queries, and sends back appropriate responses with either the IP address of the HTTP server or a root server IP address.

2. HTTP Server: The HTTP server is designed to serve content from an origin server. It is implemented using Python's socket and http.client modules. The server listens for incoming requests, retrieves content either from its cache or the origin server, and sends back the appropriate HTTP response. The cache is maintained as an OrderedDict with a size limit, and it is periodically saved to a file.

3. Local Test File: We use a test file called client.py to test the DNS and HTTP server implementation locally. It takes a domain name as input, resolves the IP address using the DNS server, and fetches the content from the HTTP server.

4. Bash Script: There are 3 Bash shell scripts to deploy, run, and stop DNS and HTTP servers remotely on specified cloud nodes. These script takes command line arguments for the port, origin server, CDN-specific name, SSH username, and the SSH key file. These scipts will operate the DNS and HTTP servers on the specific cloud nodes with the provided configuration. 

Challenges:
1. Logging in to the cloud node using the SSH key. Firstly, we needed to generate an SSH key pair and submit the public key to the system administrator to gain access to the cloud nodes. Secondly, We had to add the private key to the SSH agent on our local machine to manage the keys securely and simplify the authentication process. Finally, we had to use the correct port number and username to log in to the cloud nodes. This involved learning how to properly configure the SSH client and troubleshoot issues related to permissions and connectivity in order to establish a secure connection to the cloud nodes.

2.The second challenge we faced was understanding the entire processing logic of the client. At the beginning, we were quite confused about what the input and output of the two servers looked like, as well as how the output of the dnsserver was passed on to the httpserver. Ultimately, we decided to write a client myself to better understand the servers from the perspective of the client.

3.Implementing cache management in the HTTP server, including periodical cache writing to a file and constraining the cache size to 20MB. Also, we implemented a signal handler in the HTTP server to ensure that the cache is written to a file when the server is stopped, and incorporating this into the stop script.

Collaboration:
1. Xiaoyao implemented the DNS server, including handling queries and sending appropriate responses.

2. Wen implemented the HTTP server, including the content retrival.

3. We design a local test file to ensure the functionality of our DNS and HTTP servers works well both locally and in the cloud. 
