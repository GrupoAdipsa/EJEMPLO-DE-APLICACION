# EJEMPLO-DE-APLICACION

Script sencillo para estimar el peso de un gancho de estribo en una
columna de hormigón armado. El cálculo utiliza el diámetro del estribo,
el diámetro de la barra longitudinal y la distancia libre entre ambos.

## Uso

```bash
python calcular_peso_gancho.py \
    9.5 \
    16 \
    25
```

Los parámetros deben introducirse en milímetros en el siguiente orden:

1. `diametro_estribo` – diámetro del estribo.
2. `diametro_barra_longitudinal` – diámetro de la barra longitudinal a
   la que abraza el gancho.
3. `distancia_libre` – separación libre entre el estribo y la cara
   exterior de la barra longitudinal antes del doblez.

El programa imprime la longitud del gancho, el peso lineal del estribo y
el peso total estimado.