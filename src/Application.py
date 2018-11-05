SPLIT_CHAR = ";"
IGNORE_CHAR = '""'


class Application:

    def __init__(self, line, status_idx, soc_name_idx, state_idx):
        """
        Initializes an application and sets the certifications status, occupation name, state name
        :param line: input data regarding an application
        :param status_idx: index of certification status column
        :param soc_name_idx: index of occupation name column
        :param state_idx: index of state name column
        """
        self.data = []
        self.split_string(line)
        self.occupation = self.data[soc_name_idx].strip().strip('\"')
        self.state = self.data[state_idx].strip()
        if self.data[status_idx] == "CERTIFIED":
            self.certified = True
        else:
            self.certified = False

    def split_string(self, line, split_char=SPLIT_CHAR, ignore_char=IGNORE_CHAR):
        """
        Splits string by delimiter and ignores the split when delimiter is enclosed within ignore character
        :param line: string to be parsed
        :param split_char: delimiter
        :param ignore_char: ignore character around which delimiter isn't considered for parsing
        :return: string splitted using delimiter after ignoring the delimiter enclosed within ignore character
        """
        string = ""
        flag = False
        for char in line:
            if char == ignore_char:
                flag = True if flag is False else False
            elif char == split_char and not flag:
                self.data.append(string)
                string = ""
            else:
                string += char
