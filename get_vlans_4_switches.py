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
                                    <bd-items/>
                                </System>
                            </filter>
                           '''
            netconf_response = m.get(filter=version_filter)
#            print(netconf_response)
            vlan_list = []
            xml_name = netconf_response.data_xml
            dict_name = xmltodict.parse(xml_name)
            max_vlans = int(dict_name["data"]["System"]["bd-items"]["allVlans"])
            print("\nSwitch", dict_name["data"]["System"]["name"], "has", max_vlans, "vlans")
#            print("Number of vlans", dict_name["data"]["System"]["bd-items"]["allVlans"])
            if max_vlans == 1:
                vlan_list.append(int(dict_name["data"]["System"]["bd-items"]["bd-items"]["BD-list"]["id"]))
#                print(dict_name["data"]["System"]["bd-items"]["bd-items"]["BD-list"]["id"])
            else:
                for nn in range(max_vlans):
                    vlan_list.append(int(dict_name["data"]["System"]["bd-items"]["bd-items"]["BD-list"][nn]["id"]))
#                    print(dict_name["data"]["System"]["bd-items"]["bd-items"]["BD-list"][nn]["id"])
#            print(dict_name["data"])
            vlan_list.sort()
            print("List of vlans:")
            print(*vlan_list, sep = ", ")
           
if __name__ == '__main__':
    main()
