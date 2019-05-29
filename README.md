# CompiladorMIPS

CompiladorMIPS es un script Python para la generación automática de la representación binaria y hexadecimal de las 
instrucciones básicas en ensamblador del compilador MIPS empleado en la asignatura Arquitectura y organización de computadores 2.
Una traza de ejemplo sería:
```
pitazzo@Katana:~$ python3 compilador.py 
add r0 r1 r2
	000001 00001 00010 00000 00000000000
	0x04220000
```

## Modo de uso
1. Invocar el script mediante `python3 compilador.py`
2. Introducir línea a línea instrucciones en formato `código_operación rX rX ...`

## Instrucciones soportadas
Actualmente el compilador soporta `add`, `addfp`, `lw`, `sw` y `beq`. Es decir, las necesarias para el proyecto de AOC2 de 2018

## Requisitos
- Python 3
