# A number of people are applying for a place in some team. Each of them has his own proficiency level (p.l.), which is represented as a positive integer, and the higher the level is - the better.
# There are only n places in the team, and the recruiter hires only those who have their p.l. not less than m.
# All applicants are standing in a queue and if the current one satisfies the required conditions, he is taken into the team right away. Once the team is full, all the remaining people are denied regardless of their p.l.
# What is the total p.l. of the applicants that get be hired? It is guaranteed that all n places can be taken.


def summaryProficiency(a, n, m):
    proficiency = 0
    hired = 0
    for appl in a:
        if hired < n:
            if appl >= m:
                hired+=1
                proficiency += appl
        else:
            break
    return proficiency
