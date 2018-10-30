#!/usr/local/bin/perl
#
# Author : Wizard Computer Technology Company
# All copyright reserved
# starmap.cgi
#
# 

require "AstroLib.cgi";
require "DefaultValue.cgi";
use CGI;
#use Text::ParseWords;                                     
use Math::Trig;

&init_default;
$query = new CGI;
$sinALT=0.0;
$LST=0.0;
$HA=0.0;

&process_inputparameter($query);

# stylesheet 
$StarMapStyle=<<END;
<!-- 
    .cName {
	color:$_Constellation_NameColor;
	font-size:$_snamesize;
	width:100px;
    }
    .lName {
	color:#FFFFFF;
	font-size:$_lnamesize;
    }
    .lName_p {
	color:#000000;
	font-size:$_lnamesize;
    }
-->
END

if ($pageLanguage eq "E") {
print $query->header(	-type=>'text/html');
print $query->start_html(-title=>"Hong Kong Space Museum Interactive Star Map",
			 -BGCOLOR=>'white',
			 -meta=>{'keywords' => 'Interactive Star Map'},
			 -TEXT=>'black',
			 -style=>{-code=>$StarMapStyle},
			 -TopMargin=>'0'
			 );
} else {			 
print $query->header(	-type=>'text/html',
			-charset=>'big5');
print $query->start_html(-title=>"香港太空館網上星圖",
			 -BGCOLOR=>'white',
			 -meta=>{'keywords' => '網上星圖'},
			 -TEXT=>'black',
			 -style=>{-code=>$StarMapStyle},
			 -TopMargin=>'0'
			 );
}			 
# establish a frame
print '<table width=',$Size-20,' cellpadding=0 cellspacing=5>';
print '<tr><td class="lName" style="color:#000000;font-size:11;vertical-align:top" width=95 rowspan=2>';

if ($pageLanguage eq "E") {
  print "<input type=button value=Print onClick='javascript:window.print()'><br><br>" if $IsPrint eq "Yes";
  print "$CityName<br>";
  print "Longitude:$LONG degrees<br>";
  print "Latitude:$LAT degrees<br>";
  print "Time Zone:$TimeZone<br>";
  print "$day/$month/$year<br>";
  print $hour if $hour_min_local <= 12;
  print $hour - 12 if $hour_min_local > 12;
  print ":00";
  print ' AM' if $hour_min_local <= 12;
  print ' PM' if $hour_min_local > 12;
  print '<br>';
  print "<br>" if $Size ne "640";
  print "Magnitude of Stars";
  if ($MinMag < 4) {
  	print '<img src="./image/legend_3.gif"><br>';
  } elsif ($MinMag < 5) {
  	print '<img src="./image/legend_4.gif"><br>';
  } else  {
  	print '<img src="./image/legend_5.gif"><br>';
  }
  print "<br>" if $Size ne "640";
  print "<div style='background:#000000;'>" if $IsPrint ne "Yes";
  print "<div style='background:#EEEEEE;'>" if $IsPrint eq "Yes";
  print "<table class=lName";
  print "_p " if $IsPrint eq "Yes";
  print " width=95>";
  print '<tr><td width=65>Nebula</td><td align=center><img src="',$_DeepSky_src{2},'"></td></tr>';
  print '<tr><td >Open Cluster</td><td align=center><img src="',$_DeepSky_src{1},'"></td></tr>';
  print '<tr><td >Globular Cluster</td><td align=center><img src="',$_DeepSky_src{3},'"></td></tr>';
  print '<tr><td >Galaxy</td><td align=center><img src="',$_DeepSky_src{4},'"></td></tr>';
  print '<tr><td >Comet</td><td align=center><img src="',$_Comet_src,'"></td></tr>';
  print '<tr><td >Meteor Shower</td><td align=center><img src="',$_Shower_src,'"></td></tr>';
  print '<tr><td >Sun&nbsp</td><td align=center><img src="',$_Sun_src,'"></td></tr>';
  print '<tr><td >Moon</td><td align=center><img src="',$_Moon_src,'"></td></tr>';
  print '<tr><td >Mercury</td><td align=center><img src="',$_Mercury_src,'"></td></tr>';
  print '<tr><td >Venus</td><td align=center><img src="',$_Venus_src,'"></td></tr>';
  print '<tr><td >Mars</td><td align=center><img src="',$_Mars_src,'"></td></tr>';
  print '<tr><td >Jupiter</td><td align=center><img src="',$_Jupiter_src,'"></td></tr>';
  print '<tr><td >Saturn</td><td align=center><img src="',$_Saturn_src,'"></td></tr>';
  print "</table>";
  print "</div>";	
  print "<br>(Move your mouse over the celestial objects to see the name)";
  } else {
  print "$CityName<br>";
  print "經度:$LONG 度<br>";
  print "緯度:$LAT 度<br>";
  print "時區:$TimeZone<br>";
  print "$year 年 $month 月 $day 日<br>";
  print '上午 ' if $hour_min_local <= 12;
  print '下午 ' if $hour_min_local > 12;
  print $hour if $hour_min_local <= 12;
  print $hour - 12 if $hour_min_local > 12;
  print " 時<br>";
  print "<br>" if $Size ne "640";
  print "星等";
  if ($MinMag < 4) {
  	print '<img src="./image/legend_3.gif"><br>';
  } elsif ($MinMag < 5) {
  	print '<img src="./image/legend_4.gif"><br>';
  } else  {
  	print '<img src="./image/legend_5.gif"><br>';
  }
  print "<br>" if $Size ne "640";
  print "<div style='background:#000000;'>" if $IsPrint ne "Yes";
  print "<div style='background:#EEEEEE;'>" if $IsPrint eq "Yes";
  print "<table class=lName";
  print "_p " if $IsPrint eq "Yes";
  print " width=95>";
  print '<tr><td width=58>星雲</td><td align=center><img src="',$_DeepSky_src{2},'"></td></tr>';
  print '<tr><td >疏散星團</td><td align=center><img src="',$_DeepSky_src{1},'"></td></tr>';
  print '<tr><td >球狀星團</td><td align=center><img src="',$_DeepSky_src{3},'"></td></tr>';
  print '<tr><td >星系</td><td align=center><img src="',$_DeepSky_src{4},'"></td></tr>';
  print '<tr><td >彗星</td><td align=center><img src="',$_Comet_src,'"></td></tr>';
  print '<tr><td >流星雨</td><td align=center><img src="',$_Shower_src,'"></td></tr>';
  print '<tr><td >太陽</td><td align=center><img src="',$_Sun_src,'"></td></tr>';
  print '<tr><td >月球</td><td align=center><img src="',$_Moon_src,'"></td></tr>';
  print '<tr><td >水星</td><td align=center><img src="',$_Mercury_src,'"></td></tr>';
  print '<tr><td >金星</td><td align=center><img src="',$_Venus_src,'"></td></tr>';
  print '<tr><td >火星</td><td align=center><img src="',$_Mars_src,'"></td></tr>';
  print '<tr><td >木星</td><td align=center><img src="',$_Jupiter_src,'"></td></tr>';
  print '<tr><td >土星</td><td align=center><img src="',$_Saturn_src,'"></td></tr>';
  print "</table>";
  print "</div>";
  print "<br>(將滑鼠放在天體上可看到其名稱)";		
  
}  

