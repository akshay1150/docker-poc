#!/usr/bin/env python
"""
@license: Licensed Materials - Property of GSLab

@copyright: (c) Copyright GSLab. All Rights Reserved

@note: Note to India Government Users Restricted Rights: Use, duplication or
disclosure restricted by GSA ADP
Schedule Contract with GSLab.
"""

# import docker
import json
# client = docker.from_env()
# cont = client.containers.list()


class Container(object):
    """
    getting container
    paramters
    """

    def __init__(self):
        pass

    def container_param(self, container_id):
        """
        method return a dictionary 
        of container parameters
	:param container_id
        """
        list1 = ["AppArmorProfile", "HostConfig", "Mounts", "Config"]
        hostconfig = ["SecurityOpt", "CapAdd", "Privileged", "ReadonlyRootfs",
                      "CpuShares", "Memory", "RestartPolicy", "CgroupParent", "UTSMode", "Ulimits"]
        NetworkSetting = ["Ports"]
        dit = {}
        cmd = []
        cont1 = client.containers.get(container_id).attrs
        for var in list1:
            if(var == "HostConfig"):
                for hostconf in hostconfig:
                    if(hostconf == "RestartPolicy"):
                        dit.update(
                            {hostconf: str(cont1[var][hostconf]["MaximumRetryCount"])})
                    else:
                        dit.update({hostconf: str(cont1[var][hostconf])})
            elif(var == "Config"):
                cmd = json.dumps(cont1[var]["Cmd"])

            else:
                    dit.update({var: str(cont1[var])})
            dit.update({})
        return dit


CONT = Container()
