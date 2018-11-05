SPLIT_CHAR = ";"
IGNORE_CHAR = '""'


class Application:

    def __init__(self, line, status_idx, soc_name_idx, state_idx):
        self.data = []
        self.split_string(line)
        self.occupation = self.data[soc_name_idx].strip().strip('\"')
        self.state = self.data[state_idx].strip()
        if self.data[status_idx] == "CERTIFIED":
            self.certified = True
        else:
            self.certified = False

    def split_string(self, line, split_char=SPLIT_CHAR, ignore_char=IGNORE_CHAR):
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
