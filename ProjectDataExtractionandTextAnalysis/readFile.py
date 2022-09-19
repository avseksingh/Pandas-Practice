import os
from ProjectDataExtractionandTextAnalysis import analyzer as an

for filename in os.listdir("F:\\Pandas-Practice\\ProjectDataExtractionandTextAnalysis\\html"):
    url = "F:\\Pandas-Practice\\ProjectDataExtractionandTextAnalysis\\html\\" + str(filename)

    File_object = open(url,  "r+")
    print(File_object)
    #
    # file1 = open( "F:\\Pandas-Practice\\ProjectDataExtractionandTextAnalysis\\html\\www.google.com.txt")
    # # print(file1.read())

    title = an.GetTitle(File_object)
    print("Title :",title[0].text)

    div = an.GetDivs(File_object)
    print(div)

    para = an.GetParagraphs(File_object)
    print(para)

    inp = an.GetBody(File_object)
    print(inp)
    # file1.close()
    File_object.close()




   # with open(os.path.join("files", filename), 'r') as f:
   #     text = f.read()
   #     print(text)

