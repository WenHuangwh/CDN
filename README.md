## Project 5: Roll Your Own CDN
# High-level approach:

# Cache strategy: 
We considered two strategies: a) latency-based, in which we store the most frequently accessed content statically and the DNS server distributes HTTP servers based on latency, and b) content-based, in which the DNS server checks if any HTTP server has the requested content in cache before distributing. After testing both strategies, we found that latency had a greater impact on total time, so we implemented a latency-based strategy.

# DNS-server: 
When a client reaches the DNS server, it checks if it has a record of the best HTTP server for this client. If not, the DNS server connects with each HTTP server to measure latency and stores the server with the lowest latency. All client-server mappings are stored in a cache, which the DNS server updates periodically.

# HTTP-server: 
Each time an HTTP server is run, it uses a websites.txt file containing website distribution information to build its content cache, which remains static. The HTTP server uses the Scamper daemon to measure latency to clients. The daemon runs in the background and is connected via a socket.
    
# Implementations:

DNS Server: Implemented using the dnspython library, the DNS server uses DNS redirection to route clients to the best replica server based on latency. It includes a ReplicaManager class that periodically measures latency between servers and clients, and a DNSServer class, which processes client queries and responds with the best replica server IP address.

HTTP Server: Implemented using Python's built-in http.server module, it consists of three classes: LatencyServer, CacheManager, and HTTPServer. The HTTPServer class manages incoming HTTP requests, uses CacheManager to handle caching, measures latency to clients using Scamper and LatencyServer, and fetches content from the origin server when not available in the cache. The cache library is built in CacheManager based on the available distribution file listing the most frequently viewed pages.

Bash Script: Three Bash scripts are used to deploy, run, and stop DNS and HTTP servers remotely on specified cloud nodes. They take command-line arguments for port, origin server, CDN-specific name, SSH username, and SSH key file. These scripts operate the DNS and HTTP servers on specific cloud nodes with the provided configuration.

Challenges:

1. Measuring latency: Initially, we measured the latency between the client and the DNS server, but soon realized that we should be using the latency between the client and the replica to determine the best replica. After deploying DNS and HTTP servers to all replicas, we discovered there wasn't a direct communication channel between them. To address this, we used a socket for communication between the DNS and HTTP servers.

2. Implementing Scamper: When we realized subprocess was not recommended, we considered alternatives like ping3. After carefully reading the Scamper manual, we found that we could create a Scamper daemon running in the background and use a socket for communication. We spent a significant amount of time finding the right way to communicate with the Scamper daemon from the HTTP server.

3. Caching strategy: Since we had data on the request frequency for each piece of content and understood that it would remain constant, we believed it would be easier and more manageable to have the same cache library in each replica. This approach allows the CDN to serve the most popular content directly from its cache, reducing the load on the origin server and providing faster response times to clients. Using the same cache library also maintains consistency and mitigates synchronization issues among replicas.

4. Testing: Initially, we attempted to use print statements for debugging and recording various information such as latency, IP addresses returned by the DNS server, timestamps, and more. However, we quickly realized that the print statements would only be displayed on the machine running the DNS server, not on the local machine. To overcome this limitation, we decided to implement a logging system to record and debug the program. This approach allows us to easily access and analyze the recorded data from any machine, making the debugging and monitoring processes more efficient and convenient.

5. Cloud Node Collaboration: Any modifications to the HTTP and DNS servers require the redeployment of scripts across all replicas. To minimize disruptions and ensure efficient collaboration, we needed to carefully coordinate our testing and development efforts. By working together and planning our changes, we were able to minimize interruptions and prevent conflicts, allowing each team member to focus on improving the codebase without hindering overall progress.

Collaboration:
We discussed and tested different approaches to cache strategies and decided to go with a latency-based HTTP server selection strategy. Xiaoyao was responsible for designing the DNS server, coming up with the idea of periodically logging latency information in a separate thread. Xiaoyao also managed the project's documentation, ensuring we used the correct commands and various approaches for testing. Wen primarily worked on implementing the HTTP server, including communication between the DNS server and HTTP server, as well as communication between the HTTP server and Scamper daemon.

