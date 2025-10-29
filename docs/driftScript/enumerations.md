> Important!  
In your DriftScript code, DO NOT assume the numeric values of the enums will remain the same.  
Always use the enums and not hardcoded numeric values.  
Also DO NOT assume `Invalid` will always be equal to `0` or `-1`.

## BoundsCheck

```sq
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
```sq
enum SpecialPlayer
{
    Invalid =  0,
    Neutral = -1,
    Hostile = -2,
    Rescue  = -3
}
```

- The above are the `PlayerIDs` for the special players `Neutral`, `Hostile`, and `Rescue`
- The players `Neutral`, `Hostile`, and `Rescue` are automatically assigned to the `Neutral` Force
- These 3 special players exist in every game and game-mode.
- `Note:` Normal PlayerIDs are positive, with values: `[1-16]`

## SpecialForce
```sq
enum SpecialForce
{
	Invalid = 0,
	Neutral = -1
}
```

- The Force `Neutral` (`id = -1`) is special and exists in every game.
- The players `Neutral`, `Hostile`, and `Rescue` are automatically assigned to the `Neutral` Force
- `Note:` Normal ForceIDs are positive integers

## VictoryStatus
```sq
enum VictoryStatus
{
	Invalid,
	Pending,
	Victory,
	Defeat
}
```

- A `VictoryStatus::Pending` indicates the player is not yet assigned Victory/Defeat, usually meaning the player is still playing.
- `Draw` or `Tie` is not yet supported.

## ShapeType
```sq
enum ShapeType
{
    Invalid,
    Circle,
	Square,
	Rectangle
}
```

## TerrainType
```sq
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
```sq
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
```sq
enum ForceProp
{
					// Access		Type
	Invalid,
	Score,			// Read-Write	(int)
	Name			// Read-Write	(string)
	VictoryStatus	// Read-Write	(VictoryStatus)
}
```

- Primarily used in {{fn("property-getterssetters")}}

## PlayerProp

```sq
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

    PlayerName,             // Read-Write  		(string)
							// Is Write-Enabled only for computer players

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
	Score,					// Read-Write		(int)
    IsNormalPlayer, 		// Read				(bool)
    IsHumanPlayer, 			// Read				(bool)
    IsComputerPlayer,		// Read				(bool)
    IsHostilePlayer,		// Read				(bool)
    IsNeutralPlayer,		// Read				(bool)
    IsRescueablePlayer,		// Read				(bool)
	IsInGame,				// Read				(bool)
	VictoryStatus			// Read-Write		(VictoryStatus),
	AlliedVictory			// Read-Write		(bool)
}
```

- Primarily used in {{fn("property-getterssetters")}}

## UnitProp

```sq
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
	Level,					// Read-Write		(int)
    Identifier,             // Read-Write       (string)
    PlayerID                // Read-Write       (int)
}
```

- Primarily used in {{fn("property-getterssetters")}}
- Setting `Health` to `<= 0` will cause unit to be set to `killed` state.

## LocationProp
```sq
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
```sq
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
```sq
gx_set_unit_prop(unit_id, UnitProp.GunShipState, GunShipState.ChainGunLevel2)
```

- the above would give a gunship two chainguns

## CommandType
```sq
enum CommandType
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

```sq
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
