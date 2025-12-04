import sys
import time
import Informatics_parsing
import Informatics_parsing1
import Informatics_parsing2
import Informatics_parsing3

input_file = open("Timetable.TOML", 'r', encoding='utf-8').read()
time_start = time.time()
for i in range(100):
    Informatics_parsing.parse_schedule(input_file)
time_end = time.time()
print("Informatics_parsing: " + str(time_end - time_start))

time_start = time.time()
for i in range(100):
    Informatics_parsing1.parse_schedule(input_file)
time_end = time.time()
print("Informatics_parsing1: " + str(time_end - time_start))

time_start = time.time()
for i in range(100):
    Informatics_parsing2.main()

time_end = time.time()
print("Informatics_parsing2: " + str(time_end - time_start))

time_start = time.time()
for i in range(100):
    Informatics_parsing3.parse_schedule(input_file)
time_end = time.time()
print("Informatics_parsing3: " + str(time_end - time_start))