container = {
    "ExPosed_Ports": {
        "FAIL": range(0, 1024)
    },
    "Mount_Source": {
        "FAIL": ["/", "boot", "dev", "etc", "lib", "proc", "sys", "usr","docker.sock"]
    },
    "PidMode": {
        "FAIL": ["host"]
    },
    "MaximumRetryCount": {
        "FAIL": ["0"]
    },
    "Cmd": {
        "FAIL": ["sshd", "ssh"]
    },
    "Network_type": {
        "FAIL": ["host"]
    },
    "SecurityOpt": {
        "FAIL": ["SElinux-enable=false", "None"]
    },
    "CapAdd": {
        "PASS": ["None"]
    },
    "Devices": {
        "PASS": ["None", "[]", " "]
    },
    "Memory": {
        "FAIL": ["0"]
    },
    "UTSMode": {
        "FAIL": ["host"]
    },
    "ReadonlyRootfs": {
        "FAIL": ["False"]
    },
    "Exposed_IP": {
        "FAIL": ["0.0.0.0"]
    },
    "CpuShares": {
        "FAIL": ["0"]
    },
    "CgroupParent": {
        "FAIL": ["Null", "None"]
    },
    "Privileged": {
        "FAIL": ["True"]
    },
    "Ulimits": {
        "FAIL": ["Null", "None"]
    },
    "AppArmorProfie": {
        "FAIL": ["None"]
    },
}

images = {
    "health_check": {
        "FAIL" : ["None", "Null", " "]
    },
    "user": {
        "FAIL" : ["host", "None", "root"]
    },
    "external_port" : {
        "FAIL" : range(0,1024)
    }
}
