# 0x0F. Load balancer

### Concepts

- [Load balancer](https://intranet.alxswe.com/concepts/46)
- [Web stack debugging](https://intranet.alxswe.com/concepts/68)

## Resources
**Read or watch:**

- [Introduction to load-balancing and HAproxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts#load-balancing-algorithms)
- [HTTP header](https://www.techopedia.com/definition/27178/http-header)
- [Debian/Ubuntu HAProxy packages](https://haproxy.debian.net/)

## Requirements

#### General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7) without any error
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing

## Tasks

#### 0. Double the number of webservers

In this first task you need to configure **web-02** to be identical to **web-01**. Fortunately, you built a Bash script during your [web server project](https://github.com/BlightG/alx-system_engineering-devops/blob/master/0x0C-web_server/4-not_found_page_404), and they’ll now come in handy to easily configure **web-02**. Remember, always try to automate your work!

Since we’re placing our web servers behind a load balancer for this project, we want to add a custom Nginx response header. The goal here is to be able to track which web server is answering our HTTP requests, to understand and track the way a load balancer works. More in the coming tasks.

Requirements:

- Configure Nginx so that its HTTP response contains a custom header (on **web-01** and **web-02**)
    - The name of the custom HTTP header must be **X-Served-By**
    - The value of the custom HTTP header must be the hostname of the server Nginx is running on
- Write **0-custom_http_response_header** so that it configures a brand new Ubuntu machine to the requirements asked in this task
    - Ignore SC2154 for shellcheck
