
class Command():

    def __init__(self, path_to_file,
                 flow_rate_layer_0, flow_rate_outer_walls, flow_rate_infill, bed_temperature, print_speed, fan_bol,
                 additional_information_bol, pause_each_layer_bol, retract_syringe_bol,
                 file_name, storage_path,
                 pause_each_layer_par_1 = None, pause_each_layer_par_2 = None):

        self.path_to_file = path_to_file

        self.flow_rate_layer_0 = flow_rate_layer_0
        self.flow_rate_outer_walls = flow_rate_outer_walls
        self.flow_rate_infill = flow_rate_infill
        self.bed_temperature = bed_temperature
        self.print_speed = print_speed
        self.fan_bol = fan_bol

        self.additional_information_bol = additional_information_bol
        self.pause_each_layer_bol = pause_each_layer_bol
        self.retract_syringe_bol = retract_syringe_bol

        self.file_name = file_name
        self.storage_path = storage_path

        self.pause_each_layer_par_1 = pause_each_layer_par_1
        self.pause_each_layer_par_2 = pause_each_layer_par_2