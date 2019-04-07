import numpy as np
import pandas as pd
from nptdms import TdmsFile
import os


class tdmsConverter:
    def __init__(self, path):
        '''Constructor for the converter'''
        self.path = path

    def generateFileList(self, debug = False):
        '''Returns the list of file in the folder given as input
        as a list.

        Input parameters:
        path: a string with the folder name. If the data is in the same folder
        as the file, you can use "./"
        debug: a boolean variable (can be True or False). If False then
        no output is printed. If True then the list of files is printed.$'''
        data_files = [x for x in os.listdir(self.path) if x.endswith(".tdms")]

        if (debug):
            print("Following files has been found:")
            print("Directory: "+self.path)
            print("Files    : "+str(data_files))

        return data_files

    def getChannelName(self, channelName):
        s = str(channelName).replace("'", "")
        s = s.replace(">", "")
        s = s.split("/")
        return s[2]

    def convertToList(self, data_files, debug = False):
        '''This function convert the content of the Files
        into a list. Each element of the list is a pandas
        dataframe with two columns: x,y.

        Input parameters:
        debug: a boolean. If False no debug text is printed. If
        True then debug informations are printed.
        data_files: a list with the list of the file names.
        Typically this is the value returned by the function
        generateFileList().

        Return Value:
        1. A pandas dataframe with 3 columns:
            'data', 'groupName', and 'channelName'.
        2. the number of channels as integer.'''

        df = pd.DataFrame()

        for filename in data_files:
            tdms_file = TdmsFile(self.path+'/'+filename)

            if (debug):
                print("The following Groups and Channels are available:")
                for group in tdms_file.groups():
                    print(group)
                for channel in tdms_file.group_channels(group):
                    print(channel)

            s1 = pd.Series(tdms_file.object('Reference', 'Ramp_Output').data)

            # This DataFrame will contain the data and the name of group and
            # Channel.

            for group in tdms_file.groups():
                if (str(group) != 'Reference'):
                    for channel in tdms_file.group_channels(group):
                        channelName = tdmsConverter.getChannelName(self, channel)
                        if (debug):
                            print(">>>", str(group), '--', channelName)
                        s2=pd.Series(tdms_file.object(str(group), channelName).data)
                        df_data=pd.concat([s1, s2], axis=1)
                        df_data.columns = ['x','y']

                        df_tmp = pd.DataFrame({"data": [df_data],
                            "groupName": [str(group)],
                            "channelName": [channelName],
                            "filename": [self.path+filename]})
                        df = df.append(df_tmp)


        return df, df.shape[0]

    def averageFiles(self, df, debug = False):

        # Let's create an empty pandas datraframe for the result
        df_return = pd.DataFrame()

        for filename in df['filename'].unique():
            if (debug):
                print ("Averaging ", filename)

            df_tmp = df[df['filename'] == filename]

            # Let's get some information from the dfs
            nr_channels = df_tmp.shape[0]
            nr_points = df_tmp.iloc[0]['data'].shape[0]

            if (debug):
                print("Number of channels ", nr_channels)
                print("Number of points   ", nr_points)

            tmp_avg = np.zeros(nr_points)
            for index, df_ in df_tmp.iterrows():
                tmp_avg = tmp_avg+df_['data']['y'] / nr_channels
                # Note that this is still a numpy array

            df_tmp_avg = pd.DataFrame({'x': df_tmp.iloc[0]['data']['x'],
                                       'y': tmp_avg})

            df_tmp_ = pd.DataFrame({'filename': [filename],
                                   'average': [df_tmp_avg]})
            #print(df_tmp_.head())


            df_return = df_return.append(df_tmp_)

        return df_return
