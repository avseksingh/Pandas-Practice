import pandas as pd
from ProjectDataExtractionandTextAnalysis import analyzer as an

data = "<div> Hello Div</div><div> 2 div</div>"
r = an.GetDivs(data)
print(r[1].text)
for e in r:
    print(r[e].text)

for e in r:
    print(r[e])