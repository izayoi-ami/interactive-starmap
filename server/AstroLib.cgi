#!/usr/local/bin/perl
#
# Common Astro functions
#
# Collections of Astro functions for plotting star map

#use CGI qw/:standard/;
use Math::Trig;
#use MIME::Base64 ();
use Time::Local ;
use POSIX qw(ceil floor);

# Note RA in hour and DEC in degrees
sub RADEC2ALTAZ {
	
	my ($RA, $DEC) = @_;
	$RA = $RA * 15;
	my $ALT=0;
	my $AZ=0;
	
	$HA = $LST - $RA;
	my $DEC_rad = deg2rad($DEC);
	my $LAT_rad = deg2rad($LAT);
	my $HA_rad = deg2rad($HA);
	
	my $sinALT = sin($DEC_rad) *sin($LAT_rad) + cos($DEC_rad)*cos($LAT_rad)*cos($HA_rad);
	$ALT = rad2deg(asin($sinALT));

	my $cosALTcosAZ = cos($LAT_rad)*sin($DEC_rad) - sin($LAT_rad) * cos($HA_rad) * cos($DEC_rad);
	my $cosALTsinAZ = - sin($HA_rad) * cos($DEC_rad);
	
	$AZ = mod(rad2deg(atan2($cosALTsinAZ, $cosALTcosAZ)) , 360);
	
	return ($ALT,$AZ);

} #endsub RADEC2ALTAZ

sub Get_J2000Date {
#	my $J2000 = localtime();
#ref : http://www.xylem.f2s.com/kepler/sidereal.htm
# dwhole =367*y-INT(7*(y+INT((m+9)/12))/4)+INT(275*m/9)+day-730531.5
# dfrac = (h + mins/60 + seconds/3600)/24
#	d = dwhole + dfrac
	my $dwhole = 367*$year-int(7*($year+int(($month+9)/12))/4)+int(275*$month/9)+$day-730531.5;
	my $dfrac = ($hour_min)/24;
#	return ( timelocal(0,$min,$hour,$day,$month-1,$year-1900)  - timelocal( 0,0,0,1,0,100) ) / 86400 # 86400 = 24 * 60 * 60; in terms of days
	return $dwhole + $dfrac;
} #endsub Get_J2000Date	

# Local Siderial Time
sub Get_LST {
	my ($J2000Date, $hour_min) = @_;
	my $LST = (100.46 + 0.985647* $J2000Date + $LONG + 15*$hour_min );
	
	$LST = mod($LST,360);
	return $LST; # in degrees (positive)
} # endsub Get_LST

sub Get_SunRaDec {
# Ref : http://www.xylem.f2s.com/kepler/sun.html
	my $d = Get_J2000Date();
# 1. Mean Longitude (L)
	my $L = mod(280.461 + 0.9856474 * $d,360);
# 2. Mean anomaly (g)
	my $g = mod(357.528 + 0.9856003 * $d,360);
	
# 3. ecliptic longitude (lambda)
	my $lambda = $L + 1.915 * sin(deg2rad($g)) + 0.020 * sin(deg2rad(2*$g));
	my $lambda_rad = deg2rad($lambda);
	
# 4. obliquity of the ecliptic plane (epsilon)
	my $epsilon = 23.439 - 0.0000004 * $d;
	my $epsilon_rad = deg2rad($epsilon);
	
# 5. Right Ascension (RA) and Declination (DEC)
	my $RA = mod(rad2deg(atan2(cos($epsilon_rad) * sin($lambda_rad), cos($lambda_rad))),360); 
   	my $DEC = rad2deg(asin(sin($epsilon_rad)*sin($lambda_rad)));
  	
	return ($RA/15, $DEC); # RA in hour, DEC in degree
}
	
