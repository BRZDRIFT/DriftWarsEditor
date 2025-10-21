## gx_include
```sq
void gx_include(string filename)
```

- Includes `filename` in current compilation.
- A file is only included once by `gx_include`; subsequent calls are ignored.
- Typically called at the top of your drift script file.

## gx_create_unit
```sq
int gx_create_unit(int params)
```

```sq
table params = {
    string m_unitType,              // Required
    int m_playerID,                 // Required
    Vec2 m_position = {},           // Optional
    string m_location = {},         // Optional
    int m_level = 1                 // Optional, default unit level = 1
}
```

```sq
local new_unit = gx_create_unit({ m_unitType = "Brute", m_playerID = 1, m_location = "my_cool_location" })
```

- Will create unit of type `m_unitType` at position `m_position` or at location `m_location` for player `m_playerID`.
- It is undefined behavior to have both `m_position` and `m_location` set.
- If neither `m_position` nor `m_location` is set, unit will be created at `(0, 0)`
- Refer to {{type("Vec2")}} if needed.

## gx_get_sim_tick
```sq
int gx_get_sim_tick()
```

- Returns the current sim tick number in simulation.
- The {{entry("gx_sim_init")}} call will have `tick = 0`
- The first {{entry("gx_sim_update")}} call will have `tick = 1`
- The second {{entry("gx_sim_update")}} call will have `tick = 2`, etc..
- every tick corresponds to 50ms real time

## gx_get_distance_between_units
```sq
float gx_get_distance_between_units(int unitID, int otherUnitID)
```

- returns the distance between the edges of two units
- will return 0 if one or both of the units do not exist

## gx_get_nearby_units / gx_get_nearby_units_count
```sq
int[] gx_get_nearby_units(table params)
int gx_get_nearby_units_count(table params)
```

```sq
table params = {
    int m_unitID,                                   // unit_id to center search on
    float m_radius,                                 // search radius around unit
    int m_playerIDs[],                              // Optional, Filter for player_id
    int m_forceIDs[],                               // Optional, Filter for force_id
    string m_unitTypes[],                           // Optional, Filter for certain unit types
    string m_exceptUnitTypes[],                     // Optional, ignore certain unit types
    bool m_bIncludeAirUnits = true,                 // Optional, Set to false if you want to exclude air units
    bool m_bIncludeGroundUnits = true               // Optional, set to false if you want to exclude ground units
    bool m_bIncludeKilledUnits = false,             // Optional, Set to true if you want to include killed units
    bool m_bIncludeRemovedUnits = false             // Optional, set to true if you want to include removed units
    bool m_bIncludeProjectiles = false              // Optional, include projectiles (default: false)
}
```

- `m_unitID` required to be set
- `m_radius` required to be set
- returns units whos outer edges have a distance equal/less than `m_radius` from `m_unitID`.
- `note:` `m_unitID` will be included in part of query result

## gx_get_units / gx_get_units_count
```sq
int[] gx_get_units(table params)
int gx_get_units_count(table params)
```

```sq
table params = {
    string m_locations[],                           // Optional
    BoundsCheck m_boundsCheck                       // Default: BoundsCheck.Center
    int m_playerIDs[],                              // Optional, Filter for player_id
    int m_forceIDs[],                               // Optional, Filter for force_id
    string m_unitTypes[],                           // Optional, Filter for certain unit types
    string m_exceptUnitTypes[],                     // Optional, ignore certain unit types
    bool m_bIncludeAirUnits = true,                 // Optional, Set to false if you want to exclude air units
    bool m_bIncludeGroundUnits = true               // Optional, set to false if you want to exclude ground units
    bool m_bIncludeKilledUnits = false,             // Optional, Set to true if you want to include killed units
    bool m_bIncludeRemovedUnits = false             // Optional, set to true if you want to include removed units
    bool m_bIncludeProjectiles = false              // Optional, include projectiles (default: false)
}
```

- If `m_locations` is defined:
    - Searches at `m_locations` for units
- If `m_locations` is not defined:
    - Searches for units on entire map
- Refer to {{enum("BoundsCheck ")}} if needed.

## gx_create_explosion
```sq
void gx_create_explosion(table params)
```

```sq
table params = {
    float m_size = {},                  // Optional, Diameter of explosion
    Vec3 m_color = Vec3(1, 1, 0)        // Optional, ColorSRGB of explosion.
    string m_location = {},             // Optional, Location for explosion
    Vec2 m_pos = {}                     // Optional, Position for explosion
}
```

- Refer to {{type("Vec2")}} and {{type("Vec3")}} if needed.

Example:
```sq
gx_create_explosion( {
    m_color = Vec3(1, 0, .5),
    m_location = "my_location"
} )
```

- it is undefined behavior to set both `m_location` and `m_pos`
- if `m_size` is not set and `m_location` is set, the resolved size will be the minimum width/height of `m_location`
- if `m_size` is not set and `m_pos` is set, the resolved size will be `1`
- Explosions are purely visual. They do not do any damage.
- Default value for `m_color` is `Vec3(1,1,0)` aka `0xFFFF00` (yellow)
- Refer to {{type("Vec2")}} and {{type("Vec3")}} if needed.

## gx_kill_unit
```sq
void gx_kill_unit(int unit_id)
```

- kills the unit `unit_id`.
- It is safe to call this function on already killed units

## gx_get_kills
```sq
void gx_get_kills(int player_id, table params = {})
```

```sq
table params = {
    m_playerID = {},
    m_bAlliedKills = {},
    m_bSelfKills = {},
    m_bNonAlliedKills = {},
}
```

- if `m_playerID` is set, none of `m_bAlliedKills`, `m_bSelfKills`, `m_bNonAlliedKills` should be set
- if empty {} is passed in for params, all kills will be returned, equivalent to:
`{ m_bAlliedKills = true, m_bSelfKills = rue, m_bNonAlliedKills = true }`
- Allied kills does not include self kills


## gx_is_unit_killed
```sq
void gx_is_unit_killed(int unit_id)
```

- returns if the unit `unit_id` is killed
- returns `true` if unit does not exist
- equivalent to calling `!gx_is_unit_alive(unit_id)`

## gx_remove_unit
```sq
void gx_remove_unit(int unit_id)
```

- marks the unit to be removed by game
- `unit_id` will be removed from game before the next {{entry("gx_sim_update")}} call
- It is safe to call this function on already killed or removed units

## gx_is_unit_removed
```sq
void gx_is_unit_removed(int unit_id)
```

- returns if unit is marked to be removed
- will still return `true` if unit_id does not exist

## gx_unit_exists
```sq
bool gx_unit_exists(int unit_id)
```

- checks if unit still exists in the game

## gx_is_unit_alive_and_constructed
```sq
bool gx_is_unit_alive_and_constructed(int unit_id)
```

- returns `true` if unit is alive and constructed
- returns `false` if unit_id is invalid or unit no longer exists in game

## gx_is_unit_alive
```sq
bool gx_is_unit_alive(int unit_id)
```

- returns `true` if unit is alive
- returns `false` if unit_id is invalid or unit no longer exists in game
- Note: This function still returns `true` if unit is not yet fully constructed
- equivalent to calling `!gx_is_unit_killed(unit_id)`

## gx_get_unit_position
```sq
Vec3<float> gx_get_unit_position(int unit_id)
```

- returns position of unit
- returns Vec3(0.0, 0.0, 0.0) if unit no longer exists

## gx_set_unit_position
```sq
void gx_set_unit_position(int unit_id, table params)
```

```sq
table params = {
    string m_location = {},     // Optional, location to put unit
}
```

Example:
```sq
gx_set_unit_position(some_unit, { m_location = "location_to_teleport_to" } )
```

- it is undefined to not set `m_location` 
- if `m_location` does not exist, unit will be teleported to Vec2(0.0, 0.0)


## gx_is_ground_unit
```sq
bool gx_is_ground_unit(int unit_id)
```

- returns if unit is currently a `ground` unit
- units are always in either the `ground` or `air` state
- note: knock-back effect can cause `ground` units to temporarily become `air` units
- equivalent to calling `!gx_is_air_unit(unit_id)`

## gx_is_air_unit
```sq
bool gx_is_air_unit(int unit_id)
```

- returns if unit is currently an `air` unit
- units are always in either the `ground` or `air` state
- note: knock-back effect can cause `ground` units to temporarily become `air` units
- equivalent to calling `!gx_is_ground_unit(unit_id)`

## gx_get_players
```sq
int[] gx_get_players(table params = {})
```

```sq
table params = {
	bool m_bIncludeNormalPlayers = true;
	bool m_bIncludeDefeatedPlayers = false;
	bool m_bIncludeNeutralPlayer = false;
	bool m_bIncludeRescuePlayer = false;
	bool m_bIncludeHostilePlayer = false;
	bool m_bPlayerMustBeInGame = true;
}
```


## gx_get_player
```sq
int gx_get_player(int unit_id)
```

- returns the `player_id` for unit `unit_id`

## gx_print
```sq
void gx_print(string message, table params = {})
```

```sq
table params = {
    int m_forceID = {},      // Optional, send message to only force_id
    int m_playerID = {}     // Optional, send message to only player_id
}
```

- Should only set `m_forceID` or `m_playerID`, it is undefined to set both.
- If neither `m_forceID` nor `m_playerID` is set, message will be broadcasted to all players (and observers)

Example
```sq
// display chat message 'Hello World!' to player 3
gx_print("Hello World!", { m_playerID = 3 } )

// display chat message 'Hello World!' to everyone in force 2
gx_print("Hello World!", { m_forceID = 2 } )

// display chat message 'Hello World!' to everyone
gx_print("Hello World!")

// equivalent to above, display chat message 'Hello World!' to everyone
gx_print("Hello World!", {})
```

- outputs text to game chat (or map editor console)
- useful for debugging as well
- `print(message)` is equivalent to `gx_print(message, {})`
- `params` are ignored when running in map editor's console

## gx_modify_scoreboard
```sq
void gx_modify_scoreboard(table params = {})
```

```sq
local params = {
    bool m_bDisplay = {},
    bool m_bShowForceScores = {},
    bool m_bShowPlayerScores {}
}
```

- Set `m_bDisplay` to show scoreboard, must be `true` if you want to display
- Set `m_bShowForceScores` to show scores for forces
- Set `m_bShowPlayerScores` to show scores for players
- You can set/add/get scores by using {{fn("property-getterssetters")}}

Example:
```sq
gx_modify_scoreboard({
    m_bDisplay = true,
    m_bShowPlayerScores = true,
    m_bShowForceScores = false
})

// Set score for 'Player 3' to 7
gx_set_player_prop(PlayerProp.Score, 3, 7)
```

## gx_set_victory
```sq
void gx_set_victory(table params)
```

```sq
table params = {
    int m_playerID = {},
    int m_forceID = {}
}
```

- once a player or team is set to `victory`, future calls to `gx_set_victory`/`gx_set_defeat` for that player/team will be ignored
- should only set one of `m_playerID` or `m_forceID`, setting both is undefined
- setting `m_forceID` will set victory for all players within that force

## gx_set_defeat
```sq
void gx_set_defeat(table params)
```

```sq
table params = {
    int m_playerID = {},
    int m_forceID = {},
    bool m_bKillAllUnits = true     // Optional, (default true)
}
```

- if `m_bKillAllUnits` is `true`, all units for player (or team) will be killed.
- once a player or team is set to `defeat`, future calls to `gx_set_victory`/`gx_set_defeat` for that player/team will be ignored
- should only set one of `m_playerID` or `m_forceID`, setting both is undefined
- setting `m_forceID` will set defeat for all players within that force

## gx_encode_text
```sq
string gx_encode_text(string text)
```

Example
```sq
local someText = gx_encode_text("^23Rainbow Text")
gx_print(someText)
```

## gx_map_init_copy_ud

Creates a copy of a `unit_data`.
A `unit_data` serves as a 'definition' for a type of unit.
Required for creating new custom unit types.

```sq
void gx_map_init_copy_ud(string unit_type, string new_unit_type)
```

The example below creates a new type of unit called "User_BabyBrute"
It copies the existing definition of "Brute" to "User_BabyBrute".

Example:

```sq
gx_map_init_copy_ud("Brute", "User_BabyBrute")
```

- NOTE!! It's preferred to use the Drift Wars Map Editor to add/edit units!!
- These functions are only for convenience
- new unit type name MUST begin with `User_`. This is to prevent naming collisions for future added official units.
- this function will be a no-op if `new_unit_type` name does not begin with `User_`
- This function will return empty string if `new_unit_type` already exists or if it does not start with `User_`.
- `ud` is short for `unit_definition` 
- Can only be called during {{entry("gx_map_init")}}
- any attempt to call this outside of the {{entry("gx_map_init")}} will be ignored.

## gx_map_init_modify_ud_props
```sq
void gx_map_init_modify_ud_props(string unit_type, table params = {})
```

```sq
table params = {
    string m_friendlyName = {},     // Optional, set unit's friendly name
    int m_maxHealth = {},           // Optional, set max health
    float m_maxSpeed = {},          // Optional, set max speed
    int m_baseArmor = {},           // Optional, sets base armor
    int m_size = {}                 // Optional, set unit size,
    int m_gemstoneCost = {},
    int m_fungusCost = {},
    int m_supplyCost = {},
    int m_buildTime = {}
}
```

The example below creates a new type of unit called "User_BabyBrute".
It copies the existing `unit_definition` of "Brute" to "User_BabyBrute". 
It then sets properties such as friendly name, maxHealth, baseArmor, and size.

Example:

```sq
gx_map_init_copy_ud("Brute", "User_BabyBrute")
gx_map_init_modify_ud_props("User_BabyBrute", {
    m_friendlyName = "Baby Brute",
    m_maxHealth = 30,
    m_baseArmor = 0,
    m_size = 1
})
```

- Sets properties for a specific `unit_type`
- `ud` is short for `unit_definition` 
- Can only be called during {{entry("gx_map_init")}}
- any attempt to call this outside of the {{entry("gx_map_init")}} will be ignored.

## gx_map_init_add_build_structure_item
```sq
void gx_map_init_add_build_structure_item(string unitType, table params = {})
```

```
table params = {
    string m_structure = {},    // name of structure to build, i.e. "Microwave"
    Vec2 m_position = {},           // position in command card to place at, leaving empty will use default
    bool bBuildAdvanced = false     // default is false, if set to True, will be placed in 'build advanced' tab
}
```
- Can only be called during {{entry("gx_map_init")}}

## gx_map_init_remove_all_build_structure_items
```sq
void gx_map_init_remove_all_build_structure_items(string unitType)
```

- Remove all build structure items from worker
- Can only be called during {{entry("gx_map_init")}}

## gx_map_init_add_build_item
```sq
void gx_map_init_add_build_item(string unitType, table params)
```

```sq
table params = {
    string m_unitType = {},     // unit type to add
    string m_research ={},      // research to add
    string m_position = {}      // position in command card
}
```

- Only one `m_unitType` or `m_research` should be set
- Can only be called during {{entry("gx_map_init")}}
- Remove all build items from structure

## gx_map_init_remove_all_build_items
```sq
void gx_map_init_remove_all_build_items(string unitType)
```

- Remove all build items from structure
- Can only be called during {{entry("gx_map_init")}}

## gx_fling_unit

throws the unit

```sq
void gx_fling_unit(int unit_id, table params = {})
```

```sq
table params = {
    Vec2 m_dir = {},        // Optional, 2d direction to throw unit. Does not need to be normalized.
    Vec3 m_dir3d = {},      // Optional, 3d direction to throw unit. Does not need to be normalized.
    float m_force = 1       // Optional, velocity to throw unit
}
```

- If neither `m_dir` nor `m_dir3d` is set, unit will be thrown in random direction
- Only `m_dir` or `m_dir3d` should be set. Setting both is undefined behavior.
- Refer to {{type("Vec2")}} and {{type("Vec3")}} if needed. 

## gx_set_area_vision
```sq
void gx_set_area_vision(int player_id, table params)
```

```sq
table params = {
    string m_location = {},         // location to give or take away vision of (depending on m_bSet)
    string m_triangleGroup = {},    // triangle group to give or take away vision of (depending on m_bSet)
    bool m_bFullMapVision = {}      // If set to true, will give or take away vision of entire map (depending on m_bSet)
    bool m_bSet = true              // If true gives vision, else takes away vision. (default: true)
}
```

- This function gives or removes permanent vision of a `m_location`, `m_triangleGroup`, or `entire map`.
- Only one of `m_location`, `m_triangleGroup`, or `m_bFullMapVision` should be set.
- The only valid value of `m_bFullMapVision` is `true`. Setting to `false` is `undefined`.
- If you want to give `Full Map Vision` to a player, set `m_bFullMapVision` to `true` and `m_bSet` to `true`.
- If you want to remove `Full Map Vision` from a player, set `m_bFullMapVision` to `true` and `m_bSet` to `false`.
- The value of `m_bSet` determines if vision is given or taken away from player.

