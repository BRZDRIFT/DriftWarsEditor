## Event Queue

Event Structure:
```sq
table Event
{
    EventType m_type        // Always populated, specifies type of event.
    int m_playerID = {}
    string m_playerName = {}
    string m_oldPlayerName = {}
    int m_playerNameColorID = {}
    int m_oldPlayerNameColorID = {}
    string m_cmd = {}
    int m_unitID = {},
    int m_soundID = {},
    string m_location = {}
}
```

- Look at the comments in the definition of {{enum("EventType")}} to see which fields each `EventType` populates.

Example of reading events from queue

```sq
function gx_sim_update()
{
    while (!gx_is_event_queue_empty())
    {
        local ev = gx_pop_event_from_queue()
        if (ev.m_type == EventType.PlayerLeftGame)
        {
            gx_print("Player " + ev.m_playerID + " has left the game!")
        }
        else if (ev.m_type == EventType.PlayerNameChanged)
        {
            gx_print(ev.m_oldPlayerName + " changed name to " + ev.m_playerName)
        }
    }

    // do rest of game logic
}
```

Functions that operate on event queue:

- {{fn("gx_is_event_queue_empty")}}
- {{fn("gx_pop_event_from_queue")}}

Note:

- Any unpopped events are automatically popped off of queue after each {{entry("gx_sim_update")}} call.