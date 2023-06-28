import poro

m = poro.Match("KR", id="KR_6564220384")

print(len([p.to_dict() for p in m.participants]))