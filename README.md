# loganalysis

# Project 3: Logs Analysis Project
### By MADDI VENKATA DINESH

Logs Analysis Project, part of the Udacity [Full Stack Web Developer
Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## Project Overview

A Reporting page that prints out reports in a plain text format based on the data in the database.This reporting tool is a python program using the `psycopg2` module to connect to the database.

## Files in the project

This project consists for the following files are:

* LogAnalysis_Udacity.py - main file to run this Logs Analysis Reporting tool
* README.md - instructions to install this reporting tool
* newsdata.sql - database file
* OutPut.png

## Requirement tools for the project

1. Python
2. Vagrant
3. VirtualBox


## Dependencies

- [Vagrant](https://www.vagrantup.com/)
- [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

## How to Install and Run
Install Vagrant & VirtualBox
- For Create Vagrant file,Command:`vagrant init ubuntu/xenial64`
- For Connect to VirtualMachine,Command:`vagrant up`
- For Login to VirtualMachine,Command: `vagrant ssh`
- For Exit from current directory,Command: `cd ..`
- We should Again exit directory,Command:cd ..`
- For Changing directory path,Command:cd vagrant`
- For Update ubunut version using,command:`sudo apt-get update``

## We have to install postgresql

- Install postgresql using command `sudo apt-get install postgresql`
- Connect to postgres using command `psql su - postgres`

## We have to install modules

- Import psycopg2 module to connect database using command `pip install psycopg2`
- Create super user vagrant
- Create news database with owner vagrant using command `create database news;`
- Change ownership of database using command `alter database news owner to vagrant;`
- Exit the current running status using command `\q`
- Logout from the current user using command `logout`
-load the data in local database using the command:
  ```
    $ psql -d news -f newsdata.sql
  ```
- run `python log_ana.py`

# To run Python script use the below code
python filename.py;
python LogAnalysis_Udacity.py; 

#Creation of views
# To create views we have to connect to the psql.

##views used in this project
view1:  CREATE VIEW logstar AS
SELECT count(*) as stat, 
status, cast(time as date) as day
FROM log WHERE status like '%404%'
GROUP BY status, day
ORDER BY stat desc limit 3;

	
view2:	CREATE VIEW totalvisitors AS
SELECT count(*) as visitors,
cast(time as date) as errortime
FROM log
GROUP BY errortime;


view3:	CREATE VIEW logs AS
SELECT to_char(time,'DD-MON-YYYY') as Date, count(*) as LogCount
FROM log
GROUP BY Date;


view4: CREATE VIEW errorlogs AS
SELECT to_char(time,'DD-MON-YYYY') as Date, count(*) as ErrorCount
FROM log
WHERE STATUS = '404 NOT FOUND'
GROUP BY Date;


### Final OutPut
```

(i)*What are the most popular three articles of all time ?

 Candidate is jerk, alleges rival -- 338647 views
 Bears love berries, alleges bear -- 253801 views
 Bad things gone, say good people -- 170098 views

(ii)**Who are the most popular article authors of all time ?

 "Ursula La Multa" -- 507594 views
 "Rudolf von Treppenwitz" -- 423457 views
 "Anonymous Contributor" -- 170098 views
 "Markoff Chaney" -- 84557 views

(iii)***Days on which more than 1% of requests lead to errors ?
 On 17-JUL-2016   ===>   2.3% errors
```

## Miscellaneous
![OutPut.png]((https://github.com/maddivenkatadinesh/loganalysis_udacity/blob/master/OutPut.png))
