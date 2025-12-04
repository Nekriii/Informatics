# Author = Varfolomeev Nikita Denisovich
# Group = P3112
# 61

def parse_schedule(source_text):
    schedule = {}
    current_day_name = None
    current_lesson = {}

    for line in source_text.splitlines():
        line = line.strip()

        if not line or line.startswith('#'):
            continue

        if line.startswith('[['):
            if current_day_name and current_lesson:
                schedule[current_day_name].append(current_lesson)
                current_lesson = {}

            try:
                day_name_end = line.find('.')
                day_name = line[2:day_name_end].strip().strip('"')
                current_day_name = day_name

                if current_day_name not in schedule:
                    schedule[current_day_name] = []
            except:
                continue

        elif line.startswith('['):
            if current_day_name and current_lesson and current_lesson != {}:
                schedule[current_day_name].append(current_lesson)
                current_lesson = {}

            current_day_name = line[1:-1].strip().strip('"')
            if current_day_name not in schedule:
                schedule[current_day_name] = []

        elif '=' in line:
            try:
                parts = line.split('=', 1)
                key = parts[0].strip()
                value = parts[1].strip()

                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]

                if current_day_name is not None:
                    current_lesson[key] = value
            except:
                continue

    if current_day_name and current_lesson and current_lesson != {}:
        schedule[current_day_name].append(current_lesson)

    return schedule


def serialize_to_yaml(data_object):
    return _dump_node(data_object, indent=0)


def _dump_node(node, indent):
    output = ""
    prefix = "  " * indent

    if isinstance(node, dict):
        for key, value in node.items():
            output += f"{prefix}{key}:"

            if isinstance(value, (dict, list)):
                output += "\n" + _dump_node(value, indent + 1)
            else:
                output += f" {_escape_scalar(value)}\n"

    elif isinstance(node, list):
        for item in node:
            if isinstance(item, dict):
                keys = list(item.keys())
                if not keys:
                    continue

                first_k = keys[0]
                first_v = item[first_k]

                output += f"{prefix}- {first_k}: {_escape_scalar(first_v)}\n"

                inner_prefix = "  " * (indent + 1)
                for k in keys[1:]:
                    v = item[k]
                    output += f"{inner_prefix}{k}: {_escape_scalar(v)}\n"
            else:
                output += f"{prefix}- {_escape_scalar(item)}\n"

    return output


def _escape_scalar(val):
    s = str(val)
    if any(c in s for c in ":#[]{}") or s == "":
        return f'"{s}"'
    return s


def main():
    input_file = "Timetable.TOML"
    output_file = "Timetable.YAML"
    source_text = open(input_file, 'r', encoding='utf-8').read()

    binary_object = parse_schedule(source_text)
    yaml_text = serialize_to_yaml(binary_object)

    YAML_output = open(output_file, 'w', encoding='utf-8').write(yaml_text)



if __name__ == "__main__":
    main()