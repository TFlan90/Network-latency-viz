from pythonping import ping
import matplotlib.pyplot as plt
# Returns network latency statistics (min, max, avg RTT, packet loss % ) 
# and the full ping response object from pythonping
def ping_target(ip_or_hostname:str, quantity:int,):
    responses = [ping(ip_or_hostname, count=1, interval=1) for _ in range(quantity)]
    return responses

#returns info about Round-Trip Times
def response_info(responses):
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

responses = (ping_target(ip_or_hostname,quantity))

stats = response_info(responses,)

for k, v in stats.items():
    print(f"{k} : {v}")



for resp in responses:
     print(f"{resp.rtt_avg_ms:.2f} ms {'(success)' if resp.success else '(failed)'}")



#Plotting
# x-axis: Ping number 
# y-axis: RTT Round-Trip Time
# Get RTTs for all pings, including handling failures for plotting purposes

#ping numbers 1-quantity(of pings)
x_values = list(range(1, quantity + 1))
y_values = []
colors = []
#return blue for successful and red for failed ping
for resp in responses:
    if resp.success:
        y_values.append(resp.rtt_avg_ms)
        colors.append('blue')
    else:
        y_values.append(0)
        colors.append('red')

# generate scatter plot
plt.figure(figsize=(12, 6))

# Plot successful pings
success_x = [i for i, resp in enumerate(responses) if resp.success]
success_y = [resp.rtt_avg_ms for resp in responses if resp.success]
plt.scatter([x + 1 for x in success_x], success_y, color='blue', label='Successful Ping', s=50)

## Adding lines to connect successful pings
if len(success_x) > 1:
    plt.plot([x + 1 for x in success_x], success_y, color='lightblue', linestyle='-', linewidth=1, zorder=1)

plt.title(f"Ping RTTs to {ip_or_hostname}")
plt.xlabel("Ping Number")
plt.ylabel("Round-Trip Time (ms)")
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.xticks(x_values)  # Ensure x-ticks align with ping numbers
plt.tight_layout()  # Adjust layout to prevent labels from overlapping
plt.show()





