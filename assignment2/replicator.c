#include <stdio.h>

/* Self-Replicating Structure */
#define ROWS 129    /* max array rows */
#define COLS 129    /* max array columns */
#define TMAX 100    /* termination time */
#define pr(C,U,R,D,L,R2,RES)if(pfires(C,U,R,D,L,R2,&RES)) return(RES)
#define ar(C,U,R,D,L,RES)if(afires(C,U,R,D,L)) return(RES)

/* define global variables */
int a[ROWS+1][COLS+1][2];     /* old and current states */
int t = 0;                    /* tick */
int cur = 1,old = 0;          /* current/old state index */
int tb=64,bb=68,lb=53,rb=68;  /* borders of active region */
int c,u,r,d,l;                /* center and neighbor cell states */
int more = 1;                 /* =1 usually; =0 to terminate */
int trace = 0;                /* 0 = none; 1 = rule firings except 0->0; */
                              /* 2 = all rule firings */
char s[9]= {'.','o','>','^','<','v','+','x','#'};  /* print symbols for states */

/* display t and the current state */
void showstate(){
  int i,j; /* loop counters */
  printf("\nt=%d r:%d,%d c:%d,%d\n",t,tb-2,bb+2,lb-2,rb+2);
  for(i=tb-2;i<=bb+2;++i){
     for(j=lb-2;j<=rb+2;++j){
        printf("%c",s[a[i][j][cur]]); }
     printf("\n");                 }; 
  printf("\n");
} /* end showstate */

/* initialize structure to replicate */
void initstate(){
                      a[65][56][cur] = 6; 
  a[66][55][cur] = 6; a[66][56][cur] = 1; a[66][57][cur] = 2;
                      a[67][56][cur] = 6; 
} /* end initstate */

/* change top level state information */
void advancestate(){
  int tmp;                        /* temporary storage */
  ++t;                            /* increment time */
  tmp=cur; cur=old; old=tmp;      /* swap state location */
} /* end advancestate */

/* termination criteria */
void checkmore(){
  if(t==TMAX){
    printf("Reached max time t=%d\n",t);
    more=0;};
}  /* end checkmore */

/* return 1 if orientation-specific rule fires, else 0 */
int fires(ct,ut,rt,dt,lt)
  int ct,ut,rt,dt,lt;  /* rule antecedents */
  {
  if(c==ct && u==ut && r==rt && d==dt && l==lt){
    if(trace) printf("%d(%d,%d,%d,%d) firing\n",ct,ut,rt,dt,lt);
    return(1);}
  else return(0);
} /* end fires */

/* return 1 if rule fires, else 0 (any rotation) */
/* - this fcn. does not permute symbols during rotation - */
/* - use only for rules with no oriented symbols as faster - */
int afires(ct,ut,rt,dt,lt)
  int ct,ut,rt,dt,lt;  /* rule antecedents (ct ignored) */
  {
  if(fires(ct,ut,rt,dt,lt) || fires(ct,rt,dt,lt,ut) ||
     fires(ct,dt,lt,ut,rt) || fires(ct,lt,ut,rt,dt)) return(1);
  else return(0);
}  /* end afires */

/* permute cell state once (ccw rotation) */
int p(st)
  int st;  /* state to be permuted (rotated) */
  {
  switch(st){
  case 2:  return(3);
  case 3:  return(4);
  case 4:  return(5);
  case 5:  return(2);
  default: return(st);  }; /* end switch */
}  /* end p */

/* permute cell state twice (ccw rotation) */
int p2(st)
  int st; /* state to be permuted (rotated) */
  {
  switch(st){
  case 2:  return(4);
  case 3:  return(5);
  case 4:  return(2);
  case 5:  return(3);
  default: return(st);  }; /* end switch */
}  /* end p2 */

/* permute cell state three times (ccw rotations) */
int p3(st)
  int st; /* state to be permuted (rotated) */
  {
  switch(st){
  case 2:  return(5);
  case 3:  return(2);
  case 4:  return(3);
  case 5:  return(4);
  default: return(st);  }; /* end switch */
}  /* end p3 */

/* return 1 if rule fires, else 0 (any rotation) */
/* - this function does permute symbols during rotation - */
/* - use only for rules with oriented symbols as slower - */
int pfires(ct,ut,rt,dt,lt,nc,next)
   int ct,ut,rt,dt,lt;  /* rule antecedents */
   int nc;              /* new center cell value if rule succeeds */
   int *next;           /* ptr to result in update */
   {
   if(fires(   ct,    ut,    rt,    dt,    lt))  {*next=    nc; return(1);};
   if(fires( p(ct), p(rt), p(dt), p(lt), p(ut))) {*next= p(nc); return(1);};
   if(fires(p2(ct),p2(dt),p2(lt),p2(ut),p2(rt))) {*next=p2(nc); return(1);};
   if(fires(p3(ct),p3(lt),p3(ut),p3(rt),p3(dt))) {*next=p3(nc); return(1);};
   return(0);
}  /* end pfires */

