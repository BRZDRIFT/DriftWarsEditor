- Drift Wars supports utf-8 unicode.
    - You can usually copy paste utf-8 into Drift Wars Editor or game, and should work..
    - Alternatively, most of the Drift Wars Editor Text fields can encode unicode using this syntax:
        - `\u{unicode}`
        - Example: `\u{1F600}` = 😀

- Drift Wars also has custom-defined unicode characters that can be used for changing text color.
    - A shortcut for adding these unicode characters are `^code`
    - `^226This Text Is Red` outputs <span style="color:red">This Text Is Red</span>
    - Note: The editor might show the "color" character as a garbage character, but the Drift Wars client will render text in red.
    - You can go into Drift Wars game and look at the `Paint` dialog to find out all the color codes
    - Please note: the color codes [1-16] should not be used -- the colors they reference may change in the future.

- You can also encode unicode text with DriftScript using the `gx_encode_text` function
    ```sq
    local yellowText = gx_encode_text("^230Yellow")
    local smileyEmoji = gx_encode_text("\u{1F600}")
    ```
