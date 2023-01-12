# 0x0C. Web server

### Concepts

For this project, we expect you to look at this concept:

- [What is a Child Process?](https://intranet.alxswe.com/concepts/110)

## Background Context

In this project, some of the tasks will be graded on 2 aspects:

1. Is your web-01 server configured according to requirements
2. Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)

For example, if I need to create a file `/tmp/test` containing the string **hello world** and modify the configuration of Nginx to listen on port **8080** instead of **80**, I can use **emacs** on my server to create the file and to modify the Nginx configuration file **/etc/nginx/sites-enabled/default**.

But my answer file would contain:

	sylvain@ubuntu cat 88-script_example
	#!/usr/bin/env bash
	# Configuring a server with specification XYZ
	echo hello world > /tmp/test
	sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
	sylvain@ubuntu

As you can tell, I am not using **emacs** to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an [SRE](https://www.atlassian.com/incident-management/devops/sre), that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the **root** user, you do not need to use the **sudo** command.

A good Software Engineer is a [lazy Software Engineer](https://www.techwell.com/techwell-insights/2013/12/why-best-programmers-are-lazy-and-act-dumb).

Tips: to test your answer Bash script, feel free to reproduce the checker environment:

- start a Ubuntu 16.04 sandbox
- run your script on it
- see how it behaves

## Resources

**Read or Watch**

- [How the web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
- [Nginx](https://en.wikipedia.org/wiki/Nginx)
- [How to Configure Nginx](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04)
- [Child process concept page](https://intranet.alxswe.com/concepts/110)
- [Root and sub domain](https://landingi.com/help/domains-vs-subdomains/)
- [HTTP requests](https://www.tutorialspoint.com/http/http_methods.htm)
HTTP redirection
Not found HTTP response code
Logs files on Linux

**For reference:**

RFC 7231 (HTTP/1.1)
RFC 7540 (HTTP/2)

**man or help:**

scp
curl 