/* update a cell's state */
int update(i,j)
  int i,j; /* cell to be updated */
  {
  int res; /* result from pfires placed here */
  /* retrieve current neighborhood states */
  c=a[i][j][old]; u=a[i-1][j][old]; r=a[i][j+1][old];
  d=a[i+1][j][old]; l=a[i][j-1][old];
  /* rules for state transitions */
  switch(c){
   case 0:   /* .: quiescent state */
    if(fires(0,0,0,0,0))  return(0); 
    ar(0,0,0,0,6,0); 
    ar(0,0,6,6,0,0);  
    ar(0,0,0,1,0,0);
    // New Rules Below
    ar(0,0,0,8,6,0);
    ar(0,8,0,0,6,0);
    ar(0,6,0,6,0,0);
    ar(0,6,1,0,0,0);
    ar(0,6,0,0,1,0);
    ar(0,0,0,4,6,0); 
    ar(0,4,0,0,6,0); 
    ar(0,0,0,0,7,0); 

    pr(0,0,0,5,0,6,res);
    pr(0,0,0,2,6,0,res); 
    pr(0,2,0,0,0,0,res);

    // New Rules Below
    pr(0,0,0,2,0,0,res);
    pr(0,0,0,2,6,0,res); 
    pr(0,2,0,0,6,0,res); 
    pr(0,0,0,0,2,1,res);
    
    pr(0,0,6,0,4,0,res);
    printf("fails: 0(%d,%d,%d,%d) at (%d,%d)\n",u,r,d,l,i,j);
    more=0; return(c);
   case 1:   /* o: strand material */
     pr(1,6,2,6,6,7,res); 
     pr(1,0,0,0,2,2,res); 
     // New Rules Below
     pr(1,0,0,0,4,4,res); 
    printf("fails: 1(%d,%d,%d,%d) at (%d,%d)\n",u,r,d,l,i,j);
    more=0; return(c);
   case 2: case 3: case 4: case 5:  /* >,^,<,v: extend symbols */
     pr(2,0,0,0,1,2,res); 
     pr(2,0,1,0,7,2,res); 
     // New Rules Below
     pr(2,0,2,0,8,8,res); 
     pr(2,0,0,0,2,2,res); 
     pr(2,0,1,0,8,7,res); 
     pr(2,0,0,0,7,4,res); 
     pr(4,0,1,0,7,6,res); 
     pr(4,0,6,0,8,0,res); 
     pr(5,0,0,0,6,5,res); 
     pr(4,0,0,0,6,5,res); 
     pr(4,0,0,0,8,6,res); 
     pr(5,0,6,0,6,5,res); 
     ar(3,6,6,6,6,1);
     ar(5,6,6,1,6,1);
    printf("fails: %d(%d,%d,%d,%d) at (%d,%d)\n",c,u,r,d,l,i,j);
    more=0; return(c);
   case 6:   /* +: sheath material */
       ar(6,0,0,1,0,6);
       ar(6,0,0,7,0,6);
       // New Rules Below
       ar(6,0,0,8,0,6);
       ar(6,0,5,0,4,6);
       ar(6,0,5,0,0,6);
       pr(6,3,0,0,0,6,res);
       pr(6,0,0,0,3,6,res);
       pr(6,0,3,0,0,6,res);
       pr(6,0,0,3,0,3,res);
       pr(6,0,4,0,4,6,res);
    printf("fails: 6(%d,%d,%d,%d) at (%d,%d)\n",u,r,d,l,i,j);
    more=0; return(c);
   case 7:   /* x: internal state 1 */
    pr(7,6,2,6,6,8,res);
    // New Rules Below
    pr(7,0,2,0,8,7,res);
    pr(7,0,4,0,8,4,res);
    printf("fails: 7(%d,%d,%d,%d) at (%d,%d)\n",u,r,d,l,i,j);
    more=0; return(c);
   case 8:   /* #: internal state 2 */
   // New Rules Below
    pr(8,6,2,6,6,8,res);
    ar(8,6,8,6,6,8);
    pr(8,0,2,0,8,8,res);
    ar(8,0,7,0,8,8);
    pr(8,0,4,0,8,4,res);
    pr(8,6,4,6,6,3,res);
    printf("fails: 8(%d,%d,%d,%d) at (%d,%d)\n",u,r,d,l,i,j);
    more=0; return(c);
   default:
    printf("Illegal state %d at (%d,%d)\n",c,i,j);
    more=0; return(c);
  } /* end switch */
} /* end update */

/* update all cell states */
void applyrules(){
  int i,j;   /* cell position */
  for(i=tb-1;i<=bb+1;++i){
    for(j=lb-1;j<=rb+1;++j){
       a[i][j][cur]=update(i,j);  }} /* end fors */
} /* end applyrules */

/* main control function */
int main(){
  void showstate();
  printf("\nStarting simulation (%d,%d)\n",ROWS,COLS);
/* assign and display initial state */
  initstate();
  showstate();
/* main control loop */
  while(more){
    advancestate();
    applyrules();
    showstate();
    checkmore();
   } /* end while */
  printf("\nSimulation Terminated\n\n");
} /* end main */
