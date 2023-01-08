

class Data:
  def __init__(self,c='',nbr=0,cbin=''):
    self.s=c
    self.n=nbr
    self.c=cbin

class Node:
  def __init__(self,data=None,left=None,right=None):
    self.data=data
    self.left=left
    self.right=right

class ArbreHuffman:
  def __init__(self,racine=None):
    self.racine=racine


class Huffman:
  def __init__(self,dataTxt=''):
    self.data=dataTxt
    self.encodage=dict()
    self.arbre=None
    self.occur=dict()
  #######################
  #   Autres Fonction:  #
  #######################
  def __calculeNbrOccur__(self):      #Fonction pour calculer nbr d'occurrence
    for c in self.data:
      if self.occur.get(c)==None:
        self.occur[c]=1
      else:
        self.occur[c]+=1
  ########################
  def creeArbre(self):
    noudes=[]
    self.__calculeNbrOccur__()

    for c in self.occur.keys():
      d=Data(c,self.occur[c])
      noudes.append(Node(d))
      
    while len(noudes)>1:
      noudes=sorted(noudes,key=lambda x:x.data.n)
        #for i in noudes:
        #print("->",i.data.s,i.data.n,end=' ')
      agauche,adroite=noudes[0],noudes[1]
      agauche.data.c,adroite.data.c=0,1
      #print("\n->",agauche.data.s,adroite.data.s,agauche.data.n,adroite.data.n)
      noudes.remove(agauche)
      noudes.remove(adroite)
      d=Data(agauche.data.s+adroite.data.s,agauche.data.n+adroite.data.n)
      noudes.append(Node(d,agauche,adroite))
    self.arbre=noudes[0]
 
  ########################
  def __getEncodage__(self,noeud,val=''):
    v=val+str(noeud.data.c)
    if noeud.left!=None:
      self.__getEncodage__(noeud.left,v)
    if noeud.right!=None:
      self.__getEncodage__(noeud.right,v)
    elif noeud.left==None and noeud.right==None:
      self.encodage[noeud.data.s]=v
  def getEncodage(self):
    self.__getEncodage__(self.arbre)
  
  #####################
  def calculGain(self):
    nbrBitTotal=len(self.data)*8
    nbrBitHuffman=0
    for k,v in self.occur.items():
      nbrBitHuffman+=len(self.encodage[k])*v
    return nbrBitTotal-nbrBitHuffman
 
  #######################
  def __RGD__(self,root):
    if root:
      #if root.left==None and root.right==None:
      print(root.data.c,root.data.s,root.data.n)
      self.__RGD__(root.left)
      self.__RGD__(root.right)
  def RGD(self):
    self.__RGD__(self.arbre)
  ######################

text='BCCABBDDAECCBBAEDDCC'
#
compressTxt=Huffman(text)
compressTxt.creeArbre()
compressTxt.getEncodage()
#
occur=compressTxt.occur
encod=compressTxt.encodage
gain=compressTxt.calculGain()
#
print(f"Nombre d'occurrance de chaque caractere:{occur}")
print(f"Encodage de chaque caractere:{encod}")
#
textCompressedBin=""
for i in text:
  textCompressedBin+=encod[i]
#
print(f"{text} ===> {textCompressedBin} ")
print(f"gain = {gain} --> le nombre de bit utilse apres codage de Huffman: {8*len(text)-gain}")


