agent_win_percentage_radiant = '''
Agent Win Percentage in Radiant
-------------------------------
Jett      47%
Sage      51.2%
Raze      49.4%
Omen      50.8%
Reyna     50.9%
Killjoy   46.8%
Sova      47.8%
Cypher    60.7%
Phoenix   53.8%
Brimstone 56.8%
Breach    72.6%
Viper     60%

https://blitz.gg/valorant/stats/agents?map=all&queue=competitive&tier=24'''

tup1 = ('Jett', 'Sage', 'Raze', 'Omen', 'Reyna', 'Killjoy', 'Sova', 'Cypher',
        'Phoenix', 'Brimstone', 'Breach', 'Viper')
tup2 = ('47%', '51.2%', '49.4%', '50.8%', '50.9%', '46.8%', '47.8%', '60.7%',
        '53.8%', '56.8', '72.6%', '60%')
class Operator:
    opCount = 0

    def __init__(self, name, winrate):
        self.name = name
        self.winrate = winrate
        Operator.opCount += 1

    def displayCount(self):
        print("Total Operators %d" % Operator.opCount)

    def displayOperator(self):
        print("Operator:", self.name, ", Winrate:", self.winrate)

op1 = Operator("Jett", "47%")
op2 = Operator("Sage", "51.2%")
op3 = Operator("Raze", "49.4%")
op4 = Operator("Omen", "50.8%")
op5 = Operator("Reyna", "50.9%")
op6 = Operator("Killjoy", "46.8%")
op7 = Operator("Sova", "47.8%")
op8 = Operator("Cypher", "60.7%")
op9 = Operator("Phoenix", "53.8%")
op10 = Operator("Brimstone", "56.8%")
op11 = Operator("Breach", "76.6%")
op12 = Operator("Viper", "60%")

#op1.displayOperator()
#op2.displayOperator()
#op3.displayOperator()
#op4.displayOperator()
#op5.displayOperator()
#op6.displayOperator()
#op7.displayOperator()
#op8.displayOperator()
#op9.displayOperator()
#op10.displayOperator()
#op11.displayOperator()
#op12.displayOperator()
#print("Total Operators: %d" % Operator.opCount)

if __name__ == "__main__":
    print("test")
