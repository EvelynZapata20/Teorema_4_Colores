def añadirArista(adj, p1, p2):
    adj[p1].append(p2)
    adj[p2].append(p1)  
    return adj
  
def avido(adj, V):
    color = [-1] * V
    color[0] = 0;
    posible = [False] * V

    for i in range(1, V):
        for j in adj[i]:
            if (color[j] != -1):
                posible[color[j]] = True

        col = 0
        while col < V:
            if (posible[col] == False):
                break
            col += 1
              
        color[i] = col 
        for j in adj[i]:
            if (color[j] != -1):
                posible[color[j]] = False
  
    for i in range(V):
        c=None
        pais= None
        if (i==0):
            pais= "Colombia"
        elif (i==1):
            pais= "Venezuela"
        elif (i==2):
            pais= "Ecuador"
        elif (i==3):
            pais= "Brasil"
        elif (i==4):
            pais= "Guyana"
        elif (i==5):
            pais= "Perú"
        elif (i==6):
            pais= "Bolivia"
        elif (i==7):
            pais= "Paraguay"
        elif (i==8):
            pais= "Argentina"
        elif (i==9):
            pais= "Uruguay"
        else:
            pais= "Chile"
            
        if (color[i]==1):
            c='\033[31m'
        elif (color[i]==2):
            c='\033[36m'
        elif (color[i]==3):
            c='\033[32m'
        else:
            c='\033[35m'
        print(c+pais)
  
  
if __name__ == '__main__':
      
    g1 = [[] for i in range(11)]
    g1 = añadirArista(g1, 0, 1)
    g1 = añadirArista(g1, 0, 2)
    g1 = añadirArista(g1, 0, 3)  
    g1 = añadirArista(g1, 0, 5)
    g1 = añadirArista(g1, 1, 4)
    g1 = añadirArista(g1, 1, 3)
    g1 = añadirArista(g1, 2, 5)
    g1 = añadirArista(g1, 5, 3)
    g1 = añadirArista(g1, 5, 6)  
    g1 = añadirArista(g1, 5, 10)
    g1 = añadirArista(g1, 3, 6)
    g1 = añadirArista(g1, 3, 7)
    g1 = añadirArista(g1, 3, 9)
    g1 = añadirArista(g1, 3, 4)
    g1 = añadirArista(g1, 3, 8)  
    g1 = añadirArista(g1, 10, 8)
    g1 = añadirArista(g1, 10, 6)
    g1 = añadirArista(g1, 8, 9)
    g1 = añadirArista(g1, 8, 7)
    g1 = añadirArista(g1, 8, 6)
    g1 = añadirArista(g1, 6, 7)  
    
    print("\033[1;37m"+"PAÍSES DE SURAMÉRICA COLOREADOS"+'\033[0;m')
    avido(g1, 11)
