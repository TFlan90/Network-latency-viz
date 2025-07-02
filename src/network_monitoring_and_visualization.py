from pythonping import ping

# Returns network latency statistics (min, max, avg RTT, packet loss % ) 
# and the full ping response object from pythonping
def getPingStats(ip_or_hostname:str, quantity:int):
    response = ping(ip_or_hostname, count=quantity)
    pingDict = {
                "Min MS Wait" : f"Minimum wait time was {response.rtt_min_ms} ms",
                "Max MS Wait" : f"Maximum wait time was {response.rtt_max_ms} ms",
                "Avg MS Wait" : f"Average wait time was {response.rtt_avg_ms} ms",
                "Packet Loss" : f"Percentage of packets dropped was {response.stats_lost_ratio}%\n"
                }
    return pingDict,response

    



ip_or_hostname = input("Give an IP address or hostname\n")
ping_quantity = int(input("How many times should the address be pinged?\n"))

responseStats,responses = (getPingStats(ip_or_hostname,ping_quantity))
for value in responseStats.values():
    print(value)

for response in responses:
    print(response)





