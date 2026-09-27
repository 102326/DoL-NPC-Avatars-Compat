"""Build only the task-local source; preserve all original image bytes."""
from pathlib import Path
import hashlib, json, zipfile, difflib

ROOT = Path(__file__).resolve().parent
src = ROOT / 'src'
boot = json.loads((src/'boot.json').read_text(encoding='utf-8'))
output = ROOT / 'dist' / ('NPC.Avatars.Mod-' + boot['version'] + '.mod.zip')
output.parent.mkdir(parents=True, exist_ok=True)
for field in ('imgFileList','tweeFileList','styleFileList','scriptFileList','additionFile'):
    for name in boot.get(field,[]):
        assert (src/name).is_file(), (field, name)
changes = []
patch = []
with zipfile.ZipFile(ROOT/'original/NPC.Avatars.Mod.mod.zip') as original:
    for entry in original.infolist():
        if entry.is_dir():
            continue
        current = src/entry.filename
        assert current.is_file(), 'Original file removed: ' + entry.filename
        before, after = original.read(entry), current.read_bytes()
        if before != after:
            assert not entry.filename.startswith('img/'), 'Image altered'
            changes.append(entry.filename)
            patch.extend(difflib.unified_diff(before.decode('utf-8').replace('\r\n','\n').splitlines(True), after.decode('utf-8').replace('\r\n','\n').splitlines(True), fromfile='original/'+entry.filename,tofile='src/'+entry.filename))
with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in sorted(src.rglob('*')):
        if p.is_file():
            item = zipfile.ZipInfo(p.relative_to(src).as_posix(),date_time=(2026,9,27,0,0,0))
            item.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(item,p.read_bytes())
with zipfile.ZipFile(output) as z:
    assert z.testzip() is None
    assert json.loads(z.read('boot.json')) == boot
sha = hashlib.sha256(output.read_bytes()).hexdigest()
(ROOT/'dist/SHA256SUMS.txt').write_text(f'{sha}  {output.name}\n',encoding='utf-8')
(ROOT/'changes.diff').write_text(''.join(patch),encoding='utf-8')
report = {'file':output.name,'bytes':output.stat().st_size,'sha256':sha,'changedOriginalFiles':changes,'originalImagesUnchanged':True,'zipCRC':'passed'}
(ROOT/'dist/build-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
