import os
import re

def read(directory):
    target_groups = {}
    pattern = re.compile(r"(\w+)_(\d+)_(tpf|lc|phase)\.png")
    for filename in os.listdir(directory):
        match = pattern.match(filename)
        if match:
            target_id, index, file_type = match.groups()
            if target_id not in target_groups:
                target_groups[target_id] = {'tpf': None, 'lc': None, 'phase': None}
            file_path = os.path.join(directory, filename)
            target_groups[target_id][file_type] = file_path
    result = []
    for target_id, group in target_groups.items():
        if all(group.values()):
            result.append({
                'target_id': target_id,
                'tpf': group['tpf'],
                'lc': group['lc'],
                'phase': group['phase']
            })
            for file_type in ['tpf', 'lc', 'phase']:
                os.remove(group[file_type])

    return result