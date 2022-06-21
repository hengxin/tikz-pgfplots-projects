if __name__ == '__main__':
    # 箭头形状模板
    arrow_template = "\draw [color=brown ,draw opacity=0][fill=brown, fill opacity=0.5] {} -- {} -- {} -- {} -- {} -- {} -- cycle;"
    baseA = (80, 20)
    baseB = (135, 20)
    baseC = (140, 30)
    baseD = (135, 40)
    baseE = (80, 40)
    baseF = (85, 30)
    baseNodes = [baseA, baseB, baseC, baseD, baseE, baseF]
    
    width = 60
    # 学期文字模板
    semester_template = "\\node at {} {};"

    # 学期分割虚线模板
    dashed_template = "\draw [dashed]  {} -- {} ;"

    # 上课进度条模板
    ps_text_loc = 60  # 问题求解
    compiler_text_loc = 100  # 编译原理
    dm_text_loc = 140  # 离散数学
    cpp_text_loc = 180  # C语言


    def get_course_template(color, loc):
        return courses_template % (color, color, loc - 10, loc - 10, loc + 10, loc + 10)


    courses_template = "\draw [color=%s, draw opacity=0][fill=%s, fill opacity=0.3] ({}, %d) -- ({}, %d) -- ({}, %d) -- ({}, %d) -- cycle;"
    progress_templates = {
        'ps': get_course_template("red", ps_text_loc),
        'compiler': get_course_template("green", compiler_text_loc),
        'dm': get_course_template("violet", dm_text_loc),
        'cpp': get_course_template("blue", cpp_text_loc)
    }
    schedule = {
        'ps': [0, 1, 2, 3, 4, 5, 6],
        'compiler': [7, 9, 11],
        'dm': [8],
        'cpp': [9, 11]
    }

    # 课程文字模板
    courses_text_template = "\draw (-10,%d)  node [anchor=west][inner sep=0.75pt, align=right, font = \large] {%s};"
    courses_map = {
        '问题求解': ps_text_loc,
        '编译原理': compiler_text_loc,
        '离散数学': dm_text_loc,
        'C语言程序设计基础': cpp_text_loc,
    }

    arrows = []
    semesters = []
    dashes = []
    progresses = []
    courses = []

    for i in range(12):
        nodes = []
        for baseNode in baseNodes:
            nodes.append((baseNode[0] + width * i, baseNode[1]))
        arrows.append(arrow_template.format(nodes[0], nodes[1], nodes[2], nodes[3], nodes[4], nodes[5]))
        semesters_loc = (nodes[5][0] + 25, nodes[5][1])
        semesters_text = "{\\textbf{" + "{}-{}".format(2017 + i // 2, "春" if i % 2 == 0 else "秋") + "}}"
        semesters.append(semester_template.format(semesters_loc, semesters_text))

        dash_up = (nodes[2][0], ps_text_loc - 20)
        dash_down = (nodes[2][0], cpp_text_loc + 20)
        dashes.append(dashed_template.format(dash_up, dash_down))

    for k, terms in schedule.items():
        for i in terms:
            left = baseA[0] + width * i
            right = baseC[0] + width * i
            progresses.append(progress_templates[k].format(left, right, right, left))

    for course, loc in courses_map.items():
        courses.append(courses_text_template % (loc, course))

    for i in range(12):
        print(arrows[i])
        print(semesters[i])
        print(dashes[i])
    print()

    for progress in progresses:
        print(progress)
    print()

    for course in courses:
        print(course)
    print()
