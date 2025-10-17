## BoundsCheck 

```
enum BoundsCheck
{
	Invalid,
    Center,     // Unit's center position is in location
    Touching,   // Unit is fully inside or touching location
    Inside      // Unit fully inside a location
}
```
- The `BoundsCheck` enum is used in unit search queries within locations.  
- Primarily used in {{fn("gx_get_units-gx_get_units_count")}}

## SpecialPlayer
```
enum SpecialPlayer
{
    Invalid =  0,
    Neutral = -1,
    Hostile = -2,
    Rescue  = -3
}
```
- `Note:` Normal playerIDs are positive, with values: `[1-16]`

## ShapeType
```
enum ShapeType
{
    Invalid,
    Circle,
	Rectangle
}
```

## TerrainType
```
// Primary Terrain Types
enum TerrainType
{
	Invalid,
	
    Normal,         // See SecondaryTerrainTypeNormal
					// for valid secondary types

	Water,          // valid secondary types are 0 and 2
	Lava,           // valid secondary types are 0 and 2
	Diamond,        // valid secondary types is just 0
    Glow,           // valid secondary types are [0 - 31]
	PlayerColor,    // valid secondary types are player_id, i.e. [1-16]

	Unpassable,     // !! Not a dynamic terrain type!
					// Cannot dynamically change or be set to!

	Space,          // valid secondary type is just 0

	CliffClosed,    // !! Not a dynamic terrain type!
					// Cannot dynamically change or be set to!

	CliffBorder     // !! Not a dynamic terrain type!
					// Cannot dynamically change or be set to!
}
```

- Primarily used in {{fn("gx_set_terrain_type")}} and {{fn("gx_get_terrain_type")}}

## SecondaryTerrainTypeNormal
```
enum SecondaryTerrainTypeNormal
{
	Invalid,
	Normal,         // Units are normal on this type (no effects)
	Speed,          // Units move faster on this type
	AttackRate,     // Units have faster attack rate on this type
	Heal,           // Units heal faster on this type
	Forbidden,      // Units insta-die on this type
	Sniper,         // Units have increased range on this type
	MeleeOnly,      // Units have decreased range on this type
	Pacifist        // Units are unable to attack on this type
}
```

- Primarily used in {{fn("gx_set_terrain_type")}} and {{fn("gx_get_terrain_type")}}
- Should only be used in conjunction with `TerrainType.Normal`


## ForceProp

```
enum ForceProp
{
					// Access		Type
	Invalid,
	Score,			// Read-Write	(int)
	Name			// Read-Write	(string)
}
```
- Primarily used in {{fn("property-getterssetters")}}

## PlayerProp

```c
enum PlayerProp
{
							// Access			Type
	Invalid,
	Fungus,                 // Read-Write     	(float)
	Gemstone,               // Read-Write     	(float)
	Supply,                 // Read        		(int)
	MaxSupply,              // Read        		(int)
	NumKills,               // Read        		(int)
	NumDeaths,              // Read        		(int)
    PlayerName,             // Read        		(string)

    FullMapVision,          // Read-Write     	(bool)
                            // When set to true, player
							// is given vision of entire map

    NumUnitsProduced,       // Read        		(int)
    TagID,                  // Read        		(int)
    ChoseRandom,            // Read        		(bool)
    Race,                   // Read        		(int)
    WeaponsLevel,           // Read-Write       (int)
    ArmorLevel,             // Read-Write       (int)

    SpeedLevel,             // Read-Write       (int)
	 						// (not implemented atm)
							
    StartLocationPosition,  // Read         	(Vec2)
	Score					// Read-Write		(int)
}
```
- Primarily used in {{fn("property-getterssetters")}}

## UnitProp

```c
enum UnitProp
{
							// Access			Type
	Invalid,
	MaxHealth,            	// Read      		(int)
	Health,                 // Read-Write     	(float)
	MaxSpeed,               // Read	        	(float)
	Size,                   // Read        		(float)
	UnitType,               // Read        		(string)
    IsOnFire,               // Read        		(bool)
    GetParentJeep,          // Read        		(int)
	GetParentDropship,      // Read        		(int)
	GetParentStarShip,      // Read        		(int)
	GetParentSpinnerShip,   // Read        		(int)
    GetParentBunker,        // Read        		(int)
    GunShipState,           // Read-Write       (GunShipState)
	Level					// Read-Write		(int)
}
```
- Primarily used in {{fn("property-getterssetters")}}
- Setting `Health` to `<= 0` will cause unit to be set to `killed` state.

## LocationProp
```c
enum LocationProp
{
					// Access		Type
	Invalid,
	TopLeft,        // Read 		(Vec2)
	TopRight,       // Read 		(Vec2)
	BottomLeft,     // Read 		(Vec2)
	BottomRight,    // Read 		(Vec2)
	Center,         // Read 		(Vec2)
	Size            // Read 		(Vec2)
}
```
- Primarily used in {{fn("property-getterssetters")}}

## GunShipState 
```
enum GunShipState
{
	Invalid,
    Normal,
    StarShot,
    BigGunLevel1,
    BigGunLevel2,
    ChainGunLevel1,
    ChainGunLevel2
}
```
- Primarily used for setting/getting unit property `GunShipState` in {{fn("property-getterssetters")}}

Example:
```
gx_set_unit_prop(unit_id, UnitProp.GunShipState, GunShipState.ChainGunLevel2)
```

- the above would give a gunship two chainguns

## CommandType
```c
enum CommandType : string
{
	Invalid,
    Attack,             // valid params: [m_unitID, m_location, m_pos]
    Move,               // valid params: [m_unitID, m_location, m_pos]
    Hold,               // valid params: []
    Stop,               // valid params: []
    RightClick          // valid params: [m_unitID, m_location, m_pos]
}
```

- Primarily used in {{fn("gx_queue_command")}}
- `string` identifiers for `Spells` can be used as well.
- more to be added later

## EventType

```c
enum EventType
{
    Invalid,            	// Invalid Event

    PlayerNameChanged,  	// Populates m_playerID, m_playerName,
							// and m_oldPlayerName of the Event structure

    PlayerLeftGame,     	// Populates m_playerID, and m_playerName
							// of the Event structure

    TextCommand             // Populates m_playerID, m_playerName,
							// and m_cmd of Event structure
}
```
