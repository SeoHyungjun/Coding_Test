def solution(table, languages, preference):
    answer = {"SI":0, "CONTENTS":0, "HARDWARE":0, "PORTAL":0, "GAME":0}
    new_table = [t.split() for t in table]

    for i, lang in enumerate(languages):
        for t in new_table:
            for index in range(1, len(t)):
                if t[index] == lang:
                    answer[t[0]] += (6 - index)*preference[i]

    return sorted(answer.items(), key=lambda x : (-x[1], x[0]))[0][0]


table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]	
preference = [7, 5, 5]	
print(solution(table, languages, preference))

table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]	
preference = [7, 5]
print(solution(table, languages, preference))