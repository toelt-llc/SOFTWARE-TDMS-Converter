from tdmsUtils import tdmsConverter as tdmsc

tc = tdmsc.tdmsConverter('./ExampleData/')
df , total_number_of_channels = tc.convert_to_df(debug = True)
df_avg = tc.average_files(df, debug = True)