print '</td>';

# plot the word 'NORTH' 
print '<td ></td><td style="vertical-align:bottom" width="' ;
print $_radius{$Size}*2 ; # get some allowance for cellpadding
print '" align="center"><img height=';
print $_ESWN_height{$Size};
print ' width=';
print $_ESWN_width{$Size};
#print ' align="center" src="./image/north1.gif"></td><td ></td></tr>';
print ' align="center" src="./image/north', $_ESWN_src{$Size}, '"></td><td>' if $IsPrint ne "Yes";
print ' align="center" src="./image/north', $_ESWN_src_p{$Size}, '"></td><td>' if $IsPrint eq "Yes";
print "<input type=button value=列印 onClick='javascript:window.print()'><br><br>"  if $IsPrint eq "Yes";
print '</td></tr>';
# End plot
print '<tr>';
# plot the word 'EAST' 
print '<td align=right><img height=';
print $_ESWN_height{$Size};
print ' width=';
print $_ESWN_width{$Size};
print ' align="center" src="./image/east', $_ESWN_src{$Size}, '"></td>' if $IsPrint ne "Yes";
print ' align="center" src="./image/east', $_ESWN_src_p{$Size}, '"></td>' if $IsPrint eq "Yes";
# End plot the word 'EAST' 
print '<td style="vertical-align:top" height=';
print $_radius{$Size}*2;
print '>';
print '<div style="position:absolute">';

print $query->img({-src => "$_NightCircle_gif{$Size}"}) if $hour_min_local > 17 || $hour_min_local < 6;
print $query->img({-src => "$_DayCircle_gif{$Size}"}) if $hour_min_local <= 17 && $hour_min_local >= 6;
# add more time period if you want.

&plot_Ecliptic if $IsEcliptic eq "Yes";
&plot_Equator if $IsEquator eq "Yes";
&print_star;
&print_constellationlines;
&print_DeepSky if $IsDeepSky eq "Yes";
&print_constellationnames;
&plot_Poles if $IsPoles eq "Yes"; 
&print_sun_and_planets ;
&print_moon if $IsMoon eq "Yes";
&print_Comets if $IsComets eq "Yes";
&print_Showers if $IsShowers eq "Yes";
#&plot_GridLines;

print '</div>';
print '</td>';
# plot the word 'WEST' 
print '<td ><img height=';
print $_ESWN_height{$Size};
print ' width=';
print $_ESWN_width{$Size};
print ' align="center" src="./image/west', $_ESWN_src{$Size}, '"></td>' if $IsPrint ne "Yes";
print ' align="center" src="./image/west', $_ESWN_src_p{$Size}, '"></td>' if $IsPrint eq "Yes";
# End plot the word 'WEST' 
print '</tr>';
# plot the word 'South' and HKSM logo
print '<tr ><td colspan=3 style="vertical-align:top" ><img ';
print ' align="Left" src="./image/south', $_ESWN_src{$Size}, '"></td></tr>' if $IsPrint ne "Yes";
print ' align="Left" src="./image/south', $_ESWN_src_p{$Size}, '"></td></tr>' if $IsPrint eq "Yes";
# End plot

#print '<tr><td></td><td></td><td></td></tr>';
print '</table>';

print $query->end_html;
	

