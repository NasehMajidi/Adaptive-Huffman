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


# here, based on the tree we should makes bit streams
def encode(Temp,Time,Bit,Graph,Connection,t_):
    out=""
    out_=""
    # bb is the nodes connections
    bb=list(connection.items())
    # if the code is not NTY
    if Temp in list(time.keys()):
        # we extract the node number and symbol in index and alph respectively
        for index , alph in graph.items():
            if alph == temp:
                index_=index
                break
        # we add the path in the path var and we finish adding when we got node 51
        i=0
        flag=True
        num_=index_
        path=[num_]
        while flag:
            if num_ in bb[i][1]:
                path.append(bb[i][0])
                num_=bb[i][0]
                i=-1
            i=i+1
            if num_==51:
                flag= False
        out=""
        out_=""
        # if the node number is even we allacate 1 else 0
        for i in range(len(path)-1):
            bi= 0 if path[i]%2 else 1
            out = out+str(bi)
        for i in range(len(out)-1,-1,-1):
            out_=out_+out[i]
    # here if the code in NTY
    else:
        for index , alph in graph.items():
            if alph == "NTY":
                index_=index
                break
        i=0
        flag=True
        if t_!=0:  
            num_=index_
            path=[num_]
            while flag:
                if num_ in bb[i][1]:
                    path.append(bb[i][0])
                    num_=bb[i][0]
                    i=-1
                i=i+1
                if num_==51:
                    flag= False
            out=""
            out_=""
            for i in range(len(path)-1):
                bi= 0 if path[i]%2 else 1
                out = out+str(bi)
            # we reverse the bits
            for i in range(len(out)-1,-1,-1):
                out_=out_+out[i]
            out_=out_+" "
        # as the ascii code of a is 97 so we substract 96
        var=ord(temp)-96
        # we consider if the var is more than 2*r or not, and we add 0 if the binary number has not sufficient bit
        if var < 20:
            l_=5-(len(bin(var-1))-2)
            out_=out_+"0"*l_+str(bin(var-1)[2:])
        else:
            l_=4-(len(bin(var-1-10))-2)
            out_=out_+"0"*l_+str(bin(var-1-10)[2:])
    print("word",temp," ,code",out_)


# In[8]:


# the input for coding
inp="aardvark"
inp="aard"


# In[9]:


# number of alphabet = (2^e)+r
e_=4
r_=10
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
bit={51:"NULL"}
for i in range(len(inp)):
    temp=inp[i]
    encode(temp,time,bit,graph,connection,i)
    if temp in time.keys():
        val=w.get(temp)
        time[temp]=time[temp]+1
        for key , val in graph.items():
            if val == temp:
                node=key
                break
        w[node]=time[temp]
        for k in range(j,1,-1):
            w , connection , graph =update_weight(k,w,graph,connection)
            w[51] = w[50]+w[49]
    else:
        j=j+1
        time[temp]=1
        graph[51-2*j]="NTY"
        graph[51-2*j+1]=temp
        bit[51-2*j]=0
        bit[51-2*j+1]=1
        connection[51]=(49,50)
        if j == 1:
            w[50]=1 
        else :
            graph[51-2*(j-1)]=""
            connection[51-2*(j-1)]=(51-2*j+1,51-2*j)
            for key , val in graph.items():
                if val == temp:
                    node=key
                    break
            w[node]=1
            w[node-1]=0
            for k in range(j,1,-1):
                w , connection , graph =update_weight(k,w,graph,connection)
                w[51] = w[50]+w[49]
print("conncetion :",connection)
print("weigth :", w)
print("graph :",graph)


# In[ ]:




