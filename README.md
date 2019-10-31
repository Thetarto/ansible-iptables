# ansible-iptables
Ansible role meant to install iptable and configure some rules

## Tested plateform
* Debian 9 (Stretch)
* Debian 10 (Buster)

## Role variables

The path where the rule file will be created:
```
iptables_rules_path: /usr/local/iptables
```
List of all allowed output TCP port, for everywhere:
```
iptables_allowed_output_tcp_ports:[]
```
List of all allowed output UDP port, for everywhere:
```
iptables_allowed_output_udp_ports:[]
```
List of all allowed input TCP port, from everywhere:
```
iptables_input_allowed_tcp_port: []
```
List of all allowed input UDP port, from everywhere:
```
iptables_input_allowed_udp_port: []
```
List of all allowed input TCP port, but with restricted source:
```
iptables_allowed_restricted_input_tcp_ports:
  - {ip:xx.xx.xx.xx, port:yyy}
  - {ip:zz.zz.zz.zz, port:yyy}
```
List of all allowed input UDP port, but with restricted source:
```
iptables_allowed_restricted_input_udp_ports:
  - {ip:zz.zz.zz.zz, port:yyy}
```
List of all allowed input TCP port, with restricted source, with transfer from a port to another:
```
iptables_input_transfert_allowed_tcp_port:
- {ip:xx.xx.xx.xx, sport:yyy, dport:zzz}
```

## Examples
## Installation
```
ansible-galaxy install thetarto.iptables
```
## License