# Grab necessary parameter. If any parameter missed, then use default
sub process_inputparameter {
	my($query) = @_;
	$pageLanguage	= $query->param("pageLanguage")?$query->param("pageLanguage"):"C";
	$IsPrint 	= $query->param("PrintFriendly")?$query->param("PrintFriendly"):"No";
	$IsPoles 	= $query->param("SelectPoles")?$query->param("SelectPoles"):"No";
	$IsEquator 	= $query->param("SelectEquator")?$query->param("SelectEquator"):"No";
	$IsEcliptic 	= $query->param("SelectEcliptic")?$query->param("SelectEcliptic"):"No";
	$IsSun 		= $query->param("SelectSun")?$query->param("SelectSun"):"No";
	$IsMoon 	= $query->param("SelectMoon")?$query->param("SelectMoon"):"No";
	$IsPlanets 	= $query->param("SelectPlanets")?$query->param("SelectPlanets"):"No";
	$IsDeepSky	= $query->param("SelectDeepSky")?$query->param("SelectDeepSky"):"No";
	$IsComets	= $query->param("SelectComets")?$query->param("SelectComets"):"No";
	$IsShowers	= $query->param("SelectShowers")?$query->param("SelectShowers"):"No";
	$CityName	= $query->param("City")?$query->param("City"):"";
	$MinMag 	= $query->param("MinMag")?$query->param("MinMag"):4;
	$LAT 		= $query->param("LAT")?$query->param("LAT"):$_LAT;
	$LONG 		= $query->param("LONG")?$query->param("LONG"):$_LONG;
	$year 		= $query->param("Year")?$query->param("Year"):$_year;
	$month 		= $query->param("Month")?$query->param("Month"):$_month;
	$day 		= $query->param("Day")?$query->param("Day"):$_day;
	$TimeZone 	= $query->param("TimeZone")?$query->param("TimeZone"):0;
	$hour 		= $query->param("Hour");
	$min 		= 0;
	$hour_min_local = $hour + $min / 60;
	$hour_min 	= $hour_min_local - $TimeZone;	# ceiling of $LONG
	$RA_hour 	= $query->param("RA_hour")?$query->param("RA_hour"):0;
	$RA_min 	= $query->param("RA_min")?$query->param("RA_min"):0;
	$RA 		= $RA_hour + $RA_min / 60;
	$DEC_deg 	= $query->param("DEC_deg")?$query->param("DEC_deg"):0;
	$DEC_min 	= $query->param("DEC_min")?$query->param("DEC_min"):0;
	$DEC 		= $DEC_deg + $DEC_min / 60;
	$Size 		=  $query->param("Size")?$query->param("Size"):$_Size;
	$Radius 	= $_radius{$Size};
#	$Radius = $Size / 2;
	$ALT = 0;
	$AZ = 0;
	$X=$Y=0;
# put LST to cacluate here, no need to calcaute it for every RA,Dec. 	
	$LST = Get_LST( Get_J2000Date(), $hour_min);
	
# obliquity of ecliptic (eps) which used when printing ecliptic	
  	$eps = 23.43929111;
  	$eps_rad = deg2rad($eps);

# Array to store Constellation Name which is used to prevent duplicated entry  	
	@constellationName = ();
	
# Reassign some default file for print friendly version 
	if ($IsPrint eq "Yes") {
		$_Pole_src = $_Pole_src_print;   
		$_Comet_src = $_Comet_src_print;   
  		$_Shower_src = $_Shower_src_print;   
		$_Sun_src = $_Sun_src_print . $_PrintSize_variant{$Size};   
  		$_Moon_src = $_Moon_src_print;
  		$_Mercury_src = $_Mercury_src_print . $_PrintSize_variant{$Size};
  		$_Venus_src = $_Venus_src_print . $_PrintSize_variant{$Size};
  		$_Mars_src = $_Mars_src_print . $_PrintSize_variant{$Size};
  		$_Jupiter_src = $_Jupiter_src_print . $_PrintSize_variant{$Size};
  		$_Saturn_src = $_Saturn_src_print . $_PrintSize_variant{$Size};
  		%_DeepSky_src = %_DeepSky_src_print;
		%_NightCircle_gif = %_circle_gif_print;
		%_DayCircle_gif = %_circle_gif_print;
	 	$_Constellation_NameColor = $_Constellation_NameColor_print; 
  	}
 	$_Comet_src = $_Comet_src . $_PrintSize_variant{$Size};
	$_DeepSky_src{1} = $_DeepSky_src{1} . $_PrintSize_variant{$Size};
	$_DeepSky_src{2} = $_DeepSky_src{2} . $_PrintSize_variant{$Size};
	$_DeepSky_src{3} = $_DeepSky_src{3} . $_PrintSize_variant{$Size};
	$_DeepSky_src{4} = $_DeepSky_src{4} . $_PrintSize_variant{$Size};
} # endsub print_testinputparameter

sub print_convertRADEC2ALTAZ {
($ALT, $AZ) = RADEC2ALTAZ($RA,$DEC);

print "<h3>convert RA=$RA_hour hr. $RA_min mins , DEC = $DEC_deg &deg; $DEC_min mins to ALT and AZ</h3>";
print "ALT = $ALT";
print "<br>AZ = $AZ<br>";

} # endsub print_convertRADEC2ALTAZ

sub is_inside{
	my ($a,$b) = @_;
	# give some allowance for the starmap diagram. 
	# because the drawing may not be exactly, say a radius=500 cicle
	my $Radius1 = $Radius - 0; 
	
	# transform the coordinates to origin
	($a,$b) = ($a-$Radius1, $b-$Radius1);
	return (($a*$a + $b*$b) < ($Radius1*$Radius1));
} # endsub is_inside

# note that size of sun.gif is 25x25
sub print_sun
{
	my ($RA,$DEC) = Get_SunRaDec();
	my ($x, $y) = RADEC2XY($RA,$DEC);
	my $name = $pageLanguage eq "E"?"Sun":"太陽";
	if(is_inside($x,$y)) {
	  print '<div  style="position:absolute;top:', $y-12, 'px;left:',$x-12,'px;font-size:1;"><img ALT="',$name,'" Title="',$name,'" src="',$_Sun_src,'" ></img></div>';
	}
}	

