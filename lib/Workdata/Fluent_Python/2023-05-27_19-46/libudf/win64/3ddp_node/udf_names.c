/* This file generated automatically. */ 
/* Do not modify. */ 
#include "udf.h" 
#include "prop.h" 
#include "dpm.h" 
extern DEFINE_EXECUTE_AT_END(calculate_N_avg);				
extern DEFINE_ON_DEMAND(calculate_vd);					
__declspec(dllexport) UDF_Data udf_data[] = { 
{"calculate_N_avg", (void (*)(void))calculate_N_avg, UDF_TYPE_EXECUTE_AT_END},				
{"calculate_vd", (void (*)(void))calculate_vd, UDF_TYPE_ON_DEMAND},					
}; 
__declspec(dllexport) int n_udf_data = sizeof(udf_data)/sizeof(UDF_Data); 
#include "version.h" 
__declspec(dllexport) void UDF_Inquire_Release(int *major, int *minor, int *revision) 
{ 
*major = RampantReleaseMajor; 
*minor = RampantReleaseMinor; 
*revision = RampantReleaseRevision; 
} 
