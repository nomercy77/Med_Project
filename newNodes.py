import json
import pandas as pd
import py2neo
##graph = py2neo.Graph("http://18.208.189.145:7474/", user="", password="")



##fn is commented till we give it to docs

##graph labels: doc_spec, doc_sy, doc_diag, doc_drug, doc_test, doc_fl


def add_nodes(id,symps,diagnosis,drugs,tests,fl,spec):
    
    h='''
    merge (x:doc_id {name:'%s'})
    merge (x:doc_spec {name:'%s'})
    merge (x)-[w:weight]-(y)
    ON CREATE SET w=1
    ON MATCH SET w.count=w.count+1
    ''' % (id,spec)
    graph.run(h)

    if((len(symps)>0) and (spec)):
        spec=spec.lower()
        for s in symps:            
            s=s.lower()
            r='''
            merge (x:doc_spec {name:'%s'})
            merge (y:doc_sy {name:'%s'})            
            merge (x)-[w:weight]-(y)
            ON CREATE SET w.count=1
            ON MATCH SET w.count=w.count+1
            '''% (spec,s)
            graph.run(r)
    
    if (len(symps)==1):
        p=symps[0].lower()
        spec=spec.lower()
        c='''
        merge (x:doc_spec {name:'%s'})
        merge (y:doc_sy {name:'%s'})
        merge (x)-[w:weight]-(y)
        ON CREATE SET w.count=1
        ON MATCH SET w.count=w.count+1
        '''%(spec,p)                
        graph.run(c)    
    
    
    if (len(symps)>1):
        for i in range(1, len(symps)+1):
            p=str(symps[i-1]).lower()        
            for j in range(i + 1, len(symps)+1):
                q=''
                q=symps[j-1].lower()
                r='''
                merge (x:doc_sy {name:'%s'})
                merge (y:doc_sy {name:'%s'})
                merge (x)-[w:weight]-(y)
                ON CREATE SET w.count = 1
                ON MATCH SET w.count = w.count + 1
                '''% (p,q)
                graph.run(r)
    
    if(len(diagnosis)>0):
        for ds in diagnosis:
            d=str(ds).lower()
            for s in symps:
                p=str(s).lower()
                q='''
                merge (x:doc_sy {name:'%s'})
                merge (y:doc_diag {name:'%s'})
                merge (x)-[w:weight]-(y)
                ON CREATE SET w.count = 1
                ON MATCH SET w.count = w.count + 1                    
                '''% (p,d)
                graph.run(q)

        for diag in diagnosis:
            d=str(diag).lower()
            
            if(len(drugs)>0):
                for dr in drugs:
                    drug=str(dr.lower())
                    q='''
                    merge (x:doc_diag {name:'%s'})
                    merge (y:doc_drug {name:'%s'})
                    merge (x)-[w:weight]-(y)
                    ON CREATE SET w.count=1
                    ON MATCH SET w.count=w.count+1
                    '''% (d,drug)
                    graph.run(q)
            
            if(len(tests)>0):
                for t in tests:
                    ts=str(t).lower()
                    q='''
                    merge (x:doc_diag {name:'%s'})
                    merge (y:doc_test {name:'%s'})
                    merge (x)-[w:weight]-(y)
                    ON CREATE SET w.count=1
                    ON MATCH SET w.count=w.count+1
                    '''% (d,ts)
                    graph.run(q)

    if (len(diagnosis)>1):
        for i in range(0, len(diagnosis)):
            p=str(diagnosis[i]).lower()        
            for j in range(i+1, len(diagnosis)):
                q=''
                q=diagnosis[j].lower()
                r='''
                merge (x:doc_diag {name:'%s'})
                merge (y:doc_diag {name:'%s'})
                merge (x)-[w:weight]-(y)
                ON CREATE SET w.count = 1
                ON MATCH SET w.count = w.count + 1
                '''% (p,q)
                graph.run(r)            


    if(len(drugs)>1):
        for i in range(0, len(drugs)):
            p=str(drugs[i]).lower()        
            for j in range(i + 1, len(drugs)):
                q=''
                q=drugs[j].lower()
                r='''
                merge (x:doc_drug {name:'%s'})
                merge (y:doc_drug {name:'%s'})
                merge (x)-[w:weight]-(y)
                ON CREATE SET w.count = 1
                ON MATCH SET w.count = w.count + 1
                '''% (p,q)
                graph.run(r)

    if(len(tests)>1):
        for i in range(0, len(tests)):
            p=str(tests[i]).lower()        
            for j in range(i + 1, len(tests)):
                q=''
                q=tests[j].lower()
                r='''
                merge (x:doc_test {name:'%s'})
                merge (y:doc_test {name:'%s'})
                merge (x)-[w:weight]-(y)
                ON CREATE SET w.count = 1
                ON MATCH SET w.count = w.count + 1
                '''% (p,q)
                graph.run(r)


    if(fl>0):
        for diag in diagnosis:
            d=str(diag).lower()
            
            q='''
            merge (x:doc_diag {name:'%s'})
            merge (y:doc_fl {name:'%s'})
            merge (x)-[w:weight]-(y)
            ON CREATE SET w.count=1
            ON MATCH SET w.count=w.count+1
            '''% (d,fl)
            graph.run(q)        