sub Get_MoonRaDec {
# Ref 1 : p.152 astronomy on the personal computer
# Ref 2 : http://www.xylem.f2s.com/kepler/moon.html
	my $d = Get_J2000Date();
	my $T = $d/36525;
# 1. Mean Longitude (L)
	my $L0 = 218.32 + 481267.883*$T;
# 2. Mean anomaly (l)
	my $l = 134.9 + 477198.85 * $T;
	my $l_rad = deg2rad($l);
	
# 3. geocentric longitude (lambda)
	my $L = $L0 + 6.29 * sin($l_rad);
	$L = $L - 1.27 * sin(deg2rad(259.2 - 413335.38* $T));
	$L = $L + 0.66 * sin(deg2rad(235.7 + 890534.23* $T));
	$L = $L + 0.21 * sin(deg2rad(269.9 + 954397.7 * $T));
	$L = $L - 0.19 * sin(deg2rad(357.5 + 35999.05 * $T));
	$L = $L - 0.11 * sin(deg2rad(186.6 + 966404.05 * $T));
	my $L_rad = deg2rad($L);

# 4. geocentric latitude
	my $bm  = 5.13 * sin(deg2rad(93.3 + 483202.03 * $T));
	$bm = $bm + 0.28 * sin(deg2rad(228.2 + 960400.87 * $T));
	$bm = $bm - 0.28 * sin(deg2rad(318.3 + 6003.18 * $T));
	$bm = $bm - 0.17 * sin(deg2rad(217.6 - 407332.2 * $T));
	
	my $bm_rad = deg2rad($bm);
	
# 5. Parallax
	my $gp = 0.9508 + 0.0518 * cos(deg2rad(134.9 + 477198.85 * $T));
	$gp = $gp + 0.0095 * cos(deg2rad(259.2 - 413335.38 * $T));
	$gp = $gp + 0.0078 * cos(deg2rad(235.7 + 890534.23 * $T));
	$gp = $gp + 0.0028 * cos(deg2rad(269.9 + 954397.7 * $T));
	my $gp_rad = deg2rad($gp);

# 6. from the parallax, get the semidiameter and the radius vector
	my $sdia = 0.2725 * $gp_rad;
	my $rm = 1 / sin($gp_rad);
	my $xg = $rm * cos($L_rad) * cos($bm_rad);
	my $yg = $rm * sin($L_rad) * cos($bm_rad);
	my $zg = $rm * sin($bm_rad);

# 7. rotate to equatorial coords obliquity of ecliptic

	my $ecl_rad = deg2rad(23.4393 - 3.563e-07 * $d);
	my $xe = $xg;
	my $ye = $yg * cos($ecl_rad) - $zg * sin($ecl_rad);
	my $ze = $yg * sin($ecl_rad) + $zg * cos($ecl_rad);

# 8. Right Ascension (RA) and Declination (DEC)
	my $RA = rad2deg(atan2($ye,$xe));
	$RA = $RA>0?$RA:$RA+360;
  	my $DEC = rad2deg(atan($ze / sqrt($xe * $xe + $ye * $ye)));
# debug use:  	
#  	($x,$y) = RADEC2ALTAZ($RA/15,$DEC);
#print '<script>window.alert("x = ',$x,',y=',$y,'")</script>';
#print '<script>window.alert("ra = ',$RA/15,',dec=',$DEC,'")</script>';
   	
	return ($RA/15, $DEC); # RA in hour, DEC in degree
}

sub Get_Celestial_long {
	my ($Ra,$Dec) = @_;
	($Ra,$Dec) = (deg2rad($Ra),deg2rad($Dec));

	my $obliquity = deg2rad(23.43917);

	my $t1 = cos($Ra)*cos($Dec);
	my $t2 = 1 - (cos($obliquity)*sin($Dec) - sin($Ra)*cos($Dec)*sin($obliquity))**2;
	my $lambda = acos($t1/sqrt($t2));
	
	
	return $lambda if ($Ra <= pi);
	return 2*pi - $lambda if ($Ra > pi) ;
#       return ($lambda * -1) if ($Ra > pi) ;
} # Get_Celestial
	
sub Get_moonPhase {
# Ref:http://scienceworld.wolfram.com/physics/CelestialtoEquatorialCoordinateTransformation.html 	
	my ($sun_RA,$sun_DEC) = Get_SunRaDec();
	my ($moon_RA,$moon_DEC) = Get_MoonRaDec();
#print '<script>window.alert(" = sun RA',$sun_RA ,',moon RA=',$moon_RA,'")</script>';
	
# Sun's ecliptic longitude (lambda)
	my $sun_lambda = Get_Celestial_long($sun_RA*15,$sun_DEC);
	
# Moon's ecliptic longitude (lambda)
	my $moon_lambda = Get_Celestial_long($moon_RA*15,$moon_DEC);

#print '<script>window.alert("x = ',$sun_lambda ,',y=',$moon_lambda,'")</script>';
	
	my $phase = $sun_lambda - $moon_lambda;
	$phase = rad2deg($phase);
	$phase = $phase - 360 if $phase > 180;
	$phase = $phase + 360 if $phase < -180;
#print '<script>window.alert("phase = ',$phase,'")</script>';
# phase = 0.5 => full moon, 0 => new moon
# return phase into 9 phases:
# new,0,1,2,3,4,5,6,7,8 
        
    return '_new' if $phase > -10 and $phase < 10;
    return '0' if $phase > -40 and $phase < -10;
    return '1' if $phase > -70 and $phase < -40;
    return '2' if $phase > -110 and $phase < -70;
    return '3' if $phase > -160 and $phase < -110;
    return '4' if $phase > -180 and $phase < -160;
    return '4' if $phase > 160 and $phase < 180;
    return '5' if $phase > 110 and $phase < 160;
    return '6' if $phase > 70 and $phase < 110;
    return '7' if $phase > 40 and $phase < 70;
    return '8' if $phase > 10 and $phase < 40;
}

# 
sub Get_PlanetRaDec {
	
  my ($planet) = @_; # 1=Mercury, 2=Venus, 3=Earth, 4=Mars, 5=Jupiter, 6=Saturn
  my $ip=0;
  my $op=0;
  my $pp=0;
  my $ap=0;
  my $np=0;
  my $ep=0;
  my $lp=0;

  # Mercury parameters
  if ($planet == 1) { 
    $ip = deg2rad(7.00507);
    $op = deg2rad(48.3339);
    $pp = deg2rad(77.45399999999999);
    $ap = 0.3870978;
    $np = deg2rad(4.092353);
    $ep = 0.2056324;
    $lp = deg2rad(314.42369);
  }

  if ($planet == 2) { 
    $ip = deg2rad(3.39472);
    $op = deg2rad(76.6889);
    $pp = deg2rad(131.761);
    $ap = 0.7233238;
    $np = deg2rad(1.602158);
    $ep = 0.0067933;
    $lp = deg2rad(236.94045);
  }
  
  if ($planet == 4) { 
    $ip = deg2rad(1.84992);
    $op = deg2rad(49.5664);
    $pp = deg2rad(336.0882);
    $ap = 1.5236365;
    $np = deg2rad(0.5240613);
    $ep = 0.0934231;
    $lp = deg2rad(262.42784);

  }
  
  if ($planet == 5) { 
    $ip = deg2rad(1.30463);
    $op = deg2rad(100.4713);
    $pp = deg2rad(15.6978);
    $ap = 5.202597;
    $np = deg2rad(8.309618000000001e-02);
    $ep = 0.0484646;
    $lp = deg2rad(322.55983);
  }
  
  if ($planet == 6) { 
    $ip = deg2rad(2.48524);
    $op = deg2rad(113.6358);
    $pp = deg2rad(88.863);
    $ap = 9.571899999999999;
    $np = deg2rad(0.03328656);
    $ep = 0.0531651;
    $lp = deg2rad(20.95759);
  }
  
  # Earth parameters
  my $ie = deg2rad(0.00041); 
  my $oe = deg2rad(349.2);
  my $pe = deg2rad(102.8517);
  my $ae = 1.00002;
  my $ne = deg2rad(0.9855796);
  my $ee = 0.0166967;
  my $le = deg2rad(328.40353);

  my $eldate = 2450680.5 - 2451545; # date of elements = 2450680.5
  my $d = Get_J2000Date();
  
  # 1. find position of Earth in orbit
  my $me = $ne * ($d - $eldate) + $le - $pe;
  my $ve = kepler($me, $ee);
  my $le2 = $ve + $pe;
  my $re = $ae * (1 - $ee * $ee) / (1 + $ee * cos($ve));
  my $xe = $re * cos($ve + $pe); # http://www.xylem.f2s.com/kepler/mean.html
  my $ye = $re * sin($ve + $pe); # http://www.xylem.f2s.com/kepler/mean.html

  # 2. position of planet in its orbit
  my $mp = $np * ($d - $eldate) + $lp - $pp;
  my $vp = kepler($mp, $ep);
  my $lp2 = $vp + $pp;
  my $rp = $ap * (1 - $ep * $ep) / (1 + $ep * cos($vp));

  # 2.5 heliocentric rectangular coordinates of planet # http://www.xylem.f2s.com/kepler/mean.html
  my $xh = $rp * (cos($op) * cos($vp + $pp - $op) - sin($op) * sin($vp + $pp - $op) * cos($ip));
  my $yh = $rp * (sin($op) * cos($vp + $pp - $op) + cos($op) * sin($vp + $pp - $op) * cos($ip));
  my $zh = $rp * (sin($vp + $pp - $op) * sin($ip));

  # 2.6 convert to geocentric rectangular coordinates
  my $xg = $xh - $xe;
  my $yg = $yh - $ye;
  my $zg = $zh;

  # 2.7 rotate around x axis from ecliptic to equatorial coords
  my $ecl = deg2rad(23.429292); # value for J2000.0 frame
  my $xeq = $xg;
  my $yeq = $yg * cos($ecl) - $zg * sin($ecl);
  my $zeq = $yg * sin($ecl) + $zg * cos($ecl);
 
  # 2.8 distance
  my $rvec = sqrt($xeq * $xeq + $yeq * $yeq + $zeq * $zeq);
    
  # 3. project planet orbit onto ecliptic to get heliocentric longitude, latitude and radius vector
  my $phi = asin(sin($lp2 - $op) * sin($ip));
  my $lp3 = atan2(sin($lp2 - $op) * cos($ip), cos($lp2 - $op)) + $op;
  my $rp2 = $rp * cos($phi);
 
  my $lambda = 0;
  # 4. geocentric ecliptic longitude
  if ($planet > 2) {
    #outer planet
    $lambda = atan($re * sin($lp3 - $le2) / ($rp2 - $re * cos($lp3 - $le2))) + $lp3;
  }
  else {
    # inner planet
    $lambda = pi + $le2 + atan($rp2 * sin($le2 - $lp3) / ($re - $rp2 * cos($le2 - $lp3)));
  }    
  # 5. geocentric ecliptic latitiude
  my $beta = atan($rp2 * tan($phi) * sin($lambda - $lp3) / ($re * sin($lp3 - $le2)));
	
  # 6. mean obliquity of ecliptic - just 23.439292 if J2000.0 elements used

  my $meanEcliptic=2451545;  # date of mean ecliptic and equinox of elements

  my $t = ($meanEcliptic - 2451545) / 36525; 
  my $e = 23.439292 + (-46.815 * $t - 0.0006 * $t * $t + 0.00181 * $t**3) / 3600; #mean obliquity of ecliptic 
  $e = deg2rad($e);
	
  $RA =	rad2deg(atan2(sin($lambda) * cos($e) - tan($beta) * sin($e), cos($lambda)));
  $DEC = rad2deg(asin(sin($beta) * cos($e) + cos($beta) * sin($e) * sin($lambda)));
  
  return ($RA/15, $DEC, $rvec);
  
} # Get_PlanetRaDec

