# PyChatServer
repository for python networking training 

What’s the Problem?
Online chatting is quite common. Many chat services of various kinds (IRC, instant messaging services, and so forth) are available all over the Internet. Some of these are even full-fledged text-based virtual worlds (see http://www.mudconnect.com for a long list). If you want to set up a chat server, you can just download and install one of the many free server programs. However, writing a chat server yourself is useful for two reasons:
• You learn about network programming.
• You can customize it as much as you want.
The second point suggests that you can start with a simple chat server and develop it into basically any kind of server (including a virtual world), with all the power of Python at your fingertips. Pretty awesome, isn’t it?
For now, the chat server project has the following requirements:
• The server should be able to receive multiple connections from different users.
• It should let the users act in parallel.
• It should be able to interpret commands such as say or logout.
• The server should be easily extensible.
The two things that will require special tools are the network connections and the asynchronous nature of the program.
