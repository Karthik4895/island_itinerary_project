def parse_input(input_lines):
    H = int(input_lines[0].strip())
    C = int(input_lines[1].strip())
    customers_prefs = []
    for i in range(C):
        line = input_lines[2 + i].strip()
        bysea_list = []
        airborne_hop = None
        if line:
            pairs = [p.strip() for p in line.split(',')]
            for pair in pairs:
                if not pair:
                    continue
                parts = pair.split()
                if len(parts) < 2:
                    continue
                hop_str, mode = parts[0], parts[1].lower()
                hop = int(hop_str)
                if mode == "airborne":
                    airborne_hop = hop
                else:
                    bysea_list.append(hop)
        customers_prefs.append((bysea_list, airborne_hop))
    return H, customers_prefs