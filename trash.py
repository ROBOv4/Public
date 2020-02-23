# BITWISE 
Import  java.util.Scanner;
public class JavaApplication10 {
    public static void main(String[] args) {
       Scanner sc= new Scanner(System.in); //System.in is a standard input stream.
       System.out.print("Enter first number: ");
       int a= sc.nextInt();
       System.out.print("Enter second number: ");
       int b= sc.nextInt();  
       int c = 0;
       c = a & b;        /* 12 = 0000 1100 */
       System.out.println("a & b = " + c );       
       c = a | b;        /* 61 = 0011 1101 */
       System.out.println("a | b = " + c );
       c = a ^ b;        /* 49 = 0011 0001 */
       System.out.println("a ^ b = " + c );
      c = ~a;           /*-61 = 1100 0011 */
      System.out.println("~a = " + c );
      c = a << 2;       /* 240 = 1111 0000 */
      System.out.println("a << 2 = " + c );

      c = a >> 2;       /* 15 = 1111 */
      System.out.println("a >> 2  = " + c );
      c = a >>> 2;      /* 15 = 0000 1111 */
      System.out.println("a >>> 2 = " + c );
    } 
}


#PAGERANK
import java.util.*;
import java.io.*;

public class PageRank {

public int path[][] = new int[10][10];
public double pagerank[] = new double[10]; 
public void calc(double totalNodes){
double InitialPageRank;
double OutgoingLinks=0; 
double DampingFactor = 0.85; 
double TempPageRank[] = new double[10];

int ExternalNodeNumber;
int InternalNodeNumber; 
int k=1; // For Traversing
int ITERATION_STEP=1;

InitialPageRank = 1/totalNodes;
System.out.printf(" Total Number of Nodes :"+totalNodes+"\t Initial PageRank  of All Nodes :"+InitialPageRank+"\n");
 
for(k=1;k<=totalNodes;k++)
{
  this.pagerank[k]=InitialPageRank;
}   
  
System.out.printf("\n Initial PageRank Values , 0th Step \n");
for(k=1;k<=totalNodes;k++)
{
  System.out.printf(" Page Rank of "+k+" is :\t"+this.pagerank[k]+"\n");
}  
  
 while(ITERATION_STEP<=2) 
 {
  for(k=1;k<=totalNodes;k++)
 {  
   TempPageRank[k]=this.pagerank[k];
   this.pagerank[k]=0;
  }
    
 for(InternalNodeNumber=1;InternalNodeNumber<=totalNodes;InternalNodeNumber++)
 {
  for(ExternalNodeNumber=1;ExternalNodeNumber<=totalNodes;ExternalNodeNumber++)
   {
    if(this.path[ExternalNodeNumber][InternalNodeNumber] == 1)
    { 
      k=1;
      OutgoingLinks=0;  // Count the Number of Outgoing Links for each ExternalNodeNumber
      while(k<=totalNodes)
      {
        if(this.path[ExternalNodeNumber][k] == 1 )
        {
          OutgoingLinks=OutgoingLinks+1; // Counter for Outgoing Links
        }  
        k=k+1;  
      } 
         // Calculate PageRank     
         this.pagerank[InternalNodeNumber]+=TempPageRank[ExternalNodeNumber]*(1/OutgoingLinks);    
     }
   }  
 }    
     
   System.out.printf("\n After "+ITERATION_STEP+"th Step \n");
  
     for(k=1;k<=totalNodes;k++) 
      System.out.printf(" Page Rank of "+k+" is :\t"+this.pagerank[k]+"\n"); 
  
     ITERATION_STEP = ITERATION_STEP+1;
}

for(k=1;k<=totalNodes;k++)
{
  this.pagerank[k]=(1-DampingFactor)+ DampingFactor*this.pagerank[k]; 
  } 
 
System.out.printf("\n Final Page Rank : \n"); 
for(k=1;k<=totalNodes;k++)
{
 System.out.printf(" Page Rank of "+k+" is :\t"+this.pagerank[k]+"\n"); 
  }
}
    public static void main(String[] args) {
        int nodes,i,j,cost;
        Scanner in = new Scanner(System.in);
        System.out.println("Enter the Number of WebPages \n");
        nodes = in.nextInt();
        PageRank p = new PageRank();
        System.out.println("Enter the Adjacency Matrix with 1->PATH & 0->NO PATH Between two WebPages: \n");
        for(i=1;i<=nodes;i++)
          for(j=1;j<=nodes;j++)
          {
            p.path[i][j]=in.nextInt();
            if(j==i)
              p.path[i][j]=0;
          }
        p.calc(nodes);
    }
    }
	
	
	
# DISTANCR BETWEEN 2 STRINGS
public class EditDistanceProblem {
    public int editDistanceRecursion(String s1,String s2,int m,int n)
	{
	if(m==0)
            return n;
	if(n==0)
            return m;
	if(s1.charAt(m-1)==s2.charAt(n-1))
            return editDistanceRecursion(s1,s2,m-1,n-1);

	return 1 + Math.min(editDistanceRecursion(s1, s2, m, n-1 ),Math.min(editDistanceRecursion(s1, s2 , m-1 , n ),editDistanceRecursion(s1 ,s2 , m-1 , n-1) ) );
	}
  
    public static void main(String[] args) {
      	String s1 = "horizon";
	String s2 = "horizontal";
	EditDistanceProblem ed = new EditDistanceProblem();
	System.out.println("Minimum Edit Distance - (Recursion): " + 
	ed.editDistanceRecursion(s1,s2,s1.length(),s2.length() ) );
	}
    }


  
