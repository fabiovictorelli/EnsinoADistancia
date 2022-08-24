/*******************************************************************/
/*                                                                 */
/* burst.c - this program computes the burstiness parameters a and */
/*  b for an HTTP log, according to Chap. 10 of the book "Capacity */
/*  Planning for Web Performance: metrics, models, and methods"    */
/*  Prentice Hall, Upper Saddle River, NJ, 1998.                   */
/*                                                                 */
/*  This program has three parameters: -f <name>, that specifies   */
/*  the name of the file containing an HTTP typical log;           */ 
/*  -e <epochs> that specifies the number of epochs of the         */
/*  interval, according to definitions in Chap. 10;                */
/*  -r <number> that specifies  the number of requests in the log  */
/*  to be processed. If this parameter is not specified, its       */
/*  value is assumed to be equal to the variable maxreq (10000)    */
/*                                                                 */
/*******************************************************************/


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <sys/types.h>
#include <time.h>

#define  MAXLINE 256
#define  MAXLOG 1000000

time_t timevet[MAXLOG];
int numtime = 0;
double drand48();
char * cname = 0;
int epochs = 17;
#define MAXEPOCH 100
int maxreq = 10000; /* number of requests processed by default */
                    /* if the parameter r is omitted           */

int getline(FILE *fp, char * line){

  int pos,ch;

  memset((void*)line,0,MAXLINE);
  pos = 0;
  while (((ch=getc(fp)) != '\n') && !feof(fp)){
    line[pos] = ch;
    pos++;
  }
  line[pos] = 0;
  return pos;
}

void usage(){
  printf("burst - Calculates the burstiness parameters\n");
  printf("Options: \n");
  printf("         -f <name>           (input file name) \n");
  printf("         -e <num>            (number of epochs) \n");
  printf("         -r <num>            (number of requests) \n");

}

void parse_args(argc,argv)
int argc;
char ** argv;
{
     extern char * optarg;
     extern int optind;
     int c ;
     while ((c = getopt(argc, argv, "f:e:r:h")) != EOF)
       switch(c) {
          case 'f': /* data file name */
               cname = optarg;
               break;
          case 'e': /* epochs */
               epochs = atoi(optarg);
               if (epochs > MAXEPOCH) {
                 epochs = MAXEPOCH;
                 fprintf(stderr,"Number of epochs must be less than %d\n",
                         MAXEPOCH);
               }
               break;
          case 'r': /* requests */
               maxreq = atoi(optarg);
               break;
          case 'h':
          default: usage();
                   exit(1);
          }
      if (!cname){
        fprintf(stderr,"Missing data file name (-f)\n");
        usage();
        exit(1);
      }
}



int main(int argc, char ** argv){
  int i,j,cc;
  FILE * file_in;
  struct tm tm;
  char * pstr;
  char line[MAXLINE];
  int Arr[MAXEPOCH], ArrPlus, ArrPlusCount, ArrMinus, ArrMinusCount;
  double Lambda_k[MAXEPOCH];
  double Lambda, totalduration,epochduration, a, b;
  time_t limit;

  parse_args(argc,argv);

  file_in = fopen(cname, "r");
  if (file_in == (FILE *) 0) {
      fprintf (stderr, "fopen failed opening input file %s",cname);
      exit(-1);
  }

  while (numtime < maxreq && getline(file_in,line) != 0){
    pstr = strstr(line,"]");
    *pstr = 0;
    pstr = strstr(line,"[");
    pstr ++;
    strptime(pstr,"%d/%b/%Y:%T%t",&tm);
    timevet[numtime] = mktime(&tm);
    numtime ++;
  }
  fclose(file_in);

  Lambda = (double)(numtime)/(timevet[numtime-1]-timevet[0]);
  totalduration = (double)(timevet[numtime-1]-timevet[0]);
  epochduration = totalduration/epochs;
  ArrPlus = ArrPlusCount = ArrMinus = ArrMinusCount = cc = 0;
  j = 0;
  for (i=0; i<epochs; i++){
    limit = (time_t) (timevet[0] + epochduration*(i+1));
    for (Arr[i]=0; (j<numtime) && (timevet[j]<=limit); j++,Arr[i]++);
    Lambda_k[i] = (double)(epochs*Arr[i])/totalduration;
    if (Lambda_k[i] > Lambda){
       ArrPlus ++;
       ArrPlusCount += Arr[i];
    }
    if (Lambda_k[i] <= Lambda) {
       ArrMinus ++;
       ArrMinusCount += Arr[i];
    }
  }

  b = (double)(ArrPlus)/epochs;
  a = (double)(ArrPlusCount)/(b*numtime);
  printf("burstiness parameter a = %f\n",a);
  printf("burstiness parameter b = %f\n",b);

  exit(0);
}



