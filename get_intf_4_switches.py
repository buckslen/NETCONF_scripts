from ncclient import manager
import sys
from lxml import etree
import xmltodict

devices = [
        {"address" : "10.122.187.138",
        "netconf_port" : 830,
        "username" : "admin",
        "password" : "cisco!123"},
        {"address" : "10.122.187.139",
        "netconf_port" : 830,
        "username" : "admin",
        "password" : "cisco!123"},
        {"address" : "10.122.187.140",
        "netconf_port" : 830,
        "username" : "admin",
        "password" : "cisco!123"},
        {"address" : "10.122.187.141",
        "netconf_port" : 830,
        "username" : "admin",
        "password" : "cisco!123"}]

def main():

    for device in devices:
        with manager.connect(host=device["address"],
                             port=device["netconf_port"],
                             username=device["username"],
                             password=device["password"],
                             hostkey_verify=False) as m:

            version_filter = '''
                            <filter>
                                <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
                                  <name/>
                                  <intf-items>
                                    <phys-items>
                                      <PhysIf-list>
                                        <id>eth1/13</id>
                                        <layer/>
                                        <mode/>
                                        <accessVlan/>
                                      </PhysIf-list>
                                    </phys-items>
                                  </intf-items>
                                </System>
                            </filter>
                           '''
            netconf_response = m.get(filter=version_filter)
#            print(netconf_response)
            xml_name = netconf_response.data_xml
            dict_name = xmltodict.parse(xml_name)
#            print(dict_name)
            print("\nSwitch", dict_name["data"]["System"]["name"])
            print("Interface", dict_name["data"]["System"]["intf-items"]["phys-items"]["PhysIf-list"]["id"], dict_name["data"]["System"]["intf-items"]["phys-items"]["PhysIf-list"]["layer"], dict_name["data"]["System"]["intf-items"]["phys-items"]["PhysIf-list"]["mode"], dict_name["data"]["System"]["intf-items"]["phys-items"]["PhysIf-list"]["accessVlan"])
           
if __name__ == '__main__':
       main()
