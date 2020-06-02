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

    def normalize_select_element(self, app, raw_data):
        """

        :param app:
        :type app:
        :param raw_data:
        :type raw_data:
        :return:
        :rtype:
        """
        normalized_data = []

        for row in raw_data:
            obj = {
                "value": row.get(app.get('value')),
                "label": row.get(app.get('label'))
            }
            normalized_data.append(obj)

        return normalized_data
