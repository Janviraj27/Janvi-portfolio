"""Small integration check for the served portfolio and its local assets."""
import re
from app import app

with app.test_client() as client:
    response = client.get('/')
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert client.get('/health').json == {'status': 'ok'}
    ids = re.findall(r'\bid="([^"]+)"', html)
    assert len(ids) == len(set(ids)), 'Duplicate HTML IDs'
    for anchor in re.findall(r'href="#([^"]+)"', html):
        assert anchor in ids, f'Missing anchor {anchor}'
    for asset in re.findall(r'(?:src|href)="(/static/[^"]+)"', html):
        assert client.get(asset).status_code == 200, f'Missing asset {asset}'
    for asset in ['three.module.js', 'three.core.js', 'THREE-LICENSE.txt']:
        assert client.get('/static/js/vendor/' + asset).status_code == 200
    assert html.count('data-sculpture=') == 6, 'Missing section sculpture'
    for text in ['815', '5-fold', '7.27', 'Param Consulting Services', 'Tata Strive', 'rjanvi727@gmail.com', 'PortSwigger Labs']:
        assert text in html, f'Missing factual content {text}'
    assert 'https://www.linkedin.com/' not in html
    assert client.get('/missing').status_code == 404
    assert response.headers['X-Content-Type-Options'] == 'nosniff'
print('PASS: page, health route, static assets, anchors, factual content and headers')
