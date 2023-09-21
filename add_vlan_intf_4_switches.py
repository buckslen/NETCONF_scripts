from ncclient import manager
import sys
from lxml import etree
import xmltodict

devices = [
        {"address" : "198.18.129.1",
        "netconf_port" : 830,
        "username" : "admin",
        "password" : "cisco"},
        {"address" : "198.18.129.2",
        "netconf_port" : 830,
        "username" : "admin",
        "password" : "cisco"},
        {"address" : "198.18.129.3",
        "netconf_port" : 830,
        "username" : "admin",
        "password" : "cisco"},
        {"address" : "198.18.129.4",
        "netconf_port" : 830,
        "username" : "admin",
        "password" : "cisco"}]

def main():

    for device in devices:
        with manager.connect(host=device["address"],
                             port=device["netconf_port"],
                             username=device["username"],
                             password=device["password"],
                             hostkey_verify=False) as m:

                add_vlan = """
                           <config>
                             <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
                                <intf-items>
                                  <phys-items>
                                    <PhysIf-list>
                                      <id>eth1/13</id>
                                      <mode>access</mode>
                                      <layer>Layer2</layer>
                                      <accessVlan>vlan-100</accessVlan>
                                    </PhysIf-list>
                                  </phys-items>
                                </intf-items>
                             </System>
                           </config>
                           """
                netconf_response = m.edit_config(target="running", config=add_vlan)
                print(netconf_response) 
if __name__ == '__main__':
    main()
