import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import paramiko
import docker
import ipaddress
import socket, os



def is_host_reachable(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0

reachable = is_host_reachable("192.168.311.205")
print("reachable:::",reachable)


def get_remote_host_information():
    """
    get remote host information from a user like
    IP address, username, password
    """
    ip = input("Please enter the remote host IP address :")
    print(type(ip))
    print(ip)
    try:
        socket.inet_aton(ip)
        print("Valid ip address")
    except socket.error:
        print("Invalid IP")
    username = input("Please enter the username of remote host :")
    password = input("Please enter the password of remote host :")
    port_number = int(input("Enter ssh port number :"))
    return ip, username, password, port_number


def check_host_os():
    """
    Return name of the host OS
    """

    # assigining host os name to the host_os_name parameter
    host_os_name = platform.system()
    return host_os_name

# host_os = check_host_os()
# print("Host OS name:", host_os)

# host_ip, username, password , port_number = get_remote_host_information()

def connect_remote_host_using_ssh(host_ip, username, password, port_number):
    "Login to the remote server"
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(host_ip, port_number, username, password)

    cmd="pip install docker"
    stdin, stdout, stferr = ssh_client.exec_command(cmd)
    outlines = stdout.readlines()
    resp = ''.join(outlines)
    print(resp)
    connect_docker_daemon()

# print(connect_remote_host_using_ssh( host_ip, username, password, port_number))

def connect_docker_daemon():
    """
    Connect to the docker deamon 
    """
    result_flag = False
    try:
        client = docker.from_env()
        print(client)
        result_flag = True

    except Exception as e:
        print("Exception in connecting to the docker server")
        print("PYTHON SAYS:", e)

    return result_flag, client


# print(connect_docker_daemon())


def is_docker_running():
    """
    checks docker daemon is running or not
    return True if docker service is running
    """
    docker_status = os.system('systemctl is-active docker')
    print("docker status:",docker_status)
    if docker_status == 0 :
        return True
    return False

