# Networking Notes

1. OSI Model (7 Layers)

The OSI(Open Systems Interconnection) Model was developed to standerised the ways computer/servers cpmmunicate with each 
other.It helps us understand how data moves across a network. It is a more theorectical concept.
 It has 7 layers from physical hardware up to applications.
  
7.Application Layer –It is implemented in software.The user interact with the application.Eg: web browsers, email 
clients,messaging apps, etc.
6.Presentation Layer –It data formats from numbers,words,etc into binary formats.It handles encryption/decryption
 ,extraction and also compression.It  uses various protocols such as HTTP,FTP,SSL.
5.Session Layer –It manages connections between applications (starting, maintaining, ending sessions/connection).
It also does the authentication and authorization stuff. 
4.Transport Layer –It transports and ensures data arrives correctly using TCP or UDP.It controls flow of data and
 error control.It also handles port numbers ,controls.In this level the data are divided into smal units as segments. 
3.Network Layer – It transmits or routes packets between devices/computers that is located in different network
 using IP addresses Its function is logical addressing.
2.Data Link Layer– It allows direct communication with the computers.It recieves packages data into frames, handles
 MAC addresses, error detection on a local network.
1.Physical Layer – The actual hardware: cables, switches, and signals (electrical, optical).It transmits the lists
 from electrical signal into bits and transports it over wires and local media.
---

 2. TCP vs UDP

| Feature            | TCP(Transmission Control Protocol                     | UDP(User Datagram Protocol)                                        |
| ------------------ | ----------------------------------------------------- | ------------------------------------------ |
| Connection Type    | Connection-oriented session                           | Connectionless session                     |
| Reliability        | Highly reliable (guarantees delivery)                 | Not reliable (no guarantee packets arrive) |
| Speed              | Slower due to error checking and acknowledgements     | Faster because there is no error checking  |
| Data Order         | Packets arrive in the correct order                   | Packets may arrive out of order            |
| Error Checking     | Errors are detected and packets are retransmitted     | Very limited error checking                |
| Flow Control       | It controls how fast data is sent                     | No flow control                            |
| Packet Type        | Segments                                              | Datagrams                                  |
| Ports              | Uses source & destination ports                       | Uses source & destination ports            |
| Use Cases          | Web browsing, emails, file transfers(as it requires   | Video streaming, online games, VoIP(as it  |
|                    | precise and coreect data sending)                     | requires  real-time updates and its just   |
|                    |                                                       | throws data)                               | 




 3. 10 Common Protocols and Port Numbers


| Protocol | Full Form                              | Port  | Description                                                  |
|----------|----------------------------------------|-------|------------------------------------------------------------ -|
| HTTP     | HyperText Transfer Protocol            | 80    | Defines how data is transferred (not encrypted)              |
| HTTPS    | HyperText Transfer Protocol Secure     | 443   | Secure version of HTTP using encryption (SSL/TLS)            |
| FTP      | File Transfer Protocol                 | 21    | Used to upload or download files between computers(transfer  |
|          |                                        |       | files)                                                       |
| SSH      | Secure Shell                           | 22    | Secure remote login to servers and systems                   |
| Telnet   | Telecommunication Network              | 23    | Used for terminal emulation to remotely access and control   |
|          |                                        |       |  another system                                              |
| SMTP     | Simple Mail Transfer Protocol          | 25    | Used for sending emails between mail servers                 |
| POP3     | Post Office Protocol Version 3         | 110   | Used to download/recieve emails from a server                |
| IMAP     | Internet Message Access Protocol       | 143   | Allows users to access and manage emails directly on the     |
|          |                                        |       |  server                                                      |
| DNS      | Domain Name System                     | 53    | Converts domain names into IP addresses                      |
| DHCP     | Dynamic Host Configuration Protocol    | 67/68 | Assigns IP addresses to devices/people                       |
| VNC      | Virtual Network Computing              | 5900  | Allows remote desktop access to control another computer     |
---

 4. How DNS Works (Step by Step)

DNS (Domain Name System) is used to find Ip addresses of servers/URL/http/websites. DNS is like a phonebook for the
 internet,translating names to numbers .i.e. translating domain names to ip addresses.DNS changes a website/URLS
 name into an IP address so the computer can find the correct server.

1. When we type a website addres/URLss in the browser.
2. The browser first checks if it already knows the IP address from previous visits.
3. If it doesn't know, it asks the DNS server provided by the internet service.
4. If that server does not have the answer, it asks other DNS servers on the internet.
5. The correct DNS server finds the IP address for that website.
6. The IP address is sent back to the browser.
7. The browser then connects to that IP address and loads the website.
---


