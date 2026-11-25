import json,math,sys
T=json.load(open('wb3/all.json'))
def mat(year,countries,inds):
    rows={i:{c:T[i].get(c,{}).get(year) for c in countries} for i in inds}
    cs=[c for c in countries if all(rows[i][c] is not None for i in inds)]
    mu={i:sum(rows[i][c] for c in cs)/len(cs) for i in inds}
    sd={i:(sum((rows[i][c]-mu[i])**2 for c in cs)/len(cs))**.5 for i in inds}
    z={c:{i:(rows[i][c]-mu[i])/sd[i] for i in inds} for c in cs}
    return cs,rows,z
def dist(z,a,b,inds): return math.sqrt(sum((z[a][i]-z[b][i])**2 for i in inds)/len(inds))
dims={
 'red':['fin24fam','fin24sav','fin24work','fin24bor','fin22b'],
 'digital':['g20.any','fin26a','fin26b','fin25e2','fin34c'],
 'ahorro':['save.any.t.d','fin17a.17a1.d','fin17c','fin22a','fin22d'],
}
out={}
for year,cs0 in [('2024',['PER','ECU','BOL','PRY','COL','MEX','ARG','BRA','TUR','IND']),('2021',['PER','ECU','BOL','PRY','COL','ARG','BRA','CHL','URY','TUR','IND'])]:
    allind=sum(dims.values(),[])
    if year=='2021': allind=[i for i in allind if i!='fin25e2']
    cs,rows,z=mat(year,cs0,allind)
    print('==',year,cs)
    res={}
    for name,inds in list(dims.items())+[('total',allind)]:
        inds=[i for i in inds if i in allind]
        d={c:round(dist(z,'PER',c,inds),2) for c in cs if c!='PER'}
        res[name]=dict(sorted(d.items(),key=lambda x:x[1]))
        print(name.ljust(8),res[name])
    out[year]=dict(countries=cs,rows=rows,dist=res)
    # full pairwise clustering simple: nearest neighbor of each
    print('nearest:',{a:min((round(dist(z,a,b,allind),2),b) for b in cs if b!=a) for a in cs})
json.dump(out,open('wb3/matriz_conducta_ampliada.json','w'),ensure_ascii=False,indent=1)
