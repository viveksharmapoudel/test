
def csvfile_to_dictionaries(file_name):
    with open(file_name) as file_object:

        lines = file_object.readlines()  # list of all the lines
        persons = []
        for line in lines:  # main loop for the line

            person_details = line.split(",")

            person_details_arranged = {}

            for word in person_details:

                if person_details.index(word) == 0:
                    person_details_arranged["first_name"] = word.strip()

                elif person_details.index(word) == 1:
                    person_details_arranged["last_name"] = word.strip()

                elif person_details.index(word) == 2:
                    person_details_arranged["address"] = word.strip()

                elif person_details.index(word) == 3:
                    person_details_arranged["age"] = word.strip()

                elif person_details.index(word) == 4:
                    person_details_arranged["profession"] = word.strip()

                else:
                    print("error")

            persons.append(person_details_arranged)

    return persons


def main():

    persons = csvfile_to_dictionaries("file_name.txt")
    for person in persons:
        print(person)


main()





