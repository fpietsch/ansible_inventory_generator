# ansible_inventory_generator

usage: generate.py [-h] [pairs [pairs ...]]
Generiert dynamisch aus den Eingabe Parameter ein Ansible Inventory.

positional arguments:
-pairs 
Pairs of Hostname:ips:globalvars:specificvar=values[:specificvar=values]
Pattern: Hostname:ip,ip,...:globalvar1,globalvar2,...:specificvar1=value1,value2,...:specificvar2=value1,value2,...

examples:
web_server:10.2.3.1,10.2.3.2:ansible_become=true,ansible_user=ubuntu,ansible_become_method=su,ansible_become_exe='"sudo su -"':nodeip=192.0.0.1,192.0.0.2
es_data_nodes:10.0.0.1:ansible_become=true

optional arguments:
-h, --help show this help message and exit

example-input:
python usr/local/bin/generate.py cassandra:10.10.10.1,10.10.10.2:ansible_become=true:nodeip=192.0.0.1,192.0.0.2

example-output:
[cassandra]
cassandra-10.10.10.1 ansible_host=10.10.10.1 ansible_become=true nodeip=192.0.0.1
cassandra-10.10.10.2 ansible_host=10.10.10.2 ansible_become=true nodeip=192.0.0.2
