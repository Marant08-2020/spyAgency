# spyAgency
Test SpyAgency

This challange is on based in python 3.9 and Djaango 4.1

To provide a solution to this challenge, it is proposed to make use of user roles:

1. **Boss**
2. **Manager**
3. **Hitman**

Using a relational model of vfive tables called: 
1. users. For logging control and configuration of the roles is_boss for boss, is_manager for manager and is_hitman. 

2. manager. to store the data of this type of user. 
3. boss control.   Control the data generic.           
4. hitman. storage of each of them.
5. Hits. they are mission assigned to each hitman.

It has a one-to-one relationship between user-manager, user-boss, user-manager, and user-hitma, another one-to-many relationship between manager-hitma, 
and a many-to-many relationship between hitman-hits. So a boss has roles manager and hitman to have full access to the system.

Steps for its configuration:


1. Clone the repository `git clone https://github.com/Marant08-2020/spyAgency.git` 

2. Seaarch the directory  with cd `spyAgency`

3. Create the repository `python -m venv env`

4. Install packages with `pip: -r requirements.txt`

5. Get in to spyAgency\spyAgency and run `python manage.py runserver`

MIT License

Marco Antonio Mojica Martinez 
mojicamarc@gmail.com


