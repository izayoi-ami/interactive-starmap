
// Parameters
// You can use the following key word to seach the code so that you can modify the default values

// 1. Regions
// 2. Conntries
// 3. City
// 4. yearMinOffset (The minimum value of year that user can select = CurrentYear - yearMinOffset)
// 5. yearMaxOffset (The maximum value of year that user can select = CurrentYear - yearMinOffset)
// 6. fromTimeZone (The minimum value of time zone that user can select)
// 7. toTimeZone (The maximum value of time zone that user can select)

// 1. Regions
/* Format of regions:

 Each line (except the last line) is in this format:
 
 "AAAAAAA,BBBBBBB" +
 
 where  AAAAAAA is the region name in English.
 	BBBBBBB is the region name in Chinese.
 
 Last line format:
 
 "AAAAAAA,"
 
 E.g.
 
"Asia,亞洲,"+
"Europe,歐洲,"+
"North America,北美洲,"


 Note : 1. There is also a comma at the last line.
 	2. The default region is the line count of the region
 	
*/ 
var regions = 
// Start to copy your Regions Here
"Asia,亞洲,"+
"Europe,歐洲,"+
"North America,北美洲,"+
"South America,南美洲,"+
"Africa,非洲,"+
"Australia and South Pacific,澳洲及南太平洋,"
// copy your Regions Up to Here
;

var defaultRegion = 1;


// 2. Countries
/* Format of Countries:

 Each line (except the last line and separator line) is in this format:
 
 "AAAAAAA,BBBBBBB" +
 
 where	AAAAAAA is the country name in English.
 	BBBBBBB is the country name in Chinese.
 
 Separator line format:
 
 ",," +
 
 Last line format:
 
 "AAAAAAA,BBBBBBB"
 
 E.g.
 
"China,中國,"+
"Japan,日本,"+
",,"+
"France,法國,"+
"German,德國,"+
",,"+
"America,美國,"+
"Canada,加拿大,"
 
 Note : 1. There is also a comma at the last line.
 	2. The separator line is used to separate different regions. 
 	   In the above example, there are two separator lines which separates 
 	   three different regions. This first group matches with the first region, etc.
 	3. The default Country is the line count of country. Do not count separator. E.g. 
 	   if defaultCountry is 4, it is Germany.
 	4. The default Country should match with default region. E.g. If region is 1, 
 	   it is no meaning to set the default country to 4.
 	   
*/ 

var countries = 
// Start to copy your Countries Here
"China,中國,"+
"Japan,日本,"+
"North Korea,北韓,"+
"South Korea,南韓,"+
"Malaysia,馬來西亞,"+
"Philippines,菲律賓,"+
"Singapore,新加坡,"+
"Tailand,泰國,"+
"Vietnam,越南,"+
"Indonesia,印尼,"+
"Cambodia,柬浦寨,"+
"India,印度,"+
"Sir Lanka,斯里蘭卡,"+
"Bangladesh,孟加拉,"+
"Pakistan,巴基斯坦,"+
"United Arab Emirates,阿聯酋,"+
"Oman,安曼,"+
"Iran,伊朗,"+
"Saudi Arabia,沙特阿拉伯,"+
"Russia,俄羅斯,"+
"Kuwait,科威特,"+
"Turkey,土耳其,"+
",,"+
"Greece,希臘,"+
"Romania,羅馬尼亞,"+
"Finland,芬蘭,"+
"Cyprus,塞普路斯,"+
"Netherlands,荷蘭,"+
"Spain,西班牙,"+
"German,德國,"+
"Switzerland,瑞士,"+
"Brussels,比利時,"+
"Hungary,匈牙利,"+
"Denmark,丹麥,"+
"France,法國,"+
"Italy,意大利,"+
"Norway,挪威,"+
"Czech Republic,捷克,"+
"Sweden,瑞典,"+
"Austria,奧地利,"+
"Poland,波蘭,"+
"United Kingdom,英國,"+
"Portugal,葡萄牙,"+
",,"+
"America,美國,"+
"Canada,加拿大,"+
"Mexico,墨西哥,"+
",,"+
"Paraguay,巴拉圭,"+
"Brazil,巴西,"+
"Argentina,阿根廷,"+
"Uruguay,烏拉圭,"+
"Chile,智利,"+
"Bolivia,玻利維亞,"+
"Dominican Republic,多米尼加共和國,"+
",,"+
"Ethiopia,埃塞俄比亞,"+
"Tanzania,坦桑尼亞,"+
"Uganda,烏干達,"+
"Kenya,肯雅,"+
"Egypt,埃及,"+
"SouthAfrica,南非,"+
"Sudan,蘇丹,"+
"Nigeria,尼日利亞,"+
"Algeria,阿爾及利亞,"+
"Congo,剛果,"+
"Cameroon,喀密隆,"+
",,"+
"Australia,澳洲,"+
"New Zealand,新西蘭,"+
"Fiji,斐濟,"
// copy your Countries Up to Here
;

var defaultCountry = 1;

