from pyzabbix import ZabbixAPI

zapi = ZabbixAPI("http://localhost/zabbix")
zapi.login("Admin", "zabbix")

for h in zapi.host.get(output="extend"):
    print("Host: %s" % h["host"])
    for i in zapi.item.get(hostids=h["hostid"], output="extend"):
        print("  Item: %s" % i["name"])
        for g in zapi.graph.get(itemids=i["itemid"], output="extend"):
            print("    Graph: %s" % g["name"])
            for t in zapi.graphitem.get(graphids=g["graphid"], output="extend"):
                print("      Graph item: %s" % t["itemid"])