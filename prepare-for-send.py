"""Prepare a separate import copy. Does not upload or send anything."""
import html,json,re,sys
from pathlib import Path
from urllib.parse import urlparse

root=Path(__file__).resolve().parent
if len(sys.argv)!=2:
    raise SystemExit('Usage: python prepare-for-send.py config.json')
config=json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
required=[]
for key in ['asset_base_url']+required:
    value=config.get(key,'')
    if not isinstance(value,str) or not value.strip() or 'REPLACE_WITH' in value or 'YOUR-ASSET-HOST' in value:
        raise SystemExit('Please fill in '+key)
base=config['asset_base_url'].rstrip('/')+'/'
if urlparse(base).scheme!='https' or not urlparse(base).netloc:
    raise SystemExit('asset_base_url must be a public HTTPS URL.')
for key in required:
    if key.endswith('_URL') and key!='UNSUBSCRIBE_URL' and urlparse(config[key]).scheme not in ('https','http','mailto','tel'):
        raise SystemExit('Invalid link: '+key)
destination=root/'ready-to-import'
destination.mkdir(exist_ok=True)
for item in json.loads((root/'mailers.json').read_text(encoding='utf-8')):
    for suffix in ['.html','.txt']:
        source=root/Path(item['file']).with_suffix(suffix)
        data=source.read_text(encoding='utf-8')
        if suffix=='.html':
            data=data.replace('src="assets/','src="'+html.escape(base,quote=True))
            data=data.replace('url("assets/','url("'+html.escape(base,quote=True))
        for key in required:
            value=config[key]
            # Preserve platform merge-tag syntax verbatim for the unsubscribe URL.
            if suffix=='.html' and key!='UNSUBSCRIBE_URL':value=html.escape(value,quote=True)
            data=data.replace('{{'+key+'}}',value)
        (destination/source.name).write_text(data,encoding='utf-8')
print('Prepared six HTML emails and text alternatives in '+str(destination))
print('No emails sent. Test imports and platform unsubscribe tags before launch.')