// 3. Cities
/* Format of Cities:

 Each line (except the last line and separator line) is in this format:
 
 "AAAAAAA,BBBBBBB,NNNNN,MMMMM,DD" +
 
 where	AAAAAAA is the city name in English.
 	BBBBBBB is the city name in Chinese.
 	NNNNN is the default Latitude, note that no dot and there last two digits is the deciaml places. E.g. 11032 => 110.32
 		you can add a minus before the digits to indicate a negative Latitude
 	MMMMM is the default Longitude, note that no dot and there last two digits is the deciaml places. E.g. 11032 => 110.32
 		you can add a minus before the digits to indicate a negative Logitude
 	DD is the default time zone. 
 		you can add a minus before the digits to indicate a negative time zone
  
 Separator line format:
 
 ",,,,," +
 
 Last line format:

 "AAAAAAA,BBBBBBB,NNNNN,MMMMM,DD"
 
 E.g.
 
"Beijing,北京,3990,11600,8,"+
"Hong Kong,香港,2250,11400,8,"+
",,,,,"+
"Tokyo,東京,3575,13958,9,"+
",,,,,"+
"Paris,巴黎,4884,234,-8,"+
",,,,,"+
"Bonn,波恩,5080,710,1,"+
"Berin,柏林,5253,1342,1,"+
",,,,,"+
"New York,鈕約,4075,-7399,1,"+
"Washington DC,華盛頓,3890,-7702,1,"+
",,,,,"+
"Toronto,多倫多,4370,7940,1,"

 
 Note : 1. There is also a comma at the last line.
 	2. The separator line is used to separate different countries. 
 	   In the above example, there are five separator lines which separates 
 	   six different countries. This first group matches with the first country, etc.
 	3. The default City is the line count of city. Do not count separator. E.g. 
 	   if defaultCountry is 4, it is Paris.
 	4. The default City should match with default country. E.g. If default country is 1, 
 	   it is no meaning to set the default city to 4.
 	   
*/ 

