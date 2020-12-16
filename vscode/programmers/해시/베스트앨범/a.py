def solution(genres, plays):
    answer = []

    total_play = {}

    for i in range(len(genres)):
        if genres[i] in total_play:
            total_play[genres[i]] = total_play[genres[i]] + plays[i]
        else:
            total_play[genres[i]] = plays[i]

    total_play = sorted(total_play.items(), key = lambda item: item[1], reverse = True)
    #print(total_play)

    gen_rank = {}
    for gen, play, i in zip(genres, plays, range(len(genres))):
        #print(gen, play, i)
        if gen in gen_rank:
            gen_rank[gen].append((i, play))
        else:
            gen_rank[gen] = [ (i, play) ]

    #print(gen_rank)

    for total_gen, x in total_play:
        gen_rank[total_gen].sort(key = lambda x: x[1], reverse = True)
        #print(gen_rank[total_gen])
        for i in range(2):
            if gen_rank[total_gen]:
                answer.append(gen_rank[total_gen][0][0])
                gen_rank[total_gen].pop(0)


    return answer


gen = ['classic', 'pop', 'classic', 'classic', 'pop']
play = [500, 600, 150, 800, 2500]
print(solution(gen, play))