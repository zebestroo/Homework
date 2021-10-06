import csv
def get_top_performers(file_path, number_of_top_students=5):
    students = []
    marks = []
    top = []
    fl = open(file_path) 
    rdr = csv.reader(fl)
    next(rdr)
    for row in rdr:
        students.append(row)
        marks.append(row[2])
    i = 0
    while i < number_of_top_students:
        max_mk = max(marks)
        top.append(students[marks.index(max_mk)][0])
        students.pop(marks.index(max_mk))
        marks.pop(marks.index(max_mk))
        i += 1
    print(top)
get_top_performers("../data/students.csv")
        
def sort_by_age(file_path, file_path_w = "new_file.csv"):
    students = []
    dc = {}
    fl = open(file_path)
    rdr = csv.reader(fl)
    intr_str = next(rdr)
    for row in rdr:
        students.append(row)
    fl.close()
    for stud in students:
        dc.setdefault(stud[1], [])
        dc[stud[1]].append(stud)
    fl = open(file_path_w, "w")
    wrtr = csv.writer(fl)
    wrtr.writerow(intr_str)
    for key in reversed(sorted(dc.keys())):
        wrtr.writerows(dc[key])
    fl.close()

sort_by_age("../data/students.csv")

