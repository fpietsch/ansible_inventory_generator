import sys
from argparse import ArgumentParser

def parse_args():
    
    parser = ArgumentParser()
    parser.add_argument('pairs', help='--Pairs of Hostname:ips:globalvars:specificvar=values[:specificvar=values]--Pattern: Hostname:ip,ip,...:globalvar1,globalvar2,...:specificvar1=value1,value2,...:specificvar2=value1,value2,... --example: es_data_nodes:10.0.0.1:ansible_become=true or web_server:10.2.3.1,10.2.3.2:ansible_become=true,ansible_user=ubuntu,ansible_become_method=su,ansible_become_exe=\'"sudo su -"\':nodeip=192.0.0.1,192.0.0.2',nargs='*')
    return vars(parser.parse_args())

if __name__ == '__main__':
    args = parse_args()
    for pair in args['pairs']:
        host_pair = pair.split(":")
        host_group_name = host_pair[0]
        host_ips = host_pair[1].split(",")
        #host_single_vars = host_pair[2].split(";")
        #int number_of_single_vars = len(host_single_vars)

        host_vars = host_pair[2].split(",")
        host_vars_string = ""
        for var in host_vars:
            host_vars_string+=" "
            host_vars_string+=var
        print """
[{0}]""".format(host_group_name)
        i = 0
        for ip in host_ips:
            print """{0}-{1} ansible_host={1}{2}""".format(host_group_name,ip,host_vars_string),
            j = 0
            for specific_var in host_pair:
                j = j + 1
                if j <= 2:
                    continue
                if len(specific_var.split("=")) != 2:
                    continue
                specific_var_name = specific_var.split("=")[0]
                specific_var_list = specific_var.split("=")[1].split(',')
                if i >= len(specific_var_list):
                    continue
                print """{0}={1}""".format(specific_var_name,specific_var_list[i])
            i = i + 1
                
