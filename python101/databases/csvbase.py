import os


def read_csv(csvfile):
    """
    Function returns tuple of tuples which contains data from csv file for record in database

    :param csvfile: file with data with *.csv extension
    :return: tuple with data
    """
    data = []
    if os.path.isfile(csvfile):
        with open(csvfile, "r") as content:
            for line in content:
                line = line.replace("\n", "")
                line = line.replace("\r", "")
                # line = line.decode(encoding='UTF-8', errors='strict')
                # We add tuple to list
                data.append(tuple(line.split(",")))
    else:
        print("Plik z danymi " + csvfile + "nie istnieje")

    return tuple(data)
