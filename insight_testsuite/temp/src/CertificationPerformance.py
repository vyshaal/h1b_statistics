from Application import Application


class CertificationPerformance:

    def __init__(self, args):
        self.input_path = args[0]
        self.occupations_path = args[1]
        self.states_path = args[2]
        self.certified_applications_count = 0
        self.certified_applications_by_occupation = {}
        self.certified_applications_by_state = {}

    def calculate_statistics(self):
        try:
            with open(self.input_path, encoding="utf8", mode="r") as file:
                header = file.readline().split(";")
                for idx, column_name in enumerate(header):
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
                # sorted_occupations_list = sorted(self.certified_applications_by_occupation.items(), key=lambda x: (-x[1], x[0]))
                # sorted_states_list = sorted(self.certified_applications_by_state.items(), key=lambda x: (-x[1], x[0]))
                # self.write_results(sorted_occupations_list, criteria="TOP_OCCUPATIONS", write_file=self.occupations_path)
                # self.write_results(sorted_states_list, criteria="TOP_STATES", write_file=self.states_path)
        except Exception as error:
            print(error)

    def write_results(self, write_file, sorted_list, **kwargs):
        with open(write_file, 'w') as write_file:
            write_file.write(kwargs['criteria']+";NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
            for key, val in sorted_list[:10]:
                write_file.write("%s;%s;%.1f%%\n" % (key, val, (val/self.certified_applications_count) * 100))

    @staticmethod
    def sort_dict(my_dict):
        return sorted(my_dict.items(), key=lambda x: (-x[1], x[0]))
