#Author = Varfolomeev Nikita Denisovich
#Group = P3112
#61

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


def main():
    file_content = open("Timetable.TOML", 'r', encoding='utf-8').read()
    result_object = parse_schedule(file_content)
    print(result_object)


if __name__ == "__main__":
    main()