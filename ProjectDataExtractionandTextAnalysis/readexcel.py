import pandas as pd
from ProjectDataExtractionandTextAnalysis import downloader as dw
from ProjectDataExtractionandTextAnalysis import excelfiles as ex
from ProjectDataExtractionandTextAnalysis import analyzer as an

data = pd.read_csv("F:\\Pandas-Practice\\ProjectDataExtractionandTextAnalysis\\data2.csv", index_col=0)
l = list(data._get_column_array(0))

for url in l:
    try:
        filename = "html/" + ex.getFileName(url)
        data = str(dw.getUrlContent(url))

        title = an.GetTitle(data)
        print("Title : ",title[0].text)

        p = an.GetParagraphs(data)
        print("Paragraph : ",p[0].text)

        dw.SaveFile(filename, data)

    except:
        pass
