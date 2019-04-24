# TDMS Converter Package

[![license MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![](https://img.shields.io/github/commits-since/toelt-llc/TDMS-Converter/v1.0.svg)
![](https://img.shields.io/github/last-commit/toelt-llc/TDMS-Converter.svg)
![](https://img.shields.io/github/repo-size/toelt-llc/TDMS-Converter.svg)
![](https://img.shields.io/github/issues/toelt-llc/TDMS-Converter.svg)

This repository contains the code for a package that converts TDMS files into pandas data frame for easy usage. 

## Help

You can always get the up-to-date documentation with

    from TDMSUtils import TDMSConverter as tdmsc
    help(tdmsc)

## Example usage

The package can be easily used. An example of usage is

    from TDMSUtils import TDMSConverter as tdmsc

    tc = tdmsc.TDMSConverter('./ExampleData/')
    df , total_number_of_channels = tc.convert_to_df(debug = False)
    df_avg = tc.average_files(df, debug = False)
    
In the ```df``` pandas dataframe you will find all the measurements. An example of how it looks like is

        data                     	        groupName	channelName	                filename
    0	x y 0 0.970000 -2.358...	PD_Signal_0	Avg_Data_20190405 09:28:53.72	./ExampleData/0_cold_next_day.tdms
    0	x y 0 0.970000 -2.359...	PD_Signal_0	Avg_Data_20190405 09:29:08.93	./ExampleData/0_cold_next_day.tdms
    0	x y 0 0.970000 -2.359...	PD_Signal_0	Avg_Data_20190405 09:29:24.14	./ExampleData/0_cold_next_day.tdms
    0	x y 0 0.970000 -2.358...	PD_Signal_0	Avg_Data_20190405 09:29:39.35	./ExampleData/0_cold_next_day.tdms
    0	x y 0 0.970000 -2.358...	PD_Signal_0	Avg_Data_20190405 09:29:54.56	./ExampleData/0_cold_next_day.tdms

For example to extract the x and y from the first channel (record in the dataframe) you could do something like this
    
    x = df.iloc[0]['data']['x']
    y = df.iloc[0]['data']['y']

or if you want to plot the average of all channels for each file you can do the following

    for i in range(0, df_avg.shape[1]):
        plt.plot(df_avg.iloc[i]['average']['x'], df_avg.iloc[i]['average']['y'], 
                 label = df_avg.iloc[i]['filename'])
    plt.legend()
    plt.show()

## Documentation as of 7.4.2019 20:58

Help on module TDMSUtils.TDMSConverter in TDMSUtils:

NAME
    TDMSUtils.TDMSConverter

CLASSES
    builtins.object
        TDMSConverter
    
    class TDMSConverter(builtins.object)
     |  TDMSConverter(path)
     |  
     |  Methods defined here:
     |  
     |  __init__(self, path)
     |      Constructor for the converter
     |  
     |  average_files(self, df, debug=False)
     |      This function evaluate the average of all channels for all files.
     |      
     |      Input parameters:
     |      df: dataframe with all the files as obtained by the function
     |      convert_to_df() in this package.
     |      
     |      Return Values:
     |      A DataFrame that contains as many records as number of files. The
     |      Dataframe contains two columns: 'filemname' that contains the name
     |      of the file with the path, and 'average' that contains a pandas
     |      dataframe with two columns 'x' and 'y'.
     |  
     |  convert_to_df(self, debug=False)
     |      This function convert the content of the Files
     |      into a list. Each element of the list is a pandas
     |      dataframe with two columns: x,y.
     |      
     |      Input parameters:
     |      debug: a boolean. If False no debug text is printed. If
     |      True then debug informations are printed.
     |      data_files: a list with the list of the file names.
     |      Typically this is the value returned by the function
     |      generate_file_list().
     |      
     |      Return Value:
     |      1. A pandas dataframe with 3 columns:
     |          'data', 'groupName', and 'channelName'.
     |      2. the number of channels as integer.
     |  
     |  generate_file_list(self, debug=False)
     |      Returns the list of file in the folder given as input
     |      as a list.
     |      
     |      Input parameters:
     |      path: a string with the folder name. If the data is in the same folder
     |      as the file, you can use "./"
     |      debug: a boolean variable (can be True or False). If False then
     |      no output is printed. If True then the list of files is printed.$
     |  
     |  get_channel_name(self, channelName)
     |      This is a helper function that from the output of the
     |      tdms package for the channel name like
     |      
     |      <TdmsObject with path /'PD_Signal_0'/'Avg_Data_20190404 15:30:45.93'>
     |      
     |      extract the actual channel name. In this case
     |      
     |      Avg_Data_20190404 15:30:45.93
     |      
     |      Input Parameters:
     |      channelName: a channelName as returned, for example, from a loop
     |      like This
     |      
     |      for channel in tdms_file.group_channels(group):
     |          ......
     |      
     |      Return Value:
     |      a string with the channel name, that can be used in the function
     |      
     |      tdms_file.object(str(group), channelName).data
