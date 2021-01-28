########################################################################################################################
# The objective of this program is to load the details of the 200 people in the given data file. The data file         #
# contains the list of 200 people along with their friends. The idea of the task is to predict the spread of     #
# disease when one infected person comes in contact with another healthy person. For the given number of days and      #
# meeting probability and the health of the first patient, the stimulation for the entire set of days is calculated.   #                                                                                                       #
#                                                                                                                      #
# The second task of the program loads the peoples data as patients with the default health of the patient also with   #
# the first name and the last name from the inherited Person class. The actual stimulation for the spread of the       #
# disease is calculated with the help of meeting probability, no. of days and first patients health.                   #
# list of friends for that particular person.                                                                          #
########################################################################################################################
# Code programmed by : Shweta Sasidharan                            #
# Start_Date : 25/05/2020                                           #|#     Last_Edited_Date : 07/06/2020              #
########################################################################################################################
# File Input Read: a2_sample_set.txt (Consists of 200 records of people with their friends list).                      #
# Task 2 Accomplishment : The task loads the details of the patient records from the a2_sample_set.txt file, using the #
# Person class inherited which was imported from task 1. It stores the Patient objects in a patient list with the      #
# default initial health. It stores the the first name and last name of the patient and their friends along with the   #
# default health.                                                                                                      #
# The run_simulation function creates the stimulation for the spread of disease for the days given with the meeting    #
# probability with the patient zero health                                                                             #
# Terms used :  Meeting Probability : The probability for the meeting to take place between the two people in contact. #
#               Patient Zero Health : The Patient Health for the first record.                                         #
#               Initial Health : The initial Health of the other patients in the patient object list.                  #
#               Viral Load : Measure of the quantity of virus in the air which the other person breathes in when they  #
#                           are visiting and/or being visited by any contagious person                                 #
#               Health Points: Each person has a number of health points which changes over time depending on a        #
#                              person’s health.                                                                        #
########################################################################################################################

import random
from Populating_Population_Data import *

"""
The Person class is inherited from task 1 in Patient class, It uses the first name and last name 
from the base class Person. And a health parameter for the Patient.
"""


class Patient(Person):
    def __init__(self, first_name, last_name, health):
        super().__init__(first_name, last_name)
        self.health = health

    """
    This method returns the health of the patient.
    """

    def get_health(self):
        return self.health

    """
    This method sets the new health of the patient.
    """

    def set_health(self, new_health):
        self.health = new_health

    """
    This method checks whether the Patient is contagious and returns a boolean value for the condition.
    """

    def is_contagious(self):
        if round(self.health) <= 49:
            return True
        else:
            return False

    """
    This method infects the person with the Viral load of the infected person to the healthy person.
    The viral load is infected based on the health of the healthy person in the meeting.
    """

    def infect(self, viral_load):
        if self.health <= 29:
            new_health = round(self.health - (0.1 * viral_load))
        elif self.health > 29 and self.health < 50:
            new_health = round(self.health - (1.0 * viral_load))
        else:
            new_health = round(self.health - (2.0 * viral_load))

        if round(new_health) < 0:
            new_health = 0
        if round(new_health) > 100:
            new_health = 100

        self.set_health(new_health)  # Set the new health of the patient

    """
    This method adds sleep points to the patients health at the end of the day.
    """

    def sleep(self):
        self.health = round(self.health + 5)
        if round(self.health) < 0:
            self.health = 0
        if round(self.health) > 100:
            self.health = 100


"""
This function calculates the viral load of the infected person which will be 
infected on the healthy person.
And returns a float value for viral load.
"""


def calculate_viral_load(infected_health):
    load = 5 + pow((infected_health - 25), 2) / 62
    return load


"""
This function creates Patient objects from reading the sample data file and adds a initial health to the Patient. If 
the Patient has a list of friends it adds it using the Person Class methods.

Input Parameter : initial_health : This is the initial health of the Patient. 
Return Value : patient : This is the list of Patient Objects.
"""


