# CDN
High-level approach:
    To implement a CDN based on the project requirements, we need to include the following elements: DNS redirection, a simple web server, latency or performance measurement, and a cache strategy.

    We decided to use the Object-Oriented Design (OOD) programming paradigm for our project. First, we deployed both the HTTP and DNS servers to all replica servers. Next, we used a socket to establish communication between the HTTP server and the DNS server, allowing us to obtain latency information from the client to the HTTP server.

    For caching, we employed a library called 'cache' to store the most frequently viewed content on the HTTP replica. Finally, we used the 'scamper' tool to measure the latency to a client IP address and assess the overall performance of our implementation.

Implementations:
1. DNS Server: The DNS server uses DNS redirection to route clients to the best replica server for a CDN based on the latency between the client and the replica servers. It consists of a class called ReplicaManager that use a thread to periodically get the latency between the server and the client. Then select the replica with the lowest latency as the best replica. And another class called DNS server, which represents the actual DNS server that processes client queries and responds with the best replica server IP addresses. 

2. HTTP Server: The HTTP server has three classes: LantencyServer, CacheManager and HTTPServer. The HTTPServer class that manages incoming HTTP requests, employs a CacheManager class to handle caching of frequently viewed content, measures latency to clients using the Scamper tool and the LatencyServer class, and retrieves content from the origin server when not found in the cache.   

3. Bash Script: There are 3 Bash shell scripts to deploy, run, and stop DNS and HTTP servers remotely on specified cloud nodes. These script takes command line arguments for the port, origin server, CDN-specific name, SSH username, and the SSH key file. These scipts will operate the DNS and HTTP servers on the specific cloud nodes with the provided configuration. 

Challenges:
1. 


1 point - A short (no more than 2 pages) report describing the design decisions you made, how your evaluated their effectiveness and what you would do with more time. Include this in the README file.

Future work:
We decided to use a cache library that stores the most frequently used or viewd content. That library is deployed in all the replicas so that the replica with the lowest latency can easily get the content the client mostly likely wants. 
If we have more time, we may try to use popular caching algorithms like Least Recently Used (LRU) or Least Frequently Used (LFU).

Collaboration: