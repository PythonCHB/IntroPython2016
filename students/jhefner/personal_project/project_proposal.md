<h2>Project: </h2><h3>
Ansible Dynamic Inventory</h3>

This tool's purpose is to interface with the command line tool `ansible`. (https://www.ansible.com/)

This is going to be a tool for myself to use at work and eliminate a _*LARGE*_ amount of manual mysql, grep, awk and other data work.

The python program will need to do the following:

* Connect to mysql a remote mysql server and run select commands.
* Take data from mysql select commands and create a specifically structured dictionary for Ansible to ingest.
* Create a json output from the program for the `ansible` command line tool to ingest.

The will hopefully be featured enough to:

* Parse multiple options sent to it via the command line.
* Output useful verbose information to stdout (for validation of what is being sent to `ansible`).