def load_patients(initial_health):
    patient = []
    with open("a2_sample_set.txt", "r") as a_file:              # Reading the data file to load the people details
        for line in a_file:
            stripped_line = line.strip()
            patient_name = stripped_line.split(': ')[0]          # Patient Name from the record line
            friends = stripped_line.split(': ')[1]               # Friend Names from the record line

            fname = patient_name.split(' ')[0]                  # First name of the patient friend
            lname = patient_name.split(' ')[1]                  # Last name of the patient friend

            if not (any(((x.first_name == fname) and (x.last_name == lname)) for x in patient)):
                patient_obj = Patient(fname, lname, initial_health)  # Creating a Patient Object for the record line
                patient.append(patient_obj)                     # Appending the Patient objects in the person list

            else:
                for x in patient:
                    if (x.first_name == fname) and (x.last_name == lname):
                        patient_obj = x                         # If patient already present, skip the patient object
                        break

            friend_list = friends.split(", ")                   # Get individual friends from the friends list

            for item in friend_list:
                item = item.strip()
                friend_fname = item.split(' ')[0]               # Get person friend's first name
                friend_lname = item.split(' ')[1]               # Get person friend's last name

                if not (any(((x.first_name == friend_fname) and (x.last_name == friend_lname)) for x in patient)):
                    # Creating Friend Object for the Person Friend
                    friend = Patient(friend_fname, friend_lname, initial_health)
                    patient.append(friend)                      # Adding the friend to the list of person
                    patient_obj.add_friend(friend)              # Adding the friend object to the Person Object

                else:
                    for x in patient:
                        if (x.first_name == friend_fname) and (x.last_name == friend_lname):
                            friend = x                          # If friend already present, skip the friend object
                            break
                    patient_obj.add_friend(friend)              # Adding the friend object to the Person Object
    a_file.close()
    return patient


"""
This function calculates the stimulation of disease spread over a given period of days ,meeting probability and the 
health of the First Patient in the list. It returns a list with the daily number of contagious cases throughout the 
duration of the simulation.

Input Parameter : days : Period of days for stimulation.
                  meeting_probability: Probability of the meeting to tske place.
                  Patient_zero_health: Initial Health of the First Patient.
Output Parameter : contag_count_list : The list contains the count of contagious patients in a day.
"""


def run_simulation(days, meeting_probability, patient_zero_health):
    contag_count_list = []
    patients = load_patients(75)                   # Returns a list of Patient objects
    patients[0].health = int(patient_zero_health)  # Setting the first Patient's health as patient_zero_health
    size = int(days) + 1
    for i in range(1, size):
        for patient in patients:
            # Checks the meeting probability for the meeting
            if patient.is_contagious():            # Checks if friend is contagious
                friends = patient.friends
                for friend in friends:
                    if random.random() < float(meeting_probability):
                        if friend.is_contagious() is False:  # Checks if friend is contagious
                            # Transfer the viral load from the patient to friend
                            load = calculate_viral_load(patient.get_health())
                            friend.infect(load)     # Infect the viral load to friend

                            for x in patients:
                                if (x.first_name == friend.first_name) and (x.last_name == friend.last_name):
                                    x.infect(load)  # Reflect the friend's health in Patient
                        else:
                            # If both the patient and friend are infected then it is assumed that the patient will
                            # infect the friend first and then the friend infects the patient.
                            load = calculate_viral_load(patient.get_health())
                            friend.infect(load)
                            load = calculate_viral_load(friend.get_health())
                            patient.infect(load)

                            for x in patients:
                                if (x.first_name == friend.first_name) and (x.last_name == friend.last_name):
                                    x.infect(load)  # Reflect the friend's health in Patient

                else:  # If Patient is not contagious
                    friends = patient.friends
                    if random.random() < float(meeting_probability):
                        for friend in friends:
                            if friend.is_contagious() is False:  # Checks if friend is contagious
                                break
                            else:
                                # Transfer the viral load from the friend to patient
                                load = calculate_viral_load(friend.get_health())
                                patient.infect(load)  # Infect the viral load to patient

        count = 0
        for x in patients:
            if x.is_contagious():
                count = count + 1               # Counts the contagious patients in the list of patients
            x.sleep()                           # Adds 5 health points to the patient at the end of the day
        contag_count_list.append(count)         # Keeps track of the individual day count in a list

    print(contag_count_list)
    return contag_count_list


if __name__ == '__main__':
    for i in range(10):
        run_simulation(30, 0.6, 25)

    pass
