　      Computer programs for calculating LF/MF field strengths and phase
　　　　     in distances up to 4000 km with parabolic layer model
                                      by
 N. Wakai
                 Institution for the Advancement of Telecommunications
                               (wakai@dsk.or.jp)

Introduction
  Four computer programs revised in use of the parabolic D and E layer model are applicable for calculating field strengths and phase for frequencies from about 40 to 500 kHz over ground ranges up to 4000 km.  They are primarily based on the wave hop method in Rec. ITU-R P.684 for the sky-waves and on Rec. ITU-R P.368 for the ground-wave.
  The programs were formed originally by use of N88-basic (NEC BASIC) operative on MS-DOS and then converted to F-basic (Fujitsu BASIC) operative on Windows.  The executable files listed below accompany the respective source file written with the F-basic.

    1. List of programs
Program title
Parameters to be computed and functions　　　　　　　　　　　　
Output
684FP4F.bas
resultant field strengths and phase of 1- and 2-hop sky-waves
and the ground-wave for frequencies from 40 to 500 kHz at a
fixed time and point up to 4000 km  
display and hardcopy 
684TV4FC.bas
        
temporal variation in resultant field strengths and phase of 1- and 2-hop sky-waves and the ground-wave for frequencies from 40 to 500 kHz at a fixed point up to 4000 km 
a)  lftempv.dat 
b)  hardcopy
684DV4FC.bas
distance variation in resultant field strengths of 1- and 2- hop sky-waves and ground-wave for frequencies from 40 to 500 kHz at a fixed time in distances up to 4000 km
a)  lfdata.dat
b)   hardcopy 

2.  Quantities to be input
Transmit power in kW (for all programs)
Operating frequency in kHz (for all programs)
Geographic latitude of transmitter in degrees and its decimals with minus sign for southern latitude (for all programs)
Geographic longitude of transmitter in degrees and its decimals with minus sign for western longitude (for all programs)
Geographic latitude of receiver in degrees and its decimals with minus sign for southern latitude for 684FP4F and 684TV4FC programs
Geographic longitude of receiver in degrees and its decimals with minus sign for western longitude for 684FP4F and 684TV4FC programs
Minimum ( >100 km), maximum (4000 km) and calculation step (>1 km) distances of propagation for 684DV4FC program
Azimuth angle from transmitter to receiver in degrees measured clockwise from north for 684DV4FC program
Ground condition at transmitter; sea water, land or dry ground for all programs
Ground condition at receiver; sea water, land or dry ground for 684FP4F and 684TV4FC programs
Ground condition at path mid-point; sea water, land or dry ground for 684FP4F and 684TV4FC programs
Averaged ground condition along the course towards receiver; sea water, land or dry ground for 684DV4FC program
Solar activity epoch, minimum (ssn=0-25), medium (ssn=25-75) or maximum (ssn=75-150) for all programs
Month for which the calculation be made for all programs
Local time at transmitter for 684DV4FC program
Local time at receiver for 684FP4F and 684TV4FC programs
Start, end and step time of variation for 684TV4FC program
Local standard time meridian longitude in degrees with minus sign for western longitude for all programs

    3. Output format
For 684FP4F, results of calculation are shown numerically on the display and printed if necessary.
For 684TV4FC, resultant of 1- and 2-hop sky-waves and ground-wave in dB above μV/m, as well as the delay of phase angle of resultant of sky-waves and the ground-wave relative to the ground-wave are saved in C drive as “lftempv.dat” file.
For 684DV4FC, resultant of 1- and 2-hop sky-waves and ground-wave in dB above μV/m, as well as the delay of phase angle of resultant of sky-waves and the ground-wave relative to the ground-wave are saved in C drive as “lfdata.dat” file.
  They are also displayed and printed in the form of graphs by option at the end of calculation.  The numbers of ordinate scale in the output graphs stand for both the field strengths in dB and 1/10 of the phase delay angles in degrees.  Those figures could be rearranged graphically by use of the application software as Microsoft Excel.
   
Further information on the programs can be obtained by contacting with N. Wakai, wakai.noboru@nifty.com.
