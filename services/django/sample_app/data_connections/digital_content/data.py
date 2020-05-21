from abc import ABCMeta

from ..data import Data as BaseData


class Data(BaseData):
    __metaclass__ = ABCMeta

    def getFilterData(self, raw_data):
        return raw_data.get('data')

    def flattenLineData(self, app, raw_data):
        pass

    def flattenSingleObject(self, app, raw_data):
        row = raw_data.get('data')[0]
        obj = {}
        for col in app['fields']:
            try:
                col_data = col['data'].split('.')
                if len(col_data) == 1:
                    obj[col['data']] = row.get(col_data[0])
                elif len(col_data) == 2:
                    obj[col['data']] = row.get(col_data[0]).get(col_data[1])
                elif len(col_data) == 3:
                    obj[col['data']] = row.get(col_data[0]).get(col_data[1]).get(col_data[2])
            except:
                obj[col['data']] = ""

        return obj

    def normalize_table_data(self, app, raw_data):
        normalized_data = []

        for row in raw_data.get('data'):
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
        print ("digital_content :: normalize_table_data :: normalized_data")
        print (data)
        print ("")
        print ("")
        """
        return normalized_data

    def flattenBarLineData(self, app, raw_data):
        data = []

        for row in raw_data.get('data'):
            try:
                x_axis = app['x_axis'].split('.')
                line_metric = app['line_metric'].split('.')
                bar_metric = app['bar_metric'].split('.')

                obj = {}
                if len(x_axis) == 1:
                    obj[app['x_axis']] = row.get(x_axis[0])
                elif len(x_axis) == 2:
                    obj[app['x_axis']] = row.get(x_axis[0]).get(x_axis[1])
                elif len(x_axis) == 3:
                    obj[app['x_axis']] = row.get(x_axis[0]).get(x_axis[1]).get(x_axis[2])

                if len(line_metric) == 1:
                    obj[app['line_metric']] = row.get(line_metric[0])
                elif len(line_metric) == 2:
                    if app['line_metric_format'] == "currency" or app['line_metric_format'] == "percent":
                        obj[app['line_metric']] = float(row.get(line_metric[0]).get(line_metric[1]))
                    else:
                        obj[app['line_metric']] = row.get(line_metric[0]).get(line_metric[1])
                elif len(line_metric) == 3:
                    if app['line_metric_format'] == "currency" or app['line_metric_format'] == "percent":
                        obj[app['line_metric']] = float(row.get(line_metric[0]).get(line_metric[1]).get(line_metric[2]))
                    else:
                        obj[app['line_metric']] = row.get(line_metric[0]).get(line_metric[1]).get(line_metric[2])

                if len(bar_metric) == 1:
                    obj[app['bar_metric']] = row.get(bar_metric[0])
                elif len(bar_metric) == 2:
                    if app['bar_metric_format'] == "currency" or app['bar_metric_format'] == "percent":
                        obj[app['bar_metric']] = float(row.get(bar_metric[0]).get(bar_metric[1]))
                    else:
                        obj[app['bar_metric']] = row.get(bar_metric[0]).get(bar_metric[1])
                elif len(bar_metric) == 3:
                    if app['bar_metric_format'] == "currency" or app['bar_metric_format'] == "percent":
                        obj[app['bar_metric']] = float(row.get(bar_metric[0]).get(bar_metric[1]).get(bar_metric[2]))
                    else:
                        obj[app['bar_metric']] = row.get(bar_metric[0]).get(bar_metric[1]).get(bar_metric[2])

                data.append(obj)

            except Exception as e:
                # Need to handle errors better... what to return
                # Is this even needed? Only fatal errors?
                print ("")
                print ("=======================")
                print ("_get_data_conn_data :: barline")
                print (e)
                print ("")
                print ("")
                continue

        """
        print ("")
        print ("=======================")
        print ("accuen_api :: flattenBarLineData :: data")
        print (data)
        print ("")
        print ("")
        """
        return data

    def flattenBarPieData(self, app, raw_data):
        data = []

        for row in raw_data.get('data'):
            try:
                groupby = app['groupby'].split('.')
                selected_metric = app['selected_metric'].split('.')

                obj = {}
                if len(groupby) == 1:
                    obj[app['groupby']] = row.get(groupby[0])
                elif len(groupby) == 2:
                    obj[app['groupby']] = row.get(groupby[0]).get(groupby[1])
                elif len(groupby) == 3:
                    obj[app['groupby']] = row.get(groupby[0]).get(groupby[1]).get(groupby[2])

                if len(selected_metric) == 1:
                    obj[app['selected_metric']] = row.get(selected_metric[0])
                elif len(selected_metric) == 2:
                    obj[app['selected_metric']] = row.get(selected_metric[0]).get(selected_metric[1])
                elif len(selected_metric) == 3:
                    obj[app['selected_metric']] = row.get(selected_metric[0]).get(selected_metric[1]).get(selected_metric[2])

                data.append(obj)

            except Exception as e:
                # Need to handle errors better... what to return
                # Is this even needed? Only fatal errors?
                print ("")
                print ("=======================")
                print ("_get_data_conn_data :: else")
                print (e)
                print ("")
                print ("")
                continue

        """
        print ("")
        print ("=======================")
        print ("accuen_api :: flattenBarPieData :: data")
        print (data)
        print ("")
        print ("")
        """
        return data