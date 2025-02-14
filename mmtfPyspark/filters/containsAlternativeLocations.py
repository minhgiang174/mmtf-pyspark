#!/user/bin/env python
'''containsAlternativeLocations.py

This filter return true if this structure contains an alternative location

'''

__author__ = "Mars (Shih-Cheng) Huang"
__maintainer__ = "Mars (Shih-Cheng) Huang"
__email__ = "marshuang80@gmail.com"
__version__ = "0.2.0"
__status__ = "Done"


class ContainsAlternativeLocations(object):

    def __call__(self, t):
        structure = t[1]

        for c in structure.alt_loc_list:
            if c != '':
                return True

        return False
