import tabula
from tabula import read_pdf
myfile = 'E:/УЧЕБА/МШП/ПИТОН/price_pdf/ price_02.03.2020.pdf'
mytable = tabula.read_pdf(myfile, pages = 1)
