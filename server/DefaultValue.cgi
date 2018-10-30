#!/usr/local/bin/perl
#
# Default paramber used in the star map program
#


use Time::localtime;
 
sub init_default {
# data file
 $_starfilename = "stars.txt";
 $_constellationLinefilename = "Wline.dat";
 $_constellationNamefilename = "constellation.txt";                                                
 $_deepskyObjectfilename = "deepsky.txt";
 $_cometsObjectfilename = "comet";  # appended by yyyymm.txt
 $_showersObjecfilename = "showers.txt"; 
# set defaul datetime as local server datetime  
 $_year = localtime->year()+1900;
 $_month = localtime->mon()+1;
 $_day = localtime ->mday();
 $_hour = localtime->hour();
 $_min = localtime ->min();
 $_sec = localtime ->sec();
# default deep sky mag. Show deep sky object if Mag <= _deepSkyMag
 $_deepSkyMag = 8; 
# default Comet mag. Show Comets if Mag <= _CometMag
 $_CometMag = 4.5; 
# defult lat and long
# Ref : HK Lat and Long : http://www.info.gov.hk/landsd/geodata/cindex.htm
 $_LAT = 0;
 $_LONG = 0;
# Default star chart dimension $_sizex$_size 
 $_Size = 640;
# star color of mag = <=1,<=2,<=3,<=4,<=5,>5
 @_star_color=('#00ff00','#00ff00','#20f3ff','#20f3ff','#20f3ff','#20f3ff');
# star width in pixel of mag = <=1,<=2,<=3,<=4,<=5,>5
 @_star_width= (4,4,3,3,2,2);
# star height in pixel of mag = <=1,<=2,<=3,<=4,<=5,>5
 @_star_height=(4,4,3,3,2,2);
 $_snamesize='10pt'; # font size of star name
 $_lnamesize='9pt'; # font size of legend
 $_snamexoffset=5; # number of pixel for the star name from the star (right hand side)
 $_snameyoffset=2; # number of pixel for the star name from the star (top)
 $_Equatorlinecolor = '#00ffc0'; # Equator line color
 $_Eclipticlinecolor = '#FFFF00'; # Ecliptic line color
 $_linecolor = '#ffc000'; # consellation line color
 $_linepixel = 3; # number of pixel per point of a consellation line. minimum = 1 => solid line
 $_Constellation_NameColor = '#ee6699'; 
 $_Constellation_NameColor_print = '#000000'; 
# gif file name correspond to different star map size
 %_NightCircle_gif = ( 
        640  => './image/400.gif',
        800  => './image/500.gif',
        1024  => './image/700.gif'
    ); 
%_DayCircle_gif = ( 
        640  => './image/400d.gif',
        800  => './image/500d.gif',
        1024  => './image/700d.gif'
    ); 
## gif file name correspond to different star map size for printing
 %_circle_gif_print = ( 
        640  => './image/400p.gif',
        800  => './image/500p.gif',
        1024  => './image/700p.gif'
    ); 
# Radius of the star map, MUST be half of the gif file 
 %_radius = (
        640  => 199,
        800  => 248,
        1024  => 341
   );
# image height of East, South, West, North 
 %_ESWN_height = (
        640  => 20,
        800  => 27,
        1024  => 30
   );
   
# image width of East, South, West, North 
 %_ESWN_width = (
        640  => 40,
        800  => 53,
        1024  => 60
   );
# image source of East, South, West, North // Append to standard name
 %_ESWN_src = (
        640  => '1.gif',
        800  => '2.gif',
        1024 => '3.gif'
   );
# printing image source of East, South, West, North // Append to standard name
 %_ESWN_src_p = (
        640  => '1_p.gif',
        800  => '2_p.gif',
        1024 => '3_p.gif'
   );

# image source of DeepSky object for screen
 %_DeepSky_src = (
        1  => './image/opencluster_s',
        2  => './image/nebula_s',
        3  => './image/globularcluster_s',
        4  => './image/galaxy_s'
   );
   
# image source of DeepSky object for printing
 %_DeepSky_src_print = (
        1  => './image/opencluster_p',
        2  => './image/nebula_p',
        3  => './image/globularcluster_p',
        4  => './image/galaxy_p'
   );

# Append to standard name
 %_PrintSize_variant = (
        640  => '1.gif',
        800  => '2.gif',
        1024 => '2.gif'
   );
# star image by Mag  (for screen appended by _1.gif , _2.gif, _3.gif depends on color_index, for printing : just appended by _p.gif)
 %_Star = (
        5  => './image/star5',
        4  => './image/star4',
        3  => './image/star3',
        2  => './image/star2',
        1  => './image/star1',
        0  => './image/star0'
   );
# star center offset
 %_Star_offset = (
        5  => 0,
        4  => 1,
        3  => 2,
        2  => 2,
        1  => 3,
        0  => 4
   );

# image source of pole
  $_Pole_src = './image/pole.gif';   
  $_Pole_src_print = './image/pole_p.gif';   
# image source of comet
  $_Comet_src = './image/comet_s';   
  $_Comet_src_print = './image/comet_p';   
# image source of Meteor Shower
  $_Shower_src = './image/meteorshower_s.gif';   
  $_Shower_src_print = './image/meteorshower_p.gif';   
# image source of Meteor Shower
  $_Sun_src = './image/sun.gif';   
  $_Sun_src_print = './image/sun_p';    # the suffix is appended in starmap.cgi
# image source of Meteor Shower
  $_Moon_src = './image/moon4.gif';   
  $_Moon_src_print = './image/moon_p.gif';   
# image source of planets  
  $_Mercury_src = './image/mercury.gif';
  $_Mercury_src_print = './image/mercury_p'; # the suffix is appended in starmap.cgi
  $_Venus_src = './image/venus.gif';
  $_Venus_src_print = './image/venus_p'; # the suffix is appended in starmap.cgi
  $_Mars_src = './image/mars.gif';
  $_Mars_src_print = './image/mars_p'; # the suffix is appended in starmap.cgi
  $_Jupiter_src = './image/jupiter.gif';
  $_Jupiter_src_print = './image/jupiter_p'; # the suffix is appended in starmap.cgi
  $_Saturn_src = './image/saturn.gif';
  $_Saturn_src_print = './image/saturn_p'; # the suffix is appended in starmap.cgi
   
   
}
1;
