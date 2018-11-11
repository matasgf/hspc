import sys

for line in sys.stdin:
    srv_hours, srv_rate, stor_gb, stor_rate, bw, bw_rate = line.split()
    srv_cost = float(srv_hours) * float(srv_rate)
    stor_cost = float(stor_gb) * float(stor_rate)
    bw_cost = float(bw) * float(bw_rate)

    total_cost = round(srv_cost + stor_cost + bw_cost, 2)

    print("{0:0.2f}".format(total_cost))