#SIMILARITY BETWEEN 2 TEXTS
install.packages('tm')
install.packages('ggplot2')
install.packages('textreuse')
install.packages('devtools')
install.packages('NLP')
library('tm')
require('NLP')
library('tm')
setwd('C:/r-corpus/')
my.corpus<-Corpus(DirSource("C:/r-corpus"))
my.corpus<-tm_map(my.corpus,removeWords,stopwords(kind = "english"))
my.tdm<-TermDocumentMatrix(my.corpus)
my.df<-as.data.frame(inspect(my.tdm))



#SIMILARITY 2 SENTANCES

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
  
X ="I love horror movies"
Y ="Lights out is a horror movie"  
X_list = word_tokenize(X)  
Y_list = word_tokenize(Y) 
sw = stopwords.words('english')  
l1 =[];l2 =[] 
X_set = {w for w in X_list if not w in sw}  
Y_set = {w for w in Y_list if not w in sw} 
rvector = X_set.union(Y_set)  
for w in rvector: 
    if w in X_set: l1.append(1) # create a vector 
    else: l1.append(0) 
    if w in Y_set: l2.append(1) 
    else: l2.append(0) 
c = 0
  
for i in range(len(rvector)): 
        c+= l1[i]*l2[i] 
cosine = c / float((sum(l1)*sum(l2))**0.5) 
print("similarity: ", cosine)


#STOPWORDS REMOVE
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
  
example_sent = "This is a sample sentence, showing off the stop words filtration."
  
stop_words = set(stopwords.words('english')) 
  
word_tokens = word_tokenize(example_sent) 
  
filtered_sentence = [w for w in word_tokens if not w in stop_words] 
  
filtered_sentence = [] 
  
for w in word_tokens: 
    if w not in stop_words: 
        filtered_sentence.append(w) 
  
print(word_tokens) 
print(filtered_sentence)



#TKINTER
from tkinter import *
root=Tk()
l1=Label(root,text="Enter Number 1:")
l1.pack()
t1=Entry(root,bd="3")
t1.pack()
l2=Label(root,text="Enter Number 2:")

l2.pack()
t2=Entry(root,bd="3")
t2.pack()

def addNumber():
    a=int(t1.get())
    b=int(t2.get())
    c=a+b
    print("Addition of two NOS:",c)

b1=Button(root,text="Addition",fg="red",bg="green",command=addNumber)
b1.pack()
root.mainloop()



#WEB CRAWLER

import java.net.*;
import java.io.*;
public class Crawler {
    public static void main(String[] args)throws Exception{
    String urls[] = new String[1000];
    String url = "https://www.cricbuzz.com/live-cricket-scores/20307/aus-vs-ind-3rd-odi-india-tour-of-australia-2018-19";
    int i=0,j=0,tmp=0,total=0, MAX = 1000;
    int start=0, end=0;
    String webpage = Web.getWeb(url);
    end = webpage.indexOf("<body");
    for(i=total;i<MAX; i++, total++){
        start = webpage.indexOf("http://", end);
        if(start == -1){
            start = 0;
            end = 0;
            try{
                webpage = Web.getWeb(urls[j++]);
            }catch(Exception e){
                System.out.println("******************");
                System.out.println(urls[j-1]);
                System.out.println("Exception caught \n"+e);
            }
                        /*logic to fetch urls out of body of webpage only */
            end = webpage.indexOf("<body");
            if(end == -1){
                end = start = 0;
                continue;
            }       
        }
        end = webpage.indexOf("\"", start);
        tmp = webpage.indexOf("'", start);
        if(tmp < end && tmp != -1){
            end = tmp;
        }
        url = webpage.substring(start, end);
        urls[i] = url;
        System.out.println(urls[i]);
    }   
    System.out.println("Total URLS Fetched are " + total);
    }
}

class Web{
    public static String getWeb(String address)throws Exception{
    String webpage = "";
        String inputLine = "";
        URL url = new URL(address);
        BufferedReader in = new BufferedReader(
        new InputStreamReader(url.openStream()));
        while ((inputLine = in.readLine()) != null)
        webpage += inputLine;
        in.close();
    return webpage;
    }   
    }


#XML PARSE
emp.xml
<?xml version="1.0" encoding="UTF-8"?>
<employee>
<fname>Divesh</fname>
<lname>Saurabh</lname>
<home>Thane</home>
<expertise name="SQl"/>
<expertise name="Python"/>
<expertise name="Testing"/>
<expertise name="Business"/>
</employee>

emp.py
import xml.dom.minidom
def main():
    doc=xml.dom.minidom.parse("emp.xml");
    print(doc.nodeName)
    print(doc.firstChild.tagName)
if __name__=="__main__":
    main()

emp1.py
import xml.dom.minidom
def main():
   doc = xml.dom.minidom.parse("emp.xml");
   print (doc.nodeName)
   print (doc.firstChild.tagName)
   expertise = doc.getElementsByTagName("expertise")
   print ("%d expertise:" % expertise.length)
   for skill in expertise:
     print (skill.getAttribute("name"))
   newexpertise = doc.createElement("expertise")
   newexpertise.setAttribute("name", "BigData")
   doc.firstChild.appendChild(newexpertise)
   print (" ")
   expertise = doc.getElementsByTagName("expertise")
   print ("%d expertise:" % expertise.length)
   for skill in expertise:
     print (skill.getAttribute("name"))   
if __name__ == "__main__":
  main()

