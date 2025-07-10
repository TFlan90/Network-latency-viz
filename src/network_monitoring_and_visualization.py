from pythonping import ping
import datetime

# Returns network latency statistics (min, max, avg RTT, packet loss % ) 
# and the full ping response object from pythonping
def getPingStats(ip_or_hostname:str, quantity:int,):
    responses = [ping(ip_or_hostname, count=1, interval=1) for _ in range(quantity)]
    return responses

def responseInfo(responses,quantity):
    rtts = [resp.rtt_avg_ms for resp in responses if resp.success]
    total = len(responses)
    success = len(rtts)
    failed = total - success

    if success > 0:
        min_rtt = min(rtts)
        max_rtt = max(rtts)
        avg_rtt = sum(rtts) / success
    else:
        min_rtt = max_rtt = avg_rtt = 0.0

    return {
        "Minimum wait time": f"{min_rtt:.2f} ms",
        "Maximum wait time": f"{max_rtt:.2f} ms",
        "Average wait time": f"{avg_rtt:.2f} ms",
        "Packets sent": total,
        "Packets received": success,
        "Packet loss": f"{(failed / total) * 100:.1f}%"
    }

    



ip_or_hostname = input("Give an IP address or hostname\n")
quantity = int(input("How many times should the address be pinged?\n"))

responses = (getPingStats(ip_or_hostname,quantity))

stats = responseInfo(responses,quantity)

for k, v in stats.items():
    print(f"{k} : {v}")

print("LINE BREAK")

for resp in responses:
     print(f"{resp.rtt_avg_ms:.2f} ms {'(success)' if resp.success else '(failed)'}")





