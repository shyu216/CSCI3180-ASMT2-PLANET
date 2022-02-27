# CSCI3180-ASSIGNMENT2-PLANET

### xubuntu share files in vmware
```
sudo vim /etc/fstab
.host:/ /mnt/hgfs fuse.vmhgfs-fuse allow_other,defaults 0 0
```

### connect internet
``` 
ip link
sudo ip link set ens33 up
sudo dhclient ens33 -v
```

### makefile
```
make target
make run
```

### powershell in vscode
    crtl + `

### md 分隔符
<div STYLE="page-break-after: always;"></div>