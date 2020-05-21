from abc import ABCMeta


class Data():
    __metaclass__ = ABCMeta

    def getFilterData(self, raw_data):
        """
        Used in populate_data_conn_filter()

        :param raw_data: JSON object
        :return:
        """
        return None

    def flattenSingleObject(self, app, raw_data):
        return None

    def flattenLineData(self, app, raw_data):
        return None

    def normalize_table_data(self, app, raw_data):
        return None

    def flattenBarLineData(self, app, raw_data):
        return None

    def flattenBarPieData(self, app, raw_data):
        return None