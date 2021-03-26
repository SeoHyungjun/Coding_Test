def solution(table, languages, preference):
  table = [t.split() for t in table]  # 직업군 언어 점수
  answer = {"SI":0, "CONTENT":0, "HARDWARE":0, "PORTAL":0, "GAME":0}

  for i, lang in enumerate(languages):
    for tt in table:
      for idx in range(1,len(tt)):
        if tt[idx] == lang:
          answer[tt[0]] += (6-idx)*preference[i]

  answer = sorted([k for k,v in answer.items()], key=lambda x: x[1])
  return answer[0]

ded 