## gx_get_area_vision
```sq
bool gx_get_area_vision(int player_id, table params)
```

```sq
table params = {
    string m_location = {},         // location to query vision for
    string m_triangleGroup = {},    // triangle group to query vision for
    bool m_bFullMapVision = {}      // If set to true, queries if player has full map vision
}
```

- This function queries if the player has permanent vision of a `location`, `triangleGroup`, or `entire map`.
- Only one of `m_location`, `m_triangleGroup`, or `m_bFullMapVision` should be set.
- The only valid value of `m_bFullMapVision` is `true`. Setting to `false` is `undefined`.

## gx_set_terrain_type
```sq
void gx_set_terrain_type(params = {})
```

```sq
table params = {
    TerrainType m_type         // Required. The type of terrain to change to. See TerrainType enum. 
    int m_secondary = 0         // Secondary terrain type. (default = 0)
    Vec2 m_index = {},          // 2d index of square to change terrain type of
    int m_index2 = {},         // 0 or 1, 0 indicates bottom triangle, 1 indicates top.
                                // If index2 is not defined, entire square specified by m_index
                                // will be set to terrain type (i.e. both triangles, top and bottom).
                                // m_index and index2 are ignored if m_location is set.
    string m_location = {}      // location to set terrain tile types.,
    string m_triangleGroup = {} // triangle group to set terrian tile stype
}
```

Example that sets terrain at location `my_location` to Pacifist type:
```sq
gx_set_terrain_type({
    m_type = TerrainType.Normal,
    m_secondary = SecondaryTerrainTypeNormal.Pacifist,
    m_location = "my_location"
})
```

- Refer to {{enum("TerrainType")}} for valid `m_type` values
- If `m_type` is set to `TerrainType.Normal`, `m_secondary` must be one of {{enum("SecondaryTerrainTypeNormal")}} values
- Refer to {{type("Vec2")}} if needed.
- if only `m_index` is set, the square at `m_index` is set to terrain type (i.e. both bottom and top triangle)
- if `m_location` is set, the triangles within the `m_location` are set to the new terrain type
- if `m_triangleGroup` is set, the triangles within `m_triangleGroup` are set to the new terrain type
- if `m_location` is set, it is `undefined behavior` to also set  `m_index`, `m_index2`, or `m_triangleGroup`
- if `m_triangleGroup` is set, is it `undefined behavior` to also set `m_index`, `m_index2`, or `m_location`
- if `m_index` is set, it is `undefined behavior` to also set `m_location`, and `m_triangleGroup`

## gx_get_terrain_type
```
Vec2<int> gx_get_terrain_type(Vec2 index, int index2 = 0)
```
- returns primary terrain type in `vec.m_x` and returns secondary terrain type in `vec.m_y`

## gx_set_player_camera_look_at
```
void gx_set_player_camera_look_at(int player_id, table params)
```

```sq
local params = {
    int m_unitID = {},
    string m_location = {}
}
```

- Moves camera of `player_id` to look at `m_unit` or `m_location`
- One of `m_unit` or `m_location` should be set. Not both.

## gx_lock_player_camera
```sq
void gx_lock_player_camera(int player_id, table params = {})
```

```sq
local params = {
    int m_unitID = {},
    string m_location = {}
}
```

- locks `player_id` camera to look at `m_unitID` or `m_location`.
- camera will follow `m_unitID` or `m_location` until `m_unitID` is removed from game
- can unlock camera by calling `gx_unlock_player_camera(player_id)`
- passing empty args for `params` will unlock the camera for `player_id`.

## gx_unlock_player_camera
```sq
void gx_unlock_player_camera(int player_id)
```

- unlocks `player_id` camera position set by {{fn("gx_lock_player_camera")}}
- equivalent to calling `gx_lock_player_camera(player_id, {})`

## gx_queue_command
```sq
gx_queue_command(int unit_ids[], CommandType command, table params = {})
```

```sq
table params = {
    int m_unitID,            // unit to target
    string m_location = {},     // location to target
    string m_pos = {},          // position to target
}
```

