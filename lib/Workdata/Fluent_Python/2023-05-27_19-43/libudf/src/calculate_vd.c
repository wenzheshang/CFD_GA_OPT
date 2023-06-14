#include "udf.h"

/* This UDF is to calculate the local particle deposition velocity for each computing mesh of a wall ans store it in C_UDMI(c,t,4).  */

/* C_UDMI(c,t,0): number of particles depositing on a computing mesh of a wall per square (#/m2). */
/* C_UDMI(c,t,3): time-averaged particle number concentration for the whole cabin (#/m3). Note: only one value, just store it in all the cells. */
/* C_UDMI(c,t,4): particle deposition velocity on a computing mesh (m/s). */


#define time 600 /* calculation time (s): 4 room time constants recommended. */


DEFINE_ON_DEMAND(calculate_vd)					
{
	Domain *domain;
	cell_t c;
	Thread *t;
	int i;
 
	domain=Get_Domain(1);

	thread_loop_c(t,domain)
	{
		begin_c_loop(c,t)
		{
             		C_UDMI(c,t,4)=C_UDMI(c,t,0)/C_UDMI(c,t,3)/time;
		}
		end_c_loop(c,t)
	}
}



