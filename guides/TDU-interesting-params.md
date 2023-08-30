# TDU – (other) interesting parameters
*if you feel adventurous*

## GAMEPSP.INI

### Set startup game mode – `SetCurGameMode`

```
SetCurGameMode 			= 0			// GAME_MODE_BOOTMENU 			= 0
									// GAME_MODE_FREERIDE 			= 1
									// GAME_MODE_MAP				= 2
									// GAME_MODE_HOME				= 3
									// GAME_MODE_SHOP				= 4
									// GAME_MODE_MISSION			= 5
									// GAME_MODE_EDITOR				= 6
									// GAME_MODE_CARSHOWCASE		= 7
									// GAME_MODE_INSTANTCHALLENGE	= 8
									// GAME_MODE_TESTCAR			= 9
									// GAME_MODE_GARAGE				= 10
									// GAME_MODE_LIVING				= 11
									// GAME_MODE_SANDBOX			= 12
									// GAME_MODE_GOODIES			= 13
									// GAME_MODE_AVARTARSHOWCASE    = 14
									// GAME_MODE_DRIVEIN		    = 15
									// GAME_MODE_DRESSING			= 16
									// GAME_MODE_AFTMARKT			= 17
									// GAME_MODE_VIDEOBUMPER		= 18
									// GAME_MODE_AITRAINER			= 19
									// GAME_MODE_CINVIEWER			= 20
									// GAME_MODE_ESTATES			= 21
									// GAME_MODE_CLUB				= 22
									// GAME_MODE_TITLE			= 25
									// GAME_MODE_PAUSE			= 26									
```

#### Useful notes

* Some modes are not functional
* Some modes may generate broken savefiles. Proceed with caution.
* `GAME_MODE_MAP` – starts the game with heaps money and EXP, in a Dodge, with heaps of other vehicles. However, the game start in the map at the invalid location. To escape it without crashing, zoom in to a road and select a road to teleport to. Then, make sure to buy a house (or multiple houses) to store your vehicles. If you do not, you are guaranteed to generate a broken savefile.

### Select map – `AddLevel`

```
AddLevel				= "HAWAI"			// Level Choose
//LoadIGE					= "KOMO MAI"	// load ige from file (created by gme)
```

Possibly allows you to access test maps.

### Edit traffic – (multiple variables)

```
// VehicleMaxCount is the hard limit of simultaneous AI vehicles
// But you can set TrafficMaxCount+ParkedMaxCount > VehicleMaxCount
// Example: vehicle=16 traffic=16 parked=8
//  -> you can spawn up to 16 traffic if no parked vehicles on the area,
//     but only spawn up to 8 traffic if 8 parked are here
//     and 0 parked cars if 16 traffic cars are already spawned
//
VehicleMaxCount		=	4 //4	//2	//16
TrafficMaxCount		=	5 //4	//1	//14
ParkedMaxCount		=	0 	//1	//8
```

and

```
// Maximum count of Traffic AI that will be physics enabled at the same time
PhysicsMaxCount			=	4
```

and

```
PoliceMaxCount			=	0			// between 0 & 16 
										// NB : TrafficMaxCount + ParkedMaxCount + PoliceMaxCount must be <= 15
										// if PoliceMaxCount > 0
```

It is all in the comments

### Change difficulty – `OpponentDifficulty`

```
OpponentDifficulty		=	1.0			// between 0.0f & 1.0f
```

normally, the game runs at max difficulty.

### Enable debugging – `RemoteDebugger`

```
RemoteDebugger		=	0
```

### Tune cars and edit houses data – `[CarStateConfig]`

```
[CarStateConfig]
```

The entire section

### Online global multiplayer capabilities – `[Online]`

Test Drive Unlimited servers were shut down. However, if someone can re-create a server, a global-scale multiplayer game can be made a reality!

```
[Online]
```

The entire section. Look at, for example,

```
				// Database Server	SERVER PORT
//Server			"192.168.0.87"		4501
//Server				"tdu1"		4501
//Server				"62.39.158.22"		4501
//Server				"none"		none
Server				"none"		none

				// Database Login	Database Pass
//DefaultLogin			"none"			"edenpwd"
DefaultLogin			"amh-retail"	""

				// Server address , none = LAN discovery

// INTERNET / LAN
//Lobbying			"tdu.testdriveunlimited.com"
//Lobbying			"tdu1"
Lobbying 			"none"
```

### Unexplored – (multiple variables)

```
GrassAsTarmac		=	0

ArtPreviewCars 0

TRACETIMINGTEXT 1 
NET_CORRECTION_DISTRIBUTION		"CCCCPPCPPP"
```


## SYSPSP.INI

### Set timer (time of day?) – `SetTimer`

Sets time of day?

```
[System]
SetTimer		= FIXED_TIME	//  REAL_TIME, refresh rate is realt time
								//  FIXED_TIME, refresh rate is fixed to video system
```

### Video settings – `[Video]`

Can possibly improve quality.  

```
[Video]
SetVideo		= NTSC			// PAL50 or PAL60 or NTSC or NTSCJ
SetWindowed		= TRUE			// Window or FullScreen ?
```

