import pandas as pd
from ProjectDataExtractionandTextAnalysis import downloader as dw
from ProjectDataExtractionandTextAnalysis import excelfiles as ex
from ProjectDataExtractionandTextAnalysis import analyzer as an

data = pd.read_csv("F:\\Pandas-Practice\\ProjectDataExtractionandTextAnalysis\\input.csv", index_col=0)
l = list(data._get_column_array(0))

for url in l:
        try:
                filename=ex.getFileName(url)
                data=str(dw.getUrlContent(url))
                p = an.GetParagraphs(data)
                dw.SaveFile(filename,p)

        except:
                pass