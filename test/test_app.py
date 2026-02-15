from crs.fastapi import root

def test_root():
  resp = response.get('/')
  assert resp.status_code == 200
  assert resp.json() == {"message": "Hello Word"}
