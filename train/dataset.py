# import tensorflow as tf
import os

D = []


def filter_data(filepath):
    filtered = []
    with open(filepath) as f:
        lastline = [None, None, None]
        for line in f:
            line = [int(i) for i in line.strip().split()]
            if line[1] == 16 and line[2] == 1 and \
                    lastline[1] == 16 and lastline[2] == 0:
                filtered.pop(-1)
            else:
                filtered.append(line)
                lastline = line
    return filtered


def extract_features(filtered_data):
    H = []
    DD = []
    UD = []
    IRT = []
    B = []
    s = {}
    released_time = {}
    key_index = 0
    last_key_down = None
    previous2_key_down = None
    for t, k, a in filtered_data:
        if a == 0:
            key_index += 1
            s[k] = t
            if last_key_down:
                DD.append((t-last_key_down[0])/1000)
            previous2_key_down = last_key_down
            last_key_down = (t, k, a)
        else:
            released_time[(k, s[k])] = t
            duration = (t - s[k])/1000
            H.append(duration)
            if previous2_key_down:
                B.append((t - previous2_key_down[0])/1000)

    last_key_down_pair = None
    for t, k, a in filtered_data:
        if a == 0:
            if last_key_down_pair:
                UD.append((t-released_time[last_key_down_pair])/1000)
            last_key_down_pair = (k, t)

    for i in range(len(H)-1):
        try:
            IRT.append(H[i+1]/H[i])
        except ZeroDivisionError as e:
            IRT.append(H[i+1]/0.05)
    # print(H)
    # print(DD)
    # print(UD)
    # print(B)
    # print(IRT)
    result = H + DD + UD + B + IRT
    result.extend([0] * (96-len(result)))
    return result


def parse_user_data(dir):
    features = []
    for entry in os.scandir(dir):
        if entry.is_file():
            features.append(extract_features(filter_data(entry.path)))
    return features


def read_data(dir):
    users = []
    X = []
    Y = []
    for entry in os.scandir(dir):
        if not entry.name.startswith('.') and entry.is_dir():
            user_data = parse_user_data(entry.path)
            X.extend(user_data)
            users.append((entry.name, len(user_data)))

    index = 0
    for user, data_count in users:
        one_hot = [0] * len(users)
        one_hot[index] = 1
        index += 1
        for _ in range(data_count):
            Y.append(one_hot)
    return [X, Y]