var cities = 
// Start to copy your Cities Here
"Beijing,北京,3954,11628,8,"+
"Hong Kong,香港,2250,11400,8,"+
"Macau,澳門,2214,11335,8,"+
"Dalian,大連,3854,12138,8,"+
"Shanghai,上海,3112,12126,8,"+
"Tianjin,天津,3910,11710,8,"+
"Taiyuan,太原,3751,11233,8,"+
"Taibei,台北,2490,12200,8,"+
"Taichung,台中,2415,12067,8,"+
"Kaohsiung,高雄,2263,12028,8,"+
"XiAn,西安,3415,10855,8,"+
"Hefei,合肥,3151,11716,8,"+
"Chengdu,成都,3039,10404,8,"+
"Xining,西寧,3637,10149,8,"+
"Changsha,長沙,2812,11255,8,"+
"Hangzhou,杭州,3015,12010,8,"+
"Kunming,昆明,2503,10242,8,"+
"Hohhot,呼和浩特,4048,11138,8,"+
"Changchun,長春,4355,12518,8,"+
"Qingdao,青島,3604,12019,8,"+
"Wuhan,武漢,3037,11420,8,"+
"Lhasa,拉薩,2939,9102,8,"+
"Nanchang,南昌,2841,11553,8,"+
"Nanjing,南京,3203,11846,8,"+
"Harbin,哈爾濱,4545,12638,8,"+
"Nanning,南寧,2247,10821,8,"+
"Chongqing,重慶,2933,10633,8,"+
"Haikou,海口,2003,11010,8,"+
"Guilin,桂林,2518,11010,8,"+
"Urumqi,烏魯木齊,4346,8736,8,"+
"Guiyang,貴陽,2634,10443,8,"+
"Fuzhou,福州,2602,11919,8,"+
"Xiamen,廈門,2426,11804,8,"+
"Guangzhou,廣州,2310,11318,8,"+
"Zhengzhou,鄭州,3444,11342,8,"+
"Jinan,濟南,3640,11702,8,"+
"Shenyang,瀋陽,4148,12323,8,"+
",,,,,"+
"Tokyo,東京,3575,13958,9,"+
"Osaka,大阪,3469,13550,9,"+
"Sapporo,扎幌,4305,14135,9,"+
",,,,,"+
"Pyongyang,平壤,3954,12546,9,"+
",,,,,"+
"Seoul,首爾,3757,12700,9,"+
",,,,,"+
"Kuala Lumpur,吉隆坡,317,10170,8,"+
",,,,,"+
"Manila,馬尼拉,883,12558,8,"+
",,,,,"+
"Singapore,新加坡,129,10386,8,"+
",,,,,"+
"Bangkok,曼谷,1375,10052,7,"+
"Phuket,布吉,788,9840,7,"+
",,,,,"+
"Hanoi,河內,2103,10585,7,"+
",,,,,"+
"Jakarta,雅加達,-617,10680,7,"+
",,,,,"+
"Phnom-Penh,金邊,1155,10492,7,"+
",,,,,"+
"Bombay,孟買,1897,7283,5.5,"+
"Calcutta,加爾各答,2253,8837,5.5,"+
"New Delhi,新德里,2860,7720,5.5,"+
",,,,,"+
"Colombo,可倫坡,693,7985,6,"+
",,,,,"+
"Dhaka,達卡,2372,9041,6,"+
",,,,,"+
"Islamabad,伊斯蘭堡,3227,7192,5,"+
"Karachi,喀拉蚩,2487,6705,5,"+
",,,,,"+
"Dubai,杜拜,2525,5528,4,"+
",,,,,"+
"Muscat,馬斯喀特,2361,5859,4,"+
",,,,,"+
"Tehran,德黑蘭,3567,5142,3.5,"+
",,,,,"+
"Riyadh,利雅德,2467,4671,3,"+
",,,,,"+
"Moscow,莫斯科,5575,3758,3,"+
",,,,,"+
"Kuwait,科威特,2937,4798,3,"+
",,,,,"+
"Istanbul,伊斯坦布爾,4102,2897,2,"+
",,,,,"+
"Athens,雅典,3798,2373,2,"+
",,,,,"+
"Bucharest,布加勒斯特,4443,2610,2,"+
",,,,,"+
"Helsinki,赫爾辛基,6018,2494,2,"+
",,,,,"+
"Nicosia,尼古西亞,3517,3337,2,"+
",,,,,"+
"Amsterdam,阿姆斯特丹,5235,492,1,"+
",,,,,"+
"Barcelona,巴塞隆納,4138,218,1,"+
"Madrid,馬德里,4040,-368,1,"+
",,,,,"+
"Berin,柏林,5252,1340,1,"+
"Frankfurt,法蘭克福,5235,1455,1,"+
"Hamburg,漢堡,5355,1000,1,"+
",,,,,"+
"Zurich,蘇黎世,4737,855,1,"+
",,,,,"+
"Brussels,布魯塞爾,5083,433,1,"+
",,,,,"+
"Hungary,布達佩斯,4750,1908,1,"+
",,,,,"+
"Copenhagen,哥本哈根,5567,1258,1,"+
",,,,,"+
"Lyon,里昂,4575,485,1,"+
"Paris,巴黎,4887,233,1,"+
",,,,,"+
"Milan,米蘭,4547,920,1,"+
"Rome,羅馬,4190,1248,1,"+
",,,,,"+
"Oslo,奧斯陸,5992,1075,1,"+
",,,,,"+
"Prague,布拉格,5008,1447,1,"+
",,,,,"+
"Stockholm,斯德哥爾摩,6188,1375,1,"+
",,,,,"+
"Vienna,維也納,4820,1637,1,"+
",,,,,"+
"Warsaw,華沙,5225,2100,1,"+
",,,,,"+
"Aberdeen,阿伯丁,5715,-212,0,"+
"Edinburgh,愛丁堡,5595,-316,0,"+
"London,倫敦,5152,-11,0,"+
",,,,,"+
"Lisbon,里斯本,3872,-913,0,"+
",,,,,"+
"New York,鈕約,4075,-7399,-5,"+
"Washington DC,華盛頓,3890,-7702,-5,"+
"Chicago,芝加哥,4185,-8765,-6,"+
"New Mexico,新墨西哥,3960,-7695,-7,"+
"San Francisco  ,三藩市,3778,-12242,-8,"+
",,,,,"+
"Toronto,多倫多,4367,-7942,-5,"+
"Winnipeg,溫尼伯,4988,-9717,-6,"+
"Vancouver,溫哥華,49.25,-12313,-8,"+
",,,,,"+
"Mexico City,墨西哥城,4940,-9915,-6,"+
",,,,,"+
"Asuncion,亞松森,-2527,-5767,-3,"+
",,,,,"+
"Brasilia,巴西利亞,-11,-6873,-3,"+
"Rio de Janeiro,里約熱內盧,-229,-4323,-3,"+
",,,,,"+
"Buenos Aires,布宜洛斯艾利斯,-3461,-5847,-3,"+
",,,,,"+
"Montevideo,蒙得維的亞,-3488,-5618,-3,"+
",,,,,"+
"Santiago,聖地亞哥,-3345,-7067,-3,"+
",,,,,"+
"La Paz,拉巴斯,-165,-6815,-4,"+
",,,,,"+
"Santo Domingo,聖多明各,1847,-699,-4,"+
",,,,,"+
"Addis Ababa,亞的斯亞貝巴,903,3870,3,"+
",,,,,"+
"Dar-es-Salaam,達累斯薩拉姆,-680,3928,3,"+
",,,,,"+
"Kampala,坎帕拉,32,3258,3,"+
",,,,,"+
"Nairobi,奈洛比,-128,3682,3,"+
",,,,,"+
"Cairo,開羅,3005,3125,2,"+
",,,,,"+
"Cape Town,開普敦,-3392,1842,2,"+
"Johannesburg,約翰尼斯堡,-2620,2808,2,"+
",,,,,"+
"Khartoum,喀土木,1559,3254,2,"+
",,,,,"+
"Abuja,阿布賈,718,339,1,"+
",,,,,"+
"Algiers,阿爾及爾,3676,305,1,"+
",,,,,"+
"Brazzaville,布拉柴維爾,-426,1529,1,"+
",,,,,"+
"Yaounde,雅溫得,387,1152,1,"+
",,,,,"+
"Brisbane,布里斯本,-2747,15303,10,"+
"Melbourne,墨爾本,-3782,14497,10,"+
"Sydney,悉尼,-3387,15120,10,"+
"Darwin,達爾文,-1247,13085,9.5,"+
"Perth,伯斯,-3195,11585,8,"+
",,,,,"+
"Auckland,奧克蘭,-3685,17477,12,"+
"Wellington,威靈頓,-4128,17477,12,"+
",,,,,"+
"Suva,蘇瓦,-1813,17842,12,"
// copy your Cities Up to Here
;

