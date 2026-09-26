from io import BytesIO

def export_comic_pdf(x=None):
    b = BytesIO()
    b.write(b'%PDF-1.4 dummy')
    b.seek(0)
    return b