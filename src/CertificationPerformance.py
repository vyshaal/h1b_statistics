import sys
from Application import Application


class CertificationPerformance:

    def __init__(self, args):
        """
        Initialize class with input file and output file locations,
        Initialize # of certified applications by state, occupation
        :param args: Input file and output file locations
        """
        self.input_path = args[0]
        self.occupations_path = args[1]
        self.states_path = args[2]
        self.certified_applications_count = 0
        self.certified_applications_by_occupation = {}
        self.certified_applications_by_state = {}

    def calculate_statistics(self):
        """
        This function calculates top 10 occupations and top 10 states with highest number of certified applications
        :return: None
        """
        try:
            with open(self.input_path, mode="r") as file:
                headers = file.readline().split(";")
                status_idx = soc_name_idx = state_idx = 0
                for idx, column_name in enumerate(headers):
                    if column_name == "STATUS" or column_name == "CASE_STATUS":
                        status_idx = idx
                    if column_name == "LCA_CASE_SOC_NAME" or column_name == "SOC_NAME":
                        soc_name_idx = idx
                    if column_name == "WORKSITE_STATE" or column_name == "LCA_CASE_WORKLOC1_STATE":
                        state_idx = idx

                for line in file:
                    input_record = Application(line, status_idx, soc_name_idx, state_idx)
                    if input_record.certified:
                        self.certified_applications_count += 1
                        self.certified_applications_by_occupation[input_record.occupation] = \
                            self.certified_applications_by_occupation.get(input_record.occupation, 0) + 1
                        self.certified_applications_by_state[input_record.state] = \
                            self.certified_applications_by_state.get(input_record.state, 0) + 1

                self.write_results(self.occupations_path, self.sort_dict(self.certified_applications_by_occupation),
                                   criteria="TOP_OCCUPATIONS")
                self.write_results(self.states_path, self.sort_dict(self.certified_applications_by_state),
                                   criteria="TOP_STATES")

        except Exception as error:
            print(error, file=sys.stderr)

    def write_results(self, write_file, sorted_list, **kwargs):
        """
        Writes top 10 occupations and top 10 states to their respective output file locations
        :param write_file: output file location
        :param sorted_list: list comprising best occupations/states sorted in decreasing order
        :param kwargs: 'criteria' determines whether the list is occupations or states
        :return: None
        """
        with open(write_file, 'w') as write_file:
            write_file.write(kwargs['criteria']+";NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
            for key, val in sorted_list[:10]:
                write_file.write("%s;%s;%.1f%%\n" % (key, val, (val/self.certified_applications_count) * 100))

    @staticmethod
    def sort_dict(my_dict):
        """
        Sorts dictionary by decreasing value of value and then by increasing order of key
        :param my_dict: dictionary comprising of occupation/state as key, # of certified applications as value
        :return: list comprising best occupations/states sorted in decreasing order
        """
        return sorted(my_dict.items(), key=lambda x: (-x[1], x[0]))