var defaultCity = 2;

var yearMinOffset = 25; // The minimum value of year that user can select = CurrentYear - yearMinOffset
var yearMaxOffset = 25; // The maximum value of year that user can select = CurrentYear - yearMinOffset

var fromTimeZone = -14; // The minimum value of time zone that user can select
var toTimeZone = 14; // The maximum value of time zone that user can select

// Other public variables
var region      	= new Array;	// array contains region value
var regionName  	= new Array;	// array contains user region name. These two arrays forms a pairs of value,name. region[i] = value, regionName[i] = name
var regionNameC 	= new Array;	// Chinse name
				
var country 		= new Array;	// array contains country value
var countryName 	= new Array;	// array contains user country name
var countryNameC 	= new Array; 	// Chinese name
var regionCountry 	= new Array; 	// array contains relationship of region and country
					// e.g. regionCountry[i] = Region with region=i
					//      regioncountry[i][j] contains the country value which belongs to region=i
				
var city 	= new Array;	// array contains city value
var cityName 	= new Array;	// array contains city name
var cityNameC 	= new Array;	// Chinese name
var cityLat 	= new Array;	// array contains relationship of city and latitude
var cityLong 	= new Array;	// array contains relationship of city and longtitude
var countryCity = new Array;	// array contains relationship of country and city
var cityTimeZone = new Array;	// array contains relationship of city and timezone

var Latitude;			// Latitude read from the world map
var Longitude;			// Longitude read from the world map

var winStarMap = null; 		// This is the window name which containing the star map

// Non-Leap year Month days..
var monthDay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

// Language 
var pageLanguage;	// E=English, C=Chinese

// This is first function to be called. (Body onload)
function initComponents(arg) {
pageLanguage = arg == 0?'E':'C';
if (is_ie5up) {
  AssignWorldMap() // Get different world map according to user resolution
}
initYear();	// setup year selection 
initMonth();	// setup month selection
initDay();	// setup day selection
initHour();	// setup hour selection

initRegion(); 	// Read region  data into array region and regionName
initCountry();	// Read country data into array country and countryName. Setup relationship array regionCountry
initCity();	// Read city    data into array region and regionName
initTimeZone();	// setup time zone selection range
changeRegion(defaultRegion); // Change the region selection to default region, this also changes the country selection and city selection content.
window.document.getElementById("Region").value = defaultRegion;			
window.document.getElementById("Country").value = defaultCountry;
window.document.getElementById("City").value = defaultCity;
window.document.getElementById("LAT").value = cityLat[defaultCity]/100;		// divide 100 because the raw data does not contain decimal point. Divide 100 to get true value with 2 decimal places
window.document.getElementById("LONG").value = cityLong[defaultCity]/100;	// divide 100 because the raw data does not contain decimal point. Divide 100 to get true value with 2 decimal places
window.document.getElementById("TimeZone").value = cityTimeZone[defaultCity];
window.document.form1.MinMag[2].checked = true;
displayPage(1);									// Display page 1 initially.
if (is_nav6up) {								// we cannot use event.x and event.y to get mouse coordinates if user browser is netscape 6 or above.
	document.getElementById("mapFrame").onmousemove = getLocation; 		// This two statements are used to init mouse event functions so that we can capture mouse coordinates.
	document.getElementById("mapFrame").captureEvents(Event.MOUSEMOVE);
	}
}

// This function displays the page specified by arg.
////////////////////////////////////////////////////////////
function displayPage(arg) {
  for (var i=1; i<=2 ; i++) {
    window.document.getElementById("page"+i).style.display="none";
  }
window.document.getElementById("page"+arg).style.display="block";
} // displayPage

// This function return true if the arg is a leap year.
function isLeapYear(arg) {
return (((arg % 4 == 0) && (arg % 100 != 0)) || (arg % 400 == 0)) ? 1 : 0;
}

// This function setup the range of year selection, default current year
function initYear() {
var today = new Date();

// init year selection, default current year 
var currentYear = today.getFullYear(); // current year in 4 digits
var selectYearMin = currentYear - yearMinOffset; // the minimum year to be displayed for user selection
var selectYear = window.document.getElementById("Year");
var selectYearMax = currentYear + yearMaxOffset; 
var selectYearNum = yearMaxOffset + yearMinOffset + 1;

for (var i = 0; i < selectYearNum; i++) {
	selectYear.options[i] = new Option(selectYearMin+i,selectYearMin+i);
	}
	selectYear.value = currentYear; // set selected year be current year;
	
}	// initYear

