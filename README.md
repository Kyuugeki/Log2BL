# Log2BL
A extra security layer for OpenSSH-enabled servers

In the docstring:
    As everyone knows, thousands of bots are trying to get access to servers by
    using default or common credentials.
    This script is meant to block every access trial from every host who previously
    tried to access the server with an invalid username.
    

I wrote this script while trying to solve a problem in a specific Virtual Private Server, running Ubuntu 20.0
No special dependencies for Python3 are required, so i think you're fine with whathever Linux distribution you're using. 
Maybe you'll need to change some details, like the auth log location, perhaps.
