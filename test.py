from tdmsUtils import tdmsConverter as tdmsc
#import tdmsConverter as tdmsc
tc = tdmsc.tdmsConverter('./ExampleData/')
list_of_files = tc.generateFileList(debug = False)
df, c = tc.convertToList(list_of_files, debug = False)
print(c)
print(tc.averageFiles(df))
