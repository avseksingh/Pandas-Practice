import pandas as pd
from ProjectDataExtractionandTextAnalysis import downloader as dw
from ProjectDataExtractionandTextAnalysis import excelfiles as ex
from ProjectDataExtractionandTextAnalysis import analyzer as an

data = pd.read_csv("F:\\Pandas-Practice\\ProjectDataExtractionandTextAnalysis\\input.csv", index_col=0)
l = list(data._get_column_array(0))

for url in l:
        try:
                filename=ex.getFileName(url)
                print(filename)
                data=str(dw.getUrlContent(url))
                print(type(data))

                title = an.GetTitle(data)
                print("Title : ",title[0].text)

                p = an.GetParagraphs(data)
                print("Paragraph : ",p[0].text)

                dw.SaveFile(filename,data)

                break

        except:
                pass