sub kepler {
# ref : http://www.xylem.f2s.com/kepler/osculate.html
#   returns the true anomaly given

  my ($m, $ecc) = @_; 	# m - the mean anomaly in radians
  			# ecc - the eccentricity of the orbit
 
  my $e = $m;
  my $delta = 0.05;
  # Convergence : 10e-8
  while (abs($delta) >= 10e-8) {
      $delta = $e - $ecc * sin($e) - $m;
      $e = $e - $delta / (1 - $ecc * cos($e));
  }
  $v = 2 * atan(((1 + $ecc) / (1 - $ecc)) ** 0.5 * tan(0.5 * $e));
  return ($v < 0)?$v + 2*pi:$v;
}

sub ALTAZ2XY {
	my ($ALT, $AZ) = @_;
#	my ($ALT_rad, $AZ_rad) = (deg2rad($ALT), deg2rad($AZ));
	
# Orthograhpic projection
#	return ($Scale - $Scale*cos($ALT_rad)*sin($AZ_rad), $Scale - $Scale*cos($ALT_rad)*cos($AZ_rad));

# Stereographic projection
#	my $xpi = cos($ALT_rad)*sin($AZ_rad);
#	my $ypi = cos($ALT_rad)*cos($AZ_rad);
#	my $zpi = sin($ALT_rad);
#	return ($Scale - $Scale*2*$xpi/(1+$ypi),$Scale - $Scale*2*$ypi/(1+$ypi));
# Delphi 	
	return ($Radius + cos(deg2rad($AZ+90))*(1-$ALT/90)*$Radius, $Radius - sin(deg2rad($AZ+90))*(1-$ALT/90)*$Radius);

} # endsub ALTAZ2XY

sub RADEC2XY {
	my ($x,$y) = ALTAZ2XY(RADEC2ALTAZ(@_));
	return (ceil($x),ceil($y));
} # endsub RADEC2XY

sub Ecliptic2RaDec {
  my ($x,$y,$z) = @_;
  
  my $c = cos($eps_rad);
  my $s = sin($eps_rad);
  
  my $yy = $c*$y - $s*$z;
  my $zz = $c*$z + $s*$y;
    
  my $rho = $x**2 + $yy**2;
  my $r = sqrt($rho + *zz**2);
  my $phi = atan2($yy,$x);
  $phi = $phi + 2*pi if $phi < 0;
  $rho = sqrt($rho);
  return (rad2deg($phi)/15, rad2deg(atan2($zz,$rho)));
}	

sub mod {
#approximate is still good enougth	
	return $_[0] % $_[1];

#precise routine
#	use POSIX qw(ceil floor);
#	my ($num,$div) = @_;

#	my $int_result = $num % $div;
#	my $factorial_part = $num>0?$num - floor($num):$num-ceil($num); #preserve sign
#	my $real_result = $int_result + $factorial_part;
#	return $real_result;
}


1;
