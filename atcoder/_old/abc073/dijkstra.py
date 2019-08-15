# 初期のノード間の距離のリスト
route_list = [[0, 50, 80, 0, 0],
              [0, 0, 20, 15, 0 ],
              [0, 0, 0, 10, 15],
              [0, 0, 0, 0, 30],
              [0, 0, 0, 0, 0]]

# ノードの数
node_num = len(route_list)

# 未探索ノード
unsearched_nodes = list(range(node_num))

# ノードごとの距離のリスト
distance = [math.inf] * node_num

# 最短経路でそのノードのひとつ前に到達するノードのリスト
previous_nodes = [-1] * node_num

# 初期のノードの距離は0とする
distance[0] = 0


def get_target_min_index(min_index, distance, unsearched_nodes):
    start = 0
    while True:
        index = distance.index(min_index, start)
        found = index in unsearched_nodes
        if found:
            return index
        else:
            start = index + 1


while len(unsearched_nodes) != 0:
    # まず未探索ノードのうちdistanceが最小のものを選択する

    # 最小のdistanceを見つけるための一時的なdistance。初期値は inf に設定。
    possible_min_distance = math.inf

    # 未探索のノードのループ
    for node_index in unsearched_nodes:
        # より小さい値が見つかれば更新
        if possible_min_distance > distance[node_index]:
            possible_min_distance = distance[node_index]

    # 未探索ノードのうちで最小のindex番号を取得
    target_min_index = get_target_min_index(possible_min_distance, distance, unsearched_nodes)

    # ここで探索するので未探索リストから除去
    unsearched_nodes.remove(target_min_index)

    # ターゲットになるノードからのびるエッジのリスト
    target_edge = route_list[target_min_index]
    for index, route_dis in enumerate(target_edge):
        if route_dis != 0:
            # 過去に設定されたdistanceよりも小さい場合はdistanceを更新
            if distance[index] > (distance[ target_min_index] + route_dis):
                distance[index] = distance[ target_min_index] + route_dis

                # 　ひとつ前に到達するノードのリストも更新
                previous_nodes[index] =  target_min_index