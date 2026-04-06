import json, re

_NOT_STANDALONE = {
    'acqu','indepe','depen','rec','un','pre','con','dis','re','mis','over',
    'under','inter','trans','sub','super','anti','semi','neo','non','pro',
    'tele','micro','macro','bio','geo','auto','multi','poly','mono','hypo',
    'hyper','pseudo','quasi','peri','para','meta','infra','ultra','extra',
}
_ACADEMIC_BLOCKLIST = [
    'gratification from the acquiescence','pleasure principle','reality principle',
    'instinctual drive','unconscious wish','wish fulfillment','libidinal','cathexis',
    'phantasy','sublimation of','narcissistic gratification','psychosexual',
    'transference neurosis','anxiety neurosis','the dreamer','dream analysis',
    'archaic form','imaginative happiness','acquiescence of reality',
    'restoration of the independence','pleasurable gratification',
    'mural paper','construction paper, glue','doily cut','art therapy','art therapist',
    'the client named','clinically depressed client','paint to illustrate',
    'art technique','mask making','workbook','fliegende blätter','in f., and since',
]

def is_clean(p):
    p = p.strip()
    if len(p) < 8 or len(p) > 250: return False
    if not p[0].isalpha(): return False
    if p[-1] not in '.?!': return False
    if re.search(r'\s{2,}', p): return False
    if re.search(r'\\[a-zA-Z]', p): return False
    if re.search(r'\(\w+,\s*\d{4}\)', p): return False
    if re.search(r'\bp\.\s*\d+|\bpp\.\s*\d+|\bibid\b|\bet al\.', p.lower()): return False
    if re.search(r'\d+\.\d+\.\d+', p): return False
    if re.search(r'[a-z]-\s[a-z]', p): return False
    if re.search(r'[A-Z]{5,}', p): return False
    if re.search(r'\b\d{4,}\b', p): return False
    if re.search(r'\d+x\s*[\+\-]', p): return False
    pl = p.lower()
    if any(b in pl for b in _ACADEMIC_BLOCKLIST): return False
    for m in re.finditer(r'\b([a-z]{3,7}) ([a-z]{3,8})\b', pl):
        frag, cont = m.group(1), m.group(2)
        if frag in _NOT_STANDALONE and len(frag+cont) >= 8: return False
    if re.match(r'^[A-Z][a-z]+ (Is|For|And) [A-Z][a-z]', p): return False
    if re.search(r'\s[a-z]{1,3}$', p.rstrip('.?!')): return False
    return True

with open('docs/phrases.json', encoding='utf-8') as f:
    phrases = json.load(f)

bad = [p for p in phrases if not is_clean(p)]
good = [p for p in phrases if is_clean(p)]
print(f'Total: {len(phrases)} | Bad: {len(bad)} | Good: {len(good)}')
print('Sample BAD:')
for p in bad[:15]:
    print(' ', p[:110])

print()
must_keep = [
    'The quick brown fox jumps over the lazy dog.',
    'Play music.',
    'What is the weather?',
    'I am so angry right now I could scream.',
    'Set a timer for fifteen minutes.',
    'A rod is used to catch pink salmon.',
    'Tell me a joke.',
    'Turn on lights.',
]
print('Must-keep check:')
for p in must_keep:
    status = 'KEPT' if is_clean(p) else 'WRONGLY REMOVED'
    print(f'  [{status}] {p}')
