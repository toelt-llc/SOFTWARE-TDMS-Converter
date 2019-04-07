from tdmsUtils import tdmsConverter as tdmsc

tc = tdmsc.tdmsConverter('./ExampleData/')
df , total_number_of_channels = tc.convertToDf(debug = True)
df_avg = tc.averageFiles(df, debug = True)
