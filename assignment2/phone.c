/* Random Initial State GOL Simulator */

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define ROWS 129    /* max array rows */
#define COLS 129    /* max array columns */
#define TMAX 50    /* termination time */
#define THETA 0.75  /* probability that initial cell state is 1 */

/* define global variables */
int a[ROWS+1][COLS+1][2];   /* old and current states */
int t = 0;                  /* tick */
int cur = 1, old = 0;       /* current/old state index */
int lb,rb,tb,bb;            /* borders of active region */
int more = 1;               /* =1 usually; =0 to terminate */
int total;                  /* total number of living cells */
char s[2] = {'+','o'};      /* s[i] is print symbol for state i */
double r_double;            /* normalized float no. from int random() */

/* display t and the current state */
void showstate(){
  int i,j; /* loop counters */
  printf("\nt=%d r:%d,%d c:%d,%d  Alive: %d\n",t,tb-2,bb+2,lb-2,rb+2,total);
  for(i=tb-2;i<=bb+2;++i){
     for(j=lb-2;j<=rb+2;++j){
        printf("%c",s[a[i][j][cur]]); }
     printf("\n");                 }; 
  printf("\n");
} /* end showstate */

/* create initial state */
void makestart(){
  int i,j; /* loop counters */
  /* assign initial border values */
  tb=5; bb=50; lb=5; rb=75;
  total = 0; /* total number of alive cells */
  /* assign initial states randomly */
  
  for(i=tb;i<=bb;++i){
    for(j=lb;j<=rb;++j){
      r_double = (double) (random()) / INT_MAX;
      if (r_double < THETA) a[i][j][cur] = 1; 
      if (a[i][j][cur]==1) total++;      }}
} /* end makestart */

/* change top level state information */
void advancestate(){
  int tmp;                        /* temporary storage */
  ++t;                            /* increment time */
  tmp=cur; cur=old; old=tmp;      /* swap state location */
} /* end advancestate */

/* termination criteria */
void checkmore(){
  if(t==TMAX){
    printf("Reached max time t=%d: ",t);
    more=0;};
}  /* end checkmore */

/* update a cell's state */
// modified this method declaration because it did not compile
int update(int i,int j)
  {
  int res; /* result from neighbor sum placed here */
  int c,u,r,d,l,ul,ur,dl,dr;  /* center and neighbor cell states */
  /* retrieve current neighborhood states */
  c=a[i][j][old]; u=a[i-1][j][old]; r=a[i][j+1][old];
  d=a[i+1][j][old]; l=a[i][j-1][old];
  ul=a[i-1][j-1][old]; ur=a[i-1][j+1][old];
  dl=a[i+1][j-1][old]; dr=a[i+1][j+1][old];
  res = u + r + d + l + ul + ur +dl +dr;
  /* rules for state transitions */
  switch(c){
   case 0:   /* quiescent state */
   // Changed to only switch if res >4 (stay at 0 is res == 4)
    if(res>4) return(1); 
    return(0);
   case 1:   /* o: alive state */
   // Changed to only switch if res <4 (stay at 1 is res == 4)
    if(res>=4) return(1);
    return(0);
   default:
    printf("\nIllegal state %d at (%d,%d): ",c,i,j);
    more=0; return(c);
  } /* end switch */
} /* end update */

/* update all cell states */
void applyrules(){
  int i,j;   /* cell position */
  total = 0; /* initialize number of alive cells */
  for(i=tb;i<=bb;++i){
    for(j=lb;j<=rb;++j){
       a[i][j][cur]=update(i,j);
       if (a[i][j][cur]==1) total++;  }} /* end fors */
} /* end applyrules */

/* main control function */
int main(){
  void showstate();
  printf("\nThreshold: %4.4f",THETA);
  printf("\nStarting simulation (%d,%d)\n\n",ROWS,COLS);
/* assign and display initial state */
  makestart();
  showstate();
/* main control loop */
  while(more){
    advancestate();
    applyrules();
    showstate();
    checkmore();
   } /* end while */
  printf(" simulation terminated\n\n");
} /* end main */
