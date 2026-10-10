def pipeline(pool):
    stages = [("generated", list(pool))]
    stages.append(("endpoints", filter_start_end(stages[-1][1])))
    stages.append(("length", filter_length(stages[-1][1])))
    for vertex, kept in filter_all_vertices(stages[-1][1], range(1, 6)):
        stages.append((f"contains {vertex}", kept))
    stages.append(("verified", [p for p in stages[-1][1] if is_witness(p)]))
    return stages