- only one (or zero) unit_id, m_location, m_pos should be set
- some commands/spells only work when certain params are set
- (i.e., a spell that can only target units cannot target a `m_pos` or `m_location`)
- `CommandType` can also be a spell identifier
- See {{enum("CommandType")}} for possible command values

## gx_set_speech_bubble
```sq
void gx_set_speech_bubble(int unit_id, string text, table params = {})
```
- set a speech bubble for unit_id
- currently there are no optional params

## gx_(get|set|add)_unit_ammo
```sq
int gx_get_unit_ammo(int unit_id, string ammoName)
void gx_set_unit_ammo(int unit_id, string ammoName, int count)
void gx_add_unit_ammo(int unit_id, string ammoName, int count)
```

- Can query and set how much `unit ammo` of type `ammoName` the unit is holding

## gx_(get|set|add)_player_ammo_in_unit
```sq
int gx_get_player_ammo_in_unit(int unit_id, string ammoName)
void gx_set_player_ammo_in_unit(int unit_id, string ammoName, int count)
void gx_add_player_ammo_in_unit(int unit_id, string ammoName, int count)
```

- Can query and set how much `player ammo` of type `ammoName` the unit is holding

## gx_get_player_ammo_total
```sq
int gx_get_player_ammo_total(int player_id, string ammoName)
```

- Returns how much `player ammo` of type `ammoName` the player has

## gx_get_unit_by_name
```sq
int gx_get_unit_by_name(params = {})
```

```sq
local params = {
    string m_name,             // Required                                 (string)
    int m_player_id = 0        // Optional, used to Filter. Default = 0.   (int)
}
```

- returns unit_id with the given `m_name` or
- unit name can be set in map editor.
- if multiple units have the same name, the first will be returned.

## Property Getters/Setters
- Allows you to get/set certain properties for `simulation`, `forces`, `players`, and `units`, and other things

```sq
// getters
mixed gx_get_force_prop(ForceProp prop, int force_id)
mixed gx_get_player_prop(PlayerProp prop, int player_id)
mixed gx_get_unit_prop(UnitProp prop, int unit_id)
mixed gx_get_location_prop(LocationProp prop, string location)

// setters
void gx_set_force_prop(ForceProp prop, int force_id, mixed val)
void gx_set_player_prop(PlayerProp prop, int player_id, mixed val)
void gx_set_unit_prop(UnitProp prop, int unit_id, mixed val)

// adders
void gx_add_force_prop(ForceProp prop, int force_id, mixed val)
void gx_add_player_prop(PlayerProp prop, int player_id, mixed val)
void gx_add_unit_prop(UnitProp prop, int unit_id, mixed val)
```

- Please refer to {{enum("ForceProp")}}, {{enum("PlayerProp")}}, {{enum("UnitProp")}}, and {{enum("LocationProp")}} for possibles values you can get/set (and their types).
- Properties that are `int` or `float` and are `Read-Write` can use the `gx_add_*` functions

## UserData Getters/Setters
- Allows you to get/set userdata integers for `simulation`, `forces`, `players`, and `units`, and other things for your own purposes

```sq
// getters
int gx_get_sim_variable(string varName)
int gx_get_force_variable(int force_id, string varName)
int gx_get_player_variable(int player_id, string varName)
int gx_get_unit_variable(int unit_id, string varName)

// setters
void gx_set_sim_variable(string varName, int varValue)
void gx_set_force_variable(int force_id, string varName, int varValue)
void gx_set_player_variable(int player_id, string varName, int varValue)
void gx_set_unit_variable(int unit_id, string varName, int varValue)

// adders
void gx_add_sim_variable(string varName, int varValue)
void gx_add_force_variable(int force_id, string varName, int varValue)
void gx_add_player_variable(int player_id, string varName, int varValue)
void gx_add_unit_variable(int unit_id, string varName, int varValue)
```

- Calling `gx_get_*` to retrieve a non-existing `varValue` will return `0`.
- Only `int` values can be set.


## gx_is_event_queue_empty
```sq
bool gx_is_event_queue_empty()
```

- Check if event queue is empty.
- See {{eventQueue()}}

## gx_pop_event_from_queue
```sq
Event gx_pop_event_from_queue()
```

- Pop event from event queue.
- See {{eventQueue()}}

