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


def serialize_to_xml(data_object):
    xml_string = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_string += '<schedule>\n'

    for day_name, lessons in data_object.items():
        xml_string += f'  <day name="{day_name}">\n'
        for lesson in lessons:
            xml_string += '    <lesson>\n'
            for key, value in lesson.items():
                value = str(value).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                xml_string += f'      <{key}>{value}</{key}>\n'

            xml_string += '    </lesson>\n'

        xml_string += '  </day>\n'

    xml_string += '</schedule>'
    return xml_string


def main():
    input_file = "Timetable.TOML"
    output_file = "Timetable.xml"

    source_text = open(input_file, 'r', encoding='utf-8').read()
    binary_object = parse_schedule(source_text)
    xml_text = serialize_to_xml(binary_object)
    
    XML_output = open(output_file, 'w', encoding='utf-8').write(xml_text)




if __name__ == "__main__":
    main()