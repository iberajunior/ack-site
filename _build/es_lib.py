import re, json, html as H
INLINE = re.compile(r'^</?(strong|em|b|br|span(?:\s+class="it[^"]*"(?:\s+style="[^"]*")?)?|span)\s*/?>$', re.I)
TOK = re.compile(r'(<!--.*?-->|<script\b.*?</script>|<style\b.*?</style>|<svg\b.*?</svg>|<[^>]+>)', re.S|re.I)
HAS_WORD = re.compile(r'[A-Za-zÀ-ÿ]{2,}')
ATTR = re.compile(r'\b(alt|aria-label|placeholder|title|content|data-label)="([^"]*)"')
def segments(src):
    """yield (kind, start, end, text) for translatable runs."""
    parts=[]; pos=0
    for m in TOK.finditer(src):
        if m.start()>pos: parts.append(('t',pos,m.start()))
        parts.append(('g',m.start(),m.end())); pos=m.end()
    if pos<len(src): parts.append(('t',pos,len(src)))
    runs=[]; cur=None
    for k,a,b in parts:
        frag=src[a:b]
        if k=='t' or (k=='g' and INLINE.match(frag) and cur is not None) or (k=='g' and INLINE.match(frag) and frag.lower().startswith(('<strong','<em','<b','<span')) ):
            if cur is None: cur=[a,b]
            else: cur[1]=b
        else:
            if cur: runs.append(tuple(cur)); cur=None
    if cur: runs.append(tuple(cur))
    out=[]
    for a,b in runs:
        seg=src[a:b]
        # trim whitespace and dangling inline tags at edges kept as-is
        l=len(seg)-len(seg.lstrip()); r=len(seg.rstrip())
        core=seg[l:r]
        txt=re.sub(r'<[^>]+>','',core)
        if HAS_WORD.search(txt) and not core.startswith('{'):
            out.append((a+l,a+r,core))
    return out
def attrs(src):
    out=[]
    for m in ATTR.finditer(src):
        v=m.group(2)
        if HAS_WORD.search(v) and not v.startswith(('http','width=','#')) and m.group(1)!='content' or (m.group(1)=='content' and HAS_WORD.search(v) and ' ' in v and not v.startswith('http')):
            out.append((m.start(2),m.end(2),v))
    return out
