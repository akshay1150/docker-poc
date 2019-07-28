#!/usr/bin/env python
"""
@license: Licensed Materials - Property of GSLab

@copyright: (c) Copyright GSLab. All Rights Reserved

@note: Note to India Government Users Restricted Rights: Use, duplication or
disclosure restricted by GSA ADP
Schedule Contract with GSLab.
"""
import docker
import json

client = docker.from_env()
#cont = client.containers.list()
class Container(object):
    """
    getting container
    paramters
    """

    def __init__(self):
        pass

    def container_list(self):
        ID=[]
        Name=[]
        cont = client.containers.list()
        for var in cont:
            Id.append(str(var.attrs["Id"]))
            Name.append(str(var.attrs["Name"]))
        info = dict( zip( Id, Name))
        return info

    def container_param(self,container_id):
        """
        method return a dictionary 
        of container parameters
        """
        list1=["AppArmorProfile","Mounts"]
        hostconfig=["SecurityOpt","CapAdd","Privileged","ReadonlyRootfs","CpuShares","Memory","CgroupParent","UTSMode","Ulimits","PidMode","Devices"]
        dit={}
        cont1=client.containers.get(container_id).attrs
        for var in list1:
            dit.update({var:str(cont1[var])})
        for hostconf in hostconfig:
            dit.update({hostconf:str(cont1["HostConfig"][hostconf])})
        dit.update({"RestartPolicy": cont1["HostConfig"]["RestartPolicy"]})
        dit.update({"Ports":cont1["NetworkSettings"]["Ports"]})
        dit.update({"Cmd":[x.encode('utf-8') for x in cont1["Config"]["Cmd"]]})
        return dit
CONT=Container()
print(CONT.container_param('8b8d9005c94f'))

