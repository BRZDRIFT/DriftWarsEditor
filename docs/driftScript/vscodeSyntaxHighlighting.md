## Install Squirrel Language Support

Go to visual studio extensions:  
Search and install:  

- `Squirrel Language Supports` by marcinbar
- `Squirrel Language Linter` by marcinbar

Then modify settings to associate `.DriftScript` extension with `squirrel` language

- Go to `Preferences` --> `Settings`
- Search for setting: `Files: Associations`
- Add new item: `Item`: `DriftScript`, `Value`: `squirrel`
- Restart VSCode

## Notes
- There are future plans for a custom VSCode extension for `.DriftScript` which should
allow for improved syntax highlighting and function completion.