// This function setup the range of month selection, default current month
function initMonth() {
var today = new Date();
// init month selection, default current month
var selectMonth = window.document.getElementById("Month");
var currentMonth = today.getMonth() + 1; // getMonth returns month in 0..11

for (var i = 1; i <= 12; i++) {
	var j = ((i<10)?"0":"") + i; // display the month is exactly 2 digits
	selectMonth.options[i-1] = new Option( j, j);
	if (i == currentMonth) {
		selectMonth.value = j;
		}
	}
} // initMonth	

// This function calls setSelectDay to setup the range of day selection, default current day.
function initDay() {
var today = new Date();
// init day selection, default current day
var selectDay = window.document.getElementById("Day");
var currentDay = today.getDate(); 
setSelectDay();	
selectDay.value = ((currentDay<10)?"0":"") + currentDay;
} // initDay

// This function setup the range of day selection, the range depends on the selected year and month.
function setSelectDay() {
// clear all selection
var selectDay = window.document.getElementById("Day");
var currentSelectDay = selectDay.value; // try to remember what user selected before
selectDay.length = 0;

var selectYear = window.document.getElementById("Year");
var selectMonth = window.document.getElementById("Month");

for (var i = 1; i <= monthDay[selectMonth.value-1]; i++) {
	var j = ((i<10)?"0":"") + i; // display the day is exactly 2 digits
	selectDay.options[i-1] = new Option( j, j);
	}
if (isLeapYear(selectYear.value)) {
	if (selectMonth.value == '02') {
		selectDay.options[28] = new Option('29','29');
	}
  }		
if (currentSelectDay <= selectDay.length)  {
  selectDay.value = currentSelectDay;
  }
else  {
  selectDay.value = selectDay.options[selectDay.length-1].value;
  }
  
} // setSelectDay

// This function setup the range of hour selection, default current hour
function initHour() {
var today = new Date();
// init hour selection, default current month
var selectHour = window.document.getElementById("Hour");
var currentHour = today.getHours() ; // getMonth returns hours in 0..23

for (var i = 0; i <= 23; i++) {
	var j = ((i<10)?"0":"") + i; // display the month is exactly 2 digits
	selectHour.options[i] = new Option( j, j);
	if (i == currentHour) {
		selectHour.value = j;
		}
	}
} // initHour

// Read region data into array region and regionName
function initRegion() 	{
regionName[0] = "Select Region";
regionNameC[0] = "請選擇地區";

var re = /\s*([\w|\s]*),([^,]*),/g; // regular expression to match comma delimiter word;

var myArray = new Array;
var i = 1;

do {
  myArray = re.exec(regions);
  if (myArray != null) {
    regionName[i] = myArray[1];
    regionNameC[i] = myArray[2];
  }
  i ++;
  }
while (myArray != null)

var selectRegion = window.document.getElementById("Region");

for (var i=0; i<regionName.length;i++) {region[i] = i;}

for (var i=0;i< region.length;i++) {
   if (pageLanguage == "E") {
     selectRegion.options[i] = new Option(regionName[i],region[i]);
   } else {
     selectRegion.options[i] = new Option(regionNameC[i],region[i]);
   }
 }

} // readRegion()

// Read country data into array country and countryName. Setup relationship array regionCountry
function initCountry() {
countryName[0] = "Select Region First";
countryNameC[0] = "請先選擇地區";
//var re = /\s*([\w|\s]*),/g; // regular expression to match comma delimiter word;
var re = /\s*([\w|\s]*),([^,]*),/g; // regular expression to match comma delimiter word;
var myArray = new Array;
var j = 1; // region index
var k = 0; // region country index
regionCountry[j] = new Array;

var i = 1;
do {
  myArray = re.exec(countries);
  if (myArray != null) {
    if (myArray[1].length > 0) {
      countryName[i] = myArray[1];
      countryNameC[i] = myArray[2];
      regionCountry[j][k] = i;
      i++;
	  k++;
	}
    else {
      j++;
	  k=0;
	  regionCountry[j] = new Array;
	  }
  }
 
  }
while (myArray != null)

for (var i=0; i<countryName.length;i++) {country[i] = i;}

} // initCountry

// Read city    data into array region and regionName
function initCity() {
cityName[0] = "Select Country first";
cityNameC[0] = "請先選擇國家";
var re = /\s*([\w|\s]*)\s*,([^,]*),\s*([-]?[\w|\s]*)\s*,\s*([-]?[\w|\s]*)\s*,\s*([-]?[\x2D]?\d*[\x2E]?\d*)\s*,/g; // regular expression to match comma delimiter word;
var myArray = new Array;
var j = 1; // country index
var k = 0; // country city index
countryCity[j] = new Array;

var i = 1;
do {
  myArray = re.exec(cities);
  if (myArray != null) {
    if (myArray[1].length > 0) {
	cityName[i] = myArray[1];
	cityNameC[i] = myArray[2];
	cityLat[i] = myArray[3];
	cityLong[i] = myArray[4]; 
	cityTimeZone[i] = myArray[5];
	countryCity[j][k] = i;
	i++;
	k++;
	}
    else {
	j++;
	k=0;
	countryCity[j] = new Array;
	}
    }
 
  }
while (myArray != null)

for (var i=0; i<cityName.length;i++) {city[i] = i;}

} // initCity

