import os,json,urllib.request as w
V=dict(P=100,N=320,B=330,R=500,Q=900,K=0)
PS=dict(P="KKKKUUUUMMOQLLMPKKKOLJIKLMMGKKKK",N="ACEECGKKEKMNELNOEKNOELMNCGKLACEE",R="KKKKLMMMJKKKJKKKJKKKJKKKJKKKKKKL",Q="GIIJIKKKIKLLJKLLKKLLILLLIKLKGIIJ",K="ECCAECCAECCAECCAGEECIGGGOOKKOQMK")
T={k:[(ord(c)-75)*5 for c in s] for k,s in PS.items()};T['B']=T['N']
NO=(-19,-8,12,21,8,-12,19,-21)
KO=(-11,-9,9,11,-10,-1,1,10)
BO=KO[:4];RO=KO[4:]
NK=NO+KO
D=dict(N=NO,B=BO,R=RO,Q=BO+RO,K=KO)
I=10**6
B0=' '*20+' rnbqkbnr '+' pppppppp '+' ........ '*4+' PPPPPPPP '+' RNBQKBNR '+' '*20
def Vv(p,i):
 f=i%10-1
 return V[p]+T[p][(i//10-2)*4+min(f,7-f)]
def At(b,q):
 if b[q-9]=='p' or b[q-11]=='p':return 1
 for d in NK:
  if b[q+d]==('n' if d in NO else 'k'):return 1
 for d in KO:
  j=q+d;a='bq' if d in BO else 'rq'
  while b[j]!=' ':
   if b[j]!='.':
    if b[j] in a:return 1
    break
   j+=d
 return 0
def Ap(g,i,j):
 if j<29:
  for r in 'QRBN':g.append((i,j,r))
 else:g.append((i,j,''))
def G(p,co=False):
 b,e,c,k0=p[0],p[3],p[2],p[4][0]
 g=[]
 for i,x in enumerate(b):
  if not x.isupper():continue
  if x=='P':
   j=i-10
   if b[j]=='.':
    if j<29:Ap(g,i,j)
    elif not co:
     g.append((i,j,''))
     if i//10==8 and b[i-20]=='.':g.append((i,i-20,''))
   for d in (-11,-9):
    j=i+d
    if b[j].islower() or j==e:Ap(g,i,j)
  else:
   for d in D[x]:
    j=i+d
    while b[j]!=' ':
     if b[j].isupper():break
     if not co or b[j]!='.':g.append((i,j,''))
     if b[j]!='.' or x in 'NK':break
     j+=d
 if not co and not At(b,k0):
  if c&1 and set(b[k0+1:98])=={'.'} and not At(b,k0+1) and not At(b,k0+2):g.append((k0,k0+2,''))
  if c&2 and set(b[92:k0])=={'.'} and not At(b,k0-1) and not At(b,k0-2):g.append((k0,k0-2,''))
 return g
def Mk(p,m):
 b,s,c,e,k=p
 i,j,r=m
 x=b[i];y=b[j]
 d=-Vv(x,i)
 if y!='.':
  d+=Vv(y.upper(),119-j)
  if y=='r':c&={21:11,28:7}.get(j,15)
 d+=Vv(r or x,j)
 if x=='P' and j==e:d+=Vv('P',109-j)
 if x=='K' and abs(j-i)==2:
  f,t=(98,j-1) if j>i else (91,j+1)
  d+=-Vv('R',f)+Vv('R',t)
 if x=='K':c&=12
 elif x=='R':c&={91:13,98:14}.get(i,15)
 ne=(i+j)//2 if x=='P' and abs(j-i)==20 else -1
 nk=(j,k[1]) if x=='K' else k
 l=list(b);l[i]='.';l[j]=r or x
 if x=='P' and j==e:l[j+10]='.'
 if x=='K' and abs(j-i)==2:l[f]='.';l[t]='R'
 return (''.join(l),s+d,c,ne,nk)
def R(p):
 b,s,c,e,k=p
 return (b[::-1].swapcase(),-s,(c>>2|c<<2)&15,119-e if e+1 else -1,(119-k[1],119-k[0]))
N=0;X=False;TT={};RM=[0]
def S(p,d,al,be,pl):
 global N,X
 N+=1;X=N>=BG
 if X:return 0
 b,s,c,e,k=p
 ky=(b,c,e)
 en=TT.get(ky);tm=0
 if en:
  tm=en[3]
  if en[0]>=d and (en[2]==0 or en[2]==1 and en[1]>=be or en[2]==2 and en[1]<=al):return en[1]
 q=d<=0;ic=At(b,k[0]);ao=al
 if q and not ic:
  if s>=be:return be
  al=max(al,s)
 g=sorted(G(p,q and not ic),key=lambda m:-((10**7 if m==tm else 0)+(V[b[m[1]].upper()]*10-V[b[m[0]]] if b[m[1]]!='.' else 0)+(9000 if m[2] else 0)))
 bs=-I;bm=0;a=al
 for n,m in enumerate(g):
  c0=Mk(p,m)
  if At(c0[0],c0[4][0]):continue
  ch=R(c0)
  if n==0 or q:
   sc=-S(ch,d-1,-be,-a,pl+1)
  else:
   i,j,r=m
   rd=d>=3 and n>=3 and b[j]=='.' and j!=e and not r and not ic
   sc=-S(ch,d-1-rd,-a-1,-a,pl+1)
   if sc>a:sc=-S(ch,d-1,-be,-a,pl+1)
  if X:return 0
  if sc>bs:
   bs=sc;bm=m
   if sc>a:
    a=sc
    if a>=be:break
 if bs==-I:return -I+pl if ic else a if q else 0
 if pl==0:RM[0]=bm
 sc=bs if not q or ic else a
 TT[ky]=(d,sc,1 if a>=be else 2 if sc<=ao else 0,bm)
 return sc
H=lambda a,y:json.load(w.urlopen(a,json.dumps(y).encode()))
def v(u,n):
 f=ord(u[0])-10*int(u[1])+4;t=ord(u[2])-10*int(u[3])+4
 if n&1:f,t=119-f,119-t
 return (f,t,u[4].upper() if len(u)>4 else '')
def main():
 global N,X,BG
 u=os.environ["MAKEFUN_ENV_URL"]
 while (g:=H(u+"/game",{}))["status"]!="done":
  p=(B0,0,15,-1,(95,25))
  for n,y in enumerate(g["moves"]):p=R(Mk(p,v(y,n)))
  N=0;X=False;BG=120000;TT.clear();RM[0]=0
  for d in range(1,21):
   S(p,d,-I,I,0)
   if X:break
  f,t,pr=RM[0]
  n=len(g["moves"])
  if n&1:f,t=119-f,119-t
  H(u+"/move",{"game":g["game"],"move":f"{chr(f%10+96)}{10-f//10}{chr(t%10+96)}{10-t//10}{pr.lower() if pr else ''}"})
main()
