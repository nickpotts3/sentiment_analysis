class User:
    
    def __init__(self, e) -> None:
        self.email = e
    #Use variables / attributes

    worry_score = 0
    tragic_event = False
    alone_score = 0
    family_history = False
    eating_habit = []
    energy_level = []
    alone_sad_score = []
    lost_interest = []
    stress_factor = []

    #User functions / methods
    def appendEating(self, value):
        self.eating_habit.append(value)

    def appendEnergy(self, value):
        self.energy_level.append(value)

    def appendAlone(self, value):
        self.alone_sad_score.append(value)
    
    def appendInterest(self, value):
        self.lost_interest.append(value)

    def appendStress(self, value):
        self.stress_factor.append(value)

    def clearAttributes(self):
        self.eating_habit.clear()
        self.energy_level.clear()
        self.alone_sad_score.clear()
        self.lost_interest.clear()
        self.stress_factor.clear()

    def printInfo(self):
        print("User {self.email} has eating habits of {self.eating_habit} energy level of {self.energy_level} sad score of {self.alone_sad_score} interest has been lost? {self.lost_interest} and a stress factor of {self.stress_factor}" )


