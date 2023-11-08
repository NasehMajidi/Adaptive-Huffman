#!/usr/bin/env python
# coding: utf-8

# In[1]:


# here we update the weights of the nodes. if there is the swap condition,we swap the nodes
def update_weight(ind,Weight,Graph,Connection):
    if Connection.get(51-2*(ind-1)) is not None:
        Weight[51-2*(ind-1)]=Weight[Connection[51-2*(ind-1)][0]]+Weight[Connection[51-2*(ind-1)][1]]
        if 51-2*(ind-1)+3 <=50:
            if Weight[51-2*(ind-1)] > Weight[51-2*(ind-1)+3]:
                Graph,Connection,Weight = swap(51-2*(ind-1),51-2*(ind-1)+3,Graph,Connection,Weight)
        if 51-2*(ind-1)+1<=50:
            if Weight[51-2*(ind-1)] > Weight[51-2*(ind-1)+1]:
                Graph,Connection,Weight = swap(51-2*(ind-1),51-2*(ind-1)+1,Graph,Connection,Weight)
        #Weight[51-2*(ind-1)]=Weight[51-2*(ind)]+Weight[51-2*(ind)+1]
    elif Connection.get(51-2*(ind-1)+1) is not None:
        Weight[51-2*(ind-1)+1]=Weight[Connection[51-2*(ind-1)+1][0]]+Weight[Connection[51-2*(ind-1)+1][1]]
        if Weight[51-2*(ind-1)+1] > Weight[51-2*(ind-1)+2]:
            Graph,Connection,Weight = swap(51-2*(ind-1)+1,51-2*(ind-1)+2,Graph,Connection,Weight)
    return Weight,Connection,Graph


# In[2]:


def swap(node1,node2,Graph,Connection,Weight):
    ####
    m=Weight[node1]
    Weight[node1]=Weight[node2]
    Weight[node2]=m
    ####
    if Graph[node1] == "" and Graph[node2] =="" :
        m3=Connection[node1]
        Connection[node1]=Connection[node2]
        Connection[node2]=m3
    elif Graph[node1] == "" and Graph[node2] !="" :
        Connection[node2]=Connection[node1]
        del(Connection[node1])
    elif Graph[node1] != "" and Graph[node2] =="" :
        Connection[node1]=Connection[node2]
        del(Connection[node2])
    ###
    m2=Graph[node1]
    Graph[node1]=Graph[node2]
    Graph[node2]=m2
    ### 
    return Graph,Connection,Weight


# In[3]:


# convert binary to decimal
def bin2dec(Input):
    Out=0
    for i in range(len(Input)):
        Out=Out+int(Input[len(Input)-i-1])*(2**i)
    return Out


# In[4]:


# find all the bit streams in the tree 
def find_word(Connection,Temp,Graph):
    out=""
    out_=""
    bb=list(Connection.items())
    #print("temp", Temp)
    for index , alph in Graph.items():
        if alph == Temp:
            ind=index
            #print("A")
            break
    #print("index:",bb)
    i=0
    Flag=True
    num_=ind
    path=[num_]
    while Flag:
        #print("i: ",i)
        if num_ in bb[i][1]:
            path.append(bb[i][0])
            num_=bb[i][0]
            i=-1
        i=i+1
        if num_==51:
            Flag= False
    out=""
    out_=""
    for i in range(len(path)-1):
        bi= 0 if path[i]%2 else 1
        out = out+str(bi)
    for i in range(len(out)-1,-1,-1):
        out_=out_+out[i]
    return(out_)


# In[5]:


# update the variables when the alphabet has come for the first time
def find_first_time(j_,inp_,start,stop,r_,Connection,W,Graph,Time):
    if j_==1:
        temp=inp_[:stop]
    else:
        temp=inp_[start:start+stop]
    code=bin2dec(temp)
    if code < r_:
        if j_==1:
            temp=inp_[:stop+1]
        else:
            temp=inp_[start:start+stop+1]
        code=bin2dec(temp)
        alph=chr(code+97)
        Time , W ,Connection ,Graph=update_tree(Time,alph,Connection,Graph,W)
        Pointer=start+stop+1
    else:
        alph=chr(code+97+r_)
        Time , W ,Connection ,Graph=update_tree(Time,alph,Connection,Graph,W)
        Pointer=start+stop
    return W,Graph,Time,Connection,Pointer


# In[6]:


# update the tree as we did in the encoder
def update_tree(Time, Inp ,Connection , Graph ,W):
    J=len(Time)
    Temp=Inp
    if Temp in Time.keys():
        Val=W.get(Temp)
        Time[Temp]=Time[Temp]+1
        for Key , Val in Graph.items():
            if Val == Temp:
                Node=Key
                break
        W[Node]=Time[Temp]
        for K in range(J,1,-1):
            W , Connection , Graph =update_weight(k,w,graph,connection)
            W[51] = W[50]+W[49]
    else:
        J=J+1
        Time[Temp]=1
        Graph[51-2*J]="NTY"
        Graph[51-2*J+1]=Temp
        Connection[51]=(49,50)
        if J == 1:
            W[50]=1 
        else :
            Graph[51-2*(J-1)]=""
            Connection[51-2*(J-1)]=(51-2*J+1,51-2*J)
            for Key , Val in Graph.items():
                if Val == Temp:
                    Node=Key
                    break
            W[Node]=1
            W[Node-1]=0
            for K in range(J,1,-1):
                W , Connection , Graph =update_weight(K,w,graph,connection)
                W[51] = W[50]+W[49]
                #print("KK  ",K)
    print(Inp)
    return Time , W , Connection, Graph


# In[7]:


inp="00000101000100000110001011010110001010"


# In[8]:


# number of alphabet = (2^e)+r
e=4
r=10
# time ---> how frequently the alphabets have come
time={}
# w ---> the weight vector
w={51:0,50:0,49:0}
# graph ---> graph shows that the sybmbol which node contains
graph={}
j=0
# connection ---> it shows the kid number of each parent node
connection={51:''}
w[51]=0
flag=True
while flag:
    j=j+1
    # decoding the first letter
    if j==1:
        w,graph,time,connection,pointer=find_first_time(j,inp,0,e,r,connection,w,graph,time)
    else:
        words={}
        # we find all possible bit streams, we add the next bit,we decode when we got any pattern in the bit streams
        for i in range(min(j-1,len(time)+1)):
            dic=time.copy()
            dic.update({'NTY':"#"})
            path=find_word(connection,list(dic.keys())[i],graph)
            words[list(dic.keys())[i]]=path
        k=0
        flag2=True
        while flag2:
            k=k+1
            temp2=inp[pointer:pointer+k]
            if temp2 in words.values():
                for ind , val in words.items():
                    if temp2==val:
                        var=ind
                        if var == 'NTY':
                            flag2 = False
                            pointer=pointer+len(words['NTY'])
                            w,graph,time,connection,pointer=find_first_time(j,inp,pointer,e,r,connection,w,graph,time)
                        else:
                            flag2 = False
                            time , w , connection, graph=update_tree(time, var ,connection , graph ,w)
                            pointer=pointer+len(words[var])
        # we break the loop if we finished the bits
        if pointer==len(inp):
            flag=False


# In[ ]:




