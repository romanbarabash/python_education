import os


def add_entry(text, data):
    return data.append(text)


def load(journal_name):
    """
    This method creates and loads a new journal.

    :param journal_name: This base name of the journal to load.
    :return: The journal data structure populated with the file data.
    """
    data = []
    filename = get_file_pathname(journal_name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data


def save(name, journal_data):
    """
    This method save created journal.

    :param name: Friendly name of journal
    :param journal_data: Data of the journal to load.
    """
    filename = get_file_pathname(name)
    print("...... savind to: {}".format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def get_file_pathname(name):
    """
    This method gets filename path

    :param name: Friendly name of journal
    :return: filename path
    """
    return os.path.abspath(os.path.join('./journals/', name + '.jrl'))