// setup time zone selection range
function initTimeZone() {
var SelectTimeZone = window.document.getElementById("TimeZone");
} // initTimeZone

// This function triggers when the region changed to value arg. The country selection will have only possible country belongs that region
// The default country will set to the first country in the list.
function changeRegion(arg) {
var selectCountry = window.document.getElementById("Country");
selectCountry.options.length=0;
if (arg > 0) {	
  for (var i=0; i < (regionCountry[arg].length);i++) {
  	if (pageLanguage == "E") {
		selectCountry.options[i] = new Option(countryName[regionCountry[arg][i]],country[regionCountry[arg][i]],i==0,i==0);
	} else {
		selectCountry.options[i] = new Option(countryNameC[regionCountry[arg][i]],country[regionCountry[arg][i]],i==0,i==0);
	}
	}
  changeCountry(country[regionCountry[arg][0]]); 
  }
else  {
  	if (pageLanguage == "E") {
		selectCountry.options[0]=new Option(countryName[0],country[0],true,true);
	} else {
		selectCountry.options[0]=new Option(countryNameC[0],country[0],true,true);
	}
    changeCountry(0);
  }
}	// changeRegion

// This function triggers when the country changed to value arg. The city selection will have only possible city belongs that country
// The default city will set to the first city in the list.
// The latitude and longitude are changed accordingly
function changeCountry(arg) {
var selectCity = window.document.getElementById("City");
var selectTimeZone = window.document.getElementById("TimeZone");
selectCity.options.length=0;
if (arg > 0) {	
  for (var i=0; i < (countryCity[arg].length);i++) {
  	if (pageLanguage == "E") {
		selectCity.options[i] = new Option(cityName[countryCity[arg][i]],city[countryCity[arg][i]],i==0,i==0);
	} else {
		selectCity.options[i] = new Option(cityNameC[countryCity[arg][i]],city[countryCity[arg][i]],i==0,i==0);
	}
	}
  setLong(cityLong[city[countryCity[arg][0]]]/100);
  setLat(cityLat[city[countryCity[arg][0]]]/100);
  selectTimeZone.value = cityTimeZone[countryCity[arg][0]];
  
  }
else  {
  if (pageLanguage == "E") {
	selectCity.options[0]=new Option(cityName[0],city[0],true,true);
      } else {
	selectCity.options[0]=new Option(cityNameC[0],city[0],true,true); 
     }
  selectTimeZone.value = "0";
  }
}	// changeCountry

// This function triggers when the city changed to value arg. 
// The latitude and longitude are changed accordingly
function changeCity(arg) {
var selectTimeZone = window.document.getElementById("TimeZone");
setLong(cityLong[arg] / 100);
setLat(cityLat[arg] / 100);
selectTimeZone.value = cityTimeZone[arg];

} // changeCity

// This function displays the page specified by arg
function pageNav(arg) {
// validate 	Latitude and Longitude
if (LocationValidated() && TimeZoneValidated() ) {
	displayPage(arg);
}
} // pageNav

// This function gets the latitude and longitude from the world map and display them at browser status bar 
function getLocation(e) {
Latitude = getLat(e);
Longitude = getLong(e);
if ((Latitude >= -90) && (Longitude >= -180)) {
  window.status = "Latitude=" + Latitude +",Longitude=" + Longitude;
  } 
  else {
  window.status = "";
  }	
} getLocation

// This function gets the longitude from worldmap:
/* Uniform method: 

      -180                 +180
	--------------------- -	
	|   y               | ^	
	| x +              | |
	|                   | mapHeight
	|                   | |
	|                   | V
	---------------------
	|<--- mapWidth ---->
	
	    x
	-------- * 360 - 180 = Longitude
	mapWidth

	    y
	---------- * 180 - 90 = Latitude
	mapHeight
*/
/* 
	
	Miller' projection method:
	x = R (v - v0)
	y = R/0.8 * {ln tan (pi/4 + 0.4 w) }
	
	R is a scaling constant
	v = longitude (0 <= v <= 2pi)
	w is the latitude (-pi/2 <= w <= pi/2)
	

*/
var x0 = 0; // left margin 
var y0 = 0; // Top margin
var x1 ; // x coordinate of right boundary 
var y1 ; // y coordinate of bottom boundary 
var R=0;

function degrees(arg) {
	return arg*360/(2*Math.PI);
}
	
function getLong(e) {
//var mapWidth = document.getElementById("worldMap").offsetWidth; // World map's width (absolute)
x1 = document.getElementById("worldMap").offsetWidth; // World map's width (absolute) // only work if the map does not contain any margin
var Xpos= (is_ie5up)?event.x:(is_nav6up)?e.layerX:false;
R = (x1-x0)/(2*Math.PI);
if ((Xpos >= x0) && (Xpos <= x1)) {
	//uniform projection  return Math.round(100* ((Xpos-x0) / (x1 - x0) * 360 - 180) ) / 100;
	return Math.round(degrees((Xpos-x0)/R)-180); // Miller's projection
 } else {
  return -181;
 }  
} // getLong

