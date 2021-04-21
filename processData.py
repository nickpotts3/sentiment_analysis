# Create user object with proper variables
# Write the outcome to a new file in csv format
#FUNCTIONS NEEDED - processInitialReponse()
#                 - processDailyFive()
#                 - processIntegerScores()
#                 - processBooleanScores()
# After processing one user, store user object in array OR write to another file to save. Repeat till eof
# when determining average for numbers, have a counter variable to keep track of the number of entries for that attribute

class User: # the last index of each dictionary holds the overall score for that attribute
    
    def __init__(self, e) -> None:
        self.email = e
        self.eating_habit = []
        self.energy_level = []
        self.alone_sad_score = []
        self.lost_interest = []
        self.stress_factor = []
        self.total_score = 0.0
        self.tragic_event = False
        self.family_history = False
        self.gender = ''
    #User variables / attributes
   
    

    #User functions / methods
    def appendEating(self, value):
        if(value != ''):
            self.eating_habit.append(round(float(value), 2))

    def appendEnergy(self, value):
        if(value != ''):
            self.energy_level.append(round(float(value), 2))

    def appendAlone(self, value):
        if(value != ''):
            self.alone_sad_score.append(round(float(value), 2))
    
    def appendInterest(self, value):
        if( value == "No"):
            self.lost_interest.append(1.0)
        elif(value == "Yes"):
            self.lost_interest.append(10.0)
    def appendInterestAvg(self, value):
        self.lost_interest.append(round(float(value), 2))

    def appendStress(self, value):
        if(value != ''):
            self.stress_factor.append(round(float(value), 2))

    def clearAttributes(self):
        self.eating_habit.clear()
        self.energy_level.clear()
        self.alone_sad_score.clear()
        self.lost_interest.clear()
        self.stress_factor.clear()
    
    def calculate_average(self):
        self.appendEating( sum( self.eating_habit) / len(self.eating_habit))
        self.appendEnergy( sum( self.energy_level) / len(self.energy_level))
        self.appendAlone( sum( self.alone_sad_score) / len(self.alone_sad_score))
        self.appendStress( sum( self.stress_factor) / len(self.stress_factor))
        self.appendInterestAvg( sum( self.lost_interest) / len(self.lost_interest))
        self.total_score += (self.eating_habit[-1] + self.energy_level[-1] + self.alone_sad_score[-1] + self.stress_factor[-1] + self.lost_interest[-1]) / 5.0

    def printInfo(self):
        print("User {self.email} has eating habits of {self.eating_habit[0]} energy level of {self.energy_level} sad score of {self.alone_sad_score} interest has been lost? {self.lost_interest} and a stress factor of {self.stress_factor}" )

# --------------------------------------------------------------------------------------------------------

import csv
from types import new_class


overallMaleScore = 0.00
overallFemaleScore = 0.00
with open('dailyFive.csv', mode='r') as initial_response_file:
    csv_reader = csv.DictReader(initial_response_file)
    line_count = 0
    index = 0
    users = []
    pEmail = ""
    for row in csv_reader:
        #executed on first iteration

       # print(row)
        # line count is equal to our users index. We will add each user immeditaly into the list then work on the list index to append the results to it. 
        if line_count == 0:
            users.append(User(row["email"]))
            p1 = User(row["email"])
            pEmail = p1.email
        else:
            #print("Hello")
            if(row["email"] != pEmail): # encounter new email aka new user
                users.append(User(row["email"]))
                index += 1
               # print(index)
                #print(users)
                #users[index].clearAttributes()
                #users.append(user.User(row["email"]))


        if (pEmail == users[index].email):
            #print("If block")
            users[index].appendEating(row["eating_habits"])
            users[index].appendEnergy(row["energy_level"])
            users[index].appendAlone(row["alone_sad_score"])
            users[index].appendInterest(row["lost_interest"])
            users[index].appendStress(row["stress_factor"])
            pEmail = users[index].email
        else:
            users[index].appendEating(row["eating_habits"])
            users[index].appendEnergy(row["energy_level"])
            users[index].appendAlone(row["alone_sad_score"])
            users[index].appendInterest(row["lost_interest"])
            users[index].appendStress(row["stress_factor"])
            pEmail = users[index].email
            

        
        #print(f'\t{row["email"]} has alone score of {row["alone_sad_score"]}')
        
        line_count += 1

# now we need to read in the initial response file and add those attributes to the user class
#  get one row at a time
# get the email from that row
# if email exists as a user, store info into that user object
# if email does not exist as a user, skip it
with open('response.csv', mode='r') as response_file:
    csv_response_reader = csv.DictReader(response_file)
    avg_f_score = 0.00
    avg_m_score = 0.00
    for row in csv_response_reader:
        for u in users:
            if(row["email"] == u.email):
                if(row["gender"] == 'M'):
                    u.gender = 'M'
                elif(row["gender"] == 'F'):
                    u.gender = 'F'

                    
    for row in csv_response_reader:
        
        for i in users:
            
            if(row["email"] == i.email):
                if(row["tragic_event"] == "Yes"):
                    i.tragic_event = True
                    i.total_score += 0.3
                if(row["family_history"] == "Yes"):
                    i.family_history = True
                    i.total_score += 0.3
        

        
            
# ----------------------------------------------------------- STATS FROM PRIOR RESEARCH THAT WILL IMPACT TOTAL_SCORE --------------------------------------------------------
# FEMALES    31.0% CHANCE OF AMI (ANY MENTAL ILLNESS)
# MALES      20.2% CHANCE OF AMI
# 18-25 Y/O  38.0% CHANCE OF AMI
# OHIO       18.0% CHANCE OF AMI
# 
#
#
# FEMALE + 18-25 = 69%
# MALE   + 18-25 = 58%



print(len(users) - 1)
underFifty = 0   
#print(f'Processed {line_count} lines.')
for u in users:
    u.calculate_average()
    print("\nUser:", u.email)
    print("GENDER: ", u.gender)
    print("Eating habit: ", u.eating_habit)
    print("Energy Level: ", u.energy_level)
    print("Alone/Sad Score: ", u.alone_sad_score)
    print("Lost Interest: ", u.lost_interest)
    print("Stress Factor: ", u.stress_factor)
    print("Family History: ", u.family_history)
    print("Tragic Event: ", u.tragic_event)
    print("Total score is: ", u.total_score)
    if(u.total_score <= 5.00):
        print("--------------- :>", u.email)
        underFifty += 1
print("Number of participants under 50% ", underFifty)
avg_eating_habit = []
avg_energy_level = []
avg_alone_score = []
avg_stress_score = []
avg_score = 0.0
print("----------TOTAL SCORES-------------")
for u in users:
    avg_eating_habit.append(u.eating_habit[-1])
    avg_energy_level.append(u.energy_level[-1])
    avg_alone_score.append(u.alone_sad_score[-1])
    avg_stress_score.append(u.stress_factor[-1])
    avg_score += u.total_score
    print(u.gender, u.total_score)

print("Average eating habit = ", sum(avg_eating_habit) / len(avg_eating_habit)
    , "\nAverage energy     = ", sum(avg_energy_level) / len(avg_energy_level),
      "\nAverage sad score  = ", sum(avg_alone_score) / len(avg_alone_score),
      "\nAverage stress     = ", sum(avg_stress_score) / len(avg_stress_score)
)

print("\nAverage total score is: ", avg_score / len(users))


    
