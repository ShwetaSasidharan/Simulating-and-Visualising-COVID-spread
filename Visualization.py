########################################################################################################################
# The objective of this program is to load the details of the 200 people in the given data file. The data file         #
# contains the list of 200 people along with their friends. The idea of the task is to predict the spread of     #
# disease when one infected person comes in contact with another healthy person. For the given number of days and      #
# meeting probability and the health of the first patient, the stimulation for the entire set of days is calculated.   #                                                                                                       #
########################################################################################################################
# Code programmed by : Shweta Sasidharan                            #
# Start_Date : 01/06/2020                                           #|#     Last_Edited_Date : 07/06/2020              #
########################################################################################################################
# Task 3 Accomplishment : This task gives the visual representation of the stimulation using Matplot libraries. The    #
# visual curve is plotted against the count of contagious people and the days.                                         #
#                                                                                                                      #
# The visual_curve function creates the visual representation of the spread of disease in the given number of days.    #
# Terms used :  Meeting Probability : The probability for the meeting to take place between the two people in contact. #
#               Patient Zero Health : The Patient Health for the first record.                                         #
#               Initial Health : The initial Health of the other patients in the patient object list.                  #
#######################################################################################################################
# Scenario A : An uncontained Outbreak : The disease is seen to spread rapidly, it spreads to all the 200 people in    #
# the records, as patient is quite unwell it is expected that he will spread it across to all the different people     #
# he meets.                                                                                                            #
# Scenario B : It is an uncertain situation, wherein the patient zero health is on the initial stages of sickness and  #
# the situation may lead to his recovery and no outbreak in some cases but the patient zero may also spread the        #
# disease in other cases as seen in the figure.                                                                        #
# Scenario C : With a low meeting probability value and contagious patient zero health, it can be predicted that the   #
# spread might flatten the curve which is as seen in the figure. As with lesser chances of meeting, the spread         #
# is restricted and slow in other cases.                                                                               #
########################################################################################################################


import matplotlib.pyplot as plt
from Stimulation import *

"""
This function creates a visual representation of the stimulation for the days given and the meeting probability for the 
meeting to take place. 
Input Parameter : days : Period of days for stimulation.
                  meeting_probability: Probability of the meeting to tske place.
                  Patient_zero_health: Initial Health of the First Patient.
It displays the plot for the given stimulation days and the contagious count.
"""


def visual_curve(days, meeting_probability, patient_zero_health):
    contagious_count = run_simulation(days, meeting_probability, patient_zero_health)
    days = range(1, days + 1)
    plt.xlabel("Days", fontsize=16)
    plt.ylabel("Contagious Count", fontsize=16)
    # plt.title('Test scenario C: flattening the curve ', fontsize=18)
    plt.plot(days, contagious_count)
    plt.show()
    # plt.savefig('scenario_C.png')


if __name__ == '__main__':
    days = int(input("Enter days to run the stimulation: "))
    meeting_probability = float(input("Enter the meeting probability: "))
    patient_zero_health = int(input("Enter the patient zero health: "))
    visual_curve(days, meeting_probability, patient_zero_health)
    # visual_curve(15,0.5,10)
    # visual_curve(30, 0.6,25)
    # visual_curve(60, 0.25, 49)
    # visual_curve(90, 0.8, 40)
    # visual_curve(40, 1, 1)
