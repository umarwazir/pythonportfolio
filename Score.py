#Copyright: Umar Wazir (Creative Commons Attribution)
#Defining the generic formula for each station.
def collate(x, y, tot, portion):                        
    collate = ((((float(x) + float(y)) / 2)/float(tot)) * float(portion))
    return collate
#Prompting and calculating scores for each station.
print "Enter the score for the relevant station when prompted."
portfolio1 = raw_input("Portfolio station (1st interviewer):")
portfolio2 = raw_input("Portfolio station (2nd interviewer):")
portfolio = collate(portfolio1, portfolio2, 55, 20)
clinical1 = raw_input("Clinical scenario (1st interviewer):")
clinical2 = raw_input("Clinical scenario (2nd interviewer):")
clinical = collate(clinical1, clinical2, 20, 15)
clinicalmanagement1 = raw_input("Clinical management scenario (1st interviewer):")
clinicalmanagement2 = raw_input("Clinical management scenario (2nd interviewer):")
clinicalmanagement = collate(clinicalmanagement1, clinicalmanagement2, 20, 10)
communication1 = raw_input("Communication scenario (1st interviewer):")
communication2 = raw_input("Communication scenario (2nd interviewer):")
communication = collate(communication1, communication2, 30, 10)
team1 = raw_input("Leadership and team-working (1st interviewer):")
team2 = raw_input("Leadership and team-working (2nd interviewer):")
team = collate(team1, team2, 25, 15)
ac1 = raw_input("Academic scenario (1st interviewer):")
ac2 = raw_input("Academic scenario (2nd interviewer):")
ac = collate(ac1, ac2, 20, 10)
aud1 = raw_input("Audit scenario (1st interviewer):")
aud2 = raw_input("Audit scenario (2nd interviewer):")
aud = collate(aud1, aud2, 20, 5)
skills1 = raw_input("Technical skills station (1st interviewer):")
skills2 = raw_input("Technical skills station (2nd interviewer):")
skills = collate(skills1, skills2, 25, 15)
#Collating and printing the final score.
score = portfolio + clinical + clinicalmanagement + communication + team + ac + aud + skills
print "Your total score is ", score
