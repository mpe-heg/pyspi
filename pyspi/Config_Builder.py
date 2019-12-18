import yaml

default_GRB = {'Special_analysis': 'GRB',
               'Time_of_GRB_UTC' : '101010 010101',
               'Event_types': ['single'],
               'Detectors_to_use': 'All',
               'emin': '20',
               'emax': '8000',
               'Active_Time': '0-100',
               'Background_time_interval_1': '-100--10',
               'Background_time_interval_2': '110-200',
               'Simmulate': False}
            
           

class basic_config_builder_GRB(object):
    """
    Class to build the config yaml file used in to specify which analysis should be done.
    """

    def __init__(self, **kwargs):
        """
        Init the config file for a GRB analysis
        """
        self._config = default_GRB
        for key, value in kwargs.iteritems():
            assert key in self._config.keys(),'Please use valid key. Only {} are available.'.format(self._config.keys())
            self._config[key] = value

        self._config_savepath = './config.yaml'
        with open(self._config_savepath, 'w') as file:
            yaml.dump(self._config, file)
            
    def change_config(self, **kwargs):
        """
        Change the current config
        :param kwargs: dict with the keywords and new values
        :return:
        """
        for key, value in kwargs.iteritems():
            assert key in self._config.keys(), 'Please use valid key. Only {} are available.'.format(self._config.keys())
            self._config[key] = value
        with open(self._config_savepath, 'w') as file:
            yaml.dump(self._config, file)
            
    def display(self):
        """
        Display current config file
        :return:
        """
        print yaml.dump(self._config)

    @property
    def config(self):
        return self._config

    @property
    def save_path(self):
        return self._config_savepath
#default_Point_Source  = {'Special analysis': 'Point Source',
#                         'name': ['Crab'],
#                         'ra': 10}
#class Config_Builder_Point_Sources(object):
        