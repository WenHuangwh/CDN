# CDN
High-level approach:
    To implement a CDN based on the project requirements, we need to include the following elements: DNS redirection, a simple web server, latency or performance measurement, and a cache strategy.

    We decided to use the Object-Oriented Design (OOD) programming paradigm for our project. First, we deployed both the HTTP and DNS servers to all replica servers. Next, we used a socket to establish communication between the HTTP server and the DNS server, allowing us to obtain latency information from the client to the HTTP server.

    For caching, we employed a library called 'cache' to store the most frequently viewed content on the HTTP replica. Finally, we used the 'scamper' tool to measure the latency to a client IP address and assess the overall performance of our implementation.

Implementations:
1. DNS Server: The DNS server uses DNS redirection to route clients to the best replica server for a CDN based on the latency between the client and the replica servers. It consists of a class called ReplicaManager that use a thread to periodically get the latency between the server and the client. Then select the replica with the lowest latency as the best replica. And another class called DNS server, which represents the actual DNS server that processes client queries and responds with the best replica server IP addresses. 

2. HTTP Server: The HTTP server comprises three classes: LatencyServer, CacheManager, and HTTPServer. The HTTPServer class manages incoming HTTP requests, utilizes the CacheManager class to handle caching of frequently viewed content, measures latency to clients using the Scamper tool and the LatencyServer class, and fetches content from the origin server when it's not available in the cache. The cache libray cache is built in CacheManager based on the avilable distribution file that lists the most frequently viewed pages. 

3. Bash Script: There are 3 Bash shell scripts to deploy, run, and stop DNS and HTTP servers remotely on specified cloud nodes. These script takes command line arguments for the port, origin server, CDN-specific name, SSH username, and the SSH key file. These scipts will operate the DNS and HTTP servers on the specific cloud nodes with the provided configuration. 

Challenges:
1. Measure and log the latency. Initially, we measured the latency between the client and the DNS server, but soon realized that it's the latency between the client and the replica that should be used to determine the best replica. After deploying DNS and HTTP servers to all replicas, we discovered that there wasn't a direct communication channel between them, as they might be on different hosts. Upon reviewing the project description, we understood that the testing process would ensure both the DNS and HTTP servers are on the same host, and we wouldn't need to worry about the distance between web clients and their DNS servers. Ultimately, we chose to use a TCP socket to establish a connection between the DNS and HTTP servers to obtain the latency.

2. Caching strategy. As we have the data of the request frequency for each piece of content and understand that it will be fixed the whole time. We think it may be easier and more managerable to have the same cache library in each replica. By doing this, the CDN will be able to serve the most popular content directly from its cache, reducing the load on the origin server and providing faster response times to the clients. And using the same cache library can maintain the consistency and ease the problem of sychonization among replica. 

3. Testing: Initially, we attempted to use print statements for debugging and recording various information such as latency, the IP address returned by the DNS server, timestamps, and more. However, we quickly realized that the print statements would only be displayed on the machine running the DNS server, not on the local machine. To overcome this limitation, we decided to implement a logging system to record and debug the program. This approach allows us to easily access and analyze the recorded data from any machine, making the debugging and monitoring processes more efficient and convenient.

4. Cloud Node Collaboration: Any modifications to the HTTP and DNS servers require the redeployment of scripts across all replicas. To minimize disruptions and ensure efficient collaboration, we needed to carefully coordinate our testing and development efforts. By working together and planning our changes, we were able to minimize interruptions and prevent conflicts, allowing each team member to focus on improving the codebase without hindering the overall progress.

Future work:
We chose to use a cache library that stores the most frequently accessed content. This library is deployed on all replicas, enabling the replica with the lowest latency to quickly retrieve the content that clients are most likely to request.
Given more time, we might explore implementing popular caching algorithms such as Least Recently Used (LRU) or Least Frequently Used (LFU).

Collaboration:
Xiaoyao was responsible for the design of dns server. She comes up with the idea of periodically logging the latency information in a separate thread. Wen refactors the code into OOD style and use encapsulation to increase the readability. Xiaoyao is also in charge of the documentation of the project and ensure that we were using the correct command and different approach to test the project. 
Wen was mainly working on implementing the cache strategy that involving turning the view-frequency of content into a cache library. 
We discussed and tested different apparoch on getting and logging latency. Wen implemented a TCP socket to establish the communication between dns and http server.
