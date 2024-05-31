data=open('./input',"r").read().strip()
dataParts=data.split('\n\n')

seeds =list(map(int,dataParts[0].split(":")[1].split())) 
seed_maps = dataParts[1:]
mapping_lists=[]
locations=[]

for m in seed_maps:
    lines=m.split("\n")[1:]
    mapping = []
    for line in lines:
        dst, src, range_len = map(int, line.split())
        mapping.append((dst, src, range_len))
    mapping_lists.append(mapping)


for seed in seeds:
    for mapping in mapping_lists:
        for dst, src, range_len in mapping:
            if seed in range(src, src + range_len):
                seed = seed + dst - src
                break
    locations.append(seed) 

result1 = min(locations)
print(result1)

seeds2 = [(seeds[i], seeds[i]+seeds[i + 1]) for i in range(0, len(seeds), 2)]

for m in seed_maps:
    lines=m.split("\n")[1:]
    mapping = []
    for line in lines:
        mapping.append(list(map(int, line.split())))
    final=[]
    i = 0
    while i < len(seeds2):
        start, end=seeds2[i]
        transformed = False

        for dst, src, range_len in mapping:
            # max start of 2 range. 
            overlap_start=max(start,src)
            # min end of 2 range 
            overlap_end=min(end,src+range_len)
            if overlap_end>overlap_start:
                final.append((overlap_start-src+dst, overlap_end-src+dst))
                transformed = True
                if overlap_start > start:
                    seeds2.append((start, overlap_start))
                if overlap_end < end:
                    seeds2.append((overlap_end,end))
                break
        if transformed == False:
            final.append((start,end))
        i+=1
    seeds2=final

# print(seeds2)
print(min(seeds2)[0])
            



