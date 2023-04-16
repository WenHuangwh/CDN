# Content Delivery Network (CDN) Implementation
This project implements a simple Content Delivery Network (CDN) with custom DNS and HTTP servers.

Project Overview
The project consists of two main Python scripts, dnsserver.py and httpserver.py, which implement the custom DNS and HTTP servers, respectively. In addition, there are three bash scripts, deployCDN.sh, runCDN.sh, and stopCDN.sh, which help with deploying, running, and stopping the CDN.

dnsserver.py
This script implements a custom DNS server that resolves incoming requests for the CDN's domain name to the closest HTTP server in the network based on the client's IP address.

httpserver.py
This script implements a custom HTTP server that serves content to clients. The server caches content from the origin server and serves it to clients when requested.

deployCDN.sh
This bash script deploys the custom DNS and HTTP server code to their respective servers. It also copies the website list to each HTTP server.

Usage: ./deployCDN.sh -p <port> -o <origin> -n <name> -u <username> -i <keyfile>

runCDN.sh
This bash script starts the custom DNS and HTTP servers on their respective machines.

Usage: ./runCDN.sh -p <port> -o <origin> -n <name> -u <username> -i <keyfile>

stopCDN.sh
This bash script stops the custom DNS and HTTP servers on their respective machines.

Usage: ./stopCDN.sh -p <port> -o <origin> -n <name> -u <username> -i <keyfile>

The high-level approach to implementing the custom DNS and HTTP servers for this CDN project is as follows:

DNS Server: The custom DNS server is implemented using the dnspython library. It listens for incoming DNS queries and processes them by resolving the CDN's domain name to the closest HTTP server in the network based on the client's IP address. The DNS server calculates the nearest HTTP server using a simple distance-based algorithm, selecting the server with the smallest round-trip time (RTT) to the client.

HTTP Server: The custom HTTP server is implemented using Python's built-in http.server module. It listens for incoming HTTP requests and serves content to clients. The HTTP server caches content from the origin server and serves it to clients when requested. The cache is initialized from the content listed in websites.txt. The server handles HTTP GET requests and, if the requested content is available in the cache, it serves the content to the client. Otherwise, it fetches the content from the origin server, updates the cache, and serves the content to the client.

Challenges faced during the implementation include:

Optimizing the DNS resolution: Determining the closest HTTP server based on the client's IP address can be challenging, as the accuracy of geolocation services varies. A more advanced technique, such as using Anycast or latency-based routing, could be employed to improve the performance of the DNS resolution process.

Cache management: The HTTP server's cache management is relatively simple, with no cache eviction policy in place. In a real-world scenario, it would be essential to implement cache management strategies like Least Recently Used (LRU) or Time-To-Live (TTL) to handle cache eviction effectively and efficiently.

Scalability: The current implementation works well for a small-scale CDN, but for a large-scale CDN, more advanced load balancing and server selection strategies would be needed to ensure optimal performance and resource utilization.