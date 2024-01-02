# Commodore 64 Assembler programming

## Screenshots

![Screenshot of a COMMODORE64 with assembler code on 64MON cartridge](day01-assembler.png)  
*Dump of assembly code with 64MON cartridge*  

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

## Books and documentation

- Chapter 5, "BASIC TO MACHINE LANGUAGE" in C64 Programmer reference" by Commodore Computers (this is the [cover](c64_programmer_reference_book_cover.jpg))
- [Floating point arithmetic](https://www.c64-wiki.com/wiki/Floating_point_arithmetic)
- [I segreti del linguaggio macchina](https://archive.org/details/commodore64isegretidellinguaggiomacchina/mode/1up)
- [data conversion functions](https://sta.c64.org/cbm64basconv.html)
