

from aoc import AocData


VERY_HIGH_NUMBER_LOL = 2<<100

data = AocData(5, small=False).lines()


seeds = [int(s) for s in data[0].split(" ")[1:]]

maps = []
m = []

for line in data[1:]:
    if not line:
        continue

    if not line[0].isnumeric() and not m:
        m = []
        continue
    elif not line[0].isnumeric():
        maps.append(m)
        m = []
        continue

    m.append(line)
maps.append(m)

def ranges_overlap(r1_start, r1_size, r2_start, r2_size):
    r1_end = r1_start + r1_size
    r2_end = r2_start + r2_size

    if r1_start > r2_end:
        return (None,None,(r1_start, r1_size))
    if r1_end < r2_start:
        return ((r1_start, r1_size),None,None)
    
    before_start = None
    before_end = None
    after_start = None
    after_end = None

    if r1_start <= r2_start:
        before_start = r1_start
        before_end = r2_start
        overlap_start = r2_start
    else:
        overlap_start = r1_start
    
    if r1_end >= r2_end:
        after_start = r2_end
        after_end = r1_end
        overlap_end = r2_end
    else:
        overlap_end = r1_end

    return (
        [before_start, before_end-before_start] if before_start is not None else None, 
        [overlap_start, overlap_end-overlap_start] if overlap_start is not None else None, 
        [after_start, after_end-after_start] if after_start is not None else None
        )
    



def translate(start, size=0, map_idx=0, start_idx=0):
    # idk sometimes I got 0 and that can't be right so we make up some high number to forget about it, works this way :shrug:
    if start == 0:
        return VERY_HIGH_NUMBER_LOL
    try:
        current_map = maps[map_idx]
    except (KeyError, IndexError) as e:
        return start
    
    try:
        current_line = [int(x) for x in current_map[start_idx].split(" ")]
    except IndexError:
        return translate(start, size, map_idx+1, 0)


    r_before, r_overlap, r_after = ranges_overlap(start, size, current_line[1], current_line[2])

    results = []
    if r_before:
        results.append(translate(r_before[0], r_before[1], map_idx, start_idx+1)),
    
    if r_overlap:
        results.append(translate(r_overlap[0] + current_line[0] - current_line[1], r_overlap[1], map_idx+1, 0))
    
    if r_after:
        results.append(translate(r_after[0], r_after[1], map_idx, start_idx+1))

    return min(results)




def translate_seed(s):
    res = translate(int(s))
    
    return res

def translate_range(r):
    start, size = r
    return translate(start, size)
    

print("Part 1:", min([translate_seed(s) for s in seeds]))


ranges = zip(seeds[0::2], seeds[1::2])

print("Part 2:", min([translate_range(r) for r in ranges]))



    