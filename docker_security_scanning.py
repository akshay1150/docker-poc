import connection_methods
import image_operations
import container_operations
import sys

container_obj = container_operations.Container()
image_object = image_operations.Image()

def localhost_security_scanning():
    host_os_name = connection_methods.check_host_os()
    if host_os_name == 'windows':
        print("we are not supporting the windows os")
        print("exiting from security scan...")
        sys.exit()
    docker_running_status = connection_methods.is_docker_running()
    print("after status: ",docker_running_status)
    if docker_running_status == True:
        docker_connected_status, docker_client = connection_methods.connect_docker_daemon()
        if docker_connected_status == True:
            images_list = image_object.get_images(docker_client)
            print("image list :", images_list)
            image_info = image_object.get_image('redis', docker_client)
            print("image :", image_info)
        # container_list = container_obj.get_containers()
        # print("container list:", container_list)


def remote_host_security_scanning():
    remote_host_ip, username, password, port_number = connection_methods.get_remote_host_information()
    connection_methods.is_host_reachable(remote_host_ip)

    host_os_name = connection_methods.check_host_os()
    if host_os_name == 'windows':
        print("we are not supporting the windows os")
        print("exiting from security scan...")
        sys.exit()
    


def get_connection():
    """
    Promt user for the information required to create a connection 
    """
    print("==================================================================================================")
    print("==================================================================================================")
    print("Welcome to the Docker security scanning Tool")
    print("==================================================================================================")
    print("==================================================================================================")
    
    print("On which host you want to do docker security scanning, please select correct option \n 1. Localhost \n 2. Remote host")
    host_type_option = int(input("Select a option : "))
    if host_type_option == 1:
        print("Selected host is a localhost.")
        localhost_security_scanning()
    elif host_type_option == 2:
        print("Selected host is a remote host.")
        remote_host_security_scanning()
    else:
        print("please insert correct option")

get_connection()
