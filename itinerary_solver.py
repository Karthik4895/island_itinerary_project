from collections import deque

def plan_itinerary(H, customers_prefs):
    hop_state = [False] * H
    C = len(customers_prefs)
    bysea_count = [0] * C
    hop_to_bysea_customers = [[] for _ in range(H)]
    for ci, (bysea_list, _) in enumerate(customers_prefs):
        for hop in bysea_list:
            if 0 <= hop < H:
                bysea_count[ci] += 1
                hop_to_bysea_customers[hop].append(ci)
    
    queue = deque()
    for ci, (bysea_list, airborne_hop) in enumerate(customers_prefs):
        if bysea_count[ci] == 0:
            if airborne_hop is not None:
                if not hop_state[airborne_hop]:
                    queue.append(airborne_hop)
            else:
                return None
    while queue:
        hop = queue.popleft()
        if hop_state[hop]:
            continue
        hop_state[hop] = True
        for ci in hop_to_bysea_customers[hop]:
            if bysea_count[ci] > 0:
                bysea_count[ci] -= 1
            if bysea_count[ci] == 0:
                airborne_hop = customers_prefs[ci][1]
                if airborne_hop is not None:
                    if not hop_state[airborne_hop]:
                        queue.append(airborne_hop)
                else:
                    return None
    return ["airborne" if hop_state[i] else "by-sea" for i in range(H)]