# note that size of moon.gif is 25x25
sub print_moon
{
	my ($RA,$DEC) = Get_MoonRaDec();
	my ($x, $y) = RADEC2XY($RA,$DEC);
	my $name = $pageLanguage eq "E"?"Moon":"月亮";
	if(is_inside($x,$y)) {
	  print '<div  style="position:absolute;top:', $y-12 , 'px;left:',$x-12,'px;font-size:1;"><img ALT="',$name,'" Title="',$name,'"  src="./image/moon',Get_moonPhase(),'.gif" ></img></div>' if $IsPrint eq "No" ;
	  print '<div  style="position:absolute;top:', $y-12 , 'px;left:',$x-12,'px;font-size:1;"><img ALT="',$name,'" Title="',$name,'"  src="./image/moon',Get_moonPhase(),'_p.gif" ></img></div>' if $IsPrint eq "Yes" ;
	}
}	

sub print_sun_and_planets
{
if ($IsPlanets eq "Yes") {
# Outer planet always behind sun, therefore print them first	

	# Saturn
	my ($RA,$DEC,$Saturn_dist) = Get_PlanetRaDec(6);
	my ($x, $y) = RADEC2XY($RA,$DEC);
	$name = $pageLanguage eq "E"?"Saturn":"土星";
	if(is_inside($x,$y)) {
	  print '<div  style="position:absolute;top:', $y-10, 'px;left:',$x-10,'px;font-size:1;"><img ALT="',$name,'" Title="',$name,'" src="',$_Saturn_src,'" ></img></div>';
	}
	
	# Jupiter
	my ($RA,$DEC,$Jupiter_dist) = Get_PlanetRaDec(5);
	$name = $pageLanguage eq "E"?"Juipter":"木星";
	my ($x, $y) = RADEC2XY($RA,$DEC);
	if(is_inside($x,$y)) {
	  print '<div  style="position:absolute;top:', $y-10 , 'px;left:',$x-10,'px;font-size:1;"><img ALT="',$name,'" Title="',$name,'" src="',$_Jupiter_src,'" ></img></div>';
	}
	
	# Mars
	my ($RA,$DEC,$Mars_dist) = Get_PlanetRaDec(4);
	my ($x, $y) = RADEC2XY($RA,$DEC);
	$name = $pageLanguage eq "E"?"Mars":"火星";
	if(is_inside($x,$y)) {
	  print '<div  style="position:absolute;top:', $y-6 , 'px;left:',$x-6,'px;font-size:1;"><img ALT="',$name,'" Title="',$name,'" src="',$_Mars_src,'" ></img></div>';
	}

  }

# Sun and Inner Planet
	
	# mercury
	my ($Mercury_RA,$Mercury_DEC,$Mercury_dist) = Get_PlanetRaDec(1);

	# venus
	my ($Venus_RA,$Venus_DEC,$Venus_dist) = Get_PlanetRaDec(2);

# mercury < venus < sun
# venus < mercury < sun
# sun < mercury < venus
# mercury < sun < venus 
# sun < venus < mercury
# venus < sun < mercury 
#print '<script>window.alert("Venus = ',$Venus_dist,',Mercury =',$Mercury_dist,'")</script>';

	# display it first for larger distance
	if ((1 gt $Mercury_dist) and (1 gt $Venus_dist)) {
		&print_sun if $IsSun eq "Yes";
		
		if ($IsPlanets eq "Yes") {
  		plot_Mercury($Mercury_RA,$Mercury_DEC) if $Mercury_dist gt $Venus_dist;
		plot_Venus($Venus_RA,$Venus_DEC);
  		plot_Mercury($Mercury_RA,$Mercury_DEC) if $Mercury_dist lt $Venus_dist;
  		}
        }		

	if (($Venus_dist gt $Mercury_dist) and ($Venus_dist gt 1)) {
		plot_Venus($Venus_RA,$Venus_DEC) if $IsPlanets eq "Yes";

  		plot_Mercury($Mercury_RA,$Mercury_DEC) if ($Mercury_dist gt 1) and ($IsPlanets eq "Yes");
		&print_sun if $IsSun eq "Yes";
  		plot_Mercury($Mercury_RA,$Mercury_DEC) if ($Mercury_dist lt 1) and ($IsPlanets eq "Yes");
        }		

	if (($Mercury_dist gt $Venus_dist) and ($Mercury_dist gt 1)) {
  		plot_Mercury($Mercury_RA,$Mercury_DEC) if $IsPlanets eq "Yes";

		plot_Venus($Venus_RA,$Venus_DEC) if ($Venus_dist gt 1) and ($IsPlanets eq "Yes");
		&print_sun if $IsSun eq "Yes";
		plot_Venus($Venus_RA,$Venus_DEC) if ($Venus_dist lt 1) and ($IsPlanets eq "Yes");
        }		
}	

sub plot_Mercury 
{
	my ($RA,$DEC) = @_;
	my ($x, $y) = RADEC2XY($RA,$DEC);
        my $name = $pageLanguage eq "E"?"Mercury":"水星";
	if(is_inside($x,$y)) {
	    print '<div  style="position:absolute;top:', $y-6 , 'px;left:',$x-6,'px;font-size:1;"><img ALT="',$name,'" title="',$name,'" src="',$_Mercury_src,'" ></img></div>';
	}
} # end sub plot_Mercury

sub plot_Venus
{
	my ($RA,$DEC) = @_;
	my ($x, $y) = RADEC2XY($RA,$DEC);
	$name = $pageLanguage eq "E"?"Venus":"金星";
	if(is_inside($x,$y)) {
	  print '<div  style="position:absolute;top:', $y-9 , 'px;left:',$x-9,'px;font-size:1;"><img ALT="',$name,'" Title="',$name,'" src="',$_Venus_src,'" ></img></div>';
	}
} # end sub plot_Venus