// This function gets the latitude from worldmap:
function getLat(e) {
// var mapHeight = document.getElementById("worldMap").offsetHeight; // World map's height (absolute)
y1 = document.getElementById("worldMap").offsetHeight; // World map's height (absolute) // only work if the map does not contain any margin
var Ypos= (is_ie5up)?event.y:(is_nav6up)?e.layerY:false;
if ((Ypos >= y0) && (Ypos <= y1)) {
	//uniform projection  return Math.round(100*(90 - (Ypos-y0) / (y1 - y0) * 180) )/100;
	return -1 * Math.round(degrees((Math.atan(Math.exp((Ypos-y0-(y1-y0)/2)*0.8/R))-Math.PI/4)/0.4)); //Miller's projection
 } else {
  return -91;
 }  
} // getLat

// When user clicks a position on the world map, this function set the latitude and longitude user selection.
function setLocation() {
if (Latitude > -90 && Longitude > -180) {
  setLong(Longitude);
  setLat(Latitude);
  resetRegion(); // Since user clicks the starmap, reset region, country, city.
  }
} // setLocation

// This function sets the time zone according longitude
function setTimeZone() {
// note TimeZone 0 belongs to [-7.5,7.5)
  window.document.getElementById("TimeZone").value = Math.floor((Number(window.document.getElementById("LONG").value) + 7.5) / 15);
  if (document.form1.LongitudeSign[1].checked) {
  	window.document.getElementById("TimeZone").value = - window.document.getElementById("TimeZone").value;
  }
} // setTimeZone

// This function would be called if user manually changes the value of longitude. This function calls resetRegion to reset region,country,city.
// Moreover, time zone will be calculate again.
// Note that if user changes the value of latitude, it will directly call resetRegion because no need to calculate time zone again.
function onChangeLONG() {
resetRegion();
} //onChangeLONG

// This function set the location and time zone if user click a position on the world map.
function onClickMap() {
  setLocation();
  setTimeZone();
} // onClickMap


// This function resets region to the initial state. (i.e. no region selected) 
// It calls changeRegion(0) which will triggers country and city to initial state too.
function resetRegion() {
if (pageLanguage == "E") {	
  window.document.getElementById("Region").options[0] =  Option(regionName[0],region[0],true,true);
} else {
  window.document.getElementById("Region").options[0] =  Option(regionNameC[0],region[0],true,true);
}
changeRegion(0);
setTimeZone();
} // resetRegion

// This function construct a url to be redirected. By calling window.open, the output of CGI starmap.cgi will be displayed in the windows named "StarMap"
function OpenStarMapWindow() {
	
 if (!LocationValidated() || !TimeZoneValidated() ) { return false;} //////////////////////////////////////////////////

  var windowWidth; // the new window's width  	
  var windowHeight; // the new window's height
  
  if (document.form1.Size[0].checked) {
  	windowWidth = 640;
  	windowHeight = 480;
  }
  if (document.form1.Size[1].checked) {
  	windowWidth = 800;
  	windowHeight = 600;
  }
  if (document.form1.Size[2].checked) {
  	windowWidth = 1024;
  	windowHeight = 768;
  }

  // center the output to screen center
  if (window.screen.height > windowHeight) {
  var windowTop = (window.screen.height - windowHeight > 0)?Math.ceil((window.screen.height - windowHeight)/2):1;
  var windowLeft = (window.screen.width - windowWidth > 0)?Math.ceil((window.screen.width - windowWidth)/2):1;
  } else
  {
  var windowTop = 0; // to avoid that the starmap window exceed the window screen area.
  var windowLeft = 0;
  }
  var features = "width=" + windowWidth + ",height=" + windowHeight + ",top=" + windowTop + ",left=" + windowLeft + ",scrollbars=Yes, resizable =Yes";

  var url = "starmap.cgi?LAT=";
  
  if (document.form1.LatSign[0].checked) { //South
  	url = url + "-";
  }  	

  url = url + document.getElementById("LAT").value + "&LONG=" ;
  
  if (document.form1.LongitudeSign[1].checked) { //East
  	url = url + "-";
  }  	
    
  url = url + document.getElementById("LONG").value + 
			"&Year=" + document.getElementById("Year").value + 
			"&Month=" + document.getElementById("Month").value + 
			"&Day=" + document.getElementById("Day").value + 
			"&Hour=" + document.getElementById("Hour").value + 
			"&TimeZone=" + document.getElementById("TimeZone").value + 
			"&Size=";
			
  if (document.form1.Size[0].checked) {
  	url = url + "640";
  }  	
  if (document.form1.Size[1].checked) {
  	url = url + "800";
  }  	
  if (document.form1.Size[2].checked) {
  	url = url + "1024";
  }  	

  url = url + "&MinMag=";
  if (document.form1.MinMag[0].checked) {
  	url = url + "5.75";
  }  	
  if (document.form1.MinMag[1].checked) {
  	url = url + "5.25";
  }  	
  if (document.form1.MinMag[2].checked) {
  	url = url + "4.75";
  }  	
  if (document.form1.MinMag[3].checked) {
  	url = url + "4.25";
  }  	
  if (document.form1.MinMag[4].checked) {
  	url = url + "3.75";
  }  	
  if (document.form1.MinMag[5].checked) {
  	url = url + "3.25";
  }  	
  
  url = url + "&SelectPoles="; 
  if (document.form1.SelectPoles.checked) {
    url = url + "Yes"
  }
  else {
    url = url + "No"
  }
  
  url = url + "&SelectEquator="; 
  if (document.form1.SelectEquator.checked) {
    url = url + "Yes"
  }
  else {
    url = url + "No"
  }

  url = url + "&SelectEcliptic=";
  if (document.form1.SelectEcliptic.checked) {
    url = url + "Yes"
  }
  else {
    url = url + "No"
  }

  url = url + "&SelectSun=";
  if (document.form1.SelectSun.checked) {
    url = url + "Yes"
  }
  else {
    url = url + "No"
  }

  url = url + "&SelectMoon=";
  if (document.form1.SelectMoon.checked) {
    url = url + "Yes"
  }
  else {
    url = url + "No"
  }

  url = url + "&SelectPlanets=";
  if (document.form1.SelectPlanets.checked) {
    url = url + "Yes"
  }
  else {
    url = url + "No"
  }

  url = url + "&SelectDeepSky=";
  if (document.form1.SelectDeepSky.checked) {
    url = url + "Yes"
  }
  else {
    url = url + "No"
  }

  url = url + "&SelectComets=";
  if (document.form1.SelectComets.checked) {
    url = url + "Yes"
  }
  else {
    url = url + "No"
  }
  
  url = url + "&SelectShowers=";
  if (document.form1.SelectShowers.checked) {
    url = url + "Yes"
  }
  else {
    url = url + "No"
  }

  url = url + "&PrintFriendly=";
  if (document.form1.PrintFriendly.checked) {
    url = url + "Yes"
  }
  else {
    url = url + "No"
  }

  url = url + "&pageLanguage=" + pageLanguage;

  var selectCity = document.getElementById("City")
  if (selectCity.value > 0) {
  url = url + "&City=" + selectCity.options[selectCity.selectedIndex].text;
  }
//  window.alert(url);

  if (winStarMap) {
  	winStarMap.close();
  }
  winStarMap = window.open(url,"StarMap",features);
  
}

