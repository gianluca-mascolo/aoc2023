# Commodore 64 Assembler programming


## Cartridge

Find and download `64MON by HANDIC SOFTWARE 1983` (filename: `handics_64mon.crt`)

### Commands

#### In Basic mode
- `SYS 32820` to enter assembler mode

#### In assembler mode
- `.X` to exit assembler mode and return to Basic
- `F7` to display help/command list screen
- `.A $$$$ <instruction>` to create an assembly instruction at given address (e.g. `.A 1400 BRK`)
- `G $$$$` go to given address and start execution

#### Books and documentation

- "C64 Programmer reference" by Commodore Computers (have a look at the [cover](c64_programmer_reference_book_cover.jpg))
