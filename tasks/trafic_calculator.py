raw = [x.split(" ") for x in open("log.txt")]

rmp = {}
for ip, traffic in raw:
    if ip in rmp:
        rmp[ip] += int(traffic)
    else:
        rmp[ip] = int(traffic)

rmp_list = sorted(rmp.items(), key=lambda x: x[1], reverse=True)
[print(i[0], i[1]) for i in rmp_list]