// This function called when user clicks the "next" link.
// This checks the latitude and longitude should be in the range of -180 and 180. It also kicks out invalid entry.
function LocationValidated() {
	
var Latitude = window.document.getElementById("LAT").value;
var Longitude = window.document.getElementById("LONG").value;
var Re = /^\s*([-]?\d+[.]*\d*)\s*$/;
if ((Re.exec(Latitude) == null) || (parseFloat(Latitude) < 0) || (parseFloat(Latitude) > 90)) {
	if (pageLanguage == "E") {
	  alert('The value of Latitude should be between 0 and 90');
	} 
	else {
	  alert('請輸入緯度範圍：0 至 90');
	}  
	  return false;
	} 
if ((Re.exec(Longitude) == null) || (parseFloat(Longitude) < 0) || (parseFloat(Longitude) > 180)) {
	if (pageLanguage == "E") {
	  alert('The value of Longitude should be between 0 and 180');
	} 
	else {
	  alert('請輸入經度範圍：0 至 180');
	}  
	  return false;
	}  
	
	
return true;
		
}

// This function called when user clicks the "next" link.
// This checks the time zone range should be in the range of -14 and 14. It also kicks out invalid entry.
function TimeZoneValidated() {
	
var TimeZone = window.document.getElementById("TimeZone").value;
var Re = /^\s*([-]?\d+[.]*\d*)\s*$/;
if ((Re.exec(TimeZone) == null) || (parseFloat(TimeZone) < -14) || (parseFloat(TimeZone) > 14)) {
	if (pageLanguage == "E") {
	  alert('The value of time zone should be between -14 and 14');
	} 
	else {
	  alert('請輸入時區範圍：-14 至 14');
	}  
	  return false;
	} 
return true;
		
}

// This function set the latitude and set East/West
// arg = longitude with sign
function setLong(arg) {
  var selectLong = window.document.getElementById("LONG");
  if (arg >= 0) {	// West
    selectLong.value = arg;
    document.form1.LongitudeSign[1].checked = false;
    document.form1.LongitudeSign[0].checked = true;
    }
   else {	// East
    selectLong.value = -arg;
    document.form1.LongitudeSign[0].checked = false;
    document.form1.LongitudeSign[1].checked = true;
   }
  
}

// This function set the latitude and set South/North
// arg = Latitude with sign
function setLat(arg) {
  var selectLat = window.document.getElementById("LAT");
  if (arg >= 0) {	// North
    selectLat.value = arg;
    document.form1.LatSign[0].checked = false;
    document.form1.LatSign[1].checked = true;
    }
  else {	// South
    selectLat.value = -arg;
    document.form1.LatSign[1].checked = false;
    document.form1.LatSign[0].checked = true;
  }
}
	
// Assign WorldMap
function AssignWorldMap() {
var worldMap = window.document.getElementById("worldMap");
if (window.screen.width <= 640) {
  worldMap.src = "./image/WorldMap1.gif";
  }
else if (window.screen.width <= 800) {
  worldMap.src = "./image/WorldMap2.gif";
  }
else  {
  worldMap.src = "./image/WorldMap3.gif";
  }
}	