# input parameter: RA,DEC
sub plot_star
{
	my ($x, $y, $mag, $color_index, $starname)=@_;
	my ($ra,$dec) = ($x,$y);
	$starname=$starname?$starname:""; # prevent any undefined starname;
	($x,$y) = RADEC2XY($x,$y);

	$mag = 0 if $mag <= 0.5;
	$mag = 1 if $mag > 0.5 and $mag <= 1.5;
	$mag = 2 if $mag > 1.5 and $mag <= 2.5;
	$mag = 3 if $mag > 2.5 and $mag <= 3.5;
	$mag = 4 if $mag > 3.5 and $mag <= 4.5;
	$mag = 5 if $mag > 4.5;

	if(is_inside($x,$y)){
	if ($IsPrint eq "Yes")
	  {
#		print '<div  style="position:absolute;top:', $y-1, 'px;left:',$x-1,'px;width:',$_star_width[$mag-1],'px;height:',$_star_height[$mag-1],'px;font-size:1;"><img ALT="',$starname,'" Title="',$starname,'" src="./image/star.gif" ></img></div>';
	  	if ($starname =~ m/^[\s]*$/) { # if starname is empty
	          print '<div  style="position:absolute;top:', $y-$_Star_offset{$mag} , 'px;left:',$x-$_Star_offset{$mag},'px;font-size:1px;"><img src="',$_Star{$mag} 
	        }
	        else {
	          print '<div  style="position:absolute;top:', $y-$_Star_offset{$mag} , 'px;left:',$x-$_Star_offset{$mag},'px;font-size:1px;"><img ALT="',$starname,'" Title="',$starname,'" src="',$_Star{$mag} 
		}
		print '_p.gif" ></img></div>';
	  }
	else
	  {
	  	if ($starname =~ m/^[\s]*$/) { # if starname is empty
	          print '<div  style="position:absolute;top:', $y-$_Star_offset{$mag} , 'px;left:',$x-$_Star_offset{$mag},'px;font-size:1px;"><img src="',$_Star{$mag} 
	        }
	        else {
	          print '<div  style="position:absolute;top:', $y-$_Star_offset{$mag} , 'px;left:',$x-$_Star_offset{$mag},'px;font-size:1px;"><img ALT="',$starname,'"  Title="',$starname,'" src="',$_Star{$mag} 
		}
		print '_3.gif" ></img></div>' if $color_index < -0.1;
		print '_2.gif" ></img></div>' if $color_index >= -0.1 and $color_index <= 1.3;
		print '_1.gif" ></img></div>' if $color_index > 1.3;
 	  }
	}
} # endsub plot_star &is_inside($x,$y)

# input RA1,DEC1,RA2,DEC2
# note
# 1.Rearrange the points so that the staring point has smaller plotting value
# 2.If the starting point lays within the circle, then check if any subsequent point outside the circle, the program can exit the for loop;
# 3.However, if the starting point lays outside the circle, then check weather the ending point also outside the cirlce
# 4.Ignore the rare case that the starting point and ending point outside the circle and some portion inside the circle
# 5.This is the most time consuming part of the program

# more note
# 1. Origin at left upper corner
# 2. -------> x-axis (positive)
#    |
#    |
#    |
#    V 
#  y-axis (positive)

sub plot_line 
{
	my ($a1,$b1,$a2,$b2) = @_;
	($a1,$b1) = RADEC2XY($a1,$b1);
	($a2,$b2) = RADEC2XY($a2,$b2);
	
	return 0 if ((not is_inside($a1,$b1)) && (not is_inside($a2,$b2))) ;
	
	my $slope = 0;
	my ($a3,$b3) = ($a1, $b1);
	if (abs(($a2-$a1)) > abs(($b2-$b1))) {
		# Rearrange ($a1,$b1), ($a2,$b2) so that $a1 < $a2
		if  ($a1 > $a2) 
		{
			($a1,$b1) = ($a2,$b2);
			($a2,$b2) = ($a3,$b3);
		}
		if(($a2-$a1) != 0) 
		{
 			$slope = ($b2-$b1)/($a2-$a1);
 			# $x is the solution of the circle and the line
			my($has_solution,$x)=solve_x($slope, -$slope*$a1+$b1,$Radius);
			if ($has_solution) {
				$a1 = $x > $a1?$x:$a1;}
			else {$a1=$a2+1;}
 			for(my $x = $a1+2;$x<$a2;$x=$x+$_linepixel)   # upper limit is $a1+2. The "+2" is for allowance
 				{
 				my $y = $slope*($x - $a2) + $b2;
				($x,$y) = (ceil($x),ceil($y));
 				if (not is_inside($x,$y)) {
 					$x=$a2+1;
 					}
 				else {
					if ($IsPrint eq "Yes")
  					  {
 					print '<div style="position:absolute;top:', $y , 'px;left:',$x,'px;width:1px;height:1px;font-size:1;overflow:hidden"><img src="./image/line.gif"></img></div>';
 					  }
 					else 
 					  {
 					print '<div style="position:absolute;top:', $y , 'px;left:',$x,'px;width:1px;height:1px;background:',$_linecolor,';font-size:1;overflow:hidden"></div>';
 					  }
 					}
 				}
 		}
	} # if (abs(($a2-$a1)) > abs(($b2-$b1)))
	else
	{
		if  ($b1 > $b2) 
			{
			($a1,$b1) = ($a2,$b2);
			($a2,$b2) = ($a3,$b3);
			}
		if(($b2-$b1) != 0) 
		{
 			$slope = ($a2-$a1)/($b2-$b1);
 			# $x is the solution of the circle and the line
			my($has_solution,$x)=solve_x($slope, -$slope*$b1+$a1,$Radius);
			if ($has_solution) {
				$b1 = $x > $b1?$x:$b1;}
			else {$b1=$b2+1;}
 			for(my $y = $b1+2;$y<$b2;$y=$y+$_linepixel)  # upper limit is $b1+2. The "+2" is for allowance
 				{
 				my $x = $slope*($y - $b2) + $a2;
 				if (not is_inside($x,$y)) {$y=$b2+1;}
 				else 
 				{
					if ($IsPrint eq "Yes")
  					  {
 					print '<div style="position:absolute;top:', $y , 'px;left:',$x,'px;width:1px;height:1px;font-size:1;overflow:hidden"><img src="./image/line.gif"></img></div>';
 					  }
 					else 
 					  {
 					print '<div style="position:absolute;top:', $y , 'px;left:',$x,'px;width:1px;height:1px;background:',$_linecolor,';font-size:1;overflow:hidden"></div>';
 					  }
 				}
 				}
 		}

	} # elseif (abs(($a2-$a1)) > abs(($b2-$b1)))
} # endsub plot_line


