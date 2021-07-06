from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO


def convert_pdf_to_txt(path):
    """pdfからテキスト情報を抽出する関数"""

    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    laparams.detect_vertical = True # Trueにすることで綺麗にテキストを抽出できる
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    maxpages = 0   #最大ページ数の指定
    fstr = ''
    for page in PDFPage.get_pages(fp, maxpages=maxpages):   #1ページ分の情報を取得する
        interpreter.process_page(page)   # process_page()で1ページ分の情報をテキストに変換

        str = retstr.getvalue()  #StringIO オブジェクト内に格納されているテキスト情報を取得する。
        fstr += str   #fstr変数に取得したテキスト情報を追記していく

    fp.close()
    device.close()
    retstr.close()
    return fstr