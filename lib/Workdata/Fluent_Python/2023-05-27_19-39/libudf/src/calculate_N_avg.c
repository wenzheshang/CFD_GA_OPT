#include "udf.h"
#include "unsteady.h"

/* This UDF is to calculate the time-averaged particle number concentration for the whole cabin (C_UDMI(c,t,3)) */

/* C_UDMI(c,t,1): particle number concentration in the cell (#/m3) */
/* C_UDMI(c,t,2): accumulative particle number concentration for the whole cabin, i.e. the sum of the particle number concentration from time zero to current time (#/m3). Note: only one value, just store it in all the cells. */
/* C_UDMI(c,t,3): time-averaged particle number concentration for the whole cabin (#/m3). Note: only one value, just store it in all the cells. */


#define time_step 6000 /* total number of steps for the calculation. e.g. if calculation time is 600 s and time step size is 0.1 s, then time_step is 6000. */


DEFINE_EXECUTE_AT_END(calculate_N_avg)				
{

	Domain *domain;
	cell_t c,c1;
	Thread *t;
	Injection *Ilist;
	Injection *I;
	Particle *p;

	real num_point=0;
	real volume_point=0;
	real c_point=0;
	real x[ND_ND];
	real xcenter=0;
	real ycenter=0;
	real zcenter=0;
	real delta=0;
	real xmax=0;
	real xmin=0;
	real ymax=0;
	real ymin=0;
	real zmax=0;
	real zmin=0;

	Ilist = Get_dpm_injections();
 
	domain=Get_Domain(1);

	thread_loop_c(t,domain)
	{
		begin_c_loop(c,t)
		{
			C_UDMI(c,t,1)=0.0;
		}
		end_c_loop(c,t)
	}
	
	loop(I, Ilist)
	{
		loop(p, I->p)
		{
			c1 = P_CELL(p);
			t=Lookup_Thread(domain,2); 
					
			C_UDMI(c1,t,1)=C_UDMI(c1,t,1)+1.0/C_VOLUME(c1,t);
		}
	}

	thread_loop_c(t,domain)
	{
        	begin_c_loop(c,t)
		{
			C_CENTROID(x,c,t);

			num_point=num_point+C_UDMI(c,t,1)*C_VOLUME(c,t);
			volume_point=volume_point+C_VOLUME(c,t);
		}
		end_c_loop(c,t)

		c_point=num_point/volume_point;
	}	

	thread_loop_c(t,domain)
	{
        	begin_c_loop(c,t)
		{
			C_UDMI(c,t,2)=C_UDMI(c,t,2)+c_point;
			C_UDMI(c,t,3)=C_UDMI(c,t,2)/time_step;
		}
		end_c_loop(c,t)
	}
}


