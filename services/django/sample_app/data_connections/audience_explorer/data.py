from abc import ABCMeta

from ..data import Data as BaseData


class Data(BaseData):
    __metaclass__ = ABCMeta

    def normalize_table_data(self, app, raw_data):
        normalized_data = []

        for row in raw_data:
            obj = {}
            for col in app['columns']:
                try:
                    col_data = col['data'].split('.')
                    if len(col_data) == 1:
                        obj[col['label']] = row.get(col_data[0])
                    elif len(col_data) == 2:
                        obj[col['label']] = row.get(col_data[0]).get(col_data[1])
                    elif len(col_data) == 3:
                        obj[col['label']] = row.get(col_data[0]).get(col_data[1]).get(col_data[2])
                except:
                    obj[col['label']] = ""

            normalized_data.append(obj)

        """
        print ("")
        print ("=======================")
        print ("audience_explorer :: normalize_table_data :: normalized_data")
        print (data)
        print ("")
        print ("")
        """
        return normalized_data
