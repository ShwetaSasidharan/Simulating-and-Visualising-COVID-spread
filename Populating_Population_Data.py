########################################################################################################################
# The objective of this program is to load the details of the 200 people in the given data file. The data file         #
# contains the list of 200 people along with their friends. The idea of the assignment is to predict the spread of     #
# disease when one infected person comes in contact with another healthy person. For the given number of days and      #
# meeting probability and the health of the first patient, the stimulation for the entire set of days is calculated to #
# predict the spread of disease.                                                                                       #
#                                                                                                                      #
# The first task of the program loads the peoples data which includes the first name and the last name and also the    #
# list of friends for that particular person.                                                                          #
########################################################################################################################
# Code programmed by : Shweta Sasidharan                            #|#     Student_Id : 31224075                      #
# Start_Date : 21/05/2020                                           #|#     Last_Edited_Date : 07/06/2020              #
########################################################################################################################
# File Input Read: a2_sample_set.txt (Consists of 200 records of people with their friends list.                       #
# Task 1 Accomplishment : The task loads the details of the different person records from the a2_sample_set.txt file,  #
# It stores the the first name and last name of the person and their friends in a list which contains the objects for  #
# different people.                                                                                                    #
#                                                                                                                      #
########################################################################################################################

"""
The person class stores the first name and last name of the person record with their friends in the same object using
the add friend method.
"""


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.friends = []

    """This method adds the person's friend to be stored in the person Object
    Here friend_person is a reference to another Person object"""

    def add_friend(self, friend_person):
        self.friends.append(friend_person)

    """This method will return the full name of the person with 
    first and last name concatenated"""

    def get_name(self):
        return self.first_name + " " + self.last_name

    """This method returns the list of Person objects for the connections added as friends.
    """

    def get_friends(self):
        return self.friends


"""
This function loads the people from the input data file and when a friend list is indicated for the person record it 
adds it using the Person Class methods.
Return Value: --> person: It returns a list of Person objects.
"""


def load_people():
    with open("a2_sample_set.txt", "r") as a_file:              # Reading the data file to load the people details
        person = []  # Person Object list
        for line in a_file:
            stripped_line = line.strip()
            person_name = stripped_line.split(': ')[0]           # Person Name from the record line
            friends = stripped_line.split(': ')[1]               # Friend Names from the record line

            fname = person_name.split(' ')[0]                   # First name of the friend
            lname = person_name.split(' ')[1]                   # Last name of the friend

            if not (any(((x.first_name == fname) and (x.last_name == lname)) for x in person)):
                person_obj = Person(fname, lname)               # Creating a Person Object for the record line
                person.append(person_obj)                       # Appending the person objects in the person list
            else:
                for x in person:
                    if (x.first_name == fname) and (x.last_name == lname):
                        person_obj = x                          # If person already present, skip the person object
                        break

            friend_list = friends.split(", ")                   # Get individual friends from the friends list

            for item in friend_list:
                item = item.strip()
                friend_fname = item.split(' ')[0]               # Get person friend's first name
                friend_lname = item.split(' ')[1]               # Get person friend's last name

                if not (any(((x.first_name == friend_fname) and (x.last_name == friend_lname)) for x in person)):
                    friend = Person(friend_fname, friend_lname)  # Creating Friend Object for the Person Friend
                    person.append(friend)                        # Adding the friend to the list of person
                    person_obj.add_friend(friend)                # Adding the friend object to the Person Object

                else:
                    for x in person:
                        if (x.first_name == friend_fname) and (x.last_name == friend_lname):
                            friend = x                           # If friend already present, skip the friend object
                            break
                    person_obj.add_friend(friend)                # Adding the friend object to the Person Object

    a_file.close()
    return person


if __name__ == '__main__':
    person_list = load_people()
    # for person in person_list:
    # print(person.get_name(),len(person.get_friends()))
    print(len(person_list))
    pass
