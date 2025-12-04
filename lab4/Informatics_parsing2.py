#Author = Varfolomeev Nikita Denisovich
#Group = P3112
#61

import tomli
import yaml

input_file = "Timetable.TOML"
output_file = "Timetable.YAML"

def main():
    with open(input_file, "rb") as f:
        data_object = tomli.load(f)

    yaml_content = yaml.dump(
        data_object,
        allow_unicode=True,
        default_flow_style=False
    )


    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(yaml_content)

if __name__ == "__main__":
    main()