# Example. Note the data some are delimited by tab, some are delimited by space. !!!!!!
#9	2.833082	27.26133	2.798322	29.249493	1	Aries
#10	2.798322	29.249493	2.72422	27.713966	1	Aries
#11	2.72422	27.713966	2.833082	27.26133	1	Aries
#12	2.72422	27.713966	2.119942	23.445431	1	Aries
#13	3.818949	24.052765	4.422459	22.299515	2	Taurus
#14	5.626793	21.147869	4.598164	16.495453	2	Taurus

sub print_constellationlines {
       open (CONLINES_FILE, $_constellationLinefilename) || warn "Cannot open the file: $!";           
       while (<CONLINES_FILE>) {                                                         
           my @tmp = quotewords("	",$_);                    # separate info on each line   
           if ($tmp[0] ne ";") {                              # ignore any input line which starts with ';'  
              &plot_line($tmp[1],$tmp[2],$tmp[3],$tmp[4]);    # call subroutine to plot constellation lines
           }                                                  # 
       }                                                      # 

       close (CONLINES_FILE) || die "Cannot close $!";          # 	
	
	
} # endsub print_constellationlines

#input parameter : RA,DEC,Constallation name
sub plot_constellationname{
	my ($x,$y,$name) = @_;
my ($ra,$dec) = ($x,$y);	
	($x,$y) = RADEC2XY($x,$y);
	if (is_inside($x,$y) && (($#constellationName<0) || ($name ne $constellationName[$#constellationName])) ) {
#		print '<div class="cName" style="position:absolute;top:', $y, 'px;left:',$x, 'px;">',$name,':',$ra,',',$dec,'</div>';
		print '<div class="cName" style="position:absolute;top:', $y, 'px;left:',$x, 'px;">',$name,'</div>';

                $constellationName[$#constellationName+1] = $name;

	}
}

sub print_constellationnames{
# note that there may be more than one entry for a constellation name. This is because it can increase the chance to display a name as
# the coordinate of a name may be out of the map. Therefore remember a displayed name and don't display it if encountered again. 
       open (CONSTELLATION_FILE, $_constellationNamefilename) || warn "Cannot open the file: $!";           
       
       while (<CONSTELLATION_FILE>) {                                                         
           #chomp;                                                                      
           my @tmp = quotewords(",",$_);                    # separate info on each line   
           if ($tmp[0] ne ";") {                              # ignore any input line which starts with ';'  
             &plot_constellationname($tmp[0],$tmp[1],$tmp[2]) if $pageLanguage eq "E" ;   # call subroutine to plot constellation names (English)
             &plot_constellationname($tmp[0],$tmp[1],$tmp[3]) if $pageLanguage eq "C" ;   # call subroutine to plot constellation names (Chinese)
           }                                                   
       }                                                      

       close (CONSTELLATION_FILE) || die "Cannot close $!";          
} #endsub print_constellationnames

# Sample of Star.400
#1 0.139802 29.083334 2.000000
#2 0.152789 59.152157 2.250000
#3 0.156608 -45.756405 3.750000
#4 0.220398 15.177650 2.750000
#5 0.323912 -8.840738 3.500000
#6 0.334607 -64.887466 4.000000
#7 0.429336 -77.251892 2.750000
#8 0.436594 -43.682297 3.750000
#9 0.438122 -42.307198 2.250000

# The file is sorted by Mag. 
sub print_star{
       open (STARS_FILE, "$_starfilename") || warn "Cannot open the file: $!";           

       while (<STARS_FILE>) {                                                         
           #chomp;                                                                     
           my @tmp = quotewords("%",$_);                    # separate info on each line   
           last if $tmp[3] > $MinMag;				# Exit loop if a man of any line is greater than MinMag.
           if ($tmp[0] ne ";") {                              # ignore any input line which starts with ';'  
              if ($tmp[3] < $MinMag) {			      # ignore any star that its mag < requested dimmest star mag
                &plot_star($tmp[1],$tmp[2],$tmp[3],$tmp[4],$tmp[5]) if $pageLanguage eq "E";    # call subroutine to plot stars (english Name)
                &plot_star($tmp[1],$tmp[2],$tmp[3],$tmp[4],$tmp[6]) if $pageLanguage eq "C";    # call subroutine to plot stars (Chinese Name)
        	}
           }                                                   
       }                                                     

       close (STARS_FILE) || die "Cannot close $!";          
} #endsub print_star

sub plot_Poles {
  my ($ra,$dec) = (0,90); # North
  my ($x,$y) = RADEC2XY($ra/15,$dec);
  if(is_inside($x,$y)){
  	if ($pageLanguage eq "E") {
  		print '<div  style="position:absolute;top:', $y , 'px;left:',$x,'px;font-size:1;"><img ALT="North Celestial Pole" Title="North Celestial Pole" src="', $_Pole_src ,'"></img></div>';
	} else {
  		print '<div  style="position:absolute;top:', $y , 'px;left:',$x,'px;font-size:1;"><img ALT="北天極" Title="北天極" src="', $_Pole_src ,'"></img></div>';
	}
  }
  ($ra,$dec) = (0,-90); # South
  ($x,$y) = RADEC2XY($ra/15,$dec);
  if(is_inside($x,$y)){
  	if ($pageLanguage eq "E") {
  		print '<div  style="position:absolute;top:', $y , 'px;left:',$x,'px;font-size:1;"><img ALT="South Celestial Pole" Title="South Celestial Pole" src="', $_Pole_src ,'"></img></div>';
	} else {
  		print '<div  style="position:absolute;top:', $y , 'px;left:',$x,'px;font-size:1;"><img ALT="南天極" Title="南天極" src="', $_Pole_src ,'"></img></div>';
  	}
  }
        
} #endsub plot_poles

sub plot_Equator {
	my $dec = 0;
           for (my $ra=0;$ra <= 360; $ra=$ra+2){
                my ($x,$y) = RADEC2XY($ra/15,$dec);
		if(is_inside($x,$y)){
		  if ($IsPrint eq "Yes") {
		    print '<div style="position:absolute;top:', $y , 'px;left:',$x,'px;width:1px;height:1px;font-size:1;overflow:hidden"><img src="./image/line.gif"></img></div>';
 		    }
 		  else {
 		    print '<div style="position:absolute;top:', $y , 'px;left:',$x,'px;width:1px;height:1px;background:',$_Equatorlinecolor,';font-size:1;overflow:hidden"></div>';
 			}
 		   }
                }
} #endsub plot_Equator

sub plot_Ecliptic {
	my $dec = 0;
          for (my $ra=0;$ra <= 360; $ra=$ra+2){
            $dec = rad2deg(atan(sin(deg2rad($ra))* tan($eps_rad)));
            my ($x,$y) = RADEC2XY($ra/15,$dec);
	      if(is_inside($x,$y)){
		if ($IsPrint eq "Yes") {
		  print '<div style="position:absolute;   top:', $y , 'px; left:',$x,'px; height:1px; width:1px; overflow:hidden; font-size:1"><img src="./image/line.gif"></img></div>';
 		  }
 		else {
		  print '<div style="position:absolute;  top:',$y,'px; left:',$x,'px; height:1px; width:1px;  overflow:hidden; background:',$_Eclipticlinecolor,'; font-size:1"></div>';
		}
	      }
         }
} #endsub plot_Ecliptic

sub plot_GridLines {
	#horizonal circle 
	for (my $dec = -90;$dec <=90;$dec = $dec + 15){
           foreach my $ra (0..360){
                my ($x,$y) = RADEC2XY($ra/15,$dec);
		if(is_inside($x,$y)){
 			print '<div style="position:absolute;top:', $y , 'px;left:',$x,'px;*background:',$_linecolor,';font-size:1"></div>';
 			}
                }
            }
        #vertical circle
	for (my $ra = -90;$ra <=90;$ra = $ra + 15){
           foreach my $dec (0..360){
                my ($x,$y) = RADEC2XY($ra/15,$dec);
		if(is_inside($x,$y)){
 			print '<div style="position:absolute;top:', $y , 'px;left:',$x,'px;width:1px;height:1px;background:',$_linecolor,';font-size:1"></div>';
 			}
                }
            }
        
} #endsub plot_GridLines

# Deep sky object 12x12
sub plot_DeepSky {
	my ($commonName, $type, $Name, $x, $y, $mag)=@_;
	$name=$Name .' '. $commonName;
	($x,$y) = RADEC2XY($x,$y);
	if(is_inside($x,$y)){
	  ($x,$y) = ($x-6,$y-6); # adjust gif to center position
 	  print '<div  style="position:absolute;top:', $y , 'px;left:',$x,'px;font-size:1;"><img ALT="',$name,'" Title="',$name,'" src="', $_DeepSky_src{$type} ,'" ></img></div>';
	}
}	

sub print_DeepSky {
       open (DeepSky_FILE, $_deepskyObjectfilename) || warn "Cannot open the deepsky.TXT file: $!";           

       while (<DeepSky_FILE>) {                                                         
           my @tmp = quotewords("%",$_);                    # separate info on each line   
           if ($tmp[0] ne ";") {                              # ignore any input line which starts with ';'  
              my $mag = is_numeric($tmp[6])?$tmp[6]:0;	
              my $type = 0; 	# type of Deep Sky Objects
              if ($tmp[2] =~ /Open cluster/i) {
              	$type = 1;
                }
              if ($tmp[2] =~ /Nebula/i) {
              	$type = 2;
                }
              if ($tmp[2] =~ /Globular cluster/i) {
              	$type = 3;
                }
              if ($tmp[2] =~ /Galaxy/i) {
              	$type = 4;
                }

              if ($mag < $_deepSkyMag && $type > 0) {			      # ignore any star that its mag < requested dimmest star mag
                &plot_DeepSky($tmp[0],$type,$tmp[3],$tmp[4],$tmp[5],$mag) if $pageLanguage eq "E";    # call subroutine to plot stars (English)
                &plot_DeepSky($tmp[1],$type,$tmp[3],$tmp[4],$tmp[5],$mag) if $pageLanguage eq "C"    # call subroutine to plot stars (chinese)
        	}
           }                                                   
       }                                                     

       close (DeepSky_FILE) || die "Cannot close $!";          
}	


sub plot_Comets {
	my ($x, $y, $name)=@_;
	$name=$name?$name:""; # prevent any undefined starname;
	($x,$y) = RADEC2XY($x,$y);
	if(is_inside($x,$y)){
          # adjust gif to Comet Head 
          if ($Size = 640) {
	    ($x,$y) = ($x-4,$y-14); 
	  } else {
	    ($x,$y) = ($x-5,$y-19);
	  } 
	  print '<div  style="position:absolute;top:', $y , 'px;left:',$x,'px;font-size:1;"><img ALT="',$name,'" Title="',$name,'" src="',$_Comet_src,'" ></img></div>';    
	}
}	

sub print_Comets {
       my $CometFile = $_cometsObjectfilename . $year . $month . '.txt';
#       my $CometFile = $_cometsObjectfilename . $year . '0' . $month . '.txt' if $month < 10;
       open (Comets_FILE, $CometFile) || warn "Cannot open the Comets data file: $!";           
       my $CometName;
       my $CometName_Chinese;
       while (<Comets_FILE>) {
           my @tmp = quotewords(" ",$_);                 # separate info on each line   
           if ($tmp[0]) {                           # ignore any blank line   
       	     if ($tmp[0] =~ m!C/!) {	# a new comet found
           	$CometName = $tmp[0].$tmp[1].$tmp[2];	
	        my $line = <Comets_FILE>; # next line is Comet name in Chinese
	        @tmp = quotewords(" ",$line);
          	$CometName_chinese = $tmp[0].$tmp[1].$tmp[2];	
	     }
	     
# Sample
#2004 06 30 22    10.4969     +55.125     1.560   1.243   52.7  40.6   5.4    0.70    048.7
#2004 06 30 23    10.4979     +55.132     1.561   1.243   52.7  40.6   5.4    0.70    048.7
	  my ($RA1,$DEC1,$RA2,$DEC2,$mag,$RA,$DEC) = (0,0,0,0,0,0,0);
	  if ($tmp[0] eq $year && $tmp[1] eq $month && $tmp[2] eq $day && $tmp[3] eq $hour) {
	    ($RA,$DEC,$mag) = ($tmp[4], $tmp[5],$tmp[10]);
#	    if ($mag <= $_CometMag) {
            	&plot_Comets($RA,$DEC,$CometName)   if $pageLanguage eq "E" ;
            	&plot_Comets($RA,$DEC,$CometName_chinese)   if $pageLanguage eq "C" ;
#		}
	  }

           }                                                   
       }                                                     

       close (Comets_FILE) || die "Cannot close $!";          
}

sub plot_Showers {
	my ($name, $x, $y )=@_;
	$name=$name?$name:""; # prevent any undefined starname;
	($x,$y) = RADEC2XY($x,$y);
	if(is_inside($x,$y)){
	if ($IsPrint eq "Yes")
	  {
		print '<div  style="position:absolute;top:', $y , 'px;left:',$x,'px;font-size:1;"><img src="',$_Shower_src_print,'" ></img></div>';
	  }
	else
	  {
		print '<div  style="position:absolute;top:', $y , 'px;left:',$x,'px;font-size:1;"><img ALT="',$name,'" Title="',$name,'" src="',$_Shower_src,'" ></img></div>';
 	  }
	}
}	

sub print_Showers {
       open (Showers_FILE, $_showersObjecfilename) || warn "Cannot open the showers.TXT file: $!";           

       while (<Showers_FILE>) {                                                         
           #chomp;                                                                     
           my @tmp = quotewords("%",$_);                 # separate info on each line   
           if ($tmp[0] ne ";") {                           # ignore any input line which starts with ';'  
           	my $ShowerFromMonth = $tmp[4];	
           	my $ShowerFromDay = $tmp[5];	
           	my $ShowerToMonth = $tmp[6];
           	my $ShowerToDay = $tmp[7];
           	
           	if ((($month*100+$day) > ($ShowerFromMonth*100+$ShowerFromDay)) && (($month*100+$day) < ($ShowerToMonth*100+$ShowerToDay))) {
                  &plot_Showers($tmp[0],$tmp[2],$tmp[3]) if $pageLanguage eq "E";    # call subroutine to plot stars (English)
                  &plot_Showers($tmp[1],$tmp[2],$tmp[3]) if $pageLanguage eq "C";    # call subroutine to plot stars (Chinese)
        	}
           }                                                   
       }                                                     

       close (Showers_FILE) || die "Cannot close $!";          
}	

# solve solution of y=ax+b and x2+y2=r2
# input : a,b,r
# output : true/false, x1, x2 (x1<=x2)
sub solve_x
{
	my ($a,$b,$r) = @_;
	$b = $b+$a*$r-$r; # transform the center of circle
	my $ab = 2*$a*$b;
	my $tmp = 1+$a*$a;
	my $delta = ($ab)*($ab) - 4*$tmp*($b*$b-$r*$r);

	if ($delta < 0) {
		return (0,undef,undef);
	} 
	else {
		my $x1 = (- $ab+sqrt($delta)) / (2*$tmp) + $r;
		my $x2 = (- $ab-sqrt($delta)) / (2*$tmp) + $r;
		($x1 < $x2)?return (1,$x1,$x2):return(1,$x2,$x1);
	}
} #endsub solve_x

sub quotewords {
  my $delimiter = @_[0];
	return (@_[1] =~/([^$delimiter]+)[$delimiter\r\n]/g);
}

# ref: perlfaq4
sub getnum {
        use POSIX qw(strtod);
        my $str = shift;
        $str =~ s/^\s+//;
        $str =~ s/\s+$//;
        $! = 0;
        my($num, $unparsed) = strtod($str);
        if (($str eq '') || ($unparsed != 0) || $!) {
            return undef;
        } else {
            return $num;
        } 
    }
    
sub is_numeric { defined getnum($_[0]) }    
