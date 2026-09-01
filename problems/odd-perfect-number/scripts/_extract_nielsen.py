import re, zlib, sys
src = r"C:\Users\juma8\.claude\projects\C--Claude-Code-Math\6050354d-a0a8-48f8-9080-1ad102b0105d\tool-results\webfetch-1788286879899-9nf3nd.pdf"
dst = r"C:\Claude-Code\Math\problems\odd-perfect-number\scripts\nielsen_text.txt"
data = open(src, 'rb').read()
streams = re.findall(rb'stream\r?\n(.*?)endstream', data, re.S)
out = []
for s in streams:
    try:
        d = zlib.decompress(s)
        if b'Tj' in d or b'TJ' in d:
            out.append(d)
    except Exception:
        pass
text = b'\n'.join(out).decode('latin-1')
pat = re.compile(r'\((?:[^()\\]|\\.)*\)')
chunks = pat.findall(text)
joined = ' '.join(c[1:-1] for c in chunks)
joined = joined.replace('\\(', '(').replace('\\)', ')')
open(dst, 'w', encoding='utf-8').write(joined)
print('chars:', len(joined))