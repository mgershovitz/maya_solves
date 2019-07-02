class Island(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

class Bridge(object):
    def __init__(self, I1, I2, danger_grade):
        self.I1 = I1
        self.I2 = I2
        self.danger_grade = danger_grade

    def __repr__(self):
        return str(self.danger_grade)


def add_bridge_islands(map_v, bridge):
    for island_set in map_v:
        found_i1 = bridge.I1 in island_set
        found_i2 = bridge.I2 in island_set
        if found_i1 and found_i2:
            return 0
        if found_i1 and not found_i2:
            island_set.add(bridge.I2)
            return 1
        elif found_i2 and not found_i1:
            island_set.add(bridge.I1)
            return 1

    map_v.append({bridge.I1, bridge.I2})
    return 2

def create_map(V, E):
    if len(V) <= 1:
        return E
    import IPython
    IPython.embed()
    ordered_bridges = sorted(E, key=lambda x: x.danger_grade)
    islands_count = 0

    map_e = list()
    map_v = list()
    for bridge in ordered_bridges:
        added_islands = add_bridge_islands(map_v, bridge)
        if added_islands:
            map_e.append(bridge)
            islands_count += added_islands
        if islands_count == len(V) and len(map_v) == 1:
            break

    return list(map_e)


def run_tests():
    A = Island("A")
    B = Island("B")
    C = Island("C")
    D = Island("D")
    V = [A, B, C, D]
    #
    # e_1 = Bridge(A,B,1)
    # e_2 = Bridge(A,D,6)
    # e_3 = Bridge(A,C,2)
    # e_4 = Bridge(B,C,3)
    # e_5 = Bridge(D,C,8)
    # E = [e_1, e_2, e_3, e_4, e_5]
    # assert create_map(V,E) == [e_1,e_3,e_2]

    e_1 = Bridge(A,B,1)
    e_2 = Bridge(A,D,3)
    e_3 = Bridge(A,C,10)
    e_4 = Bridge(B,C,4)
    e_5 = Bridge(D,C,2)
    E = [e_1, e_2, e_3, e_4, e_5]
    print (create_map(V,E))
    assert create_map(V,E) == [e_1,e_5,e_3]


if __name__ == '__main__':
    run_tests()