# EbooksPortal

## Pre-Requisites
1. [python](https://www.python.org/)
2. [mysql](https://www.mysql.com/)
3. [git](https://git-scm.com/)

## Setup
1. create a folder named `ExamPortal` and clone the repository into that folder.
```shell
 git clone https://github.com/Ajay2810-hub/EbooksPortal.git
```
2. install virtualenv to create a virtual environment of any name & activate it using below commands.
```shell
 pip install virtualenv
 virtualenv [name]
 [name]\Scripts\activate
```
3. install the project dependencies
```shell
 pip install -r requirements.txt
```
4. create the database & migrate it with the initial data by using the below command.
```
 python mysql_migration.py [root_user] [root_user_password] createsuperuser loaddata
```
**Note**: You will be asked to fill username, email & password for superuser account.