#!/usr/bin/env python
"""
@license: Licensed Materials - Property of GSLab

@copyright: (c) Copyright GSLab. All Rights Reserved

@note: Note to India Government Users Restricted Rights: Use, duplication or
disclosure restricted by GSA ADP
Schedule Contract with GSLab.
"""
import json
import docker

# client = docker.DockerClient(base_url='tcp://localhost:4243')
# client = docker.from_env()


class Image(object):
    """
    Fetches the
    Image attributes
    """

    def __init__(self):
        pass

    def get_images(self, client):
        """
        Getting all 
        the Images
        """
        image_list = client.images.list(all=False)
        count = 0
        image_dict = dict()
        for image in image_list:
            image_name = json.dumps(client.images.get(
                image_list[count].id).attrs["RepoTags"])
            image_id = json.dumps(client.images.get(
                image_list[count].id).attrs["Id"])
            image_dict[image_name] = image_id
            count = count+1
        return image_dict

    # @classmethod
    def get_image(self, image_id, client):
        """ 
        image by id
        and by name
        """
        image_values = dict()
        # images = client.images.list()

        #fetching the image values
        try:
            image_name = client.images.get(image_id).attrs['RepoTags']
            image_created = client.images.get(image_id).attrs['Created']
            image_architecture = client.images.get(
                image_id).attrs['Architecture']
            image_os = client.images.get(image_id).attrs['Os']
            image_docker_version = client.images.get(
                image_id).attrs['DockerVersion']
            image_hostname = client.images.get(
                image_id).attrs['ContainerConfig']['Hostname']
            if not image_hostname:
                image_hostname = None
            image_user = client.images.get(
                image_id).attrs['ContainerConfig']['User']
            if not image_user:
                image_user = None
            check_containerconfig = client.images.get(
                image_id).attrs['ContainerConfig'].keys()
            if 'ExposedPorts' in check_containerconfig:
                image_exposed_ports = client.images.get(
                    image_id).attrs['ContainerConfig']['ExposedPorts']
            else:
                image_exposed_ports = None
            if 'Healthcheck' in check_containerconfig:
                health_check = client.images.get(
                    image_id).attrs['ContainerConfig']['Healthcheck']['Test']
            else:
                health_check = None

            image_size = client.images.get(image_id).attrs['VirtualSize']
        except:
            print ("fetching attributes failed")
        # print(image_Exposed_Ports)

        # adding values to dictionary
        image_values['name'] = image_name[0]
        image_values['created_Time'] = image_created
        image_values['architecture'] = image_architecture
        image_values['os'] = image_os
        image_values['docker_version'] = image_docker_version
        image_values['host_name'] = image_hostname
        image_values['user'] = image_user
        image_values['expose_port'] = image_exposed_ports
        image_values['image_size'] = image_size # Divide by 1024*1024
        image_values['health_check'] = health_check

        # print(json.dumps(image_values))
        return json.dumps(image_values)


# print Image.get_images()
# print Image.get_image_id(
#     "sha256:5976dac61f4fb85c1a2d1f7c717600f9c78fb02badba6b3c5961a4091ef75905")
INST = Image()
# print (INST.get_images())
# print INST.get_image_id("sha256:5976dac61f4fb85c1a2d1f7c717600f9c78fb02badba6b3c5961a4091ef75905")
# print (INST.get_image_